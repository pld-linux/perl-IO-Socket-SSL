%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Socket-SSL
Summary:	IO-Socket-SSL perl module
Summary(pl):	Modu³ perla IO-Socket-SSL
Name:		perl-IO-Socket-SSL
Version:	0.80
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Net-SSLeay
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Socket-SSL perl module.

%description -l pl
Modu³ perla IO-Socket-SSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IO/Socket/SSL.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
