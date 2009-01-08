Summary:	Stacked GIT
Summary(pl.UTF-8):	GIT z operacjami na stosie
Name:		stgit
Version:	0.14.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://homepage.ntlworld.com/cmarinas/stgit/%{name}-%{version}.tar.gz
# Source0-md5:	84447155c0a86fae795928a581dc22bd
URL:		http://www.procode.org/stgit/
BuildRequires:	git-core
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StGIT is a Python application providing similar functionality to Quilt
(i.e. pushing/popping patches to/from a stack) on top of GIT. These
operations are performed using GIT commands and the patches are stored
as GIT commit objects, allowing easy merging of the StGIT patches into
other repositories using standard GIT functionality.

%description -l pl.UTF-8
StGIT to aplikacja Pythona udostępniająca funkcjonalność podobną do
Quilta (tzn. umieszczanie/pobieranie łat na/ze stosu) w oparciu o GIT.
Operacje te są wykonywane przy użyciu poleceń GIT, a łaty są
przechowywane jako obiekty commitów GIT, co pozwala na łatwe włączanie
łat StGIT do innych repozytoriów przy użyciu standardowej
funkcjonalności GIT.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/commands/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/commands
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/commands/*.py[co]
%{_datadir}/%{name}
