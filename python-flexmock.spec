%define module flexmock
# disable html doc due to a missing theme module for sphinx
%bcond doc 0
# twisted is not built for Python 3.15
%bcond tests 0

Name:		python-flexmock
Summary:	A Python library for easy creaation of mocks,stubs and fakes
Version:	0.13.0
Release:	2
License:	BSD-2-Clause
Group:		Development/Python
# URL:		https://github.com/flexmock/flexmock
URL:		https://flexmock.readthedocs.io/
Source0:	https://github.com/flexmock/flexmock/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with doc}
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(myst-parser)
%endif
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(twisted)
%endif

%description
Flexmock is a testing library for easy creation of mocks, stubs and fakes

%if %{with doc}
%package doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.
%endif

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with doc}
%install -a
# Use sphinx-build to build html docs into buildroot docdir,
# Doc generation requires the module to be installed in order to run successfully.
PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}" \
    sphinx-build -b html docs %{buildroot}%{_docdir}/%{name}-doc/html
# remove .buildinfo and .doctrees
rm -rf %{buildroot}%{_docdir}/%{name}-doc/html/{.buildinfo,.doctrees}
%endif

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

%if %{with doc}
%files doc
%doc html README.md LICENSE
%endif
