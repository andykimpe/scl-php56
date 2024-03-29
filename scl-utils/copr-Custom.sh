#! /bin/sh -x
#wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/copr-Custom.sh -O copr-Custom.sh
#bash copr-Custom.sh
#rm -f copr-Custom.sh
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/scl-utils.spec -O scl-utils.spec
wget https://github.com/sclorg/scl-utils/archive/2.0.3/scl-utils-2.0.3.tar.gz -O scl-utils-2.0.3.tar.gz
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/macros.scl-filesystem -O macros.scl-filesystem
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/scl_source -O scl_source
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/macros.scl-filesystem.el6 -O macros.scl-filesystem.el6
wget https://github.com/andykimpe/scl-utils/archive/refs/tags/20120927.tar.gz -O scl-utils-20120927.tar.gz
wget https://github.com/andykimpe/scl-utils/archive/refs/heads/scl-utils-20130529.tar.gz -O scl-utils-20130529.tar.gz
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/scl_source.el7 -O scl_source.el7
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/macros.scl-filesystem.el7 -O macros.scl-filesystem.el7
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch -O 0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2056462-do-not-error-out-on-SIGINT.patch -O BZ-2056462-do-not-error-out-on-SIGINT.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/BZ-2091000-remove-tmp-file.patch -O BZ-2091000-remove-tmp-file.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/rpm419.patch -O rpm419.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/brp-python-hardlink.patch -O brp-python-hardlink.patch
wget https://raw.githubusercontent.com/andykimpe/scl-php56/master/scl-utils/0001-Add-all-the-collections-enabled-to-SCLS-env-variable.patch -O 0001-Add-all-the-collections-enabled-to-SCLS-env-variable.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0002-Allow-overriding-values-in-scl_package.patch -O 0002-Allow-overriding-values-in-scl_package.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0003-Delete-unnecessary-argument-from-check_asprintf.patch -O 0003-Delete-unnecessary-argument-from-check_asprintf.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0004-scl-utils-free.patch -O 0004-scl-utils-free.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0005-Use-direct-path-when-calling-scl_enabled.patch -O 0005-Use-direct-path-when-calling-scl_enabled.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0006-Execute-enable-scriptlets-only-if-they-are-not-alrea.patch -O 0006-Execute-enable-scriptlets-only-if-they-are-not-alrea.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0007-Implement-as-a-command-separator.patch -O 0007-Implement-as-a-command-separator.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0008-Changed-debuginfo-package-handling.patch -O 0008-Changed-debuginfo-package-handling.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0009-Mention-environment-modifying-commands-in-the-man-pa.patch -O 0009-Mention-environment-modifying-commands-in-the-man-pa.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0010-Changed-command-description-in-scl-man-pages.patch -O 0010-Changed-command-description-in-scl-man-pages.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0011-Added-capability-to-register-and-deregister-collecti.patch -O 0011-Added-capability-to-register-and-deregister-collecti.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0012-Fixed-dereferencing-of-null-pointer.patch -O 0012-Fixed-dereferencing-of-null-pointer.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0013-Fixed_main_metapackage_dependencies.patch -O 0013-Fixed_main_metapackage_dependencies.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0014-Add-capability-to-share-collections-using-nfs.patch -O 0014-Add-capability-to-share-collections-using-nfs.patch
wget https://github.com/andykimpe/scl-php56/raw/master/scl-utils/scl-utils-20120927-shebang.patch -O scl-utils-20120927-shebang.patch
wget https://github.com/andykimpe/scl-utils/commit/145b6ee3ebf4ff4f0735370473c44287248128a8.patch -O 145b6ee3ebf4ff4f0735370473c44287248128a8.patch
