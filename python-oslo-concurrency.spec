%if 0%{?fedora}
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name oslo.concurrency
%global pkg_name oslo-concurrency

Name:           python-oslo-concurrency
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo concurrency library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pkg_name}
Summary:        OpenStack Oslo concurrency library
%{?python_provide:%python_provide python2-%{pkg_name}}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{pkg_name} = %{upstream_version}
Obsoletes:      python-%{pkg_name} < %{upstream_version}

BuildRequires:  python2-devel
BuildRequires:  python-pbr

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

%description -n python2-%{pkg_name}
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package  -n python2-%{pkg_name}-doc
Summary:    Documentation for the Oslo concurrency library
Group:      Documentation
%{?python_provide:%python_provide python2-%{pkg_name}-doc}
# python_provide does not exist in CBS Cloud buildroot
Provides:   python-%{pkg_name}-doc = %{upstream_version}
Obsoletes:   python-%{pkg_name}-doc < %{upstream_version}

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures
BuildRequires:  python-oslo-utils
BuildRequires:  python-fasteners

%description -n python2-%{pkg_name}-doc
Documentation for the Oslo concurrency library.

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo concurrency library
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

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
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%doc README.rst
%license LICENSE
%{_bindir}/lockutils-wrapper
%{python2_sitelib}/oslo_concurrency
%{python2_sitelib}/*.egg-info

%files -n python2-%{pkg_name}-doc
%license LICENSE
%doc html

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_concurrency
%{python3_sitelib}/*.egg-info
%endif

%changelog
