%define name      fbdesk
%define version   1.4.1
%define release   %mkrel 6
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
Patch0:		  fbdesk-1.4.1-gcc-4.3.patch
BuildRoot:        %_tmppath/%{name}-%{version}-%{release}-buildroot
Buildrequires:    libx11-devel
Buildrequires:    libxext-devel
Buildrequires:    libxft-devel
Buildrequires:    libxpm-devel
Buildrequires:    libxrender-devel
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
%patch0 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %buildroot
%makeinstall_std

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
%_miconsdir/*.png
%_iconsdir/*.png
%_liconsdir/*.png
%_datadir/%name


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 1.4.1-6mdv2011.0
+ Revision: 635413
- simplify BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-5mdv2011.0
+ Revision: 618257
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.4.1-4mdv2010.0
+ Revision: 428708
- rebuild

* Wed Aug 13 2008 Funda Wang <fwang@mandriva.org> 1.4.1-3mdv2009.0
+ Revision: 271537
- add gcc 4.3 patch from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 1.4.1-1mdv2008.1
+ Revision: 141839
- fix spacing at top of description
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + J√©r√¥me Soyer <saispo@mandriva.org>
    - New release
    - import fbdesk


* Sun Apr 23 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.4.0-3mdk
- Really fix BuildRequires

* Sun Apr 23 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.4.0-2mdk
- Add BuildRequires

* Thu Apr 06 2006 Lenny Cartier <lenny@mandriva.com> 1.4.0-1mdk
- 1.4.0

* Thu Oct 06 2005 Lenny Cartier <lenny@mandriva.com> 1.2.1-1mdk
- 1.2.1

* Wed Jul 14 2004 Michael Scherer <misc@mandrake.org> 1.1.5-2mdk 
- rebuild for new gcc, patch #0

* Sun Oct 19 2003 Han Boetes <han@linux-mandrake.com> 1.1.5-1mdk
- Various Fixes among which the dreaded menu.
  Just that you need to have fluxbox installed :S

* Fri May 23 2003 Han Boetes <han@linux-mandrake.com> 1.1.4-2mdk
- Added dir entry to make distriblint happy

* Mon May 19 2003 Han Boetes <han@linux-mandrake.com> 1.1.4-1mdk
- New release.

* Thu Jan 30 2003 Han Boetes <han@linux-mandrake.com> 1.1.3-1mdk
- Bump. bugfix-release.

* Sun Jan 19 2003 Han Boetes <han@linux-mandrake.com> 1.1.2-1mdk
- Initial release.
