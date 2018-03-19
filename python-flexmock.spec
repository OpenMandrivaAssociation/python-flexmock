# Created by pyp2rpm-2.0.0
%global pypi_name flexmock
%global with_python2 1
%define version 0.10.2

Name:           python3-flexmock
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        A Python library for easy creaation of mocks,stubs and fakes

License:        BSD
URL:            http://flexmock.readthedocs.org/
Source0:        https://pypi.python.org/packages/4a/92/6ee358dfeeb1fb6d22e64c5afef525e510b60ec39d59cedfe1da195cf623/flexmock-0.10.2.tar.gz#md5=5767113cc7169ad2b8d906c159fd2eba
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
 
%if %{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
%endif # if with_python2


%description
Flexmock is a testing library for easy creation of mocks, stubs and fakes

%if 0%{?with_python2}
%package -n     python-%{pypi_name}
Summary:        A Python library for easy creation of mocks,stubs and fakes


%description -n python-%{pypi_name}
Flexmock is a testing library for easy to creation of mocks, stubs and fakes
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%endif # with_python2


%build
%{__python} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc html README.rst LICENSE
#%%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%if 0%{?with_python2}
%files -n python-%{pypi_name}
%doc html README.rst LICENSE

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python2

