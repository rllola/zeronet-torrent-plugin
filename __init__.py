import sys
import os
import zipfile

if sys.platform == 'win32':
  libtorrent_file = 'libtorrent.pyd'
else:
  libtorrent_file = 'libtorrent.so'

 
# if libtorrent lib not present look for it
if not os.path.exists(os.path.join(os.path.dirname(__file__),'libtorrent', libtorrent_file)):
  with zipfile.ZipFile('libtorrent-{}.zip'.format(sys.platform),'r') as zip_ref:
    zip_ref.extractall('libtorrent')

# Need to add libtorrent lib
sys.path.append(os.path.dirname(__file__))

from . import TorrentPlugin