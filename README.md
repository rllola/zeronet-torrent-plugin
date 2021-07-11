# Torrent Plugin

[![Build Status](https://travis-ci.org/rllola/zeronet-torrent-plugin.svg?branch=master)](https://travis-ci.org/rllola/zeronet-torrent-plugin)

An attempt to create a plugin that will allow the use of libtorrent to share big files !

Example site : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Build

We need to build libtorrent python bindings.

```

python test.py
```

It might take a couple of minutes.

If the test work, you can start Zeronet and access the test page :
http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Troubleshooting

### ZeroBundle

This plugin does not work with the default setup in ZeroBundle (currently) as ZeroBundle packages its own python binary (which won't have access to libtorrent).

### Windows

It has not been yet tested on Windows.
