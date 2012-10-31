Name:           libXcomposite
Version:        0.4.3
Release:        3
License:        MIT
Summary:        X Composite Extension library
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)

%description
X Composite Extension library

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxcomposite-devel

%description devel
X.Org X11 libXcomposite development package

%prep
%setup -q

%build
%reconfigure --disable-static\
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
#%{_mandir}/man3/X?omposite*.3
