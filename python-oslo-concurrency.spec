# Created by pyp2rpm-1.1.2
%global pypi_name oslo.concurrency

Name:           python-oslo-concurrency
Version:        1.4.1
Release:        2%{?dist}
Summary:        oslo.concurrency library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires: python-pbr
Requires: python-babel
Requires: python-iso8601
Requires: python-fixtures
Requires: python-oslo-config
Requires: python-oslo-i18n
Requires: python-oslo-utils
Requires: python-posix_ipc
Requires: python-six
Requires: python-retrying

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
cp -r oslo_concurrency/openstack %{buildroot}%{python2_sitelib}/oslo_concurrency


%files
%doc html README.rst doc/source/readme.rst
%license LICENSE
%{python2_sitelib}/oslo_concurrency
%{python2_sitelib}/oslo
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/lockutils-wrapper

%changelog
* Fri Feb 20 2015 Matthias Runge <mrunge@redhat.com> - 1.4.1-2
- added openstack/common/fileutils.py
- added dependencies

* Wed Jan 28 2015 Matthias Runge <mrunge@redhat.com> - 1.4.1-1
- Initial package (rhbz#1186826)
