# Torrent Plugin

An attempt to create a plugin that will allow the use of libtorrent to share big files !

Example site : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Download

In your Zeronet folder :
```
cd plugins
git clone https://github.com/rllola/zeronet-torrent-plugin.git Torrent --recursive
```

### Libtorrent dependencies

Debian/Ubuntu Linux :
```
sudo apt install autoconf automake libtool libboost-all-dev libssl-dev
```

MacOS :

You need to first [install homebrew](https://brew.sh) and python-pip (`sudo easy_install pip`) if you haven't already. 
Then in a terminal :
```
brew update
brew install autoconf automake libtool openssl boost boost-python
sudo -H pip2 install gevent msgpack-python
xcode-select --install
```

## Building

Linux :
```
cd libtorrent
./bootstrap.sh
make -j$(nproc)
```

MacOS :
```
cd libtorrent
./bootstrap.sh --with-openssl=/usr/local/opt/openssl --enable-python-binding
make -j$(sysctl -n hw.ncpu)
```

## Installing

Linux :
```
sudo make install
```

MacOS :
```
sudo make install
sudo ./setup.py install
```

Test here : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Troubleshooting

### ZeroBundle

This plugin does not work with the default setup in ZeroBundle (currently) as ZeroBundle packages its own python binary (which won't have access to libtorrent).

To work around this, instead of double-clicking the ZeroNet icon, navigate to `WhereverYouDownloadedZeroNet/ZeroNet.app/Contents/Resources/core`, and launch ZeroNet from there with:

```
python ./zeronet.py
```

The test page should now no longer report that the plugin is not installed.
