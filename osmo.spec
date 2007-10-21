#
######		Unknown group!
Summary:	Simple PIM app
Name:		osmo
Version:	0.1.1
Release:	1
License:	GPLv2
Group:		Applications/X11
Source0:	http://clay.ll.pl/osmo/%{name}-%{version}.tar.gz
# Source0-md5:	0593e4798fc58aa0c54c1cd17c1a64be
URL:		http://clay.ll.pl/osmo/
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
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
%doc AUTHORS README TRANSLATORS
%attr(755,root,root) %{_bindir}/osmo
%{_pixmapsdir}/osmo.png
%{_pixmapsdir}/osmo.svg
