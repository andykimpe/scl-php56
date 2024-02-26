#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: fedora-39-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/php-scl/fedora-39-x86_64/
# Build dependencies: scl-utils-build php56-runtime wget
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/php56/php56.spec -O php56.spec
wget https://github.com/andykimpe/scl-php56/raw/master/php56/macros-build -O macros-build
wget https://github.com/andykimpe/scl-php56/raw/master/README -O README
wget https://github.com/andykimpe/scl-php56/raw/master/LICENSE -O LICENSE
