# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-osmscout-server

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libboost_filesystem|libboost_regex|libboost_system|libboost_iostreams|libprotobuf|libz|liblz4|libfreetype|libharfbuzz|libicudata|libicui18n|libicuuc|libjpeg|libmapnik|libproj|libtiff.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    OSM Scout Server
Version:    1.7.0
Release:    1
Group:      Qt/Qt
License:    LGPL
URL:        https://github.com/rinigus/osmscout-server
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-osmscout-server.yaml
Source101:  harbour-osmscout-server-rpmlintrc
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libsystemd-daemon)
BuildRequires:  pkgconfig(libvalhalla)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  libmarisa-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libosmscout-qt-devel
BuildRequires:  libpostal-devel >= 1.0.0
BuildRequires:  libkyotocabinet-devel
BuildRequires:  mapnik-devel
BuildRequires:  libicu52-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  protobuf-devel
BuildRequires:  boost-devel >= 1.51
BuildRequires:  boost-date-time >= 1.51
BuildRequires:  boost-filesystem >= 1.51
BuildRequires:  boost-iostreams >= 1.51
BuildRequires:  boost-regex >= 1.51
BuildRequires:  boost-system >= 1.51
BuildRequires:  lz4-devel
BuildRequires:  desktop-file-utils

%description
Server providing map tiles, search, and routing


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5  \
    VERSION='%{version}-%{release}'

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
################################

# ship all shared libraries not allowed in Harbour with the app
mkdir -p %{buildroot}%{_datadir}/%{name}/lib

cp /usr/lib/libmapnik.so.3.0 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libproj.so.12 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libtiff.so.5 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libharfbuzz.so.0 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libjpeg.so.62 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libfreetype.so.6 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libicui18n.so.52 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libicudata.so.52 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libicuuc.so.52 %{buildroot}%{_datadir}/%{name}/lib

cp /usr/lib/libboost_filesystem-mt.so.1.51.0 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libboost_regex-mt.so.1.51.0 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libboost_system-mt.so.1.51.0 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libboost_iostreams-mt.so.1.51.0 %{buildroot}%{_datadir}/%{name}/lib

cp /usr/lib/libprotobuf.so.8  %{buildroot}%{_datadir}/%{name}/lib

cp /usr/lib/liblz4.so.1.8.1 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/liblz4.so.1 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libz.so.1.2.8 %{buildroot}%{_datadir}/%{name}/lib
cp /usr/lib/libz.so.1 %{buildroot}%{_datadir}/%{name}/lib

# mapnik fonts and input plugins
# not needed anymore since input plugins are linked
# into main mapnik library and fonts are distributed with
# the styles
#cp -r /usr/lib/mapnik %{buildroot}%{_datadir}/%{name}/lib

strip %{buildroot}%{_datadir}/%{name}/lib/libmapnik.so.3.0
strip %{buildroot}%{_datadir}/%{name}/lib/libicudata.so.52

# strip executable bit from all libraries
chmod -x %{buildroot}%{_datadir}/%{name}/lib/*.so*
#chmod -x %{buildroot}%{_datadir}/%{name}/lib/mapnik/*/*

#################################
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/translations
# >> files
# << files
