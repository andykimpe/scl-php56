#! /bin/sh -x
#wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/copr-Custom.sh -O copr-Custom.sh
#bash copr-Custom.sh
#rm -f copr-Custom.sh
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/scl-utils.spec -O scl-utils.spec
wget https://github.com/sclorg/scl-utils/archive/refs/tags/2.0.3.tar.gz -O scl-utils-2.0.3.tar.gz
wget https://github.com/andykimpe/scl-utils/archive/refs/tags/2.0.4.tar.gz -O scl-utils-2.0.4.tar.gz
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/macros.scl-filesystem -O macros.scl-filesystem
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/scl_source -O scl_source
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch -O 0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2056462-do-not-error-out-on-SIGINT.patch -O BZ-2056462-do-not-error-out-on-SIGINT.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2091000-remove-tmp-file.patch -O BZ-2091000-remove-tmp-file.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/rpm419.patch -O rpm419.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/brp-python-hardlink.patch -O brp-python-hardlink.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/145b6ee3ebf4ff4f0735370473c44287248128a8.patch -O 145b6ee3ebf4ff4f0735370473c44287248128a8.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/for-el6-issues-9.patch -O for-el6-issues-9.patch
