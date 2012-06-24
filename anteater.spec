Summary:	Dynamic MTA logfile analyser.
Summary(pl):	Dynamiczny analizator log�w MTA
Name:		anteater
Version:	0.4.5
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/anteater/%{name}-%{version}.tar.bz2
# Source0-md5:	21ab169a88e1a80942cc8816d7ea6438
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

%description -l pl
Anteater (mr�wkojad) jest analizatorem log�w MTA (np. sendmaila i
postfiksa). Narz�dzie jest napisane w 100% w C++ i jest bardzo �atwe
do przystosowania. Wej�cie i wyj�cie s� modularnymi klasami obiekt�w z
przejrzystym interfejsem.

%prep
%setup -q

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
