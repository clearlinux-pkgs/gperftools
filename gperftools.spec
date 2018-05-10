#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gperftools
Version  : 2.7
Release  : 15
URL      : https://github.com/gperftools/gperftools/releases/download/gperftools-2.7/gperftools-2.7.tar.gz
Source0  : https://github.com/gperftools/gperftools/releases/download/gperftools-2.7/gperftools-2.7.tar.gz
Summary  : Performance tools for C++
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gperftools-bin
Requires: gperftools-lib
Requires: gperftools-doc
BuildRequires : curl-dev
BuildRequires : libunwind-dev

%description
The %name packages contains some utilities to improve and analyze the
performance of C++ programs.  This includes an optimized thread-caching
malloc() and cpu and heap profiling utilities.

%package bin
Summary: bin components for the gperftools package.
Group: Binaries

%description bin
bin components for the gperftools package.


%package dev
Summary: dev components for the gperftools package.
Group: Development
Requires: gperftools-lib
Requires: gperftools-bin
Provides: gperftools-devel

%description dev
dev components for the gperftools package.


%package doc
Summary: doc components for the gperftools package.
Group: Documentation

%description doc
doc components for the gperftools package.


%package lib
Summary: lib components for the gperftools package.
Group: Libraries

%description lib
lib components for the gperftools package.


%prep
%setup -q -n gperftools-2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525095204
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1525095204
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pprof

%files dev
%defattr(-,root,root,-)
/usr/include/google/heap-checker.h
/usr/include/google/heap-profiler.h
/usr/include/google/malloc_extension.h
/usr/include/google/malloc_extension_c.h
/usr/include/google/malloc_hook.h
/usr/include/google/malloc_hook_c.h
/usr/include/google/profiler.h
/usr/include/google/stacktrace.h
/usr/include/google/tcmalloc.h
/usr/include/gperftools/heap-checker.h
/usr/include/gperftools/heap-profiler.h
/usr/include/gperftools/malloc_extension.h
/usr/include/gperftools/malloc_extension_c.h
/usr/include/gperftools/malloc_hook.h
/usr/include/gperftools/malloc_hook_c.h
/usr/include/gperftools/nallocx.h
/usr/include/gperftools/profiler.h
/usr/include/gperftools/stacktrace.h
/usr/include/gperftools/tcmalloc.h
/usr/lib64/libprofiler.so
/usr/lib64/libtcmalloc.so
/usr/lib64/libtcmalloc_and_profiler.so
/usr/lib64/libtcmalloc_debug.so
/usr/lib64/libtcmalloc_minimal.so
/usr/lib64/libtcmalloc_minimal_debug.so
/usr/lib64/pkgconfig/libprofiler.pc
/usr/lib64/pkgconfig/libtcmalloc.pc
/usr/lib64/pkgconfig/libtcmalloc_debug.pc
/usr/lib64/pkgconfig/libtcmalloc_minimal.pc
/usr/lib64/pkgconfig/libtcmalloc_minimal_debug.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gperftools/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprofiler.so.0
/usr/lib64/libprofiler.so.0.4.18
/usr/lib64/libtcmalloc.so.4
/usr/lib64/libtcmalloc.so.4.5.3
/usr/lib64/libtcmalloc_and_profiler.so.4
/usr/lib64/libtcmalloc_and_profiler.so.4.5.3
/usr/lib64/libtcmalloc_debug.so.4
/usr/lib64/libtcmalloc_debug.so.4.5.3
/usr/lib64/libtcmalloc_minimal.so.4
/usr/lib64/libtcmalloc_minimal.so.4.5.3
/usr/lib64/libtcmalloc_minimal_debug.so.4
/usr/lib64/libtcmalloc_minimal_debug.so.4.5.3
