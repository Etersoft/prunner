Name: prunner
Version: 0.0.1
Release: alt1

Summary: Running and monitoring a process group
Group: Development/Python
License: GPLv2
Url: https://gitlab.eterfund.ru/pv/prunner

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
* Thu Mar 08 2018 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- first build

