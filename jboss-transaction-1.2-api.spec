%bcond_with javadoc

Name:             jboss-transaction-1.2-api
Version:          1.1.1.Final
Release:          1
Summary:          Transaction 1.2 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
Url:              https://github.com/jboss/jboss-transaction-api_spec
Source0:          https://github.com/jboss/jboss-transaction-api_spec/archive/refs/tags/jboss-transaction-api_1.2_spec-%{version}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    cdi-api
BuildRequires:    jboss-interceptors-1.2-api

BuildArch:        noarch
BuildRequires:    python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
The Java Transaction 1.2 API classes.

%if %{with javadoc}
%package javadoc
Summary:          Javadocs for %{name}

%endif
%if %{with javadoc}
%description javadoc
This package contains the API documentation for %{name}.

%endif
%prep
%setup -q -n jboss-transaction-api_spec-jboss-transaction-api_1.2_spec-%{version}
# The wildcard import makes bnd read versions from every jar on the
# classpath. The CDI jar has no OSGi bundle version, so the range is empty.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r",\s*\*(?=\s*</Import-Package>)", "", text, count=1)
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE.txt README

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt README

%endif
