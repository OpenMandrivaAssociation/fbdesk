%define name      fbdesk
%define version   1.4.1
%define release   %mkrel 3
%define title     Fbdesk
%define longtitle Fluxbox-application to create and manage icons on your desktop

Summary:          %longtitle
Name:             %name
Version:          %version
Release:          %release
License:          MIT
Group:            Graphical desktop/Other
URL:              http://fluxbox.sourceforge.net/fbdesk
Source0:          http://fluxbox.sourceforge.net/fbdesk/%{name}-%{version}.tar.bz2
Source1:          %name-icons.tar.bz2
BuildRoot:        %_tmppath/%{name}-%{version}-%{release}-buildroot
Buildrequires:    X11-devel
Buildrequires:    png-devel
Buildrequires:    imlib2-devel

%description
FbDesk is a fluxbox-application to create and manage icons on your desktop.

Implemented Features :

 * XPM and PNG image loading
 * Antialias text
 * UTF-8 and multibyte support
 * Vertical text
 * Grid Snapping
 * GUI for editing command/label and add/remove icons
 * Fluxbox menu style


%prep

%setup -q
%setup -q -T -D -a1

%build
%configure
%make

%install
%__rm -rf %buildroot
%makeinstall

# Menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=Graphics;2DGraphics;
Name=%{title}
Comment=%{longtitle}
EOF

# icon
%__install -D -m 644 %{name}48.png %buildroot%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot%_miconsdir/%name.png

%__install -d            %buildroot%_datadir/%name
%__install -m 0644 *.png %buildroot%_datadir/%name


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif


%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc README
%_bindir/*
%{_datadir}/applications/mandriva-*.desktop

%_miconsdir/*
%_iconsdir/*
%_liconsdir/*
%_datadir/%name/*.png

%dir %_datadir/%name


