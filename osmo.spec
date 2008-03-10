Summary:	Simple PIM application
Summary(pl.UTF-8):	Prosta aplikacja PIM (do zarządzania informacjami osobistymi)
Name:		osmo
Version:	0.1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://clay.ll.pl/osmo/%{name}-%{version}.tar.gz
# Source0-md5:	0593e4798fc58aa0c54c1cd17c1a64be
URL:		http://clay.ll.pl/osmo/
BuildRequires:	gtk+2-devel >= 2:2.8.0
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
%configure
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
%{_pixmapsdir}/osmo.svg
