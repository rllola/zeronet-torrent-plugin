# Torrent Plugin

[![Build Status](https://travis-ci.org/rllola/zeronet-torrent-plugin.svg?branch=master)](https://travis-ci.org/rllola/zeronet-torrent-plugin)

**Important! This is still work in progress. Don't use it if you don't want to.**

Example site and installer : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

This project is an attempt to integrate a Torrent client in ZeroNet as a plugin. It makes available a Torrent specific api for site that allows site to add torrent files, hash or magnet. The files will be saved in the site folder which makes it available to the site (e.g `data/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/downloads`).

It also allows streaming video files out of the box. When a chunk of video will be requested by the player the torrent plugin will verify if it is available and it not will prioritize this piece. This makes it possible to watch videos when they start being being downloaded.

More information is available in the [FAQ](/FAQ.md).

## Screenshots

![Install](/screenshots/install.png)

![Form](/screenshots/form.png)

![Play](/screenshots/play.png)

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