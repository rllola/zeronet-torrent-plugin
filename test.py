import unittest
import lib.libtorrent as libtorrent

class TestBuild(unittest.TestCase):

    def test_build(self):
        self.assertEqual(libtorrent.version, '1.1.12.0')

    def test_session(self):
        session = libtorrent.session({'listen_interfaces':'0.0.0.0:6881', 'alert_mask': libtorrent.alert.category_t.progress_notification})

if __name__ == '__main__':
    unittest.main()
