%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	Descriptive
Summary:	Statistics-Descriptive perl module
Summary(pl):	Modu³ perla Statistics-Descriptive
Name:		perl-Statistics-Descriptive
Version:	2.4
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-Descriptive module provides basic functions used in
descriptive statistics.

%description -l pl
Statistics-Descriptive udostêpnia podstawowe funkcje stosowane w
statystyce opisowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Statistics/Descriptive.pm
%{_mandir}/man3/*
