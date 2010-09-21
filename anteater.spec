Summary:	Dynamic MTA logfile analyser
Summary(pl.UTF-8):	Dynamiczny analizator logów MTA
Name:		anteater
Version:	0.4.5
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/anteater/%{name}-%{version}.tar.bz2
# Source0-md5:	21ab169a88e1a80942cc8816d7ea6438
Patch0:		%{name}-configure.in.patch
Patch0:		%{name}-cstdlib.patch
URL:		http://anteater.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anteater is a log analyser for MTA logfiles (for example sendmail and
postfix). The tool is written in 100% C++ and very easy to customize.
Input, output, and the analysis are modular class objects with a clear
interface.

%description -l pl.UTF-8
Anteater (mrówkojad) jest analizatorem logów MTA (np. sendmaila i
postfiksa). Narzędzie jest napisane w 100% w C++ i jest bardzo łatwe
do przystosowania. Wejście i wyjście są modularnymi klasami obiektów z
przejrzystym interfejsem.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
