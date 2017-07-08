# Torrent Plugin

Attempt to create a plugin that will allow to use libtorrent to share big file !

Example site : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Install

In you Zeronet folder :
```
cd plugins
git clone git@github.com:rllola/zeronet-torrent-plugin.git Torrent
```

### Libtorrent binding config

Be sure to have this install for linux :
```
apt install autoconf automake libtool libboost-all-dev
```

Configure :
```
./bootstrap.sh
```

Build libtorrent :
```
make
```

Test here : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/
