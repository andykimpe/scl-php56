# rpmbuild parameters:
# --define "binutils_target arm-linux-gnu" to create arm-linux-gnu-binutils.
# --with=bootstrap: Build with minimal dependencies.
# --with=debug: Build without optimizations and without splitting the debuginfo.
# --without=docs: Skip building documentation.
# --without=testsuite: Do not run the testsuite.

# For DTS-7 on RHEL-6 we only support x86 and x86_64.
# For DTS-7 on RHEL-7 we also support ppc64, ppc64le, s390x and aarch64
%global debug_package %{nil}
%global _scl_prefix    /opt

%{?scl:%{?scl_package:%scl_package binutils}}

Summary: A GNU collection of binary utilities
Name: %{?scl_prefix}binutils
Version: 2.28
Release: 8%{?dist}.sc1
License: GPLv3+
Group: Development/Tools
URL: http://sources.redhat.com/binutils
Source0: https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-7-binutils-2.28-8.el7.sc1.x86_64.rpm
Source1: https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-7-binutils-devel-2.28-8.el7.sc1.x86_64.rpm
BuildRequires: cpio rpm rpm-build
%{?scl:BuildRequires:%scl_runtime}
%{?scl:BuildRequires:scl-utils-build}

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%package devel
Summary: BFD and opcodes static and dynamic libraries and header files
Group: System Environment/Libraries
# Note, this provide:
#   Provides: binutils-static = %{version}-%{release}
# has been suppressed so that the DTS version does not provide
# a version of the binutils that another package cannot use.
# See:  https://bugzilla.redhat.com/show_bug.cgi?id=1485002
# for more details.
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: zlib-devel
Requires: %{?scl_prefix}binutils = %{version}-%{release}
# BZ 1215242: We need touch...
Requires: coreutils

%description devel
This package contains BFD and opcodes static and dynamic libraries.

The dynamic libraries are in this package, rather than a seperate
base package because they are actually linker scripts that force
the use of the static libraries.  This is because the API of the
BFD library is too unstable to be used dynamically.

The static libraries are here because they are now needed by the
dynamic libraries.

Developers starting new projects are strongly encouraged to consider
using libelf instead of BFD.

%prep
%setup -q  -c -T -n binutils-%{version}
%build
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv
rpm2cpio %{SOURCE1} | cpio -idmv

%clean
rm -rf %{buildroot}

%post
#%if "%{build_gold}" == "both"
#%__rm -f %{_bindir}/%{?cross}ld
#%{alternatives_cmdline} --install %{_bindir}/%{?cross}ld %{?cross}ld \
#  %{_bindir}/%{?cross}ld.bfd %{ld_bfd_priority}
#%{alternatives_cmdline} --install %{_bindir}/%{?cross}ld %{?cross}ld \
#  %{_bindir}/%{?cross}ld.gold %{ld_gold_priority}
#%{alternatives_cmdline} --auto %{?cross}ld
#%endif
/sbin/ldconfig
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/as.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/ld.info.gz
exit 0

%preun
#%if "%{build_gold}" == "both"
#if [ $1 = 0 ]; then
#  %{alternatives_cmdline} --remove %{?cross}ld %{_bindir}/%{?cross}ld.bfd
#  %{alternatives_cmdline} --remove %{?cross}ld %{_bindir}/%{?cross}ld.gold
#fi
#%endif
if [ $1 = 0 ]; then
  if [ -e %{_infodir}/binutils.info.gz ]
  then
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/as.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/ld.info.gz
  fi
fi
exit 0


%postun -p /sbin/ldconfig


%files -f binutils.lang
%defattr(-,root,root,-)
#%license COPYING COPYING3 COPYING3.LIB COPYING.LIB
#%doc README
#%{_bindir}/%{?cross}[!l]*
#%if "%{build_gold}" == "both"
#%{_bindir}/%{?cross}ld.*
#%ghost %{_bindir}/%{?cross}ld
#%else
#%{_bindir}/%{?cross}ld*
#%endif
#%{_mandir}/man1/*
#%if %{enable_shared}
#%{_libdir}/lib*.so
#%exclude %{_libdir}/libbfd.so
#%exclude %{_libdir}/libopcodes.so
#%endif
#
#%if %{isnative}
#%if %{with docs}
#%{_infodir}/[^b]*info*
#%{_infodir}/binutils*info*
#%endif

%files devel
%defattr(-,root,root,-)
#%{_prefix}/include/*
#%{_libdir}/lib*.a
#%{_libdir}/libbfd.so
#%{_libdir}/libopcodes.so
#%if %{with docs}
#%{_infodir}/bfd*info*
#%endif # with docs
#%endif # %{isnative}

%changelog
* Thu Aug 31 2017 Nick Clifton  <nickc@redhat.com> 2.28-8
- Remove the Provides line from the spec file.
  (#1485002)

* Thu Jul 20 2017 Nick Clifton  <nickc@redhat.com> 2.28-7
- Add support for displaying new DWARF5 tags.
  (#1472955)

* Wed Jul 19 2017 Nick Clifton  <nickc@redhat.com> 2.28-6
- Fix s390 assembler so that it remove fake local symbols from its output.
  (#1460254)
  (#1472486)

* Mon Jun 26 2017 Nick Clifton  <nickc@redhat.com> 2.28-5
- Add support for LNIA instruction to PowerPC assembler.
  (#1357021)

* Thu Jun 15 2017 Nick Clifton  <nickc@redhat.com> 2.28-4
- Update patch to fix AArch64 copy reloc generation.
  (#1452170)

* Fri Jun 09 2017 Nick Clifton  <nickc@redhat.com> 2.28-3
- Ignore duplicate indirect symbols generated by the GOLD linker.
  (#1458003)

* Thu Jun 08 2017 Nick Clifton  <nickc@redhat.com> 2.28-2
- Eliminate the generation of incorrect dynamic copy relocations on AArch64.
  (#1452170)

* Mon May 22 2017 Nick Clifton <polacek@redhat.com> 2.28-1
- Rebase to FSF binutils 2.28
- Retire: binutils-2.23.52.0.1-addr2line-dynsymtab.patch
- Retire: binutils-2.27-local-dynsym-count.patch
- Retire: binutils-2.27-monotonic-section-offsets.patch
- Retire: binutils-2.27-aarch64-relro-default.patch
- Retire: binutils-2.27-power9.patch
- Import FSF binutils patch to fix running readelf on debug info binaries.
- Import FSF binutils patch to fix an abort with PowerPC dynamic relocs.
- Backport patch to add support for putting name, comp_dir and
  producer strings into the .debug_str section. 
- Add support for GNU BUILD NOTEs.

* Thu May 18 2017 Nick Clifton <polacek@redhat.com> 2.27-12
- Revert H.J.Lu's PLT elision patch.
  (#1452111)

* Thu Jan 12 2017 Nick Clifton  <nickc@redhat.com> 2.27-11
- Version bump to allow rebuild for DTS 6.1

* Wed Sep 28 2016 Nick Clifton  <nickc@redhat.com> 2.27-10
- Use correct default sysroot for native targets.
- Add Power9 ISA 3.0 support.

* Mon Sep 05 2016 Carlos O'Donell <carlos@redhat.com>  2.27-9
- Enable '--sysroot' option support for all configurations.

* Thu Sep 01 2016 Nick Clifton  <nickc@redhat.com> 2.27-8
- Properly disable the default generation of compressed debug sections.
  (#1366182)

* Thu Aug 18 2016 Nick Clifton  <nickc@redhat.com> 2.27-7
- Allow -z relro to be enabled by default for the AArch64 target.
  (#1367862)

* Wed Aug 17 2016 Nick Clifton  <nickc@redhat.com> 2.27-6
- Move .shstrtab section to end of section list so that the monotonic ordering of section offsets is restored.
  (#1366145)

* Fri Aug 12 2016 Nick Clifton  <nickc@redhat.com> 2.27-5
- Fix the computation of the sh_info field in the header of the .dynsym section.
  (#1366185)

* Thu Aug 04 2016 Nick Clifton  <nickc@redhat.com> 2.27-4
- Rebase on official FSF binutils 2.27 release.
  (#1358353)

* Thu Jul 21 2016 Nick Clifton  <nickc@redhat.com> 2.27-3
- Version bump so that the Brew build can be rerun, this time including ppc64 (big-endian)
  (#1358353)

* Wed Jul 20 2016 Nick Clifton  <nickc@redhat.com> 2.27-2
- Remove sim sources from tarball.
  (#1358353)

* Mon Jul 18 2016 Nick Clifton  <nickc@redhat.com> 2.27-1
- Rebase on FSF binutils 2.27 release. (#1356661)
- Retire: binutils-2.20.51.0.10-copy-osabi.patch
- Retire: binutils-2.23.2-aarch64-em.patch
- Retire: binutils-2.23.51.0.3-arm-ldralt.patch
- Retire: binutils-2.23.52.0.1-revert-pr15149.patch
- Retire: binutils-2.25.1-gold-testsuite-fixes.patch
- Retire: binutils-2.25-kernel-ld-r.bugfix.patch
- Retire: binutils-2.25-kernel-ld-r.patch
- Retire: binutils-2.25-only-keep-debug.patch
- Retire: binutils-2.25-x86_64-pie-relocs.patch
- Retire: binutils-pr18879.patch
- Retire: binutils-rh1224751.patch
- Retire: binutils-rh1309347.patch
- Retire: binutils-rh895241.patch

* Mon Apr 04 2016 Patsy Franklin <pfrankli@redhat.com> 2.25.1-10
- Fix a case where a string was being used after the memory
  containing the string had been freed.

* Wed Mar 02 2016 Nick Clifton <nickc@redhat.com> 2.25.1-9
- Bump release number by 2 in order to enable build.

* Wed Mar 02 2016 Nick Clifton <nickc@redhat.com> 2.25.1-7
- Fix GOLD testsuite failures.
  (#1312376)

* Thu Feb 25 2016 Nick Clifton <nickc@redhat.com> 2.25.1-6
- Change ar's default to be the creation of non-deterministic archives.

* Thu Feb 18 2016 Nick Clifton <nickc@redhat.com> 2.25.1-4
- Add support for Intel Memory Protection Key instructions.
  (#1309347)

* Thu Feb 04 2016 Nick Clifton <nickc@redhat.com> 2.25.1-2
- Import patch for FSF PR 18879
  (#1260034)

* Thu Jan 14 2016 Nick Clifton <nickc@redhat.com> 2.25.1-1
- Rebase on FSF binutils 2.25.1 release.
- Retire patch binutils-2.25-x86_64-pie-relocs.patch

* Tue Sep 22 2015 Nick Clifton <nickc@redhat.com> 2.25-10
- Improved patch to preserve the sh_link and sh_info fields in stripped ELF sections.
  (#1246390)

* Wed Aug 5 2015 Nick Clifton <nickc@redhat.com> 2.25-9
- Import patch from FSF to preserve the sh_link and sh_info fields in stripped ELF sections.
  (#1246390)

* Tue Aug 4 2015 Jeff Law <law@redhat.com> 2.25-8
- Backport Cary's patch to silence pedantic warning in gold
  (#895241)

* Thu Jun 4 2015 Jeff Law <law@redhat.com> 2.25-7
- Resync with Fedora (binutils-2.25)
  Reapply DTS specific patches
  Backport testsuite patch to fix gold testsuite failure
  
