#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-RSSAggregator
Summary:	POE::Component::RSSAggregator - A Simple POE RSS Aggregator
Summary(pl):	POE::Component::RSSAggregator - prosty RSS Aggregator dla POE
Name:		perl-POE-Component-RSSAggregator
Version:	0.02
Release:	1
# same as perl, but GPL2 in LICENSE
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	b69d55d29ec83bf990b11a7d0086e9dd
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.22
BuildRequires:	perl-POE-Component-Client-HTTP >= 0.51
BuildRequires:	perl-XML-RSS-Feed >= 0.01
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::RSSAggregator is a simple POE RSS aggregator.

%description -l pl
POE::Component::RSSAggregator to prosty RSS aggregator dla POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Todo
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
