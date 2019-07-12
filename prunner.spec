Name: prunner
Version: 0.0.1
Release: alt7

Summary: Running and monitoring a process group

Group: Development/Python
License: LGPLv2
Url: https://github.com/Etersoft/prunner

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Thu Feb 15 2018
# optimized out: python-base python-modules python3 python3-base
BuildRequires: python-dev

Requires: sudo python-module-psutil

%description
Running and monitoring a process group

%prep
%setup

%build

%install
install -D -m0755 bin/prunner %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Jul 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt7
- set as noarch, pack README.md

* Thu Aug 09 2018 Etersoft Builder <builder@etersoft.ru> 0.0.1-alt6
- disable build for p7

* Thu Aug 09 2018 Etersoft Builder <builder@etersoft.ru> 0.0.1-alt5
- added special build for c7 and publication of events in the telegram channel

* Thu Apr 19 2018 Etersoft Builder <builder@etersoft.ru> 0.0.1-alt4
- added LICENSE
- update URL (use github)

* Sat Mar 17 2018 Etersoft Builder <builder@etersoft.ru> 0.0.1-alt3
- added option '--run-after' ('-a') for run programs after main process terminated

* Sat Mar 10 2018 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt2
- bug fixes after debugging

* Thu Mar 08 2018 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- first build

