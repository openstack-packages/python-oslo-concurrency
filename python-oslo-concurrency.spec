%global pypi_name oslo.concurrency
%global pkg_name oslo-concurrency

Name:           python-oslo-concurrency
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.concurrency library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

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

%description
An OpenStack library for concurrency.

%package doc
Summary:    Documentation for the Oslo concurrency library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures
BuildRequires:  python-oslo-utils
# TODO: Uncomment once python-fasteners reviewed and packaged
# BuildRequires: python-fasteners

%description doc
Documentation for the Oslo concurrency library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

#delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{pypi_name}/tests/

%files
%doc README.rst LICENSE
%{_bindir}/lockutils-wrapper
%{python2_sitelib}/oslo_concurrency
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE


%changelog
