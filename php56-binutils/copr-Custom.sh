#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: fedora-39-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/php-scl/fedora-39-x86_64/
# Build dependencies: scl-utils-build php56-runtime wget
wget https://github.com/andykimpe/scl-php56/raw/master/php56-binutils/php56-binutils.spec -O php56-binutils.spec
wget https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-10-annobin-9.23-4.el7.1.x86_64.rpm -O devtoolset-10-annobin-9.23-4.el7.1.x86_64.rpm
wget https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-10-annobin-annocheck-9.23-4.el7.1.x86_64.rpm -O devtoolset-10-annobin-annocheck-9.23-4.el7.1.x86_64.rpm
