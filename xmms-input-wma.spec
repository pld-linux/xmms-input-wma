Summary:	XMMS input plugin for WMA file format support
Summary(pl):	Wtyczka dla XMMS-a odtwarzaj±ca pliki w formacie WMA dla XMMS
Name:		xmms-input-wma
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://mcmcc.bat.ru/xmms-wma/xmms-wma-%{version}.tar.bz2
# Source0-md5:	25cfcfb7deed581dea3aae3b153cc291
URL:		http://mcmcc.bat.ru/xmms-wma/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a XMMS input plugin for support WMA format.

%description -l pl
Wtyczka ta pozwala XMMS-owi odtwarzaæ muzykê w formacie WMA.

%prep
%setup -q -n xmms-wma-%{version}

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install libwma.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme*
%attr(755,root,root) %{xmms_input_plugindir}/*.so
