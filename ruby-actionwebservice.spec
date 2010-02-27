%define pkgname actionwebservice
Summary:	Web Services libraries for Ruby on Rails
Summary(pl.UTF-8):	Biblioteki usług WWW dla Ruby on Rails
Name:		ruby-%{pkgname}
Version:	1.1.6
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/12320/%{pkgname}-%{version}.tgz
# Source0-md5:	1edfe7484929a54e0cd17e2b43fdbd35
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-ActionWebService
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Service libraries for Ruby on Rails.

%description -l pl.UTF-8
Biblioteki usług WWW dla Ruby on Rails.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActionWebService
