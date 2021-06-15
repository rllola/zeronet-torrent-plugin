libtorrent:
	git clone https://github.com/arvidn/libtorrent.git
	cd libtorrent && git submodule update --init
	cd libtorrent && git checkout v2.0.4

boost:
	wget -q https://boostorg.jfrog.io/artifactory/main/release/1.74.0/source/boost_1_74_0.tar.gz
	tar -zxf boost_1_74_0.tar.gz
	rm boost_1_74_0.tar.gz
	cd boost_1_74_0 && ./bootstrap.sh


build-libtorrent: boost
	cd libtorrent/bindings/python && ../../../boost_1_74_0/b2 release --debug-configuration crypto=openssl cxxstd=17 python=3.8 libtorrent-link=static boost-link=static
	cp libtorrent/bindings/python/bin/gcc-9/release/crypto-openssl/cxxstd-17-iso/libtorrent-python-pic-on/python-3.8/libtorrent.so lib/

config-linux:
	echo "using gcc ;" >> ~/user-config.jam
	echo "using python : 3.9 ;" >> ~/user-config.jam

config-os:
	echo "using darwin ;" >> ~/user-config.jam
	echo "using python : 3.9 ;" >> ~/user-config.jam

test:
	python3 test.py

clean:
	rm lib/*.so