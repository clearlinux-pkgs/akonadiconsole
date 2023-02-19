#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadiconsole
Version  : 22.12.2
Release  : 53
URL      : https://download.kde.org/stable/release-service/22.12.2/src/akonadiconsole-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/akonadiconsole-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/akonadiconsole-22.12.2.tar.xz.sig
Summary  : Akonadi management and debugging console
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: akonadiconsole-bin = %{version}-%{release}
Requires: akonadiconsole-data = %{version}-%{release}
Requires: akonadiconsole-lib = %{version}-%{release}
Requires: akonadiconsole-license = %{version}-%{release}
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : calendarsupport-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kitemviews-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qtwebengine-dev
BuildRequires : xapian-core-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the akonadiconsole package.
Group: Binaries
Requires: akonadiconsole-data = %{version}-%{release}
Requires: akonadiconsole-license = %{version}-%{release}

%description bin
bin components for the akonadiconsole package.


%package data
Summary: data components for the akonadiconsole package.
Group: Data

%description data
data components for the akonadiconsole package.


%package lib
Summary: lib components for the akonadiconsole package.
Group: Libraries
Requires: akonadiconsole-data = %{version}-%{release}
Requires: akonadiconsole-license = %{version}-%{release}

%description lib
lib components for the akonadiconsole package.


%package license
Summary: license components for the akonadiconsole package.
Group: Default

%description license
license components for the akonadiconsole package.


%prep
%setup -q -n akonadiconsole-22.12.2
cd %{_builddir}/akonadiconsole-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676826878
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676826878
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadiconsole
cp %{_builddir}/akonadiconsole-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadiconsole/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadiconsole

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.akonadiconsole.desktop
/usr/share/icons/hicolor/128x128/apps/akonadiconsole.png
/usr/share/icons/hicolor/16x16/apps/akonadiconsole.png
/usr/share/icons/hicolor/22x22/apps/akonadiconsole.png
/usr/share/icons/hicolor/256x256/apps/akonadiconsole.png
/usr/share/icons/hicolor/32x32/apps/akonadiconsole.png
/usr/share/icons/hicolor/48x48/apps/akonadiconsole.png
/usr/share/icons/hicolor/64x64/apps/akonadiconsole.png
/usr/share/qlogging-categories5/akonadiconsole.categories
/usr/share/qlogging-categories5/akonadiconsole.renamecategories

%files lib
%defattr(-,root,root,-)
/usr/lib64/libakonadiconsole.so.5
/usr/lib64/libakonadiconsole.so.5.22.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadiconsole/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadiconsole/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/akonadiconsole/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/akonadiconsole/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/akonadiconsole/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadiconsole/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadiconsole/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/akonadiconsole/e712eadfab0d2357c0f50f599ef35ee0d87534cb
