#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: fedora-39-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/php-scl/fedora-39-x86_64/
# Build dependencies: scl-utils-build php56-runtime wget
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/scl-utils.spec -O scl-utils.spec
wget https://github.com/sclorg/scl-utils/archive/2.0.3/scl-utils-2.0.3.tar.gz -O scl-utils-2.0.3.tar.gz
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/macros.scl-filesystem -O macros.scl-filesystem
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch -O 0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2056462-do-not-error-out-on-SIGINT.patch -O BZ-2056462-do-not-error-out-on-SIGINT.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2091000-remove-tmp-file.patch -O BZ-2091000-remove-tmp-file.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/rpm419.patch -O rpm419.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/brp-python-hardlink.patch -O brp-python-hardlink.patch
