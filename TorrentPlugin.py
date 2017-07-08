import logging
import libtorrent
import time
import base64

from Plugin import PluginManager

#log = logging.getLogger("TorrentPlugin")

@PluginManager.registerTo("UiWebsocket")
class UiWebsocketPlugin(object):

    # Initiate libtorrent session

    session = libtorrent.session()
    session.listen_on(6881, 6891)

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
                params['save_path'] = save_path
                # HACK:
                # Doesn't recognise sha1_hash python object when addded to session if not converted to string
                # 'No registered converter was able to produce a C++ rvalue of type bytes from this Python object of type sha1_hash'
                params['info_hash'] = params['info_hash'].to_string()
            except:
                params = { 'save_path': save_path, \
                            'storage_mode': libtorrent.storage_mode_t.storage_mode_sparse, \
                            'info_hash': torrentIdentifier.decode('hex') }
        try:
            h = self.session.add_torrent(params)
        except Exception as exception:
            self.response(to, {'error': str(exception)})
        else:
            info_hash = h.info_hash()
            self.response(to, {'info_hash': str(info_hash)})

    #def actionPopAlerts(self, to):
    #    alert_lists = session.pop_alerts()

    def actionTorrentStatus(self, to, info_hash):
        info_hash = libtorrent.sha1_hash(info_hash.decode('hex'))
        h = self.session.find_torrent(info_hash)
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
        info_hash = libtorrent.sha1_hash(info_hash.decode('hex'))
        h = self.session.find_torrent(info_hash)
        if h.is_valid():
            ti = h.get_torrent_info()
            files = ti.files()

            arrayFiles = []
            for file in files:
                arrayFiles.append(file.path)

            self.response(to, {'name': ti.name(), \
                                'num_files' : ti.num_files(), \
                                'files': arrayFiles \
                                 })
        else:
            self.response(to, {'error': 'Torrent not found'})

    def actionHelloWorld(self, to):
        self.response(to, {'message':'Hello World'})
