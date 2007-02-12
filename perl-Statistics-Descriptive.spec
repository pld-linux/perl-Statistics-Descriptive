#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	Descriptive
Summary:	Statistics::Descriptive Perl module
Summary(cs.UTF-8):   Modul Statistics::Descriptive pro Perl
Summary(da.UTF-8):   Perlmodul Statistics::Descriptive
Summary(de.UTF-8):   Statistics::Descriptive Perl Modul
Summary(es.UTF-8):   Módulo de Perl Statistics::Descriptive
Summary(fr.UTF-8):   Module Perl Statistics::Descriptive
Summary(it.UTF-8):   Modulo di Perl Statistics::Descriptive
Summary(ja.UTF-8):   Statistics::Descriptive Perl モジュール
Summary(ko.UTF-8):   Statistics::Descriptive 펄 모줄
Summary(nb.UTF-8):   Perlmodul Statistics::Descriptive
Summary(pl.UTF-8):   Moduł perla Statistics::Descriptive
Summary(pt_BR.UTF-8):   Módulo Perl Statistics::Descriptive
Summary(pt.UTF-8):   Módulo de Perl Statistics::Descriptive
Summary(ru.UTF-8):   Модуль для Perl Statistics::Descriptive
Summary(sv.UTF-8):   Statistics::Descriptive Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Statistics::Descriptive
Summary(zh_CN.UTF-8):   Statistics::Descriptive Perl 模块
Name:		perl-Statistics-Descriptive
Version:	2.6
Release:	3
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

%description -l pl.UTF-8
Statistics::Descriptive udostępnia podstawowe funkcje stosowane w
statystyce opisowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

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
