# disable html doc due to a missing plugin for sphinx
%bcond_with doc

Summary:	A Python library for easy creaation of mocks,stubs and fakes
Name:		python-flexmock
Version:	0.11.3
Release:	2
Group:		Development/Python
License:	BSD
URL:		http://flexmock.readthedocs.org/
Source0:	https://files.pythonhosted.org/packages/source/f/flexmock/flexmock-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(poetry-core)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
# docs
%if %{with doc}
BuildRequires:	python3dist(sphinx)
%endif
# for testing with various runners (twisted contains trial)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(twisted)

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

