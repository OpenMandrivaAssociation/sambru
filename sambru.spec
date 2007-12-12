%define name	sambru
%define version	0.23
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Transfers addressbook to/from Samsung phones.
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://lager.dyndns.org/sambru/
License:	GPL
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl uucp

%description
SamBru (Samsung Backup and Restore Utility) is a perl script that will talk
to a Samsung SCH-6100 or SCH-8500 phone. It is also reported to work with the
SCH-850, SPH-T100, i and "uproar" phones. (Note: it will most likely NOT work
with a SCH-3500, as it uses a different (binary) format.) You can use it to
back up and restore the phone book, calendar, and TODO list. It can save the
data in either raw/native format, or as vCard/vCalendar data so that
GnomeCard and GnomeCal can be used to view & edit the data. Currently, only
the phone list is supported.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO Changelog
%{_bindir}/%name

