%global __cmake_in_source_build 1
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:       scl-utils
%if 0%{?rhel} == 6
Epoch:      1
Version:	20120927
Release:	30%{?dist}
Source0:	https://github.com/andykimpe/scl-utils/archive/refs/heads/scl-utils-20120927.tar.gz
Source1:	https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem
Source2:	https://github.com/andykimpe/scl-php56/raw/master/scl_source
Source3:	https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem.el6
Source4:    https://github.com/sclorg/scl-utils/archive/2.0.3/scl-utils-2.0.3.tar.gz
%endif
%if 0%{?rhel} == 7
Epoch:      1
Version:	20120927
Release:	30%{?dist}
Source0:	https://github.com/andykimpe/scl-utils/archive/refs/heads/scl-utils-20120927.tar.gz
Source1:	https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem.el6
Source2:	https://github.com/andykimpe/scl-php56/raw/master/scl_source
Source3:	https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem.el6
Source4:    https://github.com/andykimpe/scl-utils/archive/refs/heads/scl-utils-20120927.tar.gz
%endif
%if 0%{?fedora} > 36 || 0%{?rhel} > 7
Epoch:      1
Version:    2.0.3
Release:    7%{?dist}
Source0:    https://github.com/sclorg/scl-utils/archive/2.0.3/scl-utils-2.0.3.tar.gz
Source1:    https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem
Source3:	https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem.el6
Source4:    https://github.com/andykimpe/scl-utils/archive/refs/heads/scl-utils-20120927.tar.gz
%endif
Patch1:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
Patch2:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/BZ-2056462-do-not-error-out-on-SIGINT.patch
Patch3:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/BZ-2091000-remove-tmp-file.patch
Patch4:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/rpm419.patch
# commit https://patch-diff.githubusercontent.com/raw/sclorg/scl-utils/pull/43
# patch
# https://patch-diff.githubusercontent.com/raw/sclorg/scl-utils/pull/43.patch
Patch5:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/brp-python-hardlink.patch
Patch6: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0001-Add-all-the-collections-enabled-to-SCLS-env-variable.patch
Patch7: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0002-Allow-overriding-values-in-scl_package.patch
Patch8: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0003-Delete-unnecessary-argument-from-check_asprintf.patch
Patch9: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0004-scl-utils-free.patch
Patch10: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0005-Use-direct-path-when-calling-scl_enabled.patch
Patch11: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0006-Execute-enable-scriptlets-only-if-they-are-not-alrea.patch
Patch12: 	https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0007-Implement-as-a-command-separator.patch
Patch13:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0008-Changed-debuginfo-package-handling.patch
Patch14:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0009-Mention-environment-modifying-commands-in-the-man-pa.patch
Patch15:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0010-Changed-command-description-in-scl-man-pages.patch
Patch16:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0011-Added-capability-to-register-and-deregister-collecti.patch
Patch17:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0012-Fixed-dereferencing-of-null-pointer.patch
Patch18:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0013-Fixed_main_metapackage_dependencies.patch
Patch19:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0014-Add-capability-to-share-collections-using-nfs.patch
Patch20:    https://github.com/andykimpe/scl-php56/raw/master/scl-utils/scl-utils-20120927-shebang.patch

Summary:    Utilities for alternative packaging
License:    GPLv2+
URL:        https://github.com/sclorg/scl-utils

BuildRequires:	gcc make
BuildRequires:  cmake
BuildRequires:  rpm-devel
%if 0%{?fedora} > 36 || 0%{?rhel} > 7
BuildRequires:  libcmocka libcmocka-devel environment-modules
Requires:   %{_bindir}/modulecmd
%endif

%description
Run-time utility for alternative packaging.

%package build
Summary:    RPM build macros for alternative packaging
Requires:   iso-codes
Requires:   redhat-rpm-config

%description build
Essential RPM build macros for alternative packaging.

%prep
%if 0%{?rhel} == 6
%setup -q -n scl-utils-scl-utils-%{version}
%patch6 -p1 -b .all-collections
%patch7 -p1 -b .overriding
%patch8 -p1 -b .check-asprintf
%patch9 -p1
%patch10 -p1 -b .direct-path
%patch11 -p1 -b .enable-once
%patch12 -p1 -b .command-separator
%patch13 -p1 -b .debuginfo
%patch14 -p1 -b .man-env
%patch15 -p1 -b .man-command
%patch16 -p1 -b .register
%patch17 -p1 -b .deref
%patch18 -p1 -b .meta-deps
%patch19 -p1 -b .nfsmoutable
%patch20 -p1 -b .shebang
%endif
%if 0%{?rhel} == 7
%setup -q -n scl-utils-scl-utils-%{version}
%patch21 -p1 -b .Scl-utils-layout-patch-from-fedora-famillecollet.com
%patch22 -p1 -b .BZ-2056462-do-not-error-out-on-SIGINT
%patch23 -p1 -b .BZ-2091000-remove-tmp-file
%patch24 -p1 -b .rpm419
%patch25 -p1 -b .brp-python-hardlink
%endif
%if 0%{?fedora} > 36 || 0%{?rhel} > 7
%setup -q -n scl-utils-%{version}
%patch1 -p1 -b .Scl-utils-layout-patch-from-fedora-famillecollet.com
%patch2 -p1 -b .BZ-2056462-do-not-error-out-on-SIGINT
%patch3 -p1 -b .BZ-2091000-remove-tmp-file
%patch4 -p1 -b .rpm419
%patch5 -p1 -b .brp-python-hardlink
%endif





%setup -q  -c -T -n scl-utils-%{version}
%autosetup -p1

%build
%if 0%{?rhel} == 6
echo "rhel 6"
echo "sleep 600000"
sleep 600000
%endif
%if 0%{?rhel} == 7
echo "rhel7"
echo "sleep 600000"
sleep 600000
%endif
%if 0%{?fedora} > 36 || 0%{?rhel} > 7
echo "new"
echo "sleep 600000"
sleep 600000
%endif
%cmake .
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
if [ %{macrosdir} != %{_sysconfdir}/rpm ]; then
    mkdir -p %{buildroot}%{macrosdir}
    mv %{buildroot}%{_sysconfdir}/rpm/macros.scl %{buildroot}%{macrosdir}
    rmdir %{buildroot}%{_sysconfdir}/rpm
fi
cat %SOURCE1 >> %{buildroot}%{macrosdir}/macros.scl
mkdir -p %{buildroot}%{_sysconfdir}/scl
cd %{buildroot}%{_sysconfdir}/scl
mkdir modulefiles
mkdir prefixes
ln -s prefixes conf

%check
make check

%files
%dir %{_sysconfdir}/scl
%dir %{_sysconfdir}/scl/modulefiles
%dir %{_sysconfdir}/scl/prefixes
%{_sysconfdir}/scl/conf
%{_sysconfdir}/scl/func_scl.csh
%config %{_sysconfdir}/bash_completion.d/scl
%config %{_sysconfdir}/profile.d/scl-init.sh
%config %{_sysconfdir}/profile.d/scl-init.csh
%{_bindir}/scl
%{_bindir}/scl_enabled
%{_bindir}/scl_source
%{_mandir}/man1/scl.1.gz
%doc LICENSE

%files build
%{macrosdir}/macros.scl
%{_rpmconfigdir}/scldeps.sh
%{_rpmconfigdir}/fileattrs/scl.attr
%{_rpmconfigdir}/fileattrs/sclbuild.attr
%{_rpmconfigdir}/brp-scl-compress
%{_rpmconfigdir}/brp-scl-python-bytecompile


%changelog
