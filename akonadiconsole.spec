#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadiconsole
Version  : 19.08.3
Release  : 16
URL      : https://download.kde.org/stable/applications/19.08.3/src/akonadiconsole-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/akonadiconsole-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/akonadiconsole-19.08.3.tar.xz.sig
Summary  : Akonadi management and debugging console
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
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
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : kcalcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : xapian-core-dev

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
%setup -q -n akonadiconsole-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573536791
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573536791
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadiconsole
cp %{_builddir}/akonadiconsole-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/akonadiconsole/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/akonadiconsole-19.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/akonadiconsole/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/akonadiconsole-19.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadiconsole/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/share/kconf_update/akonadiconsole-15.08-kickoff.sh
/usr/share/kconf_update/akonadiconsole.upd
/usr/share/qlogging-categories5/akonadiconsole.categories
/usr/share/qlogging-categories5/akonadiconsole.renamecategories

%files lib
%defattr(-,root,root,-)
/usr/lib64/libakonadiconsole.so.5
/usr/lib64/libakonadiconsole.so.5.12.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadiconsole/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/akonadiconsole/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/akonadiconsole/9a1929f4700d2407c70b507b3b2aaf6226a9543c
