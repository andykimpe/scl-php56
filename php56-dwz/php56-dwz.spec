%global debug_package %{nil}
%global __brp_check_rpaths %{nil}
%global _scl_prefix    /opt
%{?scl:%scl_package php56}
Summary: DWARF optimization and duplicate removal tool
Name: php56-dwz
Version: 0.12
Release: 2%{?dist}.sc1
License: GPLv2+ and GPLv3+
Group: Development/Tools
Source0: https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-7-dwz-0.12-1.el7.sc1.x86_64.rpm
BuildRoot: %(mktemp -ud %{_tmppath}/dwz-%{version}-%{release}-XXXXXX)
BuildRequires: cpio rpm rpm-build
BuildRequires: php56-macro
%{?scl:BuildRequires:%scl_runtime}
%{?scl:BuildRequires:scl-utils-build}

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup -q  -c -T -n dwz-%{version}
%build
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv
mkdir -p %{buildroot}/opt/php56/root/
cp -R %{buildroot}/opt/rh/devtoolset-7/root/* %{buildroot}/opt/php56/root/
rm -rf %{buildroot}/opt/rh/
cd %{buildroot}/opt/php56/root/usr/share/doc/
mv devtoolset-7-dwz-0.12 php56-dwz-0.12

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%doc COPYING COPYING3 COPYING.RUNTIME
/opt/php56/root/usr/share/doc/php56-dwz-0.12/COPYING
/opt/php56/root/usr/share/doc/php56-dwz-0.12/COPYING.RUNTIME
/opt/php56/root/usr/share/doc/php56-dwz-0.12/COPYING3
/opt/php56/root/usr/bin//dwz
/opt/php56/root/usr/share/man/man1/dwz.1.gz

%changelog
* Tue Jul 14 2015 Jakub Jelinek <jakub@redhat.com> 0.12-1
- fix up alignment of moved non-allocated sections and section header table

* Wed May 21 2014 Marek Polacek <polacek@redhat> 0.11-1.1
- add .1 to Release

* Tue Jul  2 2013 Jakub Jelinek <jakub@redhat.com> 0.11-1
- handle .gdb_index version 8 (#969454)

* Mon Mar 11 2013 Jakub Jelinek <jakub@redhat.com> 0.10-1
- when creating DW_AT_stmt_list, use DW_FORM_sec_offset for dwarf4
  and DW_FORM_data4 for dwarf[23] rather than vice versa (#919755)

* Mon Feb  4 2013 Jakub Jelinek <jakub@redhat.com> 0.9-1
- fix up handling of DIE equality if more than one DIE in the same
  CU compare equal (#889283)
- check DW_FORM_ref_addr properly during fi_multifile phase

* Thu Nov 29 2012 Jakub Jelinek <jakub@redhat.com> 0.8-1
- fix recompute_abbrevs (#880634)
- optimize DW_FORM_data[48] DW_AT_high_pc that GCC 4.8 produces

* Fri Aug 10 2012 Jakub Jelinek <jakub@redhat.com> 0.7-1
- fix iterative hasing on big-endian targets (#846685)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Jakub Jelinek <jakub@redhat.com> 0.6-1
- add --version/-v option support (Matt Newsome)
- fix building on RHEL 5

* Wed Jul  4 2012 Jakub Jelinek <jakub@redhat.com> 0.5-1
- handle .gdb_index version 7

* Fri Jun 22 2012 Jakub Jelinek <jakub@redhat.com> 0.4-1
- fix up DIE counting in low-mem mode for testing the -L limit

* Fri Jun 15 2012 Jakub Jelinek <jakub@redhat.com> 0.3-1
- update to dwz-0.3 (#830863)

* Mon Jun 11 2012 Jakub Jelinek <jakub@redhat.com> 0.2-1
- new package
