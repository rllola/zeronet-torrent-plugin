import base64

class AlertEncoder(object):

    def __init__(self, alert):
        self.alert = alert
        self.encodeAlert()

        if self.response['what'] == 'read_piece':
            self.encodeReadPieceAlert()
        elif self.response['what'] == 'add_torrent':
            print('Add Torrent Alert !')
        elif self.response['what'] == 'piece_finished':
            self.encodePieceFinishedAlert()


    def encodeAlert(self):
        self.response = {
            'what': self.alert.what(),
            'message': self.alert.message(),
            'category': self.alert.category()
        }

    def encodeReadPieceAlert(self):
        if hasattr(self.alert, 'error') and self.alert.error.value() != 0:
            self.response['error'] = { 
                'value': self.alert.error.value(),
                'message': self.alert.error.message()
            }
        else :
            self.response['pieceIndex'] = self.alert.piece
            self.response['size'] = self.alert.size
            self.response['buffer'] = self.alert.buffer

    def encodePieceFinishedAlert(self):
        self.response['handle'] = self.alert.handle
        self.response['pieceIndex'] = self.alert.piece_index

    def get(self):
        return self.response
