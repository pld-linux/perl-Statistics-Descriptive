%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Statistics-Descriptive perl module
Summary(pl):	Modu� perla Statistics-Descriptive
Name:		perl-Statistics-Descriptive
Version:	2.4
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-Descriptive-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Statistics-Descriptive module provides basic functions used in descriptive
statistics. 

%description -l pl
Statistics-Descriptive udost�pnia podstawowe funkcje stosowane w statystyce
opisowej.

%prep
%setup -q -n Statistics-Descriptive-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/Descriptive
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Statistics/Descriptive.pm
%{perl_sitearch}/auto/Statistics/Descriptive

%{_mandir}/man3/*
