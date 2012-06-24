%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-Descriptive perl module
Summary(pl):	Modu� perla Statistics-Descriptive
Name:		perl-Statistics-Descriptive
Version:	2.4
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-Descriptive-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-Descriptive module provides basic functions used in
descriptive statistics.

%description -l pl
Statistics-Descriptive udost�pnia podstawowe funkcje stosowane w
statystyce opisowej.

%prep
%setup -q -n Statistics-Descriptive-%{version}
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
