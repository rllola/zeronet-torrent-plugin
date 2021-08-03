import sys
import os
import zipfile

if sys.platform == 'win32':
  libtorrent_file = 'libtorrent.pyd'
else:
  libtorrent_file = 'libtorrent.so'

libtorrent_zip_path = os.path.join(os.path.dirname(__file__),'libtorrent-{}.zip'.format(sys.platform))

# if libtorrent lib not present look for it
if not os.path.exists(os.path.join(os.path.dirname(__file__),'libtorrent', libtorrent_file)):
  with zipfile.ZipFile(libtorrent_zip_path,'r') as zip_ref:
    zip_ref.extractall(os.path.join(os.path.dirname(__file__),'libtorrent'))

# Need to add libtorrent lib
sys.path.append(os.path.dirname(__file__))

from . import TorrentPlugin