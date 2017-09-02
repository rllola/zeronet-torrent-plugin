#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
apt-get update
apt-get install -y python-pip msgpack-python python-gevent git cmake
# apt install -y autoconf libtool build-essential libboost-all-dev libssl-dev
pip install --upgrade pip
pip install conan

echo "===== INSTALL ZERONET ====="
wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz
tar xvpfz master.tar.gz

echo "===== INSTALL LIBTORRENT & LIBTORRENT PYTHON BINDINGS ====="
conan remote add libtorrent https://api.bintray.com/conan/rllola80/Libtorrent
cd /home/ubuntu/ZeroNet-master/plugins/Torrent
conan install -g txt --build Boost OpenSSL
