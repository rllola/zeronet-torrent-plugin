# Torrent Plugin

[![Build Status](https://travis-ci.org/rllola/zeronet-torrent-plugin.svg?branch=master)](https://travis-ci.org/rllola/zeronet-torrent-plugin)

An attempt to create a plugin that will allow the use of libtorrent to share big files !

Example site : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Download

In your Zeronet folder :
```
cd plugins
git clone https://github.com/rllola/zeronet-torrent-plugin.git Torrent
```

## Build

You need to have conan installed : https://www.conan.io/downloads

```
conan install --build=missing
conan build
python test.py
```

It might take a couple of minutes.

Test here : http://127.0.0.1:43110/1ChMNjXpW5vU5iXb9DSXzqAUfY46Pc2RTL/

## Troubleshooting

### ZeroBundle

This plugin does not work with the default setup in ZeroBundle (currently) as ZeroBundle packages its own python binary (which won't have access to libtorrent).

To work around this, instead of double-clicking the ZeroNet icon, navigate to `WhereverYouDownloadedZeroNet/ZeroNet.app/Contents/Resources/core`, and launch ZeroNet from there with:

```
python ./zeronet.py
```

The test page should now no longer report that the plugin is not installed.
