#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent cmake libboost-all-dev git
# apt install -y autoconf libtool build-essential libboost-all-dev libssl-dev
# This line broke pip so lets not use it for now
#pip install --upgrade pip
sudo pip install conan

echo "===== INSTALL ZERONET ====="
wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz
sudo tar xvpfz master.tar.gz

echo "===== UPDATE CMAKE (for trusty) ====="
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:george-edison55/cmake-3.x
sudo apt-get update

echo "===== INSTALL LIBTORRENT & LIBTORRENT PYTHON BINDINGS ====="
conan remote add libtorrent https://api.bintray.com/conan/rllola80/Libtorrent
cd /home/ubuntu/ZeroNet-master/plugins/Torrent
conan install --build=missing .
conan build .
