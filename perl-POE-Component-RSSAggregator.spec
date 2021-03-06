#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Component-RSSAggregator
Summary:	POE::Component::RSSAggregator - a simple POE RSS aggregator
Summary(pl.UTF-8):	POE::Component::RSSAggregator - prosty Agregator RSS dla POE
Name:		perl-POE-Component-RSSAggregator
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5d3283587a8e82dbd73f725cd9c5779
URL:		http://search.cpan.org/dist/POE-Component-RSSAggregator/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.22
BuildRequires:	perl-POE-Component-Client-HTTP >= 0.51
BuildRequires:	perl-XML-RSS-Feed >= 0.01
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::RSSAggregator is a simple POE RSS aggregator.

%description -l pl.UTF-8
POE::Component::RSSAggregator to prosty RSS aggregator dla POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/POE/*/*.pm
%{_mandir}/man3/*
