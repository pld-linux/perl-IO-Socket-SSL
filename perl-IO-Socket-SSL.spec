%include	/usr/lib/rpm/macros.perl
Summary:	IO-Socket-SSL perl module
Summary(pl):	Modu³ perla IO-Socket-SSL
Name:		perl-IO-Socket-SSL
Version:	0.73
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO::Socket/IO-Socket-SSL-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Net-SSLeay
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Socket-SSL perl module 

%description -l pl
Modu³ perla IO-Socket-SSL

%prep
%setup -q -n IO-Socket-SSL-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT
install demo/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IO/Socket/SSL
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/IO/Socket/SSL.pm
%{perl_sitearch}/auto/IO/Socket/SSL

%{_mandir}/man3/*

/usr/src/examples/%{name}
