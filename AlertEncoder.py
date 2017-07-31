import base64

class AlertEncoder(object):

    def __init__(self, alert):
        self.alert = alert
        self.encodeAlert()

        if self.response['what'] == 'read_piece_alert':
            self.encodeReadPieceAlert()
        elif self.response['what'] == 'add_torrent_alert':
            print 'Add Torrent Alert !'
        elif self.response['what'] == 'piece_finished_alert':
            self.encodePieceFinishedAlert()


    def encodeAlert(self):
        self.response = {
            'what': self.alert.what(),
            'message': self.alert.message(),
            'category': self.alert.category()
        }

    def encodeReadPieceAlert(self):
        if hasattr(self.alert, 'error'):
            self.response['error'] = self.alert.error
        else :
            self.response['pieceIndex'] = self.alert.piece
            self.response['size'] = self.alert.size
            self.response['buffer'] = base64.b64encode(self.alert.buffer)

    def encodePieceFinishedAlert(self):
        self.response['pieceIndex'] = self.alert.piece_index

    def get(self):
        return self.response
