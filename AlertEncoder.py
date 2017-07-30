import base64

class AlertEncoder(object):

    def __init__(self, alert):
        self.alert = alert
        self.encodeAlert()

        print self.response['what']

        if self.response['what'] == 'read_piece_alert':
            self.encodeReadPieceAlert()
        elif self.response['what'] == 'add_torrent_alert':
            print 'Add Torrent Alert !'
        else:
            print 'Unknown alert !'

    def encodeAlert(self):
        self.response = {
            'what': self.alert.what(),
            'message': self.alert.message(),
            'category': self.alert.category()
        }

    def encodeReadPieceAlert(self):
        print 'Received read_piece_alert for piece ' + str(self.alert.piece)
        if hasattr(self.alert, 'error') :
            print self.alert.error
            self.response['error'] = self.alert.error
        else :
            self.response['pieceIndex'] = self.alert.piece
            self.response['size'] = self.alert.size
            self.response['buffer'] = base64.b64encode(self.alert.buffer)

    def get(self):
        return self.response
