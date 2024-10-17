%define upstream_name    Mixin-ExtraFields-Param
%define upstream_version 0.011

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Make your class provide a familiar "param" method
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mixin/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Mixin::ExtraFields)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module mixes in to your class to provide a 'param' method like the
ones provided by the CGI manpage, the CGI::Application manpage, and other
classes. It uses Mixin::ExtraFields, which means it can use any
Mixin::ExtraFields driver to store your data.

By default, the methods provided are:

* * param

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.11.0-2mdv2011.0
+ Revision: 655046
- rebuild for updated spec-helper

* Sat Jun 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 383352
- updating buildrequires:
- import perl-Mixin-ExtraFields-Param


* Fri May 29 2009 cpan2dist 0.011-1mdv
- initial mdv release, generated with cpan2dist

