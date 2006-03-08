Summary:	Web Services libraries for Ruby on Rails
Summary(pl):	Biblioteki us³ug WWW dla Ruby on Rails
Name:		ruby-ActionWebService
%define tarname actionwebservice
Version:	1.0.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/7651/%{tarname}-%{version}.tgz
# Source0-md5:	7a154235a515e55120fd47ef9841e5ec
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Service libraries for Ruby on Rails.

%description -l pl
Biblioteki us³ug WWW dla Ruby on Rails.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActionWebService
