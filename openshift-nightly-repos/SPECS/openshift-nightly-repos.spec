Name:		openshift-nightly-repos
Version:	1
Release:	1%{?dist}
Summary:	Extra Packages for OpenShift nightly repository configuration

Group:		System Environment/Base
License:	MIT
URL:		http://people.redhat.com/~hhorak/software-collections/
Source0:	openshift-nightly.repo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

%description
This package contains the Openshift nightly repository


%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .


%build

%install
rm -rf $RPM_BUILD_ROOT

#yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%config(noreplace) /etc/yum.repos.d/*


%changelog
* Fri Jul 05 2013 Filirom1 <filirom1@gmail.com> - 1-1
- Initial Package
