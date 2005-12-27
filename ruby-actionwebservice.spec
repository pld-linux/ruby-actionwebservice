Summary:	Web Services libraries for Ruby on Rails
Summary(pl):	Biblioteki us³ug WWW dla Ruby on Rails
Name:		ruby-ActionWebService
%define tarname actionwebservice
Version:	0.9.1
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6578/%{tarname}-%{version}.tgz
# Source0-md5:	56d75b6e8b8cc5eee38446c56888f16f
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
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
