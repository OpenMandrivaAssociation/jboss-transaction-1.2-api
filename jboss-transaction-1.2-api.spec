%global namedreltag .Alpha3
%global namedversion %{version}%{?namedreltag}

Name:             jboss-transaction-1.2-api
Version:          1.0.0
Release:          0.3%{namedreltag}%{dist}
Summary:          Transaction 1.2 API
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-transaction-api_spec/archive/jboss-transaction-api_1.2_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    felix-osgi-foundation
BuildRequires:    felix-parent
BuildRequires:    maven-local
BuildRequires:    jboss-interceptors-1.2-api

BuildArch:        noarch

%description
The Java Transaction 1.2 API classes.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-transaction-api_spec-jboss-transaction-api_1.2_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt README

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt README

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.Alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Alpha3
- Initial packaging


