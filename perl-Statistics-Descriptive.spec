#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
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
Summary(nb):	Perlmodul Statistics::Descriptive
Summary(pl):	Modu³ perla Statistics::Descriptive
Summary(pt_BR):	Módulo Perl Statistics::Descriptive
Summary(pt):	Módulo de Perl Statistics::Descriptive
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Statistics::Descriptive
Summary(sv):	Statistics::Descriptive Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Statistics::Descriptive
Summary(zh_CN):	Statistics::Descriptive Perl Ä£¿é
Name:		perl-Statistics-Descriptive
Version:	2.6
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	05602b7028ada0393b503acee79d2616
Patch0:		%{name}-fix.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Statistics/Descriptive.pm
%{_mandir}/man3/*
