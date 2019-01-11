%define		kdeplasmaver	5.14.5
%define		qtver		5.9.0
%define		kpname		kde-cli-tools
Summary:	Tools based on KDE Frameworks 5 to better interact with the system
Name:		kp5-%{kpname}
Version:	5.14.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	be9fe02e19e8e815b9b50b05b25faf0e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesu-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kp5-plasma-workspace-devel >= 5.14.5
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools based on KDE Frameworks 5 to better interact with the system.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang kde-cli-tools --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kde-cli-tools.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbroadcastnotification
%attr(755,root,root) %{_bindir}/kcmshell5
%attr(755,root,root) %{_bindir}/kde-open5
%attr(755,root,root) %{_bindir}/kdecp5
%attr(755,root,root) %{_bindir}/kdemv5
%attr(755,root,root) %{_bindir}/keditfiletype5
%attr(755,root,root) %{_bindir}/kioclient5
%attr(755,root,root) %{_bindir}/kmimetypefinder5
%attr(755,root,root) %{_bindir}/kstart5
%attr(755,root,root) %{_bindir}/ksvgtopng5
%attr(755,root,root) %{_bindir}/ktraderclient5
%attr(755,root,root) %{_libexecdir}/kf5/kdeeject
%attr(755,root,root) %{_libexecdir}/kf5/kdesu
%attr(755,root,root) %{_libdir}/libkdeinit5_kcmshell5.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_filetypes.so
%{_datadir}/kservices5/filetypes.desktop
%{_mandir}/man1/kdesu.1*
%lang(ca) /usr/share/man/ca/man1/kdesu.1*
%lang(de) /usr/share/man/de/man1/kdesu.1*
%lang(es) /usr/share/man/es/man1/kdesu.1*
%lang(et) /usr/share/man/et/man1/kdesu.1*
%lang(it) /usr/share/man/it/man1/kdesu.1*
%lang(nb) /usr/share/man/nb/man1/kdesu.1*
%lang(nl) /usr/share/man/nl/man1/kdesu.1*
%lang(pt) /usr/share/man/pt/man1/kdesu.1*
%lang(pt_BR) /usr/share/man/pt_BR/man1/kdesu.1*
%lang(ru) /usr/share/man/ru/man1/kdesu.1*
%lang(sr) /usr/share/man/sr/man1/kdesu.1*
%lang(sv) /usr/share/man/sv/man1/kdesu.1*
%lang(uk) /usr/share/man/uk/man1/kdesu.1*
