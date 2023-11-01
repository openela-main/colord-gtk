Summary:   GTK support library for colord
Name:      colord-gtk
Version:   0.2.0
Release:   7%{?dist}
License:   LGPLv2+
URL:       http://www.freedesktop.org/software/colord/
Source0:   http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: docbook5-style-xsl
BuildRequires: gettext >= 0.19.8
BuildRequires: glib2-devel
BuildRequires: colord-devel >= 0.1.23
BuildRequires: lcms2-devel >= 2.2
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools
BuildRequires: gtk3-devel
BuildRequires: gtk-doc

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson -Ddocs=true -Dgtk2=false -Dman=true -Dtests=false -Dvapi=true
%meson_build

%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README AUTHORS NEWS COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/libcolord-gtk.so.*
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files devel
%{_libdir}/libcolord-gtk.so
%{_libdir}/pkgconfig/colord-gtk.pc
%dir %{_includedir}/colord-1
%{_includedir}/colord-1/colord-gtk.h
%dir %{_includedir}/colord-1/colord-gtk
%{_includedir}/colord-1/colord-gtk/*.h
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%doc %{_datadir}/gtk-doc/html/colord-gtk
%{_datadir}/vala/vapi/colord-gtk.vapi
%{_datadir}/vala/vapi/colord-gtk.deps
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.0-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.0-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Richard Hughes <richard@hughsie.com> 0.2.0-1
- New upstream version.

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.1.26-11
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.26-7
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 02 2014 Richard Hughes <richard@hughsie.com> 0.1.26-1
- New upstream version.
- Install the cd-convert utility
- Do not link against the unused gio-unix-2.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.25-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Richard Hughes <rhughes@redhat.com> - 0.1.25-2
- Rebuild for colord soname bump

* Tue Mar 19 2013 Richard Hughes <richard@hughsie.com> 0.1.25-1
- New upstream version.
- Give the sample widget slightly curved corners and a gray outline
- Do not use deprecated functions from libcolord
- Fix warnings when building ColordGtk-1.0.gir
- Fix up the licence boilerplate for CdSampleWidget

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Richard Hughes <richard@hughsie.com> 0.1.24-1
- New upstream version.

* Wed Aug 29 2012 Richard Hughes <richard@hughsie.com> 0.1.23-1
- New upstream version.
- Remove upstreamed patch
- Add include guards to cd-sample-window.h

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Richard Hughes <richard@hughsie.com> 0.1.22-2
- Backport a patch from git master that fixes an include issue with
  projects that want to use colord-gtk.h and colord.h at the same time.

* Tue Jun 26 2012 Richard Hughes <richard@hughsie.com> 0.1.22-1
- New version after Fedora package review.

* Mon Jun 18 2012 Richard Hughes <richard@hughsie.com> 0.1.1-1
- Initial version for Fedora package review.
