%global DATE 20220819
%global gitrev 12a206c28987ada47b447ebd200d1fd9639c8edd
%global gcc_version 12.2.1
%global gcc_major 12
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 2
%global nvptx_tools_gitrev 5f6f343a302d620b0868edab376c00b15741e39e
%global newlib_cygwin_gitrev 50e2a63b04bdd018484605fbb954fd1bd5147fa0
%global _unpackaged_files_terminate_build 0
%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%undefine _auto_set_build_flags
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif
# Strip will fail on nvptx-none *.a archives and the brp-* scripts will
# fail randomly depending on what is stripped last.
%if 0%{?__brp_strip_static_archive:1}
%global __brp_strip_static_archive %{__brp_strip_static_archive} || :
%endif
%if 0%{?__brp_strip_lto:1}
%global __brp_strip_lto %{__brp_strip_lto} || :
%endif
%if 0%{?fedora} < 32 && 0%{?rhel} < 8
%global multilib_64_archs sparc64 ppc64 ppc64p7 s390x x86_64
%else
%global multilib_64_archs sparc64 ppc64 ppc64p7 x86_64
%endif
%if 0%{?rhel} > 7
%global build_ada 0
%global build_objc 0
%global build_go 0
%global build_d 0
%else
%ifarch %{ix86} x86_64 ia64 ppc %{power64} alpha s390x %{arm} aarch64 riscv64
%global build_ada 1
%else
%global build_ada 0
%endif
%global build_objc 1
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 %{mips} riscv64
%global build_go 1
%else
%global build_go 0
%endif
%ifarch %{ix86} x86_64 %{arm} aarch64 %{mips} s390 s390x riscv64
%global build_d 1
%else
%global build_d 0
%endif
%endif
%ifarch %{ix86} x86_64 ia64 ppc64le
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global build_libasan 1
%else
%global build_libasan 0
%endif
%ifarch x86_64 ppc64 ppc64le aarch64 s390x
%global build_libtsan 1
%else
%global build_libtsan 0
%endif
%ifarch x86_64 ppc64 ppc64le aarch64 s390x
%global build_liblsan 1
%else
%global build_liblsan 0
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global build_libubsan 1
%else
%global build_libubsan 0
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 %{mips} riscv64
%global build_libatomic 1
%else
%global build_libatomic 0
%endif
%ifarch %{ix86} x86_64 %{arm} alpha ppc ppc64 ppc64le ppc64p7 s390 s390x aarch64
%global build_libitm 1
%else
%global build_libitm 0
%endif
%if 0%{?rhel} > 8
%global build_isl 0
%else
%global build_isl 1
%endif
%global build_libstdcxx_docs 1
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 %{mips}
%global attr_ifunc 1
%else
%global attr_ifunc 0
%endif
%ifarch x86_64 ppc64le
%global build_offload_nvptx 1
%else
%global build_offload_nvptx 0
%endif
%if 0%{?fedora} < 32 && 0%{?rhel} < 8
%ifarch s390x
%global multilib_32_arch s390
%endif
%endif
%ifarch sparc64
%global multilib_32_arch sparcv9
%endif
%ifarch ppc64 ppc64p7
%global multilib_32_arch ppc
%endif
%ifarch x86_64
%global multilib_32_arch i686
%endif
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
%global build_annobin_plugin 1
%else
%global build_annobin_plugin 0
%endif
Summary: Various compilers (C, C++, Objective-C, ...)
Name: gcc-12
Version: %{gcc_version}
Release: %{gcc_release}%{?dist}
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Source0: gcc-%{version}-%{DATE}.tar.xz
Source1: nvptx-tools-%{nvptx_tools_gitrev}.tar.xz
Source2: newlib-cygwin-%{newlib_cygwin_gitrev}.tar.xz
%global isl_version 0.18
Source3: https://gcc.gnu.org/pub/gcc/infrastructure/isl-%{isl_version}.tar.bz2
URL: http://gcc.gnu.org
%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
BuildRequires: binutils >= 2.31
%else
BuildRequires: binutils >= 2.24
%endif
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, texinfo-tex, /usr/bin/pod2man
BuildRequires: systemtap-sdt-devel >= 1.3
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 3.1.0, libmpc-devel >= 0.8.1
BuildRequires: python3-devel, /usr/bin/python
BuildRequires: gcc, gcc-c++, make
%if %{build_go}
BuildRequires: hostname, procps
%endif
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
BuildRequires: libzstd-devel
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
%ifarch %{multilib_64_archs} sparcv9 ppc
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif
%if %{build_ada}
# Ada requires Ada to build
BuildRequires: gcc-gnat >= 3.1, libgnat >= 3.1
%endif
%if %{build_d}
# D requires D to build
BuildRequires: gcc-gdc >= 11.0.0, libgphobos-static >= 11.0.0
%endif
%ifarch ia64
BuildRequires: libunwind >= 0.98
%endif
%if %{build_libstdcxx_docs}
BuildRequires: doxygen >= 1.7.1
BuildRequires: graphviz, dblatex, texlive-collection-latex, docbook5-style-xsl
%endif
%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
Requires: binutils >= 2.31
%else
Requires: binutils >= 2.24
%endif
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
%ifarch ppc ppc64 ppc64le ppc64p7 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
Requires: glibc >= 2.3.90-35
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%ifarch %{arm}
Requires: glibc >= 2.16
%endif
%endif
# lto-wrapper invokes make
Requires: make


%description
The gcc package contains the GNU Compiler Collection version 12.
You'll need this package in order to compile C code.


%prep
%setup -q -n gcc-%{version}-%{DATE} -a 1 -a 2 -a 3


%build

export CONFIG_SITE=NONE

CC=gcc
CXX=g++
./configure --build=x86_64-redhat-linux --host=x86_64-redhat-linux \
	--program-prefix=12 \
	--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=/usr/bin \
	--sbindir=/usr/sbin \
	--sysconfdir=/etc \
	--datadir=/usr/share \
	--includedir=/usr/include \
	--libdir=/usr/lib64 \
	--libexecdir=/usr/libexec \
	--localstatedir=/var \
	--sharedstatedir=/var/lib \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
  --enable-languages=c,c++,fortran --disable-multilib --disable-libstdcxx-pch --with-system-zlib
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install prefix=%{buildroot}%{_prefix}

%check

%files


%changelog
* Wed Sep 07 2022 Kalev Lember <klember@redhat.com> 12.2.1-2
- enable GDC on aarch64

* Fri Aug 19 2022 Jakub Jelinek <jakub@redhat.com> 12.2.1-1
- update from releases/gcc-12 branch
  - GCC 12.1 release
  - PRs c++/67048, c++/106369, c/106016, d/106623, d/106638, lto/106334,
	lto/106540, middle-end/106492, tree-optimization/106513
- fix an if-conversion wrong-code bug (PR rtl-optimization/106590)
- implement C++23 P2327R1 - de-deprecating volatile compound operations - as
  a DR

* Wed Aug  8 2022 Jakub Jelinek <jakub@redhat.com> 12.1.1-4
- update from releases/gcc-12 branch
  - PRs analyzer/105285, analyzer/106204, analyzer/106225, c++/53164,
	c++/96363, c++/100374, c++/105541, c++/105626, c++/105634, c++/105637,
	c++/105758, c++/105842, c++/105848, c++/105912, c++/106024,
	c++/106102, c++/106230, c++/106311, c++/106361, d/106139, d/106555,
	d/106563, debug/106261, fortran/101330, fortran/103137,
	fortran/103138, fortran/103504, fortran/103693, fortran/104313,
	fortran/105243, fortran/105691, fortran/105813, fortran/105954,
	fortran/106121, libfortran/106079, libstdc++/88881, libstdc++/100823,
	libstdc++/104443, libstdc++/105844, libstdc++/105880,
	libstdc++/105957, libstdc++/105995, libstdc++/106162,
	libstdc++/106248, lto/106129, middle-end/105965, middle-end/106027,
	middle-end/106144, middle-end/106331, middle-end/106449,
	preprocessor/97498, rtl-optimization/105041, rtl-optimization/106032,
	target/103722, target/105459, target/105930, target/105991,
	target/106091, target/106097, target/106122, testsuite/106345,
	tree-optimization/105665, tree-optimization/105860,
	tree-optimization/105946, tree-optimization/105969,
	tree-optimization/105971, tree-optimization/106063,
	tree-optimization/106087, tree-optimization/106112,
	tree-optimization/106114, tree-optimization/106131,
	tree-optimization/106189

* Thu Jun 30 2022 Jakub Jelinek <jakub@redhat.com> 12.1.1-3
- fix up libtsan on s390x

* Tue Jun 28 2022 Jakub Jelinek <jakub@redhat.com> 12.1.1-2
- update from releases/gcc-12 branch
  - PRs c++/49387, c++/102307, c++/102651, c++/104470, c++/105491, c++/105589,
	c++/105623, c++/105652, c++/105655, c++/105725, c++/105734,
	c++/105756, c++/105761, c++/105779, c++/105795, c++/105852,
	c++/105871, c++/105885, c++/105908, c++/105925, c++/105931,
	c++/105964, c++/106001, c/105635, d/105544, fortran/105230,
	gcov-profile/105535, ipa/100413, ipa/105600, ipa/105639, ipa/105739,
	libgomp/105745, libgomp/106045, libstdc++/104731, libstdc++/105284,
	libstdc++/105671, libstdc++/105681, middle-end/105537,
	middle-end/105604, middle-end/105711, middle-end/105951,
	middle-end/105998, middle-end/106030, other/105527,
	preprocessor/105732, rtl-optimization/105455, rtl-optimization/105559,
	rtl-optimization/105577, sanitizer/105714, sanitizer/105729,
	target/101891, target/104871, target/105162, target/105209,
	target/105292, target/105472, target/105556, target/105599,
	target/105854, target/105879, target/105953, target/105960,
	target/105970, target/105981, target/106096, tree-optimization/103116,
	tree-optimization/105431, tree-optimization/105458,
	tree-optimization/105528, tree-optimization/105562,
	tree-optimization/105618, tree-optimization/105726,
	tree-optimization/105736, tree-optimization/105786,
	tree-optimization/105940
- enable tsan and lsan on s390x (#2101610)
- trim RHEL fortran patches
- fix nvptx build (PRs bootstrap/105551, target/105938)

* Sat May  7 2022 Jakub Jelinek <jakub@redhat.com> 12.1.1-1
- update from releases/gcc-12 branch
  - GCC 12.1 release
  - PRs c++/105476, libstdc++/103911, libstdc++/105441, libstdc++/105502,
	middle-end/105376, middle-end/105461, target/102059, testsuite/105433,
	tree-optimization/105394, tree-optimization/105437,
	tree-optimization/105484

* Thu May  5 2022 Stephen Gallagher <sgallagh@redhat.com> 12.0.1-0.18
- fix annobin plugin conditional to build for ELN

* Fri Apr 29 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.17
- update from trunk and releases/gcc-12 branch
  - GCC 12.1-rc1
  - PRs analyzer/105252, analyzer/105264, analyzer/105365, analyzer/105366,
	c++/65211, c++/82980, c++/86193, c++/90107, c++/97219, c++/100838,
	c++/101442, c++/101698, c++/102629, c++/102804, c++/102987,
	c++/103868, c++/104051, c++/104624, c++/104646, c++/104996,
	c++/105256, c++/105265, c++/105268, c++/105287, c++/105289,
	c++/105297, c++/105301, c++/105304, c++/105321, c++/105322,
	c++/105353, c++/105386, c++/105398, c++/105425, c++/105426,
	debug/105089, debug/105203, fortran/70673, fortran/78054,
	fortran/102043, fortran/103662, fortran/104717, fortran/105242,
	fortran/105310, fortran/105379, fortran/105381, gcov-profile/105282,
	ipa/103818, ipa/105306, libgomp/105358, libstdc++/93602,
	libstdc++/99290, libstdc++/102994, libstdc++/104858,
	libstdc++/105269, libstdc++/105324, libstdc++/105375,
	libstdc++/105417, lto/105364, lto/105399, middle-end/104492,
	rtl-optimization/105231, rtl-optimization/105314,
	rtl-optimization/105333, sanitizer/105396, target/89125,
	target/103197, target/104676, target/105247, target/105257,
	target/105271, target/105331, target/105334, target/105338,
	target/105339, target/105349, target/105367, testsuite/105266,
	tree-optimization/100810, tree-optimization/103941,
	tree-optimization/104010, tree-optimization/105219,
	tree-optimization/105254, tree-optimization/105276,
	tree-optimization/105312, tree-optimization/105368,
	tree-optimization/105374

* Wed Apr 13 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.16
- update from trunk
  - PRs c++/97296, c++/98249, c++/100111, c++/103105, c++/104142, c++/104669,
	c++/105223, c++/105233, c++/105245, jit/104071, jit/104072,
	jit/104073, jit/104293, middle-end/105253, middle-end/105259,
	rtl-optimization/105211, target/95325, target/97348, target/101755,
	target/102146, target/103623, target/104144, target/104894,
	target/105213, target/105214, target/105234, testsuite/105183,
	tree-optimization/104912, tree-optimization/105226,
	tree-optimization/105232, tree-optimization/105235,
	tree-optimization/105250, tree-optimization/105263

* Mon Apr 11 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.15
- update from trunk
  - PRs analyzer/102208, analyzer/103892, c++/91618, c++/92385, c++/96604,
	c++/96645, c++/99479, c++/100370, c++/100608, c++/101051, c++/101677,
	c++/101717, c++/101894, c++/103328, c++/103852, c++/104668,
	c++/104702, c++/105110, c++/105143, c++/105186, c++/105187,
	c++/105191, c/105149, c/105151, d/104740, driver/105096,
	fortran/104210, fortran/105138, fortran/105184, ipa/103376,
	ipa/104303, ipa/105166, jit/102824, libstdc++/105031,
	libstdc++/105128, libstdc++/105146, libstdc++/105153,
	libstdc++/105154, middle-end/105140, middle-end/105165,
	rtl-optimization/104985, target/101908, target/102024, target/103147,
	target/104049, target/104253, target/104409, target/104853,
	target/104897, target/104987, target/105002, target/105069,
	target/105123, target/105139, target/105144, target/105147,
	target/105157, target/105197, testsuite/103196, testsuite/105095,
	testsuite/105122, testsuite/105196, tree-optimization/102586,
	tree-optimization/103761, tree-optimization/104639,
	tree-optimization/104645, tree-optimization/105132,
	tree-optimization/105142, tree-optimization/105148,
	tree-optimization/105150, tree-optimization/105163,
	tree-optimization/105173, tree-optimization/105175,
	tree-optimization/105185, tree-optimization/105189,
	tree-optimization/105198, tree-optimization/105218
- build annobin gcc plugin as part of gcc build into gcc-plugin-annobin
  subpackage

* Sun Apr  3 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.14
- update from trunk
  - revert delayed parse DMI change (PR c++/96645)
- fix up aarch64 make install

* Fri Apr  1 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.13
- update from trunk
  - PRs ada/104767, ada/104861, analyzer/95000, analyzer/99771,
	analyzer/103533, analyzer/104308, analyzer/104793, analyzer/104863,
	analyzer/104943, analyzer/104954, analyzer/104955, analyzer/104979,
	analyzer/104997, analyzer/105017, analyzer/105057, analyzer/105074,
	analyzer/105087, c++/39751, c++/58646, c++/59426, c++/65396,
	c++/71637, c++/84964, c++/87820, c++/92918, c++/93280, c++/95999,
	c++/96329, c++/96437, c++/96440, c++/96645, c++/96780, c++/98644,
	c++/99445, c++/100474, c++/101030, c++/101515, c++/101767, c++/102045,
	c++/102071, c++/102123, c++/102137, c++/102489, c++/102538,
	c++/102740, c++/102869, c++/102990, c++/103177, c++/103291,
	c++/103299, c++/103337, c++/103455, c++/103460, c++/103769,
	c++/103943, c++/103968, c++/104008, c++/104108, c++/104284,
	c++/104476, c++/104527, c++/104568, c++/104583, c++/104608,
	c++/104620, c++/104622, c++/104623, c++/104641, c++/104752,
	c++/104806, c++/104823, c++/104846, c++/104847, c++/104944,
	c++/104994, c++/105003, c++/105006, c++/105035, c++/105050,
	c++/105061, c++/105064, c++/105067, c++/105092, c/82283, c/84685,
	c/98198, c/104711, d/103528, d/104911, d/105004, debug/104564,
	debug/104778, fortran/50549, fortran/100892, fortran/103039,
	fortran/103560, fortran/103691, fortran/104126, fortran/104570,
	fortran/104571, fortran/104811, fortran/104849, fortran/104999,
	ipa/102513, ipa/103083, ipa/103171, ipa/104813, jit/63854,
	libgcc/86224, libgomp/105042, libstdc++/92546, libstdc++/103407,
	libstdc++/104242, libstdc++/104859, libstdc++/104866,
	libstdc++/104870, libstdc++/104875, libstdc++/104990,
	libstdc++/105021, libstdc++/105027, lto/102426, middle-end/90115,
	middle-end/98420, middle-end/99578, middle-end/100680,
	middle-end/102330, middle-end/103597, middle-end/104086,
	middle-end/104285, middle-end/104436, middle-end/104774,
	middle-end/104786, middle-end/104869, middle-end/104885,
	middle-end/104892, middle-end/104966, middle-end/104971,
	middle-end/104975, middle-end/105032, middle-end/105049, other/65095,
	other/102664, other/104899, other/105114, rtl-optimization/103775,
	rtl-optimization/104814, rtl-optimization/104961,
	rtl-optimization/104989, rtl-optimization/105028,
	rtl-optimization/105091, sanitizer/105093, target/86722, target/91229,
	target/94680, target/96882, target/99754, target/102125,
	target/102215, target/102772, target/102986, target/103074,
	target/104004, target/104666, target/104688, target/104714,
	target/104762, target/104783, target/104790, target/104815,
	target/104818, target/104829, target/104840, target/104842,
	target/104857, target/104868, target/104882, target/104890,
	target/104898, target/104902, target/104903, target/104910,
	target/104916, target/104923, target/104925, target/104946,
	target/104952, target/104957, target/104963, target/104967,
	target/104974, target/104976, target/104977, target/104978,
	target/104982, target/104998, target/105000, target/105011,
	target/105052, target/105058, target/105066, target/105068,
	testsuite/102841, testsuite/104759, testsuite/105055,
	testsuite/105085, tree-optimization/80334, tree-optimization/84201,
	tree-optimization/90356, tree-optimization/98335,
	tree-optimization/100834, tree-optimization/101895,
	tree-optimization/102008, tree-optimization/102586,
	tree-optimization/102645, tree-optimization/102943,
	tree-optimization/104645, tree-optimization/104755,
	tree-optimization/104851, tree-optimization/104880,
	tree-optimization/104941, tree-optimization/104942,
	tree-optimization/104960, tree-optimization/104970,
	tree-optimization/105012, tree-optimization/105053,
	tree-optimization/105056, tree-optimization/105070,
	tree-optimization/105080, tree-optimization/105094,
	tree-optimization/105109

* Tue Mar  8 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.12
- fix up promoted SUBREG handling (#2045160, PR rtl-optimization/104839)
- fix up check for asm goto (PR rtl-optimization/104777)

* Tue Mar  8 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.11
- update from trunk
  - PRs analyzer/101983, fortran/99585, fortran/104430, libstdc++/104807,
	middle-end/104381, target/99297, target/104779, target/104794,
	target/104797, translation/90148, translation/104552,
	tree-optimization/104782, tree-optimization/104825
- fix build on i686 where gnat1 was hanging (PR target/104838,
  PR target/104781)

* Sun Mar  6 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.10
- update from trunk
  - PRs analyzer/103521, analyzer/104434, c++/70077, c++/79493, c++/103443,
	c++/104618, c++/104667, c++/104682, c/104627, c/104633, d/104659,
	d/104736, debug/100541, fortran/84519, fortran/104131, fortran/104573,
	fortran/104619, gcov-profile/104677, ipa/104533, ipa/104648,
	libstdc++/96526, libstdc++/104602, libstdc++/104748, middle-end/80270,
	middle-end/100400, middle-end/102276, middle-end/103836,
	middle-end/103984, middle-end/104061, middle-end/104132,
	middle-end/104133, middle-end/104529, middle-end/104540,
	middle-end/104550, middle-end/104558, middle-end/104679,
	middle-end/104721, middle-end/104757, middle-end/104761,
	middle-end/104784, rtl-optimization/104154, rtl-optimization/104589,
	rtl-optimization/104637, rtl-optimization/104686, target/87496,
	target/88134, target/99555, target/100757, target/101325,
	target/102429, target/103302, target/104121, target/104208,
	target/104489, target/104656, target/104664, target/104674,
	target/104681, target/104698, target/104704, target/104724,
	target/104726, target/104758, testsuite/100407, testsuite/104687,
	testsuite/104725, testsuite/104727, testsuite/104728,
	testsuite/104730, testsuite/104732, testsuite/104791,
	tree-optimization/91384, tree-optimization/101636,
	tree-optimization/103037, tree-optimization/103845,
	tree-optimization/103856, tree-optimization/104601,
	tree-optimization/104644, tree-optimization/104675,
	tree-optimization/104676, tree-optimization/104700,
	tree-optimization/104715, tree-optimization/104716
- fix constraints on s390x conditional trap (PR target/104775)

* Tue Feb 22 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.9
- update from trunk
  - PRs analyzer/104524, analyzer/104560, analyzer/104576, c++/85493,
	c++/90451, c++/94944, c++/95036, c++/104107, c++/104507, c++/104539,
	c++/104565, c/104506, c/104510, c/104531, c/104532, debug/104517,
	debug/104557, fortran/77693, fortran/104211, libstdc++/104542,
	libstdc++/104559, lto/104617, middle-end/104355, middle-end/104522,
	rtl-optimization/104447, rtl-optimization/104498,
	rtl-optimization/104544, sanitizer/102656, target/99708, target/99881,
	target/100056, target/100874, target/103069, target/104253,
	target/104257, target/104335, target/104440, target/104448,
	target/104536, target/104581, target/104598, target/104612,
	testsuite/104146, tree-optimization/96881, tree-optimization/103771,
	tree-optimization/104519, tree-optimization/104526,
	tree-optimization/104543, tree-optimization/104551,
	tree-optimization/104582, tree-optimization/104604

* Mon Feb 14 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.8
- update from trunk
  - PRs ada/97504, ada/98724, c/104505, fortran/104228, libstdc++/100912,
	middle-end/104497, tree-optimization/104511, tree-optimization/104528
  - fix handling of return in arm constexpr ctors and on all arches return in
    constexpr dtors (PR c++/104513)

* Sat Feb 12 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.7
- update from trunk
  - PRs analyzer/98797, analyzer/101081, analyzer/102052, analyzer/103872,
	analyzer/104274, analyzer/104417, analyzer/104452, c++/80951,
	c++/96242, c++/96876, c++/102204, c++/103706, c++/103752, c++/104033,
	c++/104379, c++/104403, c++/104410, c++/104425, c++/104432,
	c++/104472, c/104427, debug/104407, fortran/66193, fortran/104329,
	libgomp/104385, libstdc++/104442, middle-end/100775,
	middle-end/104402, middle-end/104446, middle-end/104450,
	middle-end/104464, middle-end/104467, middle-end/104496,
	rtl-optimization/104059, rtl-optimization/104153,
	rtl-optimization/104198, rtl-optimization/104400,
	rtl-optimization/104459, sanitizer/104449, target/35513, target/79754,
	target/97005, target/97040, target/100593, target/102140,
	target/103627, target/104117, target/104283, target/104327,
	target/104345, target/104364, target/104441, target/104451,
	target/104453, target/104456, target/104458, target/104462,
	target/104469, target/104474, target/104502, testsuite/104481,
	tree-optimization/102832, tree-optimization/104288,
	tree-optimization/104373, tree-optimization/104420,
	tree-optimization/104445, tree-optimization/104466,
	tree-optimization/104479, tree-optimization/104499

* Sat Feb  5 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.6
- update from trunk
  - PRs analyzer/104369, c++/92385, c++/104079, c++/104300, c++/104302,
	debug/104337, debug/104366, fortran/104311, fortran/104328,
	middle-end/90348, middle-end/104092, middle-end/104260,
	rtl-optimization/101885, target/95082, target/100808, target/103686,
	target/104219, target/104362, target/104380, tree-optimization/103641,
	tree-optimization/104119, tree-optimization/104356,
	tree-optimization/104389

* Wed Feb  2 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.5
- update from trunk
  - PRs analyzer/104270, c++/101874, c++/102414, c++/102434, c++/103186,
	c++/104291, c++/104294, d/104287, demangler/98886, demangler/99935,
	fortran/104331, libstdc++/101831, libstdc++/104301, lto/104333,
	middle-end/104232, middle-end/104307, middle-end/95115,
	preprocessor/104147, rtl-optimization/101260, target/94372,
	target/100428, target/104189, target/104298, target/104323,
	tree-optimization/95424, tree-optimization/100499,
	tree-optimization/102819, tree-optimization/103169,
	tree-optimization/103514, tree-optimization/104279,
	tree-optimization/104280, tree-optimization/104281
- fix a VRP bug with 1-3 bit precision types (PR tree-optimization/104334)

* Sat Jan 29 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.4
- update from trunk
  - PRs ada/104258, analyzer/104224, analyzer/104247, bootstrap/67102,
	c++/51344, c++/59950, c++/82632, c++/92752, c++/92944, c++/99895,
	c++/100030, c++/100198, c++/100282, c++/101532, c++/101988,
	c++/103057, c++/103341, c++/103678, c++/104206, c++/104225,
	c++/104226, c++/104235, c++/104245, fortran/84784, fortran/103790,
	fortran/104128, fortran/104212, fortran/104227, libfortran/104233,
	libstdc++/100516, libstdc++/104161, libstdc++/104217,
	libstdc++/104259, lto/104237, middle-end/103642, target/103702,
	target/104201, target/104213, target/104239, testsuite/70230,
	tree-optimization/104196, tree-optimization/104203,
	tree-optimization/104263, tree-optimization/104267, web/104254
- configure with --enable-libstdcxx-backtrace and package
  libstdc++_libbacktrace.a

* Tue Jan 25 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.3
- update from trunk
  - PRs ada/103538, analyzer/94362, analyzer/103685, analyzer/104062,
	analyzer/104089, analyzer/104150, analyzer/104159, bootstrap/104135,
	bootstrap/104170, c++/20040, c++/55227, c++/91911, c++/101072,
	c++/101405, c++/101715, c++/102300, c++/102338, c++/103631,
	c++/103672, c++/103681, c++/104025, c++/104055, c++/104084,
	c++/104134, c++/104139, c++/104148, c++/104173, c++/104182,
	c++/104197, c/104115, debug/103874, fortran/102621, fortran/103695,
	fortran/104127, libgcc/104207, libstdc++/87193, libstdc++/104019,
	libstdc++/104032, libstdc++/104099, libstdc++/104101,
	libstdc++/104123, libstdc++/104174, middle-end/100786,
	middle-end/102860, middle-end/104069, middle-end/104076,
	middle-end/104140, other/104176, other/104181, preprocessor/104030,
	rtl-optimization/102478, sanitizer/99673, sanitizer/104158,
	target/64821, target/94193, target/100784, target/102517,
	target/103676, target/103771, target/104090, target/104136,
	target/104188, testsuite/102833, testsuite/103763, testsuite/104021,
	testsuite/104022, testsuite/104109, tree-optimization/100089,
	tree-optimization/100740, tree-optimization/101508,
	tree-optimization/101972, tree-optimization/102087,
	tree-optimization/102131, tree-optimization/103721,
	tree-optimization/103997, tree-optimization/104112,
	tree-optimization/104114, tree-optimization/104152,
	tree-optimization/104156, tree-optimization/104214
  - don't emit C++ mangling aliases for compatibility with GCC 8.1 ppc64le
    IEEE quad long double (PR target/104172)
- mark IEEE quad long double in DWARF as implicit typedef to _Float128
  (PR debug/104194)

* Tue Jan 18 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.2
- update from trunk
  - PRs c++/104007, c++/104074, fortran/103692, ipa/103989, libstdc++/101124,
	libstdc++/104098, middle-end/103163, tree-optimization/103987,
	tree-optimization/104038
- default to -mabi=ieeelongdouble on ppc64le
- fix -Wdangling-pointer with -fsanitize=address (PR middle-end/104103)
- fix -masm=intel (PR target/104104)

* Tue Jan 18 2022 Jakub Jelinek <jakub@redhat.com> 12.0.1-0.1
- update from trunk
  - PRs c++/104031, c/63272, fortran/83079, fortran/87711, fortran/97896,
	libstdc++/103650, libstdc++/104080, middle-end/101292, target/103124,
	target/103973, target/104005, testsuite/104035, testsuite/104037,
	tree-optimization/80532, tree-optimization/101941,
	tree-optimization/104064

* Sat Jan 15 2022 Jakub Jelinek <jakub@redhat.com> 12.0.0-0.5
- update from trunk
  - PRs ada/104027, analyzer/104029, c++/70417, c++/103705, c++/103991,
	c/104002, fortran/67804, fortran/99256, fortran/103782,
	libfortran/104006, libstdc++/91260, libstdc++/91383, libstdc++/95065,
	libstdc++/103992, middle-end/100280, middle-end/101475,
	middle-end/104026, target/94790, target/98737, target/100637,
	target/103935, target/103941, target/104001, target/104003,
	target/104014, tree-optimization/83072, tree-optimization/83073,
	tree-optimization/96707, tree-optimization/97909,
	tree-optimization/102192, tree-optimization/103989,
	tree-optimization/104009, tree-optimization/104015
- include rs6000-vecdefines.h on ppc* (#2040825)

* Wed Jan 12 2022 Jakub Jelinek <jakub@redhat.com> 12.0.0-0.4
- update from trunk
  - PRs ada/79724, analyzer/102692, analyzer/103940, c++/89074, c++/103480,
	c++/100588, c++/101597, c++/103783, c++/103831, c++/103879,
	c++/103912, c++/103946, c/101537, c/103881, fortran/82207,
	fortran/101762, fortran/103366, fortran/103777, fortran/103789,
	libstdc++/77760, libstdc++/100017, libstdc++/103726, libstdc++/103866,
	libstdc++/103891, libstdc++/103955, middle-end/70090,
	middle-end/101530, rtl-optimization/98782, rtl-optimization/103974,
	target/53652, target/102024, target/102239, target/103465,
	target/103804, target/103861, testsuite/102935, testsuite/103820,
	tree-optimization/76174, tree-optimization/83541,
	tree-optimization/100359, tree-optimization/103551,
	tree-optimization/103821, tree-optimization/103948,
	tree-optimization/103961, tree-optimization/103971,
	tree-optimization/103977, tree-optimization/103990

* Sat Jan  8 2022 Jakub Jelinek <jakub@redhat.com> 12.0.0-0.3
- new package
