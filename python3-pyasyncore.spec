#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests (localhost networking required)

%define		module	template
Summary:	Make asyncore available for Python 3.12 onwards
Summary(pl.UTF-8):	Moduł pyasncore dostępny dla Pythona 3.12 i nowszych
Name:		python3-pyasyncore
Version:	1.0.4
Release:	1
License:	PSF v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyasyncore/
Source0:	https://files.pythonhosted.org/packages/source/p/pyasyncore/pyasyncore-%{version}.tar.gz
# Source0-md5:	f97e2b69f1fa11470867b395c2fabf84
URL:		https://pypi.org/project/pyasyncore/
BuildRequires:	python3-modules >= 1:3.12
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the asyncore module as found in Python versions
prior to 3.12 (<https://docs.python.org/3.11/library/asyncore.html>).
It is provided so that existing code relying on "import asyncore" is
able to continue being used without significant refactoring.

%description -l pl.UTF-8
Ten pakiet zawiera moduł asyncore, obecny w wersjach Pythona starszych
niż 3.12 (<https://docs.python.org/3.11/library/asyncore.html>). Jest
udostępniany, aby istniejący kod polegający na "import asyncore" nadal
działał bez potrzeby większego refaktorowania.

%prep
%setup -q -n pyasyncore-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/asyncore
%{py3_sitescriptdir}/pyasyncore-%{version}-py*.egg-info
