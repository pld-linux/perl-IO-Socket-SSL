#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Socket-SSL
Summary:	IO::Socket::SSL -- Nearly transparent SSL encapsulation for IO::Socket::INET
Summary(pl):	IO::Socket::SSL -- prawie przezroczysta obudowa SSL dla IO::Socket::INET
Name:		perl-IO-Socket-SSL
Version:	0.92
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Net-SSLeay
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a true drop-in replacement for IO::Socket::INET that
uses SSL to encrypt data before it is transferred to a remote server
or client. IO::Socket::SSL supports all the extra features that one
needs to write a full-featured SSL client or server application:
multiple SSL contexts, cipher selection, certificate verification, and
SSL version selection. As an extra bonus, it works perfectly with
mod_perl.

%description -l pl
Ten modu³ jest prawdziwym zamiennikiem dla IO::Socket::INET,
u¿ywaj±cym SSL do kodowania danych przed przesy³aniem do zdalnego
serwera lub klienta. IO::Socket::SSL wspiera wszystkie dodatkowe
rzeczy potrzebne do napisania w pe³ni funkcjonalnego klienta lub
serwera SSL: wiele kontekstów SSL, wybór szyfru, weryfikacja
certyfikatu, wybór wersji SSL. Ponadto wspaniale dzia³a z mod_perlem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/* util/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README docs/*
%{perl_sitelib}/IO/Socket/SSL.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
