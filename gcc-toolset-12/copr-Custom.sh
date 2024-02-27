#! /bin/sh -x
#
#
#
#
wget https://mirror.stream.centos.org/9-stream/AppStream/source/tree/Packages/gcc-toolset-12-12.0-5.el9.src.rpm
rpm2cpio *.src.rpm | cpio -idmv
rm -f *.src.rpm gcc-toolset-12.spec
wget https://github.com/andykimpe/scl-php56/raw/master/gcc-toolset-12/gcc-toolset-12.spec -O gcc-toolset-12.spec
