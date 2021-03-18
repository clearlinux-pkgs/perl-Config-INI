#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-INI
Version  : 0.025
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-INI-0.025.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-INI-0.025.tar.gz
Summary  : 'simple .ini-file format'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Config-INI-license = %{version}-%{release}
Requires: perl-Config-INI-perl = %{version}-%{release}
Requires: perl(Data::OptList)
Requires: perl(Mixin::Linewise::Readers)
Requires: perl(Mixin::Linewise::Writers)
Requires: perl(Params::Util)
Requires: perl(Sub::Exporter)
Requires: perl(Sub::Install)
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Mixin::Linewise::Readers)
BuildRequires : perl(Mixin::Linewise::Writers)
BuildRequires : perl(Params::Util)
BuildRequires : perl(PerlIO::utf8_strict)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)

%description
This archive contains the distribution Config-INI,
version 0.025:
simple .ini-file format

%package dev
Summary: dev components for the perl-Config-INI package.
Group: Development
Provides: perl-Config-INI-devel = %{version}-%{release}
Requires: perl-Config-INI = %{version}-%{release}

%description dev
dev components for the perl-Config-INI package.


%package license
Summary: license components for the perl-Config-INI package.
Group: Default

%description license
license components for the perl-Config-INI package.


%package perl
Summary: perl components for the perl-Config-INI package.
Group: Default
Requires: perl-Config-INI = %{version}-%{release}

%description perl
perl components for the perl-Config-INI package.


%prep
%setup -q -n Config-INI-0.025
cd %{_builddir}/Config-INI-0.025

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-INI
cp %{_builddir}/Config-INI-0.025/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-INI/27e158af651b5a0cac04a11de0e4ab7abe601a0b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::INI.3
/usr/share/man/man3/Config::INI::Reader.3
/usr/share/man/man3/Config::INI::Writer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-INI/27e158af651b5a0cac04a11de0e4ab7abe601a0b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Config/INI.pm
/usr/lib/perl5/vendor_perl/5.32.1/Config/INI/Reader.pm
/usr/lib/perl5/vendor_perl/5.32.1/Config/INI/Writer.pm
