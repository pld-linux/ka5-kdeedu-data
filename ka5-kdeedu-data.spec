#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdeedu-data
Summary:	kdeedu-data
Name:		ka5-%{kaname}
Version:	22.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fbd20ddf754bb1c482e7816415aaabab
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdeedu data.

%description -l pl.UTF-8
Dane dla kdeedu.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/hicolor/16x16/actions/editplots.png
%{_iconsdir}/hicolor/16x16/actions/functionhelp.png
%{_iconsdir}/hicolor/16x16/actions/integral_func.png
%{_iconsdir}/hicolor/16x16/actions/maximum.png
%{_iconsdir}/hicolor/16x16/actions/minimum.png
%{_iconsdir}/hicolor/16x16/actions/newdifferential.png
%{_iconsdir}/hicolor/16x16/actions/newfunction.png
%{_iconsdir}/hicolor/16x16/actions/newimplicit.png
%{_iconsdir}/hicolor/16x16/actions/newparametric.png
%{_iconsdir}/hicolor/16x16/actions/newpolar.png
%{_iconsdir}/hicolor/16x16/actions/resetview.png
%{_iconsdir}/hicolor/22x22/actions/editplots.png
%{_iconsdir}/hicolor/22x22/actions/functionhelp.png
%{_iconsdir}/hicolor/22x22/actions/maximum.png
%{_iconsdir}/hicolor/22x22/actions/minimum.png
%{_iconsdir}/hicolor/22x22/actions/newdifferential.png
%{_iconsdir}/hicolor/22x22/actions/newfunction.png
%{_iconsdir}/hicolor/22x22/actions/newimplicit.png
%{_iconsdir}/hicolor/22x22/actions/newparametric.png
%{_iconsdir}/hicolor/22x22/actions/newpolar.png
%{_iconsdir}/hicolor/22x22/actions/resetview.png
%{_iconsdir}/hicolor/32x32/actions/coords.png
%{_iconsdir}/hicolor/32x32/actions/deriv_func.png
%{_iconsdir}/hicolor/32x32/actions/editconstants.png
%{_iconsdir}/hicolor/32x32/actions/editplots.png
%{_iconsdir}/hicolor/32x32/actions/func.png
%{_iconsdir}/hicolor/32x32/actions/functionhelp.png
%{_iconsdir}/hicolor/32x32/actions/integral_func.png
%{_iconsdir}/hicolor/32x32/actions/lessen.png
%{_iconsdir}/hicolor/32x32/actions/magnify.png
%{_iconsdir}/hicolor/32x32/actions/maximum.png
%{_iconsdir}/hicolor/32x32/actions/minimum.png
%{_iconsdir}/hicolor/32x32/actions/newdifferential.png
%{_iconsdir}/hicolor/32x32/actions/newfunction.png
%{_iconsdir}/hicolor/32x32/actions/newimplicit.png
%{_iconsdir}/hicolor/32x32/actions/newparametric.png
%{_iconsdir}/hicolor/32x32/actions/newpolar.png
%{_iconsdir}/hicolor/32x32/actions/resetview.png
%{_iconsdir}/hicolor/48x48/actions/editplots.png
%{_iconsdir}/hicolor/48x48/actions/functionhelp.png
%{_iconsdir}/hicolor/48x48/actions/maximum.png
%{_iconsdir}/hicolor/48x48/actions/minimum.png
%{_iconsdir}/hicolor/48x48/actions/newdifferential.png
%{_iconsdir}/hicolor/48x48/actions/newfunction.png
%{_iconsdir}/hicolor/48x48/actions/newimplicit.png
%{_iconsdir}/hicolor/48x48/actions/newparametric.png
%{_iconsdir}/hicolor/48x48/actions/newpolar.png
%{_iconsdir}/hicolor/48x48/actions/resetview.png
%{_iconsdir}/hicolor/64x64/actions/maximum.png
%{_iconsdir}/hicolor/64x64/actions/minimum.png
%{_iconsdir}/hicolor/scalable/actions/deriv_func.svgz
%{_iconsdir}/hicolor/scalable/actions/editconstants.svgz
%{_iconsdir}/hicolor/scalable/actions/editplots.svgz
%{_iconsdir}/hicolor/scalable/actions/functionhelp.svgz
%{_iconsdir}/hicolor/scalable/actions/integral_func.svgz
%{_iconsdir}/hicolor/scalable/actions/maximum.svgz
%{_iconsdir}/hicolor/scalable/actions/minimum.svgz
%{_iconsdir}/hicolor/scalable/actions/newfunction.svgz
%{_iconsdir}/hicolor/scalable/actions/newparametric.svgz
%{_iconsdir}/hicolor/scalable/actions/newpolar.svgz
%{_iconsdir}/hicolor/scalable/actions/resetview.svgz
%{_datadir}/apps/kvtml
