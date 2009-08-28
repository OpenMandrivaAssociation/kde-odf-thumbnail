%define	name	kde-odf-thumbnail
%define	version	0.0.1
%define	release	%mkrel 1
%define	section	Graphical desktop/KDE
%define	Summary	OpenOffice Thumbnail plugin for KDE


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://arielch.fedorapeople.org/devel/src/OpenOfficeorgThumbnail-%{version}.tar.gz
License:	GPLv3
Group:		%section
URL:		http://www.kde-look.org/content/show.php/OpenOffice.org+Thumbnail+plugin?content=110864
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
Provides:	kde-office-thumbnails = %{name}-%{version}

%description 
Plugin for KDE file managers (Dolphin and Konqueror) to preview
OpenOffice.org files (Open Document Format) as Thumbnails.You do not
need to install OpenOffice.org for it to work (it only uses KDE API).

%files 
%defattr(-,root,root)
%doc README
%{_kde_libdir}/kde4/openofficeorgthumbnail.so
%{_kde_services}/openofficeorgthumbnail.desktop

%prep
%setup -q -n OpenOfficeorgThumbnail-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}
