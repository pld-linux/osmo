Summary:	Simple PIM application
Summary(pl.UTF-8):	Prosta aplikacja PIM (do zarządzania informacjami osobistymi)
Name:		osmo
Version:	0.4.4
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/osmo-pim/%{name}-%{version}.tar.gz
# Source0-md5:	4a22d229c57c12899520edecd73e6bb9
Patch0:		%{name}-datadir.patch
URL:		http://clayo.org/osmo/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gspell-devel >= 1.2.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-webkit4-devel >= 2.8.0
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libgringotts-devel >= 1.2.1
BuildRequires:	libical-devel >= 1.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:1.20
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2-devel >= 1:2.6.0
Requires:	gspell >= 1.2.0
Requires:	gtk+3 >= 3.10.0
Requires:	gtk-webkit4 >= 2.8.0
Requires:	pango >= 1:1.20
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
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicates of gl,ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{gl_ES,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%banner %{name} -e << EOF

Since version 0.4.0 Osmo uses XDG Base Directory Specification
(http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)
for storing configuration and data files.

The files are stored in locations indicated by XDG_CONFIG_HOME and
XDG_DATA_HOME environmental variables. Typically, these variables are set
to \$HOME/.config/osmo and \$HOME/.local/share/osmo directories.

In order to run Osmo with other setup, these variables have to be
adjusted - e.g. (for BASH shell):

export XDG_CONFIG_HOME="path/to/osmo/config"
export XDG_DATA_HOME="path/to/osmo/data"

EOF

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TRANSLATORS
%attr(755,root,root) %{_bindir}/osmo
%{_datadir}/%{name}
%{_pixmapsdir}/osmo*.png
%{_pixmapsdir}/moonphase_*.png
%{_desktopdir}/osmo.desktop
%{_iconsdir}/hicolor/*/actions/osmo*
%{_iconsdir}/hicolor/*/apps/osmo.*
%{_mandir}/man1/osmo.1*
