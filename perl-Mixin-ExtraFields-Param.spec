%define upstream_name    Mixin-ExtraFields-Param
%define upstream_version 0.011

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Make your class provide a familiar "param" method
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mixin/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


