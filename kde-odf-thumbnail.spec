Summary:	Summary	ODF Thumbnail plugin for KDE
Name:		kde-odf-thumbnail
Version:	1.0.0
Release:	5
Source0:	http://kenai.com/projects/%{name}/downloads/download/%{version}/%{name}-%{version}.tar.gz
License:	LGPLv3
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php?content=110864
# Patch to add some translations in the desktop file
Patch0:		kde-odf-thumbnail-1.0.0-mdv-add-translation-in-desktopfile.patch
BuildRequires:	kdebase4-devel
Provides:	kde-office-thumbnails = %{version}-%{release}

%description 
Plugin for KDE file managers (Dolphin and Konqueror) to preview ODF files (Open
Document Format) as Thumbnails.You do not need to install OpenOffice.org or any
other office suite for it to work (it only uses KDE API).

%files 
%doc README LICENSE
%{_kde_libdir}/kde4/opendocumentthumbnail.so
%{_kde_services}/opendocumentthumbnail.desktop

%prep
%setup -q 
%patch0

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

