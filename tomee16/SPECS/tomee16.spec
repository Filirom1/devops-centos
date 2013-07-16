%global nightly 20130715.041110-127
%define __jar_repack 0 

Name:		apache-tomee-jaxrs
Version:	1.6.0
Release:	SNAPSHOT
Summary:	Apache TomEE 1.6 is an open source software implementation of the Java Servlet and JavaServer Pages technologies

Group:		System Environment/Base
License:	Apache
URL:		http://tomee.apache.org/
Source0:	https://repository.apache.org/content/groups/snapshots/org/apache/openejb/apache-tomee/%{version}-SNAPSHOT/apache-tomee-%{version}-%{nightly}-jaxrs.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

%description
Apache TomEE 1.6 is an open source software implementation of the Java Servlet and JavaServer Pages technologies

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}-%{version}-%{release}/
cp -fr * %{buildroot}%{_libdir}/%{name}-%{version}-%{release}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}-%{version}-%{release}/bin
%{_libdir}/%{name}-%{version}-%{release}/conf
%{_libdir}/%{name}-%{version}-%{release}/lib
%{_libdir}/%{name}-%{version}-%{release}/endorsed
%{_libdir}/%{name}-%{version}-%{release}/LICENSE
%{_libdir}/%{name}-%{version}-%{release}/logs
%{_libdir}/%{name}-%{version}-%{release}/NOTICE
%{_libdir}/%{name}-%{version}-%{release}/RELEASE-NOTES
%{_libdir}/%{name}-%{version}-%{release}/RUNNING.txt
%{_libdir}/%{name}-%{version}-%{release}/temp
%{_libdir}/%{name}-%{version}-%{release}/webapps
%{_libdir}/%{name}-%{version}-%{release}/work

%changelog
* Mon Jul 15 2013 Filirom1 <filirom1@gmail.com> - 1-1
- Initial Package
