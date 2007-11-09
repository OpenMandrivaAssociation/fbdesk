%define name      fbdesk
%define version   1.4.1
%define release   %mkrel 1
%define section   Fluxbox/action
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
Buildrequires:    XFree86-devel
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
mkdir -p %buildroot%{_menudir}
cat > %buildroot%_menudir/%name << EOF
?package(%name): \
command="%{_bindir}/%{name}" \
needs="fluxexec" \
icon="%{name}.png" \
section="%{section}" \
title="%{title}" \
longtitle="%{longtitle}"
EOF

# icon
%__install -D -m 644 %{name}48.png %buildroot%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot%_miconsdir/%name.png

%__install -d            %buildroot%_datadir/%name
%__install -m 0644 *.png %buildroot%_datadir/%name


%post
%update_menus

%postun
%clean_menus


%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc README
%_bindir/*
%_menudir/*

%_miconsdir/*
%_iconsdir/*
%_liconsdir/*
%_datadir/%name/*.png

%dir %_datadir/%name


