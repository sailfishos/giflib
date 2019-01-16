Summary: Library for manipulating GIF format image files
Name: giflib
Version: 4.2.3
Release: 1
License: MIT
URL: http://sourceforge.net/projects/giflib/
Source0: http://downloads.sourceforge.net/giflib/giflib-%{version}.tar.bz2
Group: System/Libraries

Obsoletes: libungif <= %{version}-%{release}
Provides: libungif <= %{version}-%{release}

%description
The giflib package contains a shared library of functions for
loading and saving GIF format image files.  It is API and ABI compatible
with libungif, the library which supported uncompressed GIFs while the
Unisys LZW patent was in effect.

Install the giflib package if you need to write programs that use GIF files.
You should also install the giflib-utils package if you need some simple
utilities to manipulate GIFs.

%package devel
Summary: Development tools for programs which will use the libungif library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libungif-devel <= %{version}-%{release}
Obsoletes: libungif-devel <= %{version}-%{release}

%description devel
This package contains the static libraries, header files and
documentation necessary for development of programs that will use the
giflib library to load and save GIF format image files.

You should install this package if you need to develop programs which
will use giflib library functions.  You'll also need to install the
giflib package.

%package utils
Summary: Programs for manipulating GIF format image files
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Obsoletes: libungif-progs <= %{version}-%{release}

%description utils
The giflib-utils package contains various programs for manipulating
GIF format image files.

Install this package if you need to manipulate GIF format image files.
You'll also need to install the giflib package.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}
%{__sed} -i 's/\r//' doc/lzgif.txt

%build
%configure
cd lib ; make %{?_smp_mflags} ; cd ..
cd util ; make %{?_smp_mflags} ; cd ..

MAJOR=`echo '%{version}' | sed 's/\([0-9]\+\)\..*/\1/'`
%{__cc} $RPM_OPT_FLAGS -shared -Wl,-soname,libungif.so.$MAJOR -Llib/.libs -lgif -o libungif.so.%{version}

%install
rm -rf ${RPM_BUILD_ROOT}

%make_install

install -m 0755 -p libungif.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libungif.so.%{version} ${RPM_BUILD_ROOT}%{_libdir}/libungif.so.4
ln -sf libungif.so.4 ${RPM_BUILD_ROOT}%{_libdir}/libungif.so

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} README NEWS

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/*.h

%files utils
%defattr(-,root,root,-)
%{_bindir}/*

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
