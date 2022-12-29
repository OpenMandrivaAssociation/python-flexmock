# disable html doc due to a missing plugin for sphinx
%bcond_with doc

Name:		python-flexmock
Version:	0.11.3
Release:	1
Group:		Development/Python
Summary:	A Python library for easy creaation of mocks,stubs and fakes

License:	BSD
URL:		http://flexmock.readthedocs.org/
Source0:	https://files.pythonhosted.org/packages/source/f/flexmock/flexmock-%{version}.tar.gz
BuildArch:	noarch
 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
# docs
%if %{with doc}
BuildRequires:	python-sphinx
%endif
# for testing with various runners (twisted contains trial)
BuildRequires:	python-nose
BuildRequires:	python-pytest
BuildRequires:	python-twisted

%description
Flexmock is a testing library for easy creation of mocks, stubs and fakes

%files
%license LICENSE
%doc README.md
%{?with_doc:%doc html}
%{python3_sitelib}/flexmock/
%{python3_sitelib}/flexmock*-info

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n flexmock-%{version}

# Remove bundled egg-info
rm -rf flexmock.*-info

# generate html docs
%if %{with doc}
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%build
%py_build

%install
%py_install

