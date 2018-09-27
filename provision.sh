#!/usr/bin/env bash

echo "===== INSTALL DEPENDENCIES ====="
sudo apt update
sudo apt install -y python-pip msgpack-python python-gevent git
# apt install -y autoconf libtool build-essential libboost-all-dev libssl-dev
# This line broke pip so lets not use it for now
#pip install --upgrade --user pip
sudo pip install conan

echo "===== UPDATE CMAKE (for trusty) ====="
sudo apt purge cmake
wget https://cmake.org/files/v3.12/cmake-3.12.1-Linux-x86_64.tar.gz
tar -xvf cmake-3.12.1-Linux-x86_64.tar.gz
cd cmake-3.12.1-Linux-x86_64
sudo cp -r bin /usr/
sudo cp -r share /usr/
sudo cp -r doc /usr/share/
sudo cp -r man /usr/share/
cd ..
sudo rm -r cmake-3.12.1-Linux-x86_64

echo "===== INSTALL ZERONET ====="
wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz
sudo tar xvpfz master.tar.gz

echo "===== INSTALL LIBTORRENT & LIBTORRENT PYTHON BINDINGS ====="
conan remote add libtorrent https://api.bintray.com/conan/rllola80/Libtorrent
cd /home/vagrant/ZeroNet-master/plugins/Torrent
conan install --build=missing .
conan build .
