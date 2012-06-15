Summary:	Like `chown -R`
Name:		nodejs-chownr
Version:	0.0.1
Release:	1
License:	MIT
Group:		Libraries
URL:		https://github.com/isaacs/chownr
Source0:	http://registry.npmjs.org/chownr/-/chownr-%{version}.tgz
# Source0-md5:	fdd96f06b67ab23f7523ac2e423feb96
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Like `chown -R`.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/chownr
cp -p chownr.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/chownr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/chownr
