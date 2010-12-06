%define	name	kde-odf-thumbnail
%define	version	1.0.0
%define	release	%mkrel 3
%define	Summary	ODF Thumbnail plugin for KDE


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://kenai.com/projects/%{name}/downloads/download/%{version}/%{name}-%{version}.tar.gz
License:	LGPLv3
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php?content=110864
# Patch to add some translations in the desktop file
Patch0:		kde-odf-thumbnail-1.0.0-mdv-add-translation-in-desktopfile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
Provides:	kde-office-thumbnails = %{name}-%{version}

%description 
Plugin for KDE file managers (Dolphin and Konqueror) to preview ODF files (Open
Document Format) as Thumbnails.You do not need to install OpenOffice.org or any
other office suite for it to work (it only uses KDE API).

%files 
%defattr(-,root,root)
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
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}
