%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name oslo.concurrency
%global pkg_name oslo-concurrency

Name:           python-oslo-concurrency
Version:        3.6.0
Release:        1%{?dist}
Summary:        OpenStack Oslo concurrency library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pkg_name}
Summary:        OpenStack Oslo concurrency library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
# Required for tests
BuildRequires:  python-hacking
BuildRequires:  python-oslotest
BuildRequires:  python-coverage
BuildRequires:  python-futures
BuildRequires:  python-fixtures
BuildRequires:  python-enum34
BuildRequires:  python-eventlet

Requires:       python-babel
Requires:       python-iso8601
Requires:       python-fixtures
Requires:       python-oslo-config
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-posix_ipc
Requires:       python-retrying
Requires:       python-six
Requires:       python-fasteners
Requires:       python-enum34

%description -n python2-%{pkg_name}
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package  -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo concurrency library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures
BuildRequires:  python-oslo-utils
BuildRequires:  python-fasteners

%description -n python-%{pkg_name}-doc
Documentation for the Oslo concurrency library.

%package  -n python-%{pkg_name}-tests
Summary:    Tests for the Oslo concurrency library

Requires:  python-%{pkg_name} = %{version}-%{release}
Requires:  python-hacking
Requires:  python-oslotest
Requires:  python-coverage
Requires:  python-futures
Requires:  python-fixtures

%description -n python-%{pkg_name}-tests
Tests for the Oslo concurrency library.

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo concurrency library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# Required for tests
BuildRequires:  python3-hacking
BuildRequires:  python3-oslotest
BuildRequires:  python3-coverage
BuildRequires:  python3-fixtures
BuildRequires:  python3-eventlet

Requires:       python3-babel
Requires:       python3-iso8601
Requires:       python3-fixtures
Requires:       python3-oslo-config
Requires:       python3-oslo-i18n
Requires:       python3-oslo-utils
Requires:       python3-posix_ipc
Requires:       python3-retrying
Requires:       python3-six
Requires:       python3-fasteners

%description -n python3-%{pkg_name}
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.
%endif

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%doc README.rst
%license LICENSE
%{_bindir}/lockutils-wrapper
%{python2_sitelib}/oslo_concurrency
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_concurrency/tests

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc html

%files -n python-%{pkg_name}-tests
%{python2_sitelib}/oslo_concurrency/tests


%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_concurrency
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_concurrency/tests
%endif

%changelog
* Wed Mar 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 3.6.0-
- Update to 3.6.0

