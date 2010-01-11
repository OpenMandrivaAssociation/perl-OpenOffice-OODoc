%define upstream_name	 OpenOffice-OODoc
%define upstream_version 2.111

#(nl) this 2 requires are not needed, they are on a exemple file only
%define _requires_exceptions  perl(Tk::Dialog)\\|perl(Tk) 

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/OpenOffice/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(XML::Twig)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A library for Open Document processing

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%make test

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
