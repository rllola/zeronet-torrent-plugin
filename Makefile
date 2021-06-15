libtorrent: boost
	git clone https://github.com/arvidn/libtorrent.git
	cd libtorrent && git submodule update --init
	cd libtorrent && git checkout v2.0.4

boost:
	wget -q https://boostorg.jfrog.io/artifactory/main/release/1.74.0/source/boost_1_74_0.tar.gz
	tar -zxf boost_1_74_0.tar.gz
	rm boost_1_74_0.tar.gz
	echo "using python : 3.8 ;" >> ~/user-config.jam
	cd boost_1_74_0 && ./bootstrap.sh --with-python=/usr/local/bin/python3


build-libtorrent:
	cd libtorrent/bindings/python && ../../../boost_1_74_0/b2 release --debug-configuration crypto=openssl cxxstd=17 python=3.8 libtorrent-link=static boost-link=static
	cp libtorrent/bindings/python/bin/gcc-9/release/crypto-openssl/cxxstd-17-iso/libtorrent-python-pic-on/python-3.8/libtorrent.so lib/

test:
	python3 test.py

clean:
	rm lib/*.so