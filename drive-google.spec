%global debug_package   %{nil}
%global bname           drive
%global commit          52aed62548f4c408a3042cd2375661ac869d7710
%global commit_short    %(c=%{commit}; echo ${c:0:7})

Name:           %{bname}-google
Version:        0.3.9.1
Release:        1.%{commit_short}%{?dist}
Summary:        Pull or push Google Drive files
License:        ASL 2.0
URL:            http://github.com/odeke-em/drive
Source0:        https://github.com/odeke-em/drive/archive/%{commit}.tar.gz#/%{bname}-%{commit_short}.tar.gz
BuildRequires:  gcc
BuildRequires:  golang >= 1.7.0
BuildRequires:  git


%description
drive is a program to pull or push Google Drive files.


%prep
%setup -n %{bname}-%{commit}


%build
export GOPATH="$(pwd)/_build"
go get -u github.com/odeke-em/%{bname}/cmd/%{bname}
go get github.com/odeke-em/ripper/src
go get github.com/odeke-em/xon/pkger/src

#drive-google
pushd %{name}
go build -o %{name}
popd

#drive-server
go get github.com/odeke-em/rsc/qr
go get github.com/martini-contrib/binding
pushd %{bname}-server
go build -o %{bname}-server
popd


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{name}/%{name} %{buildroot}%{_bindir}/
install -p -m 0755 %{bname}-server/%{bname}-server %{buildroot}%{_bindir}/

install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -p -m 0644 icons/*.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/

install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes
install -p -m 0644 icons/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/icons/hicolor/*


%changelog
* Tue Apr 04 2017 Vaughan <devel at agrez dot net> - 0.3.9.1-1.52aed62
- New release
- Update to git commit: 52aed62548f4c408a3042cd2375661ac869d7710

* Sun Jan 15 2017 Vaughan <devel at agrez dot net> - 0.3.9-1.a9f53bc
- New release
- Update to git commit: a9f53bc4cc9d9d2eada836602ad4b4a7902424a6

* Wed Oct 12 2016 Vaughan <devel at agrez dot net> - 0.3.8.1-1.aa79e32
- New release
- Update to git commit: aa79e324a22a2073b68c61783f4015426b7dbe67

* Wed Aug 24 2016 Vaughan <devel at agrez dot net> - 0.3.7-1.bd7e3f5
- New release
- Update to git commit: bd7e3f5ad5a67a27892e47da5c36452bfdfb8513

* Tue May 24 2016 Vaughan <devel at agrez dot net> - 0.3.6-1.d75bc82
- New release
- Update to git commit: d75bc827514eb54378c54452b7bb00b325ffb885

* Mon Mar 14 2016 Vaughan <devel at agrez dot net> - 0.3.5-1.2334708
- Initial package
- Git commit 2334708ccbaff51544634a8b8d93cd08910765cf

