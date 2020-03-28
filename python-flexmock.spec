%global pypi_name flexmock

Name:           python-flexmock
Version:        0.10.4
Release:        1
Group:          Development/Python
Summary:        A Python library for easy creaation of mocks,stubs and fakes

License:        BSD
URL:            http://flexmock.readthedocs.org/
Source0:        https://github.com/bkabrda/flexmock/releases/tag/0.10.4/flexmock-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
 
# for testing with various runners (twisted contains trial)
BuildRequires:  python-nose
BuildRequires:  python-pytest
BuildRequires:  python-twisted

%{?python_provide:%python_provide python-flexmock}

%description
Flexmock is a testing library for easy creation of mocks, stubs and fakes


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%py3_build


%install
%py3_install


%files
%doc html README.rst LICENSE
#%%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/__pycache__/*.pyc


