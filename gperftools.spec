#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gperftools
Version  : 2.4
Release  : 5
URL      : https://googledrive.com/host/0B6NtGsLhIcf7MWxMMF9JdTN3UVk/gperftools-2.4.tar.gz
Source0  : https://googledrive.com/host/0B6NtGsLhIcf7MWxMMF9JdTN3UVk/gperftools-2.4.tar.gz
Summary  : Performance tools for C++
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gperftools-bin
Requires: gperftools-lib
Requires: gperftools-doc
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
%setup -q -n gperftools-2.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
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
/usr/include/gperftools/profiler.h
/usr/include/gperftools/stacktrace.h
/usr/include/gperftools/tcmalloc.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gperftools/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
