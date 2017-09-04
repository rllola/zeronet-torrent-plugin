#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt-get update
sudo apt-get install -y python-pip msgpack-python python-gevent git cmake
# apt install -y autoconf libtool build-essential libboost-all-dev libssl-dev
pip install --upgrade pip
sudo pip install conan

echo "===== INSTALL ZERONET ====="
wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz
sudo tar xvpfz master.tar.gz

echo "===== INSTALL LIBTORRENT & LIBTORRENT PYTHON BINDINGS ====="
conan remote add libtorrent https://api.bintray.com/conan/rllola80/Libtorrent
cd /home/ubuntu/ZeroNet-master/plugins/Torrent
conan install --build Libtorrent Boost OpenSSL
