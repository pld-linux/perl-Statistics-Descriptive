#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	Descriptive
Summary:	Statistics::Descriptive Perl module
Summary(cs):	Modul Statistics::Descriptive pro Perl
Summary(da):	Perlmodul Statistics::Descriptive
Summary(de):	Statistics::Descriptive Perl Modul
Summary(es):	Módulo de Perl Statistics::Descriptive
Summary(fr):	Module Perl Statistics::Descriptive
Summary(it):	Modulo di Perl Statistics::Descriptive
Summary(ja):	Statistics::Descriptive Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Statistics::Descriptive ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Statistics::Descriptive
Summary(pl):	Modu³ perla Statistics::Descriptive
Summary(pt_BR):	Módulo Perl Statistics::Descriptive
Summary(pt):	Módulo de Perl Statistics::Descriptive
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Statistics::Descriptive
Summary(sv):	Statistics::Descriptive Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Statistics::Descriptive
Summary(zh_CN):	Statistics::Descriptive Perl Ä£¿é
Name:		perl-Statistics-Descriptive
Version:	2.6
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::Descriptive module provides basic functions used in
descriptive statistics.

%description -l pl
Statistics::Descriptive udostêpnia podstawowe funkcje stosowane w
statystyce opisowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Statistics/Descriptive.pm
%{_mandir}/man3/*
