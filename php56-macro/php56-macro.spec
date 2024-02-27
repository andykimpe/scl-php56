%global debug_package %{nil}
%global __brp_check_rpaths %{nil}
%global _scl_prefix    /opt

Summary: macro for php56 scl
Name: php56-macro
Version: 1.0
Release: 1%{?dist}
License: GPLv3+
Group: Development/Tools
URL: https://github.com/andykimpe/scl-php56
Source0: macro.php56
BuildRequires: coreutils binutils rpm rpm-build

%description
macro for php56 scl.

%prep
%setup -q  -c -T -n php56-macro-%{version}
%build
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cp %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_rpmconfigdir}/macros.d/macro.php56

%changelog
