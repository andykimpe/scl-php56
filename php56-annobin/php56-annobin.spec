
%define __python /opt/rh/gcc-toolset-9/root/usr/bin/python3
%{?scl:%scl_package annobin}
%global _scl_prefix    /opt/

Name:    %{?scl_prefix}annobin
Summary: Annotate and examine compiled binary files
Version: 9.23
Release: 4%{?dist}
License: GPLv3+
# ProtocolURL: https://fedoraproject.org/wiki/Toolchain/Watermark
# Maintainer: nickc@redhat.com

#---------------------------------------------------------------------------------

Source0:  https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-10-annobin-9.23-4.el7.1.x86_64.rpm
Source1:  https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/sclo/x86_64/rh/Packages/d/devtoolset-10-annobin-annocheck-9.23-4.el7.1.x86_64.rpm

#---------------------------------------------------------------------------------

BuildRequires: cpio rpm rpm-build
%{?scl:BuildRequires:%scl_runtime}
%{?scl:BuildRequires:scl-utils-build}

#%define gcc_for_annobin %{?_scl_root}/usr/bin/gcc
#%define gxx_for_annobin %{?_scl_root}/usr/bin/g++

%description
Provides a plugin for GCC that records extra information in the files
that it compiles.

Note - the plugin is automatically enabled in gcc builds via flags
provided by the redhat-rpm-macros package.

#---------------------------------------------------------------------------------

BuildRequires: elfutils-debuginfod-client-devel


#---------------------------------------------------------------------------------

%package annocheck
Summary: A tool for checking the security hardening status of binaries

BuildRequires: gcc elfutils elfutils-devel elfutils-libelf-devel rpm-devel binutils-devel
BuildRequires: elfutils-debuginfod-client-devel

%description annocheck
Installs the annocheck program which uses the notes generated by annobin to
check that the specified files were compiled with the correct security
hardening options.


#---------------------------------------------------------------------------------



#---------------------------------------------------------------------------------

%prep

# %%autosetup -p1
%setup -q  -c -T -n annobin-%{version}

%build


#---------------------------------------------------------------------------------

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv
rpm2cpio %{SOURCE1} | cpio -idmv

#---------------------------------------------------------------------------------


%files
#%{ANNOBIN_GCC_PLUGIN_DIR}
#%license COPYING3 LICENSE
#%exclude %{_datadir}/doc/annobin-plugin/COPYING3
#%exclude %{_datadir}/doc/annobin-plugin/LICENSE
#%doc %{_datadir}/doc/annobin-plugin/annotation.proposal.txt
#%{_infodir}/annobin.info*
#%{_mandir}/man1/annobin.1*
#%{_mandir}/man1/built-by.1*
#%{_mandir}/man1/check-abi.1*
#%{_mandir}/man1/hardened.1*
#%{_mandir}/man1/run-on-binaries-in.1*

#%if %{with clangplugin}
#%{ANNOBIN_CLANG_PLUGIN_DIR}
#%endif
#%if %{with llvmplugin}
#%{ANNOBIN_CLANG_PLUGIN_DIR}
#%endif

#%if %{with annocheck}
%files annocheck
#%{_bindir}/annocheck
#%{_mandir}/man1/annocheck.1*
#%endif

#---------------------------------------------------------------------------------

%changelog
* Thu Feb 18 2021 Nick Clifton <nickc@redhat.com> - 9.23-4
- NVR bump to allow rebuilding against the latest DTS-10 gcc.

* Mon Aug 10 2020 Nick Clifton <nickc@redhat.com> - 9.23-3
- Improve results when running annobin rpms through annocheck.  (#1866825)

* Thu Aug 06 2020 Martin Cermak <mcermak@redhat.com> - 9.23-2
- Fix rhbz1866774

* Mon Jul 13 2020 Nick Clifton <nickc@redhat.com> - 9.23-1
- INITIAL CREATION OF DTS-10 ANNOBIN. (#1852725)
- Annocheck: Do not skip tests of the short-enums notes.  (#1743635)
- Add (optional) llvm plugin.
  9.21-3
- Fix the computations of ANNOBIN_GCC_PLUGIN_DIR and ANNOBIN_CLANG_PLUGIN_DIR.
  9.21-1
- Fix stack clash protection problem. (#1803173)
  9.21-1
- Annobin: Fall back on using the flags if the option cannot be found in cl_options.  (#1817659)
  9.20-1
- Annocheck: Detect Fortran compiled programs.  (#1824393)
  9.19-1
- Annobin: If option name mismatch occurs, seach for the real option.  (#1817452)
  9.18-1
- Annocheck: Fix a division by zero error when parsing GO binaries.  (#1818863)
  9.16-1
- Annobin: Fix access to the -flto and -fsanitize flags.
  9.14-1
- Annobin: Use offsets stored in gcc's cl_option structure to access the global_options array, thus removing the need to check for changes in the size of this structure.
  9.13-1
- Rename gcc plugin directory to gcc-plugin.
- Stop annocheck from complaining about missing options when the binary has been built in a mixed environment.
  9.12-1
- Improve builtby tool.
- Stop annocheck complaining about missing notes when the binary is not compiled by either gcc or clang.
- Skip the check of the ENTRY instruction for binaries not compiled by gcc or clang.  (#1809656)
  9.11-1
- Fix infinite loop hangup in annocheck.
- Disable debuginfod support by default.
- Improve parsing of .comment section.
  9.10-1
- Fix clang plugin to use hidden symbols.
  9.09-1
- Add ability to build clang plugin (disabled by default).
  9.08-1
- Annocheck: Fix error printing out the version number.
  9.07-1
- Annobin: Add checks of the exact location of the examined switches.
  9.06-1
- Annobin: Note when stack clash notes are generated.
- Annocheck: Handle multiple builder IDs in the .comment section.
  9.05-1
- Add configure option to suppress building annocheck.
  9.04-1
- Fix debuginfod test.
  9.03-2
- Correct the build requirement for building with debuginfod support.
  9.03-1
- Add debuginfod support.
  9.01-1
- Add clang plugin (experimental).
  8.92-1
- Have annocheck ignore notes with an end address of 0.
  8.91-1
- Improve checking of gcc versions.
  8.90-1
- Do not skip positive results.
  8.88-1
- Generate a WARN result for code compiled with instrumentation enabled.  (#1753918)
  8.87-1
- Replace address checks with dladdr1.
  8.86-1
- Use libabigail like checking to ensure variable address consistency.
  8.85-1
- Skip generation of global notes for hot/cold sections.
  8.84-1
- Generate FAIL results if -Wall or -Wformat-security are missing.
  8.83-1
- If notes cannot be found in the executable look for them in the debuginfo file, if available.
- Generate a FAIL if notes are missing from the executable/debuginfo file.
- Record and report the setting of the AArcht64 specific -mbranch-protection option.
  8.81-1
- Improve detection of GO binaries.
- Add gcc version information to annobin notes.
- Do not complain about missing FORTIFY_SOURCE and GLIBCXX_ASSERTIONS in LTO compilations.

* Wed Aug 21 2019 Nick Clifton <nickc@redhat.com> - 8.79-2
- INITIAL CREATION OF DTS-9 ANNOBIN.

* Thu Aug 08 2019 Nick Clifton <nickc@redhat.com> - 8.79-2
- Import the missing tests/ sub-directory.

* Thu Aug 08 2019 Nick Clifton <nickc@redhat.com> - 8.79-1
- Allow the compiler used to run tests to be specified on the command line.

* Tue Aug 06 2019 Nick Clifton <nickc@redhat.com> - 8.78-1
- Fix a memory allocation error in the annobin plugin.  (#1737306)

* Tue Jul 23 2019 Nick Clifton <nickc@redhat.com> - 8.77-4
- Change the requirement of gcc-toolset-9 to gcc-toolset-9-gcc.  (#1732767)

* Tue Jul 23 2019 Nick Clifton <nickc@redhat.com> - 8.77-2
- Version bump to allow rebuilding with scl_prefix.

* Tue Jul 23 2019 Nick Clifton <nickc@redhat.com> - 8.77-1
- gcc-toolset-9: INITIAL IMPORT OF ANNOBIN FROM RAWHIDE.  (#1730483)

* Mon Jun 24 2019 Nick Clifton <nickc@redhat.com> - 8.77-1
- Another attempt at fixing the detection and reporting of missing -D_FORTIFY_SOURCE options.  (#1703500)

* Mon Jun 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.76-4
- Rebuild for RPM 4.15

* Mon Jun 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.76-3
- Rebuild for RPM 4.15

* Thu Jun 06 2019 Panu Matilainen <pmatilai@redhat.com> - 8.76-2
- Really enable annocheck sub-package

* Tue Apr 30 2019 Nick Clifton <nickc@redhat.com> - 8.76-1
- Report a missing -D_FORTIFY_SOUCRE option if -D_GLIBCXX_ASSERTIONS was detected.  (#1703499)
- Do not report problems with -fstack-protection if the binary was not built by gcc or clang.  (#1703788)    

* Fri Apr 26 2019 Nick Clifton <nickc@redhat.com> - 8.74-1
- Add tests of clang command line options recorded in the DW_AT_producer attribute.

* Wed Apr 24 2019 Nick Clifton <nickc@redhat.com> - 8.73-1
- Fix test for an executable stack segment.  (#1700924)

* Thu Apr 18 2019 Nick Clifton <nickc@redhat.com> - 8.72-1
- Rebuild annobin with the latest rawhide gcc sources.  (#1700923)

* Thu Feb 28 2019 Nick Clifton <nickc@redhat.com> - 8.71-1
- Annobin: Suppress more calls to free() which are triggering memory checker errors.  (#1684148)

* Fri Feb 01 2019 Nick Clifton <nickc@redhat.com> - 8.70-1
- Add section flag matching ability to section size tool.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Björn Esser <besser82@fedoraproject.org> - 8.69-6
- Use 'with' for rich dependency on gcc

* Tue Jan 29 2019 Björn Esser <besser82@fedoraproject.org> - 8.69-5
- Really fix rhbz#1607430.

* Mon Jan 28 2019 Björn Esser <besser82@fedoraproject.org> - 8.69-4
- Rebuilt with annotations enabled

* Mon Jan 28 2019 Björn Esser <besser82@fedoraproject.org> - 8.69-3
- Fix rpm query for gcc version.

* Mon Jan 28 2019 Nick Clifton <nickc@redhat.com> - 8.69-2
- Add an exact requirement on the major version of gcc. (#1607430)

* Thu Jan 24 2019 Nick Clifton <nickc@redhat.com> - 8.69-1
- Annobin: Add support for .text.startup and .text.exit sections generated by gcc 9.
- Annocheck: Add a note displaying tool.

* Wed Jan 23 2019 Nick Clifton <nickc@redhat.com> - 8.68-1
- Annocheck: Skip checks for -D_FORTIFY_SOURCE and -D_GLIBCXX_ASSERTIONS if there is no compiler generated code in the binary.

* Mon Jan 21 2019 Björn Esser <besser82@fedoraproject.org> - 8.67-3
- Rebuilt with annotations enabled

* Mon Jan 21 2019 Björn Esser <besser82@fedoraproject.org> - 8.67-2
- Rebuilt for GCC 9

* Thu Jan 17 2019 Nick Clifton <nickc@redhat.com> - 8.67-1
- Annocheck: Only skip specific checks for specific symbols.  (#1666823)
- Annobin: Record the setting of the -fomit-frame-pointer option.

* Wed Jan 02 2019 Nick Clifton <nickc@redhat.com> - 8.66-1
- Annocheck: Do not ignore -Og when checking to see if an optimization level has been set.  (#1624162)

* Tue Dec 11 2018 Nick Clifton <nickc@redhat.com> - 8.65-1
- Annobin: Fix handling of multiple .text.unlikely sections.

* Fri Nov 30 2018 Nick Clifton <nickc@redhat.com> - 8.64-1
- Annocheck: Skip gaps in PPC64 executables covered by start_bcax_ symbols.  (#1630564)

* Mon Nov 26 2018 Nick Clifton <nickc@redhat.com> - 8.63-1
- Annocheck: Disable ENDBR test for shared libraries.  (#1652925)

* Mon Nov 26 2018 Nick Clifton <nickc@redhat.com> - 8.62-1
- Annocheck: Add test for ENDBR instruction at entry address of x86/x86_64 executables.  (#1652925)

* Tue Nov 20 2018 David Cantrell <dcantrell@redhat.com> - 8.61-2
- Adjust how the gcc_vr macro is set.

* Mon Nov 19 2018 Nick Clifton <nickc@redhat.com> - 8.61-1
- Fix building with gcc version 4.

* Tue Nov 13 2018 Nick Clifton <nickc@redhat.com> - 8.60-1
- Skip -Wl,-z,now and -Wl,-z,relro checks for non-gcc produced binaries.  (#1624421)

* Mon Nov 05 2018 Nick Clifton <nickc@redhat.com> - 8.59-1
- Ensure GNU Property notes are 8-byte aligned in x86_64 binaries.  (#1645817)

* Thu Oct 18 2018 Nick Clifton <nickc@redhat.com> - 8.58-1
- Skip PPC64 linker stubs created in the middle of text sections (again). (#1630640)

* Thu Oct 18 2018 Nick Clifton <nickc@redhat.com> - 8.57-1
- Suppress free of invalid pointer. (#1638371)

* Thu Oct 18 2018 Nick Clifton <nickc@redhat.com> - 8.56-1
- Skip PPC64 linker stubs created in the middle of text sections. (#1630640)

* Tue Oct 16 2018 Nick Clifton <nickc@redhat.com> - 8.55-1
- Reset the (PPC64) section start symbol to 0 if its section is empty.  (#1638251)

* Thu Oct 11 2018 Nick Clifton <nickc@redhat.com> - 8.53-1
- Also skip virtual thinks created by G++.  (#1630619)

* Wed Oct 10 2018 Nick Clifton <nickc@redhat.com> - 8.52-1
- Use uppercase for all fail/mayb/pass results.  (#1637706)

* Wed Oct 10 2018 Nick Clifton <nickc@redhat.com> - 8.51-1
- Generate notes for unlikely sections.  (#1630620)

* Mon Oct 08 2018 Nick Clifton <nickc@redhat.com> - 8.50-1
- Fix edge case computing section names for end symbols.  (#1637039)

* Mon Oct 08 2018 Nick Clifton <nickc@redhat.com> - 8.49-1
- Skip dynamic checks for binaries without a dynamic segment.  (#1636606)

* Fri Oct 05 2018 Nick Clifton <nickc@redhat.com> - 8.48-1
- Delay generating attach_to_group directives until the end of the compilation.  (#1636265)

* Mon Oct 01 2018 Nick Clifton <nickc@redhat.com> - 8.47-1
- Fix bug introduced in previous delta which would trigger a seg-fault when scanning for gaps.

* Mon Oct 01 2018 Nick Clifton <nickc@redhat.com> - 8.46-1
- Annobin:   Fix section name selection for startup sections.
- Annocheck: Improve gap skipping heuristics.   (#1630574)

* Mon Oct 01 2018 Nick Clifton <nickc@redhat.com> - 8.45-1
- Fix function section support (again).   (#1630574)

* Fri Sep 28 2018 Nick Clifton <nickc@redhat.com> - 8.44-1
- Skip compiler option checks for non-GNU producers.  (#1633749)

* Wed Sep 26 2018 Nick Clifton <nickc@redhat.com> - 8.43-1
- Fix function section support (again).   (#1630574)

* Tue Sep 25 2018 Nick Clifton <nickc@redhat.com> - 8.42-1
- Ignore ppc64le notes where start = end + 2.  (#1632259)

* Tue Sep 25 2018 Nick Clifton <nickc@redhat.com> - 8.41-1
- Make annocheck ignore symbols suffixed with ".end".  (#1639618)

* Mon Sep 24 2018 Nick Clifton <nickc@redhat.com> - 8.40-1
- Reinstate building annobin with annobin enabled.  (#1630550)

* Fri Sep 21 2018 Nick Clifton <nickc@redhat.com> - 8.39-1
- Tweak tests.

* Fri Sep 21 2018 Nick Clifton <nickc@redhat.com> - 8.38-1
- Generate notes and groups for .text.hot and .text.unlikely sections.
- When -ffunction-sections is active, put notes for startup sections into .text.startup.foo rather than .text.foo.
- Similarly put exit section notes into .text.exit.foo.  (#1630574)
- Change annocheck's maybe result for GNU Property note being missing into a PASS if it is not needed and a FAIL if it is needed.

* Wed Sep 19 2018 Nick Clifton <nickc@redhat.com> - 8.37-1
- Make the --skip-* options skip all messages about the specified test.

* Tue Sep 18 2018 Nick Clifton <nickc@redhat.com> - 8.36-1
- Improve error message when an ET_EXEC binary is detected.

* Mon Sep 17 2018 Nick Clifton <nickc@redhat.com> - 8.35-1
- Skip failures for PIC vs PIE.  (#1629698)

* Mon Sep 17 2018 Nick Clifton <nickc@redhat.com> - 8.34-1
- Ensure 4 byte alignment of note sub-sections.  (#1629671)

* Wed Sep 12 2018 Nick Clifton <nickc@redhat.com> - 8.33-1
- Add timing tool to report on speed of the checks.
- Add check for conflicting use of the -fshort-enum option.
- Add check of the GNU Property notes.
- Skip check for -O2 if compiled with -Og.  (#1624162)

* Mon Sep 03 2018 Nick Clifton <nickc@redhat.com> - 8.32-1
- Add test for ET_EXEC binaries.  (#1625627)
- Document --report-unknown option.

* Thu Aug 30 2018 Nick Clifton <nickc@redhat.com> - 8.31-1
- Fix bug in hardened tool which would skip gcc compiled files if the notes were too small.
- Fix bugs in section-size tool.
- Fix bug in built-by tool.

* Wed Aug 29 2018 Nick Clifton <nickc@redhat.com> - 8.30-1
- Generate notes for comdat sections. (#1619267)

* Thu Aug 23 2018 Nick Clifton <nickc@redhat.com> - 8.29-1
- Add more names to the gap skip list. (#1619267)

* Thu Aug 23 2018 Nick Clifton <nickc@redhat.com> - 8.28-1
- Skip gaps covered by _x86.get_pc_thunk and _savegpr symbols. (#1619267)
- Merge ranges where one is wholly covered by another.

* Wed Aug 22 2018 Nick Clifton <nickc@redhat.com> - 8.27-1
- Skip gaps at the end of functions. (#1619267)

* Tue Aug 21 2018 Nick Clifton <nickc@redhat.com> - 8.26-1
- Fix thinko in ppc64 gap detection code. (#1619267)

* Mon Aug 20 2018 Nick Clifton <nickc@redhat.com> - 8.25-1
- Skip gaps at the end of the .text section in ppc64 binaries. (#1619267)

* Wed Aug 15 2018 Nick Clifton <nickc@redhat.com> - 8.24-1
- Skip checks in stack_chk_local_fail.c
- Treat gaps as FAIL results rather than MAYBE.

* Wed Aug 08 2018 Nick Clifton <nickc@redhat.com> - 8.23-1
- Skip checks in __stack_chk_local_fail.

* Wed Aug 08 2018 Nick Clifton <nickc@redhat.com> - 8.22-1
- Reduce version check to gcc major version number only.  Skip compiler option checks if binary not built with gcc.  (#1603089)

* Tue Aug 07 2018 Nick Clifton <nickc@redhat.com> - 8.21-1
- Fix bug in annobin plugin.  Add --section-size=NAME option to annocheck.

* Thu Aug  2 2018 Peter Robinson <pbrobinson@fedoraproject.org> 8.20-2
- rebuild for new gcc

* Thu Aug 02 2018 Nick Clifton <nickc@redhat.com> - 8.20-1
- Correct name of man page for run-on-binaries-in script.  (#1611155)

* Wed Jul 25 2018 Nick Clifton <nickc@redhat.com> - 8.19-1
- Allow $ORIGIN to be at the start of entries in DT_RPATH and DT_RUNPATH.

* Mon Jul 23 2018 Nick Clifton <nickc@redhat.com> - 8.18-1
- Add support for big endian targets.

* Mon Jul 23 2018 Nick Clifton <nickc@redhat.com> - 8.17-1
- Count passes and failures on a per-component basis and report gaps.

* Fri Jul 20 2018 Nick Clifton <nickc@redhat.com> - 8.16-1
- Use our own copy of the targetm.asm_out.function_section() function.  (#159861 comment#17)

* Fri Jul 20 2018 Nick Clifton <nickc@redhat.com> - 8.15-1
- Generate grouped note section name all the time.  (#159861 comment#16)

* Thu Jul 19 2018 Nick Clifton <nickc@redhat.com> - 8.14-1
- Fix section conflict problem.  (#1603071)

* Wed Jul 18 2018 Nick Clifton <nickc@redhat.com> - 8.13-1
- Fix for building with gcc version 4.
- Fix symbol placement in functions with local assembler.

* Tue Jul 17 2018 Nick Clifton <nickc@redhat.com> - 8.12-1
- Fix assertions in range checking code.  Add detection of -U options.

* Tue Jul 17 2018 Nick Clifton <nickc@redhat.com> - 8.11-1
- Handle function sections properly.  Handle .text.startup and .text.unlikely sections.  Improve gap detection and reporting.  (#1601055)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Nick Clifton <nickc@redhat.com> - 8.10-1
- Fix construction of absolute versions of --dwarf-dir and --debug-rpm options.

* Tue Jul 10 2018 Nick Clifton <nickc@redhat.com> - 8.9-1
- Fix buffer overrun when very long symbol names are encountered.

* Tue Jul 10 2018 Nick Clifton <nickc@redhat.com> - 8.8-1
- Do not force the generation of function notes when -ffunction-sections is active.  (#1598961)

* Mon Jul 09 2018 Nick Clifton <nickc@redhat.com> - 8.7-1
- Skip the .annobin_ prfix when reporting symbols.  (#1599315)

* Mon Jul 09 2018 Nick Clifton <nickc@redhat.com> - 8.6-1
- Use the assembler (c++ mangled) version of function names when switching sections.  (#1598579)

* Mon Jul 09 2018 Nick Clifton <nickc@redhat.com> - 8.5-1
- Do not call function_section.  (#1598961)

* Fri Jul 06 2018 Nick Clifton <nickc@redhat.com> - 8.4-1
- Ignore cross-section gaps.  (#1598551)

* Thu Jul 05 2018 Nick Clifton <nickc@redhat.com> - 8.3-1
- Do not skip empty range notes in object files.  (#1598361)

* Mon Jul 02 2018 Nick Clifton <nickc@redhat.com> - 8.2-1
- Create the start symbol at the start of the function and the end symbol at the end.  (#1596823)

* Mon Jul 02 2018 Nick Clifton <nickc@redhat.com> - 8.1-1
- Fix --debug-rpm when used inside a directory.

* Thu Jun 28 2018 Nick Clifton <nickc@redhat.com> - 8.0-1
- Use a prefix for all annobin generated symbols, and make them hidden.
- Only generate weak symbol definitions for linkonce sections.

* Wed Jun 27 2018 Nick Clifton <nickc@redhat.com> - 7.1-1
- Skip some checks for relocatable object files, and dynamic objects.
- Stop bogus complaints about stackrealignment not being enabled.

* Mon Jun 25 2018 Nick Clifton <nickc@redhat.com> - 7.0-1
- Add -debug-rpm= option to annocheck.
- Only use a 2 byte offset for the initial symbol on PowerPC.

* Fri Jun 22 2018 Nick Clifton <nickc@redhat.com> - 6.6-1
- Use --dwarf-path when looking for build-id based debuginfo files.

* Fri Jun 22 2018 Nick Clifton <nickc@redhat.com> - 6.5-1
- Fix premature closing of dwarf handle.

* Fri Jun 22 2018 Nick Clifton <nickc@redhat.com> - 6.4-1
- Fix scoping bug computing the name of a separate debuginfo file.

* Tue Jun 19 2018 Nick Clifton <nickc@redhat.com> - 6.3-1
- Fix file descriptor leak.

* Tue Jun 19 2018 Nick Clifton <nickc@redhat.com> - 6.2-1
- Add command line options to annocheck to disable individual tests.

* Fri Jun 08 2018 Nick Clifton <nickc@redhat.com> - 6.1-1
- Remove C99-ism from annocheck sources.

* Wed Jun 06 2018 Nick Clifton <nickc@redhat.com> - 6.0-1
- Add the annocheck program.

* Fri Jun 01 2018 Nick Clifton <nickc@redhat.com> - 5.11-1
- Do not use the SHF_GNU_BUILD_NOTE section flag.

* Thu May 31 2018 Nick Clifton <nickc@redhat.com> - 5.10-1
- Remove .sh extension from shell scripts.

* Wed May 30 2018 Nick Clifton <nickc@redhat.com> - 5.9-1
- Record the setting of the -mstackrealign option for i686 binaries.

* Mon May 14 2018 Nick Clifton <nickc@redhat.com> - 5.8-1
- Hide the annobin start of file symbol.

* Tue May 08 2018 Nick Clifton <nickc@redhat.com> - 5.7-1
- Fix script bug in hardended.sh.  (Thanks to: Stefan Sørensen <stefan.sorensen@spectralink.com>)

* Thu May 03 2018 Nick Clifton <nickc@redhat.com> - 5.6-3
- Version number bump so that the plugin can be rebuilt with the latest version of GCC.

* Mon Apr 30 2018 Nick Clifton <nickc@redhat.com> - 5.6-2
- Rebuild the plugin with the newly created plugin enabled.  (#1573082)

* Mon Apr 30 2018 Nick Clifton <nickc@redhat.com> - 5.6-1
- Skip the isa_flags check in the ABI test because the crt[in].o files are compiled with different flags from the test files.

* Fri Apr 20 2018 Nick Clifton <nickc@redhat.com> - 5.3-1
- Add manual pages for annobin and the scripts.

* Tue Apr 03 2018 Nick Clifton <nickc@redhat.com> - 5.2-1
- Do not record a stack protection setting of -1.  (#1563141)

* Tue Mar 20 2018 Nick Clifton <nickc@redhat.com> - 5.1-1
- Do not complain about a dwarf_version value of -1.  (#1557511)

* Thu Mar 15 2018 Nick Clifton <nickc@redhat.com> - 5.0-1
- Bias file start symbols by 2 in order to avoid them confused with function symbols.  (#1554332)
- Version jump is to sync the version number with the annobin plugins internal version number.

* Mon Mar 12 2018 Nick Clifton <nickc@redhat.com> - 3.6-1
- Add --ignore-gaps option to check-abi.sh script.
- Use this option in the abi-test check.
- Tweak hardening test to skip pic and stack protection checks.

* Tue Mar 06 2018 Nick Clifton <nickc@redhat.com> - 3.5-1
- Handle functions with specific assembler names.  (#1552018)

* Fri Feb 23 2018 Nick Clifton <nickc@redhat.com> - 3.4-2
- Add an explicit requirement on the version of gcc used to built the plugin.  (#1547260)

* Fri Feb 09 2018 Nick Clifton <nickc@redhat.com> - 3.4-1
- Change type and size of symbols to STT_NOTYPE/0 so that they do not confuse GDB.  (#1539664)
- Add run-on-binaries-in.sh script to allow the other scripts to be run over a repository.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Nick Clifton <nickc@redhat.com> - 3.3-1
- Rebase on 3.3 release, which adds support for recording -mcet and -fcf-protection.

* Mon Jan 29 2018 Florian Weimer <fweimer@redhat.com> - 3.2-3
- Rebuild for GCC 8

* Fri Jan 26 2018 Nick Clifton <nickc@redhat.com> - 3.2-2
- Fix the installation of the annobin.info file.

* Fri Jan 26 2018 Nick Clifton <nickc@redhat.com> - 3.2-1
- Rebase on 3.2 release, which now contains documentation!

* Fri Jan 26 2018 Richard W.M. Jones <rjones@redhat.com> - 3.1-3
- Rebuild against GCC 7.3.1.

* Tue Jan 16 2018 Nick Clifton <nickc@redhat.com> - 3.1-2
- Add --with-gcc-plugin-dir option to the configure command line.

* Thu Jan 04 2018 Nick Clifton <nickc@redhat.com> - 3.1-1
- Rebase on version 3.1 sources.

* Mon Dec 11 2017 Nick Clifton <nickc@redhat.com> - 2.5.1-5
- Do not generate notes when there is no output file.  (#1523875)

* Fri Dec 08 2017 Nick Clifton <nickc@redhat.com> - 2.5.1-4
- Invent an input filename when reading from a pipe.  (#1523401)

* Thu Nov 30 2017 Florian Weimer <fweimer@redhat.com> - 2.5.1-3
- Use DECL_ASSEMBLER_NAME for symbol references (#1519165)

* Tue Oct 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.1-2
- Cleanups in spec

* Tue Sep 26 2017 Nick Clifton <nickc@redhat.com> - 2.5.1-1
- Touch the auto-generated files in order to stop them from being regenerated.

* Tue Sep 26 2017 Nick Clifton <nickc@redhat.com> - 2.5-2
- Stop the plugin complaining about compiler datestamp mismatches.

* Thu Sep 21 2017 Nick Clifton <nickc@redhat.com> - 2.4-1
- Tweak tests so that they will run on older machines.

* Thu Sep 21 2017 Nick Clifton <nickc@redhat.com> - 2.3-1
- Add annobin-tests subpackage containing some preliminary tests.
- Remove link-time test for unsupported targets.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 2.0-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jun 28 2017 Nick Clifton <nickc@redhat.com> - 2.0-1
- Fixes for problems reported by the package submission review:
   * Add %%license entry to %%file section.
   * Update License and BuildRequires tags.
   * Add Requires tag.
   * Remove %%clean.
   * Add %%check.
   * Clean up the %%changelog.
- Update to use version 2 of the specification and sources.

* Thu May 11 2017 Nick Clifton <nickc@redhat.com> - 1.0-1
- Initial submission.
