#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadiconsole
Version  : 24.08.0
Release  : 77
URL      : https://download.kde.org/stable/release-service/24.08.0/src/akonadiconsole-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/akonadiconsole-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/akonadiconsole-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Akonadi management and debugging console
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: akonadiconsole-bin = %{version}-%{release}
Requires: akonadiconsole-data = %{version}-%{release}
Requires: akonadiconsole-lib = %{version}-%{release}
Requires: akonadiconsole-license = %{version}-%{release}
Requires: akonadiconsole-locales = %{version}-%{release}
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
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
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
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
BuildRequires : xapian-core-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

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


%package locales
Summary: locales components for the akonadiconsole package.
Group: Default

%description locales
locales components for the akonadiconsole package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n akonadiconsole-24.08.0
cd %{_builddir}/akonadiconsole-24.08.0
pushd ..
cp -a akonadiconsole-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724703741
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724703741
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadiconsole
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/akonadiconsole-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang akonadiconsole
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akonadiconsole
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
/usr/share/qlogging-categories6/akonadiconsole.categories
/usr/share/qlogging-categories6/akonadiconsole.renamecategories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libakonadiconsole.so.6.2.0
/usr/lib64/libakonadiconsole.so.6
/usr/lib64/libakonadiconsole.so.6.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadiconsole/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadiconsole/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/akonadiconsole/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/akonadiconsole/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadiconsole/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/akonadiconsole/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadiconsole/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadiconsole/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadiconsole.lang
%defattr(-,root,root,-)

