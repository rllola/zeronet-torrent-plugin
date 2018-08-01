#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent cmake
# apt install -y autoconf libtool build-essential libboost-all-dev libssl-dev
# This line broke pip so lets not use it for now
#pip install --upgrade pip
sudo pip install conan

echo "===== INSTALL ZERONET ====="
wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz
sudo tar xvpfz master.tar.gz

echo "===== INSTALL LIBTORRENT & LIBTORRENT PYTHON BINDINGS ====="
conan remote add libtorrent https://api.bintray.com/conan/rllola80/Libtorrent
cd /home/ubuntu/ZeroNet-master/plugins/Torrent
conan install --build=missing .
conan build .
