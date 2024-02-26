#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: fedora-39-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/php-scl/fedora-39-x86_64/
# Build dependencies: scl-utils-build php56-runtime wget
wget https://github.com/andykimpe/scl-php56/raw/master/php56-dwz/php56-dwz.spec -O php56-dwz.spec
wget https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-7-dwz-0.12-1.el7.sc1.x86_64.rpm -O devtoolset-7-dwz-0.12-1.el7.sc1.x86_64.rpm
