import logging
import time
import base64
import gevent
import sys
import libtorrent

from .AlertEncoder import AlertEncoder

from Plugin import PluginManager

libtorrent = libtorrent.libtorrent

VERSION = '0.4.4'

def popAlerts(session):
    while 1:
        alertsList = session.pop_alerts()
        # Need encoding
        for alert in alertsList:
            result = AlertEncoder(alert)
            for instanceOfUiWebsocketPlugin in UiWebsocketPlugin._instances:
                if alert.what() == 'read_piece' and not 'error' in result.get():
                    for instanceOfUiRequestPlugin in UiRequestPlugin._instances:
                        if result.get()["pieceIndex"] in instanceOfUiRequestPlugin.piece_index_requested:
                            instanceOfUiRequestPlugin.requested_pieces.append(result.get())
                instanceOfUiWebsocketPlugin.cmd(alert.what(), result.get())
        gevent.sleep(0.250)

# Initiate libtorrent session
session = libtorrent.session({'listen_interfaces':'0.0.0.0:6881', 'alert_mask': libtorrent.alert.category_t.progress_notification+libtorrent.alert.category_t.status_notification})
gevent.spawn(popAlerts, session)

@PluginManager.registerTo("UiRequest")
class UiRequestPlugin(object):
    _instances = []

    def __init__(self, *args, **kwargs):
        super(UiRequestPlugin, self).__init__(*args, **kwargs)
        UiRequestPlugin._instances.append(self)
        self.requested_pieces = []
        self.file = None
        self.piece_index_requested = []

    def getTorrentFile(self, file_path):
        torrent_handles = session.get_torrents()
        for h in torrent_handles:
            for file_index in range(0,files.num_files()):
                file = ti.file_at(file_index)

                if file.path in file_path:
                    print(file.path)
                    return ti.info_hash()
        return False

    def actionFile(self, file_path, *args, **kwargs):
        if "info_hash" in self.get:
            print("info hash :", self.get["info_hash"])
            print("File index :", self.get["file_index"])

            info_hash = libtorrent.sha1_hash(bytes.fromhex(self.get["info_hash"]))
            h = session.find_torrent(info_hash)

            if h.is_valid():
                ti = h.torrent_file()
                files = ti.files()
                for file_index in range(0,files.num_files()):
                    file = ti.file_at(file_index)

                    if file.path in file_path:
                        # priotarize file (7 max priority)
                        h.file_priority(file_index, 7)

                        kwargs["block_size"] = ti.piece_length()
                        print("piece_size : {}".format(kwargs["block_size"]))
                        self.file = file
                        kwargs["file_size"] = file.size
                        kwargs["file_obj"] = TorrentFile(h, file, self)

        return super(UiRequestPlugin, self).actionFile(file_path, *args, **kwargs)


@PluginManager.registerTo("UiWebsocket")
class UiWebsocketPlugin(object):

    _instances = []

    def __init__(self, *args, **kwargs):
        super(UiWebsocketPlugin, self).__init__(*args, **kwargs)
        UiWebsocketPlugin._instances.append(self)

    def actionGetVersion(self, to):
        self.response(to, {'version': VERSION})

    def actionAddTorrent(self, to, torrentIdentifier):
        save_path = './data/' + self.site.address + '/downloads/'
        try:
            e = libtorrent.bdecode(base64.b64decode(torrentIdentifier))
            info = libtorrent.torrent_info(e)
            params = { 'save_path': save_path, \
                        'storage_mode': libtorrent.storage_mode_t.storage_mode_sparse, \
                        'ti': info }
        except Exception as exception:
            try:
                # Test if a magnet
                params = libtorrent.parse_magnet_uri(torrentIdentifier)
                params.save_path = save_path
                # HACK:
                # Doesn't recognise sha1_hash python object when added to session if not converted to string
                # 'No registered converter was able to produce a C++ rvalue of type bytes from this Python object of type sha1_hash'
                #params['info_hash'] = params['info_hash'].to_string()
            except Exception as exception:
                params = { 'save_path': save_path, \
                            'storage_mode': libtorrent.storage_mode_t.storage_mode_sparse, \
                            'info_hash': torrentIdentifier.decode('hex') }
        try:
            session.async_add_torrent(params)
        except Exception as exception:
            self.response(to, {'error': str(exception)})
        else:
            if type(params) is libtorrent.add_torrent_params:
                info_hash = params.info_hashes.get_best()
            else:
                if not info is None:
                    info_hash = info.info_hashes().get_best()
                else:
                    info_hash = params['info_hash']
            self.response(to, {'info_hash': str(info_hash)})

    def actionTorrentStatus(self, to, info_hash):
        info_hash = libtorrent.sha1_hash(bytes.fromhex(info_hash))
        h = session.find_torrent(info_hash)
        if h.is_valid():
            s = h.status()
            self.response(to, {'progress': s.progress, \
                                'download_rate': s.download_rate, \
                                'upload_rate': s.upload_rate, \
                                'num_peers': s.num_peers, \
                                'state': str(s.state) })
        else:
            self.response(to, {'error': 'Torrent not found'})

    def actionGetTorrentInfo(self, to, info_hash):
        info_hash = libtorrent.sha1_hash(bytes.fromhex(info_hash))
        h = session.find_torrent(info_hash)
        if h.is_valid():
            ti = h.get_torrent_info()
            files = ti.files()

            arrayFiles = []
            for file in files:
                arrayFiles.append({'path': file.path, \
                                    'offset': file.offset, \
                                    'size': file.size \
                                    })

            self.response(to, {'name': ti.name(), \
                                'num_files' : ti.num_files(), \
                                'files': arrayFiles, \
                                'piece_length': ti.piece_length() \
                                 })
        else:
            self.response(to, {'error': 'Torrent not found'})

    def actionReadPiece(self, to, info_hash, piece_index):
        info_hash = libtorrent.sha1_hash(bytes.fromhex(info_hash))
        h = session.find_torrent(info_hash)
        if h.is_valid():
            h.read_piece(piece_index)
            self.response(to, 'ok')
        else:
            self.response(to, {'error': 'Torrent not found'})

    def actionHavePiece(self, to, info_hash, piece_index):
        info_hash = libtorrent.sha1_hash(bytes.fromhex(info_hash))
        h = session.find_torrent(info_hash)
        if h.is_valid():
            response = h.have_piece(piece_index)
            self.response(to, response)
        else:
            self.response(to, {'error': 'Torrent not found'})


    def actionPrioritizePiece(self, to, info_hash, piece_index, new_priority):
        info_hash = libtorrent.sha1_hash(bytes.fromhex(info_hash))
        h = session.find_torrent(info_hash)
        if h.is_valid():
            if 0 <= new_priority <= 7 :
                h.piece_priority(piece_index, new_priority)
                self.response(to, 'ok')
            else :
                self.response(to, {'error': 'new_priority should be an integer bewteen 0 and 7'})
        else:
            self.response(to, {'error': 'Torrent not found'})

    #def __del__(self):
    #    print 'DESTROY !'
    #    if self in UiWebsocketPlugin._instances:
    #        print 'Hola !'

class TorrentFile(object):
    def __init__(self, torrent_handle, file, uirequest):
        self.torrent_handle = torrent_handle
        self.read_bytes = 0
        self.file = file
        self._offset = file.offset
        self.uirequest = uirequest
        self.cache = []


    def read(self, buff=64 * 1024):
        chunk_file = 0x00
        ti = self.torrent_handle.torrent_file()
        piece_index = (self.file.offset + self.read_bytes) // ti.piece_length()
        #print("Piece Index requested : {} ( ({} + {}) // {})".format(piece_index, self.file.offset, self.read_bytes, ti.piece_length()))

        self.uirequest.piece_index_requested.append(piece_index)

        # TODO: `set_piece_deadline` has the same behavior as read when piece already available
        if self.torrent_handle.have_piece(piece_index):
            self.torrent_handle.read_piece(piece_index)
        else:
            print("Piece not available!")
            # deadline in milliseconds so we have a 900 seconds deadline after what maybe we can have a timeout ?
            self.torrent_handle.set_piece_deadline(piece_index, 900 * 1000, libtorrent.deadline_flags_t.alert_when_available)
        
        while chunk_file == 0x00:
            for piece in self.uirequest.requested_pieces:
                if piece["pieceIndex"] == piece_index:
                    if self._offset:
                        chunk_file = piece["buffer"][self._offset:]
                        self._offset = 0
                    else:
                        chunk_file = piece["buffer"]
                    self.read_bytes += len(chunk_file)
                    self.uirequest.requested_pieces.remove(piece)
                    break
            gevent.sleep(0.1)
            pass

        return chunk_file

    def seek(self, pos, whence=0):
        #print("SEEKING {}".format(pos))
        self.read_bytes = pos
        ti = self.torrent_handle.torrent_file()
        self._offset = (self.file.offset + self.read_bytes) % ti.piece_length()
        return

    def close(self):
        pass
