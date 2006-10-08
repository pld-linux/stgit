Summary:	Stacked GIT
Summary(pl):	GIT z operacjami na stosie
Name:		stgit
Version:	0.10
Release:	1
License:	GPL
Group:		Applications
Source0:	http://homepage.ntlworld.com/cmarinas/stgit/%{name}-%{version}.tar.gz
# Source0-md5:	121b22bc3904c8c645ba46c13ac79eae
URL:		http://www.procode.org/stgit/
BuildRequires:	python
Requires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StGIT is a Python application providing similar functionality to Quilt
(i.e. pushing/popping patches to/from a stack) on top of GIT. These
operations are performed using GIT commands and the patches are stored
as GIT commit objects, allowing easy merging of the StGIT patches into
other repositories using standard GIT functionality.

%description -l pl
StGIT to aplikacja Pythona udostêpniaj±ca funkcjonalno¶æ podobn± do
Quilta (tzn. umieszczanie/pobieranie ³at na/ze stosu) w oparciu o GIT.
Operacje te s± wykonywane przy u¿yciu poleceñ GIT, a ³aty s±
przechowywane jako obiekty commitów GIT, co pozwala na ³atwe w³±czanie
³at StGIT do innych repozytoriów przy u¿yciu standardowej
funkcjonalno¶ci GIT.

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
