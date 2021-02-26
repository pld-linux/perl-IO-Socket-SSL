#
# Conditional build:
%bcond_with	tests	# perform "make test" - needs network connection
#
%define		pdir	IO
%define		pnam	Socket-SSL
Summary:	IO::Socket::SSL - nearly transparent SSL encapsulation for IO::Socket::INET
Summary(pl.UTF-8):	IO::Socket::SSL - prawie przezroczysta obudowa SSL dla IO::Socket::INET
Name:		perl-IO-Socket-SSL
Version:	2.070
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c8df96b5249c02025e2eb48596c213b
URL:		http://search.cpan.org/dist/IO-Socket-SSL/
%if %{with tests}
BuildRequires:	perl-Net-SSLeay >= 1.46
BuildRequires:	perl-Scalar-List-Utils
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
# actually Net::SSLeay using openssl >= 0.9.8
Requires:	openssl >= 0.9.8
Suggests:	perl-Net-IDN-Encode
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

%description -l pl.UTF-8
Ten moduł jest prawdziwym zamiennikiem dla IO::Socket::INET,
używającym SSL do kodowania danych przed przesyłaniem do zdalnego
serwera lub klienta. IO::Socket::SSL wspiera wszystkie dodatkowe
rzeczy potrzebne do napisania w pełni funkcjonalnego klienta lub
serwera SSL: wiele kontekstów SSL, wybór szyfru, weryfikacja
certyfikatu, wybór wersji SSL. Ponadto wspaniale działa z mod_perlem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "n" | \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Socket/SSL.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README docs/*
%{perl_vendorlib}/IO/Socket/SSL.pm
%{perl_vendorlib}/IO/Socket/SSL
%{_mandir}/man3/IO::Socket::SSL*.3pm*
%{_examplesdir}/%{name}-%{version}
