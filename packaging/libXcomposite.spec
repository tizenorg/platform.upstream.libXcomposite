%bcond_with x

Name:           libXcomposite
Version:        0.4.4
Release:        3
License:        MIT
Summary:        X Composite Extension library
Url:            http://www.x.org
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXcomposite.manifest

BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)

%if !%{with x}
ExclusiveArch:
%endif

%description
X Composite Extension library

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXcomposite development package

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
