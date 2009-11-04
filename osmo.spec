#
# Conditional builds:
%bcond_with	libsyncml	# enable experimental SyncML plugin
#
Summary:	Simple PIM application
Summary(pl.UTF-8):	Prosta aplikacja PIM (do zarządzania informacjami osobistymi)
Name:		osmo
Version:	0.2.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/osmo-pim/%{name}-%{version}.tar.gz
# Source0-md5:	7fa83efd27cd3ecc54e73f0ec4e91d81
URL:		http://clayo.org/osmo/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libgringotts-devel >= 1.2.1
BuildRequires:	libical-devel >= 0.27
BuildRequires:	libnotify-devel >= 0.4.4
%{?with_libsyncml:BuildRequires:	libsyncml-devel >= 0.4.0}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Osmo is a handy personal organizer which includes calendar, tasks
manager and address book modules. It was designed to be a small, easy
to use and good looking PIM tool to help to manage personal
information. In current state the organizer is quite convenient in use
- for example, user can perform nearly all operations using keyboard.
Also, a lot of parameters are configurable to meet user preferences.
On the technical side, Osmo is GTK+ based tool which use plain XML
database to store all personal data.

%description -l pl.UTF-8
Osmo to podręczny osobisty organizer, zawierający moduły kalendarza,
zarządzania zadaniami i książki adresowej. Został zaprojektowany jako
małe, łatwe w użyciu i dobrze wyglądające narzędzie PIM, mające pomóc
w zarządzaniu informacjami osobistymi. W aktualnym stanie rozwoju
organizer jest w miarę wygodny w użyciu - na przykład można wykonywać
prawie wszystkie operacje z klawiatury. Ponadto większość parametrów
jest konfigurowalna zgodnie z upodobaniami użytkownika. Od strony
technicznej Osmo jest aplikacją opartą na GTK+, wykorzystującą do
przechowywania danych bazę danych w czystym XML-u.

%prep
%setup -q

%build
%configure \
	--with%{!?with_libsyncml:out}-libsyncml
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TRANSLATORS
%attr(755,root,root) %{_bindir}/osmo
%{_pixmapsdir}/osmo.png
%{_desktopdir}/osmo.desktop
%{_iconsdir}/hicolor/*/apps/osmo.*
%{_mandir}/man1/osmo.1*
