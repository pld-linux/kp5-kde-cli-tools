#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.25.3
%define		qtver		5.15.2
%define		kpname		kde-cli-tools
Summary:	Tools based on KDE Frameworks 5 to better interact with the system
Name:		kp5-%{kpname}
Version:	5.25.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	bd0a98128f544474cd1c26ba348ab025
URL:		https://www.kde.org/
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
BuildRequires:	kp5-plasma-workspace-devel >= %{version}
BuildRequires:	ninja
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
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang kde-cli-tools --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/kde-open
%attr(755,root,root) %{_bindir}/kdecp
%attr(755,root,root) %{_bindir}/kdemv
%attr(755,root,root) %{_bindir}/keditfiletype
%attr(755,root,root) %{_bindir}/kioclient
%attr(755,root,root) %{_bindir}/kmimetypefinder
%attr(755,root,root) %{_bindir}/kstart
%attr(755,root,root) %{_bindir}/ksvgtopng
%attr(755,root,root) %{_libexecdir}/kf5/kdeeject
%attr(755,root,root) %{_libexecdir}/kf5/kdesu
%attr(755,root,root) %{_bindir}/plasma-open-settings
%{_desktopdir}/org.kde.plasma.settings.open.desktop
%{_mandir}/man1/kdesu.1*
%lang(ca) %{_mandir}/ca/man1/kdesu.1*
%lang(de) %{_mandir}/de/man1/kdesu.1*
%lang(es) %{_mandir}/es/man1/kdesu.1*
%lang(et) %{_mandir}/et/man1/kdesu.1*
%lang(it) %{_mandir}/it/man1/kdesu.1*
%lang(nb) %{_mandir}/nb/man1/kdesu.1*
%lang(nl) %{_mandir}/nl/man1/kdesu.1*
%lang(pt) %{_mandir}/pt/man1/kdesu.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kdesu.1*
%lang(ru) %{_mandir}/ru/man1/kdesu.1*
%lang(sr) %{_mandir}/sr/man1/kdesu.1*
%lang(sv) %{_mandir}/sv/man1/kdesu.1*
%lang(uk) %{_mandir}/uk/man1/kdesu.1*
%{_desktopdir}/org.kde.keditfiletype.desktop
%attr(755,root,root) %{_bindir}/kde-inhibit
%lang(fr) %{_mandir}/fr/man1/kdesu.1*
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%{_desktopdir}/kcm_filetypes.desktop
