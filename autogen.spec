#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC9EF76DEB74EE762 (bkorb@gnu.org)
#
Name     : autogen
Version  : 5.18.12
Release  : 23
URL      : http://ftp.gnu.org/gnu/autogen/rel5.18.12/autogen-5.18.12.tar.gz
Source0  : http://ftp.gnu.org/gnu/autogen/rel5.18.12/autogen-5.18.12.tar.gz
Source99 : http://ftp.gnu.org/gnu/autogen/rel5.18.12/autogen-5.18.12.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: autogen-bin
Requires: autogen-lib
Requires: autogen-data
Requires: autogen-doc
BuildRequires : gc-dev
BuildRequires : gmp-dev
BuildRequires : guile
BuildRequires : guile-dev
BuildRequires : libxml2-dev
BuildRequires : zlib-dev
Patch1: 0001-Allow-guile-2.2-as-a-valid-version.patch

%description
This is AutoGen, an automated text file generator.  It was inspired out of
frustration and hassle with maintaining syncronization between option flag
lists, global variables and usage information.  The desire for more than
#define macros came about when it became apparent that macros alone were
insufficient for reducing the maintenance into a single option list.  The
impetus to actually start something finally came when I had to maintain a
large callout procedure table and associated lookup tables.

%package bin
Summary: bin components for the autogen package.
Group: Binaries
Requires: autogen-data

%description bin
bin components for the autogen package.


%package data
Summary: data components for the autogen package.
Group: Data

%description data
data components for the autogen package.


%package dev
Summary: dev components for the autogen package.
Group: Development
Requires: autogen-lib
Requires: autogen-bin
Requires: autogen-data
Provides: autogen-devel

%description dev
dev components for the autogen package.


%package doc
Summary: doc components for the autogen package.
Group: Documentation

%description doc
doc components for the autogen package.


%package lib
Summary: lib components for the autogen package.
Group: Libraries
Requires: autogen-data

%description lib
lib components for the autogen package.


%prep
%setup -q -n autogen-5.18.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503352885
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1503352885
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/autogen/tpl-config.tlib

%files bin
%defattr(-,root,root,-)
/usr/bin/autogen
/usr/bin/autoopts-config
/usr/bin/columns
/usr/bin/getdefs

%files data
%defattr(-,root,root,-)
/usr/share/autogen/Mdoc.pm
/usr/share/autogen/aginfo.tpl
/usr/share/autogen/aginfo3.tpl
/usr/share/autogen/agman-cmd.tpl
/usr/share/autogen/agman-file.tpl
/usr/share/autogen/agman.tlib
/usr/share/autogen/agman1.tpl
/usr/share/autogen/agman3.tpl
/usr/share/autogen/agmdoc-cmd.tpl
/usr/share/autogen/agmdoc-file.tpl
/usr/share/autogen/agpl.lic
/usr/share/autogen/agtexi-cmd.tpl
/usr/share/autogen/agtexi-file.tpl
/usr/share/autogen/autoopts.m4
/usr/share/autogen/bits.tpl
/usr/share/autogen/cmd-doc.tlib
/usr/share/autogen/confmacs.tlib
/usr/share/autogen/conftest.tpl
/usr/share/autogen/def2pot.tpl
/usr/share/autogen/fsm-macro.tlib
/usr/share/autogen/fsm-trans.tlib
/usr/share/autogen/fsm.tpl
/usr/share/autogen/getopt.tpl
/usr/share/autogen/gpl.lic
/usr/share/autogen/gplv2.lic
/usr/share/autogen/lgpl.lic
/usr/share/autogen/lgplv2.lic
/usr/share/autogen/libopts-41.1.16.tar.gz
/usr/share/autogen/liboptschk.m4
/usr/share/autogen/man2mdoc
/usr/share/autogen/man2texi
/usr/share/autogen/mbsd.lic
/usr/share/autogen/mdoc2man
/usr/share/autogen/mdoc2texi
/usr/share/autogen/optcode.tlib
/usr/share/autogen/opthead.tlib
/usr/share/autogen/options.tpl
/usr/share/autogen/optlib.tlib
/usr/share/autogen/optmain.tlib
/usr/share/autogen/perlopt.tpl
/usr/share/autogen/rc-sample.tpl
/usr/share/autogen/stdoptions.def
/usr/share/autogen/str2enum.tpl
/usr/share/autogen/str2init.tlib
/usr/share/autogen/str2mask.tpl
/usr/share/autogen/strings.tpl
/usr/share/autogen/texi2man
/usr/share/autogen/texi2mdoc
/usr/share/autogen/tpl-config.tlib
/usr/share/autogen/usage.tlib

%files dev
%defattr(-,root,root,-)
/usr/include/autoopts/options.h
/usr/include/autoopts/usage-txt.h
/usr/lib64/libopts.so
/usr/lib64/pkgconfig/autoopts.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopts.so.25
/usr/lib64/libopts.so.25.16.1
