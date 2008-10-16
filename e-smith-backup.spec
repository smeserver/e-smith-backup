# $Id: e-smith-backup.spec,v 1.30 2008/10/16 16:15:54 slords Exp $

Summary: e-smith module to provide the backup panel
%define name e-smith-backup
Name: %{name}
%define version 2.2.0
%define release 4
Version: %{version}
Release: %{release}%{?dist}
License: Artistic
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-backup-2.2.0-localise_fix.patch
Patch2: e-smith-backup-2.2.0-fixPleaseConfigure.patch
Patch3: e-smith-backup-2.2.0-restore_list.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools >= 1.11.0-03
BuildRequires: gettext
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-lib >= 1.15.1-19
Requires: perl(Quota)
Requires: perl(Unix::PasswdFile)
Requires: perl(Unix::GroupFile)
Requires: perl(POSIX)
Requires: perl(Locale::gettext)
Requires: perl(Digest::MD5)
Requires: perl(File::Copy)
Requires: perl(esmith::I18N)
Requires: dar
Requires: e-smith-formmagick >= 1.4.0-12

%changelog
* Thu Oct 16 2008 Shad L. Lords <slords@mail.com> 2.2.0-4.sme
- Make dar use defined list of directories to backup [SME: 4676]

* Thu Oct 16 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-3.sme
- Correct translation of CONFIGURATION_TO_BE_DONE to be proper English [SME: 4669]

* Thu Oct 9 2008 Shad L. Lords <slords@mail.com> 2.2.0-2.sme
- Fix localization strings in backup panel [SME: 4650]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Thu Aug 7 2008 Shad L. Lords <slords@mail.com> 1.15.0-22
- Localise status of workstation backup [SME: 4481]

* Fri Aug 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.15.0-21
- Fix too greedy removel of locale key CONFIGURE_TAPE_BACKUP [SME: 4469]

* Sat Jul 26 2008 Shad L. Lords <slords@mail.com> 1.15.0-20
- Make full backups have priority over incremental [SME: 4395]

* Sat Jul 26 2008 Shad L. Lords <slords@mail.com> 1.15.0-19
- Fix redirect to stderr on check tape cronjob [SME: 4458]

* Sun Jul 7 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.15.0-18
- Add common <base> tags to e-smith-formmagick's general [SME: 4286]

* Sat May 31 2008 Gavin Weight <gweight@gmail.com> 1.15.0-17
- Fix Dar manager to redirect correctly in system call. [SME: 4304]

* Mon May 26 2008 Gavin Weight <gweight@gmail.com> 1.15.0-16
- Fix Dar to expand correctly. [SME: 4304]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.15.0-15
- Add common <base> tags to e-smith-formmagick's general [SME: 4286]

* Wed Apr 09 2008 Stephen Noble <support@dungog.net> 1.15.0-14
- Minor fix in translation of hours [SME: 4179]

* Tue Mar 25 2008 Shad L. Lords <slords@mail.com> 1.15.0-13
- Fix localization in restore routine [SME: 3989]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 1.15.0-12
- Remove <br> tag from error msg  [SME: 3989]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 1.15.0-11
- Move/copy Backup_Desc to Backup_Desc_Dar for 1.15 rel [SME: 4024]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.15.0-10
- Remove <base> tags now in general [SME: 3912]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.15.0-9
- Remove duplicate <base> entries [SME: 3887]

* Thu Nov 29 2007 Gavin Weight <gweight@gmail.com> 1.15.0-8
- Fix restore files location path. [SME: 3593]

* Mon Nov 19 2007 Gavin Weight <gweight@gmail.com> 1.15.0-7
- Fix compression setting range (Thanks JPL) . [SME: 3560]

* Fri Nov 09 2007 Gavin Weight <gweight@gmail.com> 1.15.0-06
- Enhancement to DAR code (Thanks JPL) . [SME: 3538]

* Fri Oct 26 2007 Gavin Weight <gweight@gmail.com> 1.15.0-05
- Fix up DAR code to enable backup to complete. [SME: 3373]

* Tue Sep 11 2007 Charlie Brady <charlie_brady@mitel.com> 1.15.0-04
- Remove desktop verify and desktop restore features. Note that
  lexicon entries have not been removed. [SME: 3372]

* Fri Sep 07 2007 Charlie Brady <charlie_brady@mitel.com> 1.15.0-03
- Reformat new DAR code to match existing coding style.

* Wed Sep 05 2007 Jean-Paul Leclere <jean-paul@leclere.org> 1.15.0-02
- Dar workstation backup patch

* Wed Sep 05 2007 Charlie Brady <charlie_brady@mitel.com> 1.15.0-01
- Roll new development version.

* Sun Jul 01 2007 Shad L. Lords <slords@mail.com> 1.14.0-16
- Remove files/dirs that don't exist from the backup list [SME: 3115]

* Sat Jun 30 2007 Shad L. Lords <slords@mail.com> 1.14.0-15
- force proxy request to 1.0 to improve backup2desktop speed [SME: 178]

* Sun Jun 03 2007 Gavin Weight <gweight@gmail.com> 1.14.0-14
- Backup to desktop changes BackupType fix. [SME 3026]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Wed Mar 07 2007 Shad L. Lords <slords@mail.com> 1.14.0-13
- Add db entry to override who gets backup reminder email [SME: 23]

* Fri Jan 26 2007 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-12
- Restore group entry for machine accounts and update tests [SME: 1792]

* Sat Jan 06 2007 Shad L. Lords <slords@mail.com> 1.14.0-11
- Change restore-from-disk to chroot tar from cpio [SME: 2318]

* Sat Jan 06 2007 Shad L. Lords <slords@mail.com> 1.14.0-10
- Link in eject action. [SME: 795]
- Fix do_backup to actually pass backup type. [SME: 1055]

* Fri Jan 05 2007 Shad L. Lords <slords@mail.com> 1.14.0-9
- Make tape actions depend on tape backup. [SME: 1055]
- Make backup type configurable via db. [SME: 1055]

* Wed Jan 03 2007 Shad L. Lords <slords@mail.com> 1.14.0-8
- Add eject action and default to no. [SME: 795]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Nov 08 2006 Charlie Brady <charlie_brady@mitel.com> 1.14.0-06
- Use tarsize not dumpsize to determine when backup is too large.
  [SME: 2041]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-05
- Fix typo in crontab template for 'disabled' case [SME: 1092]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-04
- Move /etc/cron.d/backup into /etc/crontab fragment [SME: 1172]
- Expand /etc/crontab in conf-backup. e-smith-base already does
  it for us in bootstrap-console-save [SME: 1172]
- Remove /etc/cron.d/backup in post [SME: 1172]

* Wed Mar 15 2006 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-03
- Add semi-colon to last code change. Saves head-scratching if
  someone removes the braces at some later stage. [SME: 1045]

* Wed Mar 15 2006 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-02
- Add warning about desktop backup if the server has more than
  2GB of data. [SME: 1045]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.14.0-01
- Roll stable stream version. [SME: 1016]

* Sun Mar 12 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.4-10
- Another fix to restore-from-disk script. [SME: 821]

* Thu Feb 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.4-09
- Fix restore-from-disk script. [SME: 821]

* Mon Feb  6 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.4-08
- Fix 24->12 hour time display problem (courtesy of Federico Simoncelli).
  [SME: 667]

* Wed Feb 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.4-07
- Add restore-from-disk script. [SME: 615]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.4-06
- Don't delete config dbs in pre-restore [SME: 229]

* Tue Dec 06 2005 Filippo Carletti <carletti@mobilia.it> 1.13.4-05
- Tape reminder uses mt status to check if tape loaded [SME: 251]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.4-04
- Bump release number only

* Tue Nov  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.4-03]
- Improve user feedback if pre-backup or pre-restore events fail. [SF: 1334923]

* Mon Oct 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.4-02]
- Create empty /etc/e-smith/db/backups directory to trigger migration
  to new location. [SF: 1335862]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.4-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.3-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.2-17]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Sun Sep 25 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.2-16]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Sun Sep 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-15]
- Remove explict use of CGI (which caused double construction of
  the CGI object, and loss of uploaded data file). [SF: 1264699]

* Fri Sep 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-14]
- Don't delete configuration dbs in pre-restore event until
  we have finished using them. [SF: 1292448]

* Tue Aug 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-13]
- Really add delete-configuration-dbs action. [SF: 1246347,1275962]

* Fri Aug 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.13.2-12]
- Delete configuration dbs from /home/e-smith/db/ prior to
  a restore to ensure that the ones coming from tape are the
  only ones on the system after the restore [SF: 1246347]

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-11]
- Restore passwd file entries for machine accounts. [SF: 1254663]

* Fri Jul 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-10]
- Enforce Posix behaviour of df command, in restore functions of panel.
  [SF: 1242986]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-09]
- Remove last deprecated esmith::config API calls. [SF: 1216546]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-08]
- Remove explicit paths to db files. [SF: 1216546]

* Fri Apr 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-07]
- Remove another anacronistic version requires in perl library.
  Grrrr!!! [charlieb MN00050370]

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-06]
- Use generic_template_expand action in place of conf-backup.
  Update e-smith-lib dependency. [MN00064130]

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-05]
- Ensure that smbpasswd file appears last in list during restore/verification.
  [MN00073362]
- Fix merging of samba files. [MN00073365]

* Mon Nov  8 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-04]
- Explicitly list required perl modules - RPM didn't work it out correctly.
  [charlieb MN00050751]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.2-03]
- Remove deprecated "require v5.6.0". [charlieb MN00050370]
- Allow RPM to work out what the perl Requires headers should be.
  [charlieb MN00050751]

* Thu Sep 16 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-02]
- Fixed Content-disposition header. [msoulier MN00049326]

* Sat Jun 19 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.2-01]
- skipping mps branch start - 1.13.2

* Fri May 21 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-06]
- Added /etc/samba/secrets.tdb to the restore list. [msoulier MN00020969]

* Mon Mar  1 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-05]
- Updated do_backup to pass a "tape" argument when using signal-event
  and rewind-tape to exit if a second argument is not given.
  [msoulier dpar-22041]

* Wed Jan 14 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-04]
- Added /etc/sudoers to backup list for desktop backup. [msoulier 4954]

* Fri Nov 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-03]
- Display big-red reboot warning like other panels. Wow, it's hard to miss
  now. [msoulier 10240]

* Fri Nov 28 2003 Mark Knox <markk@e-smith.com>
- [1.13.0-02]
- Display reboot warning and button after successful desktop restore [markk
  1312]

* Thu Nov  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-01]
- rolling to dev stream - 1.13.0

* Thu Sep 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.1-02]
- Relocate /etc/secrets.tdb to /etc/samba [gordonr 9759]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.1-01]
- Rebuild [gordonr 1305]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.0-09]
- Adjusted Copyright [gordonr 1305]

* Mon Jul 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.0-08]
- Whitespace fix in Backup.pm [gordonr 9428]
 
* Mon Jul 14 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-07]
- Remove /etc/samba/smbpasswd symlink if we find it, before doing
  the move/symlink shuffle with smbpasswd files. This prevents us
  "preserving" old symlinks. [charlieb 9416]

* Mon Jul 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.0-06]
- Rename the pre-restore cache files in $file.time(). This preserves
  them in case we want to wander back through them after an
  upgrade, and ensures that they won't be around to confuse another
  post-upgrade [gordonr 9428]

* Wed Jul  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.0-05]
- Handle the "everything o.k. with relocation" case [gordonr 9333]

* Wed Jul  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.12.0-04]
- Further safeguards for the /etc/smbpasswd -> /etc/samba/smbpasswd
  relocation [gordonr 9333]

* Fri Jun 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-03]
- Fix backup panel text change. Made text non-specific about the location of
  the smbpasswd file. [charlieb 9220]

* Fri Jun 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-02]
- Account for the path change of smbpasswd file in desktop restore/verify.
  [charlieb 9220]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Changing version to stable stream number - 1.12.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-04]
- Spanish nav bar [gordonr 9153]

* Fri Jun 13 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-03]
- Corrected logic for switching /etc{/samba,}/smbpasswd [gordonr 8747]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-02]
- Remove some remnants of templated /sbin/e-smith/backup.
- Use Backup program parameter in /sbin/e-smith/do_backup.
  [charlieb 7853]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-01]
- Roll new development stream to 1.11.1

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-56]
- And symlink /etc/smbpasswd to avoid confusion [gordonr 8809]
- Move guard so we skip if /etc/smbpasswd is not a file [gordonr 8809]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-55]
- Migrate /etc/smbpasswd to /etc/samba/smbpasswd after restore [gordonr 8809]

* Wed May 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-54]
- Fix return check for ->group and ->passwd [gordonr 8766]
- Fix tests for BackupHistoryDB.pm [gordonr 5908, in passing]

* Tue May 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-53]
- Extract the tests at build time [gordonr 8766]

* Tue May 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-52]
- Completed merge_group and tests, including admin, www, shared [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-51]
- Added test files and skeleton for merge_group [gordonr 8766]
- TODO: Complete merge_group and tests [gordonr 8766]
- TODO: Handle admin, www, shared groups [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-50]
- Further work, and tests, for merge_passwd [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-49]
- Code cleanups [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-48]
- Constructors are nice to have in objects :-( [gordonr 8766]
- Link merge-system-files into post-upgrade [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-47]
- Added esmith::Backup::{save,merge}_system_files [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-46]
- Modified backup panel to use esmith::Backup library [gordonr 8766]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-45]
- Added esmith::Backup library to centralise list of files/directories to
  restore [gordonr 8766]
- Save away important system files in pre-restore [gordonr 8766]

* Tue May  6 2003 Mark Knox <markk@e-smith.com>
- [1.11.0-44]
- Pass the right type of object to genResult [markk 8498]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-43]
- Add Spanish translation for backup [lijied 3793]

* Tue Apr 29 2003 Trevor Poole <trevorp@e-smith.com>
- [1.11.0-42]
- add the BackupType to the record for the desktop case. [trevor 5908]

* Mon Apr 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-41]
- Fix calls to create new backup records. [charlieb 5908]

* Mon Apr 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-40]
- Record each backup attempt separately in a backup history db. [charlieb 5908]

* Wed Apr 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-39]
- Record success or otherwise of backup to desktop attempts in config db.
  [charlieb 5908]
- Gracefully handle SIGPIPE in backup to desktop. [charlieb 8490]

* Wed Apr 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-38]
- Fix typo in rewind-tape fix. [charlieb 8475]

* Wed Apr 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-37]
- Call signal-event {pre,post}-backup with extra "desktop" parameter
  from desktop backup code, and use that parameter to skip tape rewinding.
  [charlieb 7853]
- Fix device lookup code in rewind-tape action. [charlieb 8475]

* Wed Apr 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-36]
- Fix a few semantic problems with reset--restore-idle-flag script.
  [charlieb 8466]

* Wed Apr 16 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-35]
- Replaced bad call to processTemplate. [msoulier 7600]

* Wed Apr  9 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-34]
- Remove deprecated /sbin/e-smith/backup in %post script.
  [charlieb 7853]

* Tue Apr  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-33]
- Fix typo in rewind-tape action. [charlieb 5908]
- Change Copyright => License in header.

* Fri Apr  4 2003 Mark Knox <markk@e-smith.com>
- [1.11.0-32]
- Removed redundant refs to bootstrap-console from panel [markk 6164]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-31]
- Change table to start_table where applicable [tonyc 8034]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-30]
- Removed "Mitel Network SME server' branding [lijied 8016]
- Fix layout/css in backup panel [tonyc 7950]

* Mon Mar 31 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-29]
- Re-write do_backup in perl.  [charlieb 5908]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-28]
- Modified directory po/fr_CA to fr  [lijied 6787] 

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-27]
- Modified gettext() extraction based on changes in 1.11.0-25 [gordonr 5908]

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-26]
- Call genFooter/genResult with an FM object (subclass of CGI) so
  footers get localised [gordonr 3553]

* Thu Mar 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-25]
- Remove templated /sbin/e-smith/backup and add non-templated
  do_backup script. Alter cron template to suit. Move tape
  rewind into pre-backup and post-backup actions. Log
  start, finish and result properties from backup script.
  [charlieb 5908]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-24]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Tue Mar 25 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-23]
- Add link to fr-ca PAGE_REFRESH_IN translation [tonyc 6491]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-22]
- Deleted ./sbin/e-smith/backup/template-begin, and modified
  %build [lijied 3295]

* Fri Mar 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-21]
- Changed the post restore code such that the backup panel is blocked until
  the server reboots. [msoulier 6471]

* Mon Mar 10 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-20]
- Modified charset tag in .po file [lijied 3930]

* Fri Mar  7 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-19]
- Modified e-smith-devtools again [lijied 7578]

* Fri Mar  7 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-18]
- Modified e-smith-devtools version [lijied 7578]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-17]
- Added the generate lexicon code [lijied 7442]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-16]
- Added the .po file to po/fr_CA again [lijied 7442]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-15]
- Cleaned up .po->.mo build [lijied 7442]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-14]
- Added .po->.mo instructions to %build [lijied 7442]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-13]
- Modified backup panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-12]
- Remodify the lexicon file  [lijied 4030]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-11]
- Split en-us lexicon from backup panel [lijied 4030]

* Fri Feb 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-10]
- Rebuild RPM - commit missed last time [lijied 5003]

* Fri Feb 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-09]
- Added French lexicon for backup [lijied 5003]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-08]
- Rewrote template to use esmith::I18N [gordonr 5212]

* Fri Dec 13 2002 Mark Knox <markk@e-smith.com>
- [1.11.0-07]
- Added "click here" text on tape restore page [markk 6094]

* Thu Dec 12 2002 Mark Knox <markk@e-smith.com>
- [1.11.0-06]
- Removed redundant success message after restore [markk 6094]

* Thu Dec 12 2002 Mark Knox <markk@e-smith.com>
- [1.11.0-05]
- Added refresh and status messages to tape restore process [markk 6094]

* Tue Dec  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Tidy up and update /sbin/e-smith/backup templates, preparatory to adding
  support for non-tape devices. [charlieb 5521]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-03]
- ui update  [miked 5494]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-02]
- update to new UI system [miked 5494]

* Wed Nov  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Rolling development stream version to 1.11.0

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.1-01]
- New checkout to force head revisions to 1.10.1

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Roll to maintained version number to 1.10.0

* Fri Oct 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-09]
- Added missing closing paren - code police needed earlier [gordonr 5168]

* Fri Oct 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- Renamed duplicate lexicon tag RESTORE_IN_PROGRESS{,_BEGAN_AT}
  RESTORE_IN_PROGRES_DESC -> MUST_REBOOT_AFTER_RESTORE in tape restore
  [gordonr 5168]

* Wed Oct  9 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-07]
- Fixed double call of pre-restore [miked 5158]

* Wed Oct  9 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-06]
- Fixed references to ext2 filesystem in CalculateSizes; cahnged them to ext3

* Wed Sep 25 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Add calls to signal-event pre-restore before tape or desktop restore
  (currently to stop slapd and remove LDIF dump file).  [charlieb 2745]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Fix XML errors in backup panel.  [charlieb 2745]

* Fri Sep 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Complete previous change - the web panel needed to be updated as well.
  [charlieb 2745]

* Thu Aug 29 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Change mysql-dump-tables and mysql-delete-dumps events to pre-backup and
  post-backup events. [charlieb 2745]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to development stream number to 1.9.0

* Fri May 31 2002 Tony Clayton <apc@e-smith.com>
- [1.8.2-01]
- Reverting previous change - "it's a feature" [tonyc 3746]

* Fri May 31 2002 Tony Clayton <apc@e-smith.com>
- [1.8.1-01]
- Prevent tape/destop restores from dieing in state=running [tonyc 3746]

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to maintained stream number to 1.8.0

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [1.7.20-01]
- Fixed some funny table cells that were causing trouble in Netscape 
  [markk 3764]

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.19-01]
- Removed unused config db tie in restore-idle-flag.
- Add initialisation of backup service entry in config db.
  This will allow restore from tape to work out of the box.
  [charlieb 1254, 3746]

* Wed May 29 2002 Tony Clayton <apc@e-smith.com>
- [1.7.18-01]
- Fix bad string concats in /sbin/e-smith/backup fragments [tonyc 3180]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.17-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.16-01]
- testing co2rpm --force

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.15-01]
- testing co2rpm --force

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.14-01]
- testing co2rpm --force

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.13-01]
- testing co2rpm --force

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.12-01]
- Changed quoting in /etc/crond.d/backup template [gordonr 3029]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.11-01]
- "Verify complete" -> "Verification is complete" [gordonr 3544]

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [1.7.10-01]
- Allow form uploads and large files to be posted. [markk 3159]

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [1.7.9-01]
- Localised a few more strings in sbin/e-smith/backup templates [markk 3029]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.8-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Tue Apr 16 2002 Mark Knox <markk@e-smith.com>
- [1.7.7-01]
- I18n backup cronjob using gettext. Also converted to ConfigDB. [markk 3029]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.7-01]
- Language en->en-us

* Fri Apr 12 2002 Mark Knox <markk@e-smith.com>
- [1.7.6-01]
- Internationalized using FormMagick lexicon [markk 3159]
- Converted to esmith::ConfigDB API [markk 3159]

* Fri Mar 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.5-01]
- Include "du -s " of all backed up files and directories other than
  /home/e-smith in desktop backup estimate.

* Thu Mar 14 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-01]
- Fix error in use of AccountsDB interface (#2139).

* Thu Mar 07 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-01]
- Include /root in desktop backup and in size estimate (#2322).
- Change text to indicate that desktop backup file will be somewhat
  smaller if files are compressible.

* Thu Mar 07 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Use Quota module to estimate desktop backup size, by summing over all
  user accounts (#2139).

* Wed Feb 27 2002 Jason Miller <jmiller@e-smith.com>
- [1.7.1-01]
- Rolled to version 1.7.1-01 to verify CVS contents from 1.7.0-01.
  Includes all patchesup to 1.7.0-01.

* Wed Feb 27 2002 Jason Miller <jay@e-smith.com>
- [1.7.0-01]
- rollRPM: Rolled version number to 1.7.0-01. Includes patches up to 1.6.0-01.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-04.

* Thu Dec  6 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-04]
- Adding text to restore screen that warns that your restore
  is not complete until you see the words Restore complete and
  /etc/smbpasswd is restored.

* Wed Nov 28 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-03]
- Report restore/verify problems if they are detected. Do not do any
  post processing unless the restore completes successfully.

* Tue Nov 13 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-02]
- adding last patch to prep section.  feels like monday.

* Tue Nov 13 2001 Tony Clayton <tonyc@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-06.
- use esmith::lockfile for lockfile stuff
- add dependency on e-smith-lib >= 1.7.0-20 for esmith::lockfile

* Tue Nov 13 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-06]
- backing out lockfile patch - moving to new stream

* Mon Nov 12 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-05]
- use esmith::lockfile for lockfile stuff
- add dependency on e-smith-lib >= 1.7.0-20 for esmith::lockfile

* Wed Nov 07 2001 Tony Clayton <tonyc@e-smith.com>
- [1.4.0-04]
- rebranding to Mitel Networks

* Fri Aug 17 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Changed default network backup filename to "smeserver.tgz"
- Note: We can still restore the old format "esmithsg.bak" files

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-10.

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-10]
- More branding changes

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-09]
- More branding changes

* Tue Jul 31 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-08]
- Branding/marketing text changes email/e-mail 

* Sun Jul 29 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-07]
- Branding text changes to the backup web panel

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.3.0-06]
- Changed license to GPL

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-05]
- Default to .tgz for desktop backup/restore/verify
- Allow uuencoded tar (esmithsg.bak) for restore/verify backwards compatability

* Thu Jun 07 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-04]
- Add --verbose to tar --extract so web panels shows restored files

* Thu Jun 07 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-03]
- Add option to verify desktop backup file contents.

* Thu Jun 07 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Avoid use of redundant temporary file, CGI.pm already creates one for us,
  and provides us with a file handle.

* Wed Apr 11 2001 Adrian Chung <mac@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-11.

* Wed Feb 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-11]
- Add tape rewind action to tape restore

* Wed Feb 21 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-10]
- Now rewinds tape before zeroing tape.
- Writes 32k of zeroes instead of 10k.

* Thu Feb 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-09]
- Add conf-backup to bootstrap-console-save.
- Don't need templates-user-custom directory now, it's in e-smith-base RPM.

* Mon Feb 12 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-08]
- Duping STDOUT fails for netscape. Now just redirecting STDOUT to STDERR.

* Mon Feb 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-07]
- rolling release number for GPG signing.

* Sun Feb 11 2001 Charlie Brady
- [1.2.0-06]
- Include etc/e-smith/templates-user-custom in backup

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Thu Feb 8 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-04]
- Zero pad minutes for backup and reminder times.
- Fix nasty problem stopping flexbackup running in the background.
  Needed to dup STDOUT, close STDOUT, and reset STDOUT to duped fd.

* Tue Jan 30 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-03]
- Changed size calculations so that minimum size displayed is 1Mb.
- Changed wording of size of snapshot.
- Notify user how much free space exists in /tmp.
- Remove uploaded file after restore.

* Mon Jan 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Preserve gid of www across restore.
- Add comment about upbuffering output

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-17.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-17]
- Added html output to reboot function of manager panel

* Wed Jan 24 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-16]
- /sbin/e-smith/backup zeroes tape before starting. This is a hack to
  work around talking to ide tapes via ide-scsi.

* Wed Jan 17 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-15]
- mysql tables are deleted before and after backups and restores

* Tue Jan 16 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-14]
- cron job now runs every day

* Mon Jan 15 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-13]
- removed unnecessary /sbin/e-smith/tape-restore template
- fixed html formatting problem in backup panel
- fixed backgrounding problem in backup panel - need to close STDOUT in child
- format fixes in backup panel

* Mon Jan 15 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-12]
- Changes to the menu item ordering for the e-smith manager

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-11]
- Changed fork and signal handling again - doesn't seem to make much
  difference. Could be the lock file interaction - needs testing.

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-10]
- Fixed order of files to be restored
- Moved signal handling but it makes no difference, still can't background

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-09]
- /sbin/e-smith/backup now dumps mysql tables to /home/e-smith prior
  to running the tape backup

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-08]
- fixed uninitialised variables
- reboot action calls backgroundCommand instead of showing new panel

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-07]
- fixed syntax error in /etc/e-smith/events/actions/conf-backup

* Fri Jan 12 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-06]
- flexbackup is merely the default backup program
- cron job calls /sbin/e-smith/backup which is a templated file
- restore-tape action now given to flexbackup as it is flexbackup specific

* Fri Jan 12 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-05]
- Removed checks for uptime. The state in /etc/e-smith/restore is not
  changed, regardless of reboots. It is changed by bootstrap-console.
- Lots of text changes for consistency and to reinforce the need to
  reboot after a restore
- Mail is sent to the admin user after a tape restore indicating
  success or failure.
- mysql tables are dumped to /home/e-smith prior to network backup.
- Calculation of tarsize handles negative values sensibly.

* Fri Jan 12 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-04]
- No longer checks for current state of EthernetDrive1 and LocalIP.
- Does not do a forced reboot under any circumstances.
- Calls post-upgrade after the restore instead of post-restore.

* Thu Jan 11 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-03]
- Major changes to panel. Now does tape restore in background. Lots of
  checks and balances to avoid concurrent restores/backups etc.

* Wed Jan 10 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-02]
- Minor change to the copyright for consistency

* Tue Jan 9 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-01]
- Rolled version to 1.1.0-01. Includes patches upto 0.1-4

* Mon Jan 8 2001 Peter Samuel <peters@e-smith.com>
- [0.1-4]
- Now restores config from tape

* Sun Jan 7 2001 Jason Miller <jmiller@e-smith.com>
- [0.1-2] through [0.1-3]
- completed the update section for configuration database
  of flexbackup
- prepared the restore-tape option for the call to the
  proper event for restoring from tape

* Sun Jan 7 2001 Jason Miller <jmiller@e-smith.com>
- initial release

%description
e-smith server central backup administration panel

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
/sbin/e-smith/buildtests 10e-smith-backup

mkdir -p root/etc/e-smith/events/{pre-,post-}backup
perl createlinks

# Extract a new copy of the English .po, though we won't use it for this build
xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/backup.po  \
	root/etc/e-smith/templates/etc/crontab/backup \
	root/sbin/e-smith/do_backup

/sbin/e-smith/generate-lexicons

mkdir -p root/var/cache/e-smith/restore
mkdir -p root/var/cache/e-smith/restore/etc
mkdir -p root/var/cache/e-smith/restore/etc/samba
mkdir -p root/etc/e-smith/db/backups
mkdir -p root/etc/dar
mkdir -p root/mnt/smb

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc Copying" >> %{name}-%{version}-%{release}-filelist
echo "%doc Artistic" >> %{name}-%{version}-%{release}-filelist
echo "%doc LICENSE" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
