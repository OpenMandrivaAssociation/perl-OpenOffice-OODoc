%define upstream_name	 OpenOffice-OODoc
%define upstream_version 2.125

#(nl) this 2 requires are not needed, they are on a exemple file only
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Tk::Dialog\\)|perl\\(Tk\\)'
%else
%define _requires_exceptions  perl(Tk::Dialog)\\|perl(Tk) 
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/OpenOffice/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(XML::Twig)

BuildArch:	noarch

%description
A library for Open Document processing

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{perl_vendorlib}/OpenOffice
%{_mandir}/*/*


%changelog
* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.125.0-1mdv2011.0
+ Revision: 553134
- update to 2.125

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.124.0-1mdv2010.1
+ Revision: 532153
- update to 2.124

* Mon Mar 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.123.0-1mdv2010.1
+ Revision: 526451
- update to 2.123

* Thu Mar 11 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.122.0-1mdv2010.1
+ Revision: 518082
- update to 2.122

* Fri Jan 29 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.112.0-1mdv2010.1
+ Revision: 497915
- update to 2.112

* Mon Jan 11 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.111.0-1mdv2010.1
+ Revision: 489516
- update to 2.111

* Wed Jan 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.109.0-1mdv2010.1
+ Revision: 486605
- update to 2.109

* Mon May 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.108-1mdv2010.0
+ Revision: 379520
- update to new version 2.108

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.107-1mdv2009.1
+ Revision: 311992
- update to new version 2.107

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.106-1mdv2009.1
+ Revision: 300710
- update to new version 2.106

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.105-1mdv2009.1
+ Revision: 292338
- update to new version 2.105

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.103-1mdv2009.0
+ Revision: 220150
- update to new version 2.103

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.102-1mdv2009.0
+ Revision: 201863
- update to new version 2.102

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.035-1mdv2008.0
+ Revision: 47703
- update to new version 2.035


* Tue Aug 29 2006 guillomovitch
+ 2006-08-29 10:35:55 (58590)
- new version\nfix directory ownership

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 15:03:03 (43229)
- import perl-OpenOffice-OODoc-2.026-1mdv2007.0

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.026-1mdv2007.0
- New version 2.026

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.025-1mdv2007.0
- New release 2.025

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.024-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Mon Mar 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.024-1mdk
- New release 2.024

* Wed Feb 22 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.023-1mdk
- New release 2.023

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.022-1mdk
- New release 2.022
- fix non-interactive build

* Thu Jan 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.019-2mdk
- Fix Typo
- Fix Requires

* Tue Jan 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.019-1mdk
- first mdk release

