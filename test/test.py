import unittest
import libtorrent

class TestBuild(unittest.TestCase):

    def test_build(self):
        self.assertEqual(libtorrent.version, '1.1.4.0')


if __name__ == '__main__':
    unittest.main()
