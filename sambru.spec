%define name	sambru
%define version	0.23
%define release 7

Name: 	 	%{name}
Summary: 	Transfers addressbook to/from Samsung phones
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.23-6mdv2010.0
+ Revision: 433601
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.23-5mdv2009.0
+ Revision: 260486
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.23-4mdv2009.0
+ Revision: 251883
- rebuild
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.23-2mdv2008.1
+ Revision: 126945
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import sambru


* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 0.23-2mdk
- stale rebuild

* Sat Mar 29 2003 Austin Acton <aacton@yorku.ca> 0.23-1mdk
- initial package
