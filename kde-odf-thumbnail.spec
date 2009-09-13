%define	name	kde-odf-thumbnail
%define	version	1.0.0
%define	release	%mkrel 1
%define	Summary	OpenOffice Thumbnail plugin for KDE


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://arielch.fedorapeople.org/devel/src/OpenOfficeorgThumbnail-%{version}.tar.gz
License:	LGPLv3
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/OpenOffice.org+Thumbnail+plugin?content=110864
# Patch to add some translations in the desktop file
Patch0:		kde-odf-thumbnail-desktopfile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
Provides:	kde-office-thumbnails = %{name}-%{version}

%description 
Plugin for KDE file managers (Dolphin and Konqueror) to preview
OpenOffice.org files (Open Document Format) as Thumbnails.You do not
need to install OpenOffice.org for it to work (it only uses KDE API).

%files 
%defattr(-,root,root)
%doc README LICENSE
%{_kde_libdir}/kde4/openofficeorgthumbnail.so
%{_kde_services}/openofficeorgthumbnail.desktop

%prep
%setup -q -n OpenOfficeorgThumbnail-%{version}
%patch0

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}
