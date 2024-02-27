#! /bin/sh -x
wget https://mirror.stream.centos.org/9-stream/AppStream/source/tree/Packages/gcc-toolset-12-12.0-5.el9.src.rpm
rpm2cpio *.src.rpm | cpio -idmv
rm -f *.src.rpm
