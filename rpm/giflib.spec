Summary: Library for manipulating GIF format image files
Name: giflib
Version: 5.2.2
Release: 1
License: MIT
URL: http://sourceforge.net/projects/giflib/
Source0: giflib-%{version}.tar.bz2
Patch1: 0001-Disable-building-docs.patch
Patch2: 0002-Avoid-timestamps.patch
Patch3: 0003-Clean-up-memory-better-at-end-of-run-CVE-2021-40633.patch

%description
The giflib package contains a shared library of functions for
loading and saving GIF format image files.

%package devel
Summary: Development tools for programs which will use the libungif library
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the static libraries, header files and
documentation necessary for development of programs that will use the
giflib library to load and save GIF format image files.

%package utils
Summary: Programs for manipulating GIF format image files
Requires: %{name} = %{version}-%{release}

%description utils
The giflib-utils package contains various programs for manipulating
GIF format image files.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%make_build

%install
make PREFIX="%{_prefix}" LIBDIR="%{_libdir}" DESTDIR="%{?buildroot}" install

# Drop static library
rm -f %{buildroot}%{_libdir}/libgif.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libgif.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgif.so
%{_includedir}/*.h

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
