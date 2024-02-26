%global __cmake_in_source_build 1
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:       scl-utils

Epoch:      1
Version:    2.0.3
Release:    7%{?dist}
Summary:    Utilities for alternative packaging

License:    GPLv2+
URL:        https://github.com/sclorg/scl-utils
Source0:    https://github.com/sclorg/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    https://github.com/andykimpe/scl-php56/raw/master/macros.scl-filesystem
BuildRequires:	gcc make
BuildRequires:  cmake
BuildRequires:  rpm-devel
BuildRequires:  libcmocka libcmocka-devel environment-modules
Requires:   %{_bindir}/modulecmd

Patch1:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/0003-Scl-utils-layout-patch-from-fedora-famillecollet.com.patch
Patch2:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/BZ-2056462-do-not-error-out-on-SIGINT.patch
Patch3:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/BZ-2091000-remove-tmp-file.patch
Patch4:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/rpm419.patch
# commit https://patch-diff.githubusercontent.com/raw/sclorg/scl-utils/pull/43
# patch
# https://patch-diff.githubusercontent.com/raw/sclorg/scl-utils/pull/43.patch
Patch5:     https://github.com/andykimpe/scl-php56/raw/master/scl-utils/brp-python-hardlink.patch

%description
Run-time utility for alternative packaging.

%package build
Summary:    RPM build macros for alternative packaging
Requires:   iso-codes
Requires:   redhat-rpm-config

%description build
Essential RPM build macros for alternative packaging.

%prep
%autosetup -p1

%build
%if 0%{?rhel} == 6
echo "rhel 6"
echo "sleep 6000"
sleep 6000
%endif
%if 0%{?rhel} == 7
echo "rhel7"
echo "sleep 6000"
sleep 6000
%endif
%if 0%{?fedora} > 37 || 0%{?rhel} > 8
echo "new"
echo "sleep 6000"
sleep 6000
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
