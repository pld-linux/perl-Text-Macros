%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Macros
Summary:	Text::Macros.pm - an object-oriented text macro engine
Summary(pl):	Text::Macros.pm - obiektowo zorientowany silnik makr tekstowych
Name:		perl-Text-Macros
Version:	0.04
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Macros.pm - an object-oriented text macro engine.

%description -l pl
Text::Macros.pm - obiektowo zorientowany silnik makr tekstowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Text/Macros.pm
%{_mandir}/man3/*
