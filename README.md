# Torrent Plugin

An attempt to create a plugin that will allow the use of libtorrent to share big files !

Example site : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Install

In your Zeronet folder :
```
cd plugins
git clone https://github.com/rllola/zeronet-torrent-plugin.git Torrent --recursive
```

### Libtorrent binding config

Be sure to have this installed for linux (debian/ubuntu) :
```
apt install autoconf automake libtool libboost-all-dev libssl-dev
```

Configure and build :
```
cd libtorrent
./bootstrap.sh
make -j$(nproc)
```

Test here : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/
