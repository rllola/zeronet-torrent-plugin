# Torrent Plugin

[![Build Status](https://travis-ci.org/rllola/zeronet-torrent-plugin.svg?branch=master)](https://travis-ci.org/rllola/zeronet-torrent-plugin)

Example site and installer : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

This project is an attempt to integrate a Torrent client in ZeroNet as a plugin. It makes available a Torrent specific api that allow adding torrent files, hash or magnet. The files will be saved in the site folder which makes it available to the site.

It also allows streaming video files out of the box.

## TODO

- [ ] Save torrents list at shut down and restart using this list
- [ ] UI for managing the Torrent client and vizualize files being downloaded
- [ ] Config UI (trackers, limits, ...)

## Dev (for linux)

We need to build libtorrent python bindings with at least boost 1.74.

```
$ make config-linux
$ make boost
$ make libtorrent-repo
$ export BOOST_BUILD_PATH=${PWD}/boost_1_74_0/tools/build
$ export BOOST_ROOT=${PWD}/boost_1_74_0
$ cd libtorrent-repo/bindings/python && ../../../boost_1_74_0/b2 release --debug-configuration crypto=openssl cxxstd=14 python=3.8 libtorrent-link=static boost-link=static
$ cd ../../..
$ cp libtorrent-repo/bindings/python/bin/gcc-9/release/crypto-openssl/cxxstd-14-iso/libtorrent-python-pic-on/python-3.8/libtorrent.so libtorrent/

$ python test.py
```

It might take a couple of minutes.

## Troubleshooting

...