# Created by pyp2rpm-1.1.2
%global pypi_name oslo.concurrency

Name:           python-oslo-concurrency
Version:        1.8.0
Release:        1%{?dist}
Summary:        OpenStack Oslo concurrency library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-config
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-posix_ipc
Requires:       python-retrying
Requires:       python-six
# FIXME exported testing infra which should be sub-packaged
Requires:       python-fixtures

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package doc
Summary:    Documentation for the Oslo concurrency library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx >= 2.5.0

%description doc
Documentation for the Oslo concurrency library.

%prep
%setup -q -n %{pypi_name}-%{version}
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
rm -fr %{buildroot}%{python2_sitelib}/oslo_concurrency/tests/

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo_concurrency
%{python2_sitelib}/oslo
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/lockutils-wrapper

%files doc
%license LICENSE
%doc html

%changelog
* Wed Apr 01 2015 Alan Pevec <apevec@redhat.com> - 1.8.0-1
- update to 1.8.0

* Wed Mar 11 2015 Matthias Runge <mrunge@redhat.com> - 1.6.0-1
- upgrade to 1.6.0

* Fri Feb 20 2015 Matthias Runge <mrunge@redhat.com> - 1.4.1-2
- added openstack/common/fileutils.py
- added dependencies

* Wed Jan 28 2015 Matthias Runge <mrunge@redhat.com> - 1.4.1-1
- Initial package (rhbz#1186826)
