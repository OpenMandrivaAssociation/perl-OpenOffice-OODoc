%define module	OpenOffice-OODoc
%define name	perl-%{module}
%define version 2.103
%define release %mkrel 1

#(nl) this 2 requires are not needed, they are on a exemple file only
%define _requires_exceptions  perl(Tk::Dialog)\\|perl(Tk) 

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/OpenOffice/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(XML::Twig)
BuildRequires:	perl(Archive::Zip)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A library for Open Document processing

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{perl_vendorlib}/OpenOffice
%{_mandir}/*/*


