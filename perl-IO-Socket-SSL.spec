#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Socket-SSL
Summary:	IO::Socket::SSL -- Nearly transparent SSL encapsulation for IO::Socket::INET.
#Summary(pl):	IO::Socket::SSL -- 
Name:		perl-IO-Socket-SSL
Version:	0.901
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-18
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Net-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a true drop-in replacement for IO::Socket::INET that uses
SSL to encrypt data before it is transferred to a remote server or client.
IO::Socket::SSL supports all the extra features that one needs to write
a full-featured SSL client or server application: multiple SSL contexts,
cipher selection, certificate verification, and SSL version selection.
As an extra bonus, it works perfectly with mod_perl.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install example/* util/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%{perl_sitelib}/IO/Socket/SSL.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
