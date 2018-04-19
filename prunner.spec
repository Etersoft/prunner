Name: prunner
Version: 0.0.1
Release: alt3

Summary: Running and monitoring a process group
Group: Development/Python
License: GPLv2
Url: https://github.com/Etersoft/prunner

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: %name-%version.tar

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

%pre

%files
# %doc README.md
%_bindir/%name

%changelog
* Sat Mar 17 2018 Etersoft Builder <builder@etersoft.ru> 0.0.1-alt3
- added option '--run-after' ('-a') for run programs after main process terminated

* Sat Mar 10 2018 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt2
- bug fixes after debugging

* Thu Mar 08 2018 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- first build

