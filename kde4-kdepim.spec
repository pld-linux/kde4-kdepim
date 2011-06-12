%define		_state	stable
%define		qtver	4.7.2
%define		orgname	kdepim
Summary:	Personal Information Management (PIM) for KDE
Summary(ko.UTF-8):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl.UTF-8):	Zarządca informacji osobistej (PIM) dla KDE
Summary(ru.UTF-8):	Персональный планировщик (PIM) для KDE
Summary(uk.UTF-8):	Персональный планувальник (PIM) для KDE
Name:		kde4-kdepim
Version:	4.6.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdepim-%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	72396ca638233f52fcc69cac74fcc06d
Patch100:	%{name}-branch.diff
# http://mirrors.ludost.net/gentoo/distfiles/kleopatra-4.4.3-assuan2.patch.bz2
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	akonadi-devel >= 1.1.2
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cyrus-sasl-devel
BuildRequires:	dblatex
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gpgme-devel >= 1:1.2.0
BuildRequires:	grantlee-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libassuan-devel
BuildRequires:	libindicate-qt-devel >= 0.2.2
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel >= 2.3.0
BuildRequires:	strigi-devel >= 0.6.5
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-runtime >= %{version}
Obsoletes:	%{name}-kpilot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%description -l ru.UTF-8
kdepim - это набор утилит для управления персональной информацией для
K Desktop Environment (KDE).

%description -l uk.UTF-8
kdepim - це набір утиліт для керування персональною информацією для K
Desktop Environment (KDE).

%package kontact
Summary:	Kontact Personal Information Management
Summary(pl.UTF-8):	Kontact Personal Information Management
Group:		X11/Applications
Requires:	pinentry-qt4
Provides:	kde4-kontact
Obsoletes:	kde4-kontact

%description kontact
Kontact Personal Information Management.

%description kontact -l pl.UTF-8
Kontact Personal Information Management.

%package knode
Summary:	KDE News Reader
Summary(pl.UTF-8):	Czytnik newsów dla KDE
Summary(pt_BR.UTF-8):	Leitor de notícias (news) do KDE
Group:		X11/Applications
# ?Requires:	kde4-kdebase >= %{version}
Requires:	%{name}-libs = %{version}-%{release}

%description knode
KNode is an online newsreader (GKNSA compliant) for the K Desktop
Environment. It features:
- all basic features of a newsreader (read articles, post articles,
  threading ...)
- support for multiple newsservers
- reading and composing of MIME multipart messages
- inline display of attachments (text and images)
- support for sending mail via smtp
- customizable filters, fonts, colors
- full scoring
- and more...

%description knode -l pl.UTF-8
KNode to czytnik newsów zgodny ze specyfikacją GKNSA przeznaczony dla
środowiska KDE. Jego możliwości obejmują:
- wszystkie podstawowe cechy czytnika newsów (czytanie i wysyłanie
  artykułów, wątkowanie...)
- obsługę wielu serwerów news
- czytanie i tworzenie wieloczęściowych wiadomości MIME
- wyświetlanie załączników w tekście (tekstowych i obrazków)
- konfigurowalne filtry, fonty i kolory
- pełny scoring
- wiele więcej...

%description knode -l pt_BR.UTF-8
Leitor de notícias (news) do KDE.


%package kontact-plugin-knode
Summary:	Knode plugin for Kontact
Summary(pl.UTF-8):	plugin Knode dla Kontact
Group:		X11/Applications
Requires:	%{name}-knode = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}

%description kontact-plugin-knode
Knode plugin for Kontact.

%description kontact-plugin-knode -l pl.UTF-8
Plugin Knode dla Kontact.

%package ktimetracker
Summary:	Personal timetracker
Summary(pl.UTF-8):	Osobisty czasomierz
Group:		X11/Applications

%description ktimetracker
KTimeTracker - tracks time spent on various tasks. It is useful for
tracking hours to be billed to different clients.

%description ktimetracker -l pl.UTF-8
KTimeTracker śledzi czas spędzony na różnych zajęciach. Jest przydatny
przy obliczaniu godzin do wystawiania rachunków wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl.UTF-8):	Program pocztowy KDE
Summary(pt_BR.UTF-8):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications/Mail
URL:		http://kontact.kde.org/kmail/
# ? Requires:	kde4-kdebase >= %{version}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pinentry-qt4

%description kmail
This is electronic mail client for KDE with a huge amount of features:
- SMTP/maildir/POP3/IMAP support with SSL/TLS and pipelining
- address book
- automatic encryption using OpenPGP (PGP or GnuPG)
- powerful mail filters
- mailinglist aware nested mail folders
- on-demand downloading or deleting without downloading of big mails
  on a POP3 server
- full support for mails in all languages and charsets supported by Qt
- message search result presentation in virtual folders
- duplicate mail removal
- threading of messages
- spell checking as you type
- import of mail from other clients
- and more...

%description kmail -l pl.UTF-8
Program pocztowy dla KDE o olbrzymich możliwościach, obejmujących:
- obsługę SMTP/maildir/POP3/IMAP z SSL/TLS i pipeliningiem
- książkę adresową
- automatyczne szyfrowanie przy użyciu OpenPGP (PGP lub GnuPG)
- potężne filtry pocztowe
- zagnieżdżone skrzynki pocztowe z obsługą list pocztowych
- ściąganie na żądanie lub usuwanie bez ściągania dużych listów z
  serwera POP3
- pełną obsługę listów we wszystkich językach i zestawach znaków
  obsługiwanych przez Qt
- przeszukiwanie wiadomości z prezentacją w wirtualnych folderach
- usuwanie powtórzonych listów
- wątkowanie wiadomości
- kontrolę pisowni w locie
- import poczty z innych klientów
- wiele więcej...

%description kmail -l pt_BR.UTF-8
Poderoso cliente / leitor de e-mails para o KDE.

%package kontact-plugin-kmail
Summary:	Kmail plugin for Kontact
Summary(pl.UTF-8):	plugin Kmail dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kmail = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kmail
Obsoletes:	kde4-kontact-plugin-kmail

%description kontact-plugin-kmail
Kmail plugin for Kontact.

%description kontact-plugin-kmail -l pl.UTF-8
Plugin Kmail dla Kontakt.

%package kontact-plugin-ktimetracker
Summary:	Ktimer plugin for Kontact
Summary(pl.UTF-8):	plugin Ktimer dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Requires:	%{name}-ktimetracker = %{version}-%{release}
Provides:	kde4-kontact-plugin-ktimetracker
Obsoletes:	kde4-kontact-plugin-ktimetracker

%description kontact-plugin-ktimetracker
Ktimer plugin for Kontact.

%description kontact-plugin-ktimetracker -l pl.UTF-8
Plugin Ktimer dla Kontakt.


%package kaddressbook
Summary:	Address book
Summary(pl.UTF-8):	Książka adresowa
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdelibs >= %{version}

%description kaddressbook
The KDE address book.

%description kaddressbook -l pl.UTF-8
Książka adresowa dla KDE.

%package kontact-plugin-kaddressbook
Summary:	Kaddressbook plugin for Kontact
Summary(pl.UTF-8):	plugin Kaddressbook dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kaddressbook = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kaddressbook
Obsoletes:	kde4-kontact-plugin-kaddressbook

%description kontact-plugin-kaddressbook
Kaddressbook plugin for Kontact.

%description kontact-plugin-kaddressbook -l pl.UTF-8
Plugin Kaddressbook dla Kontakt.

%package kontact-plugin-planner
Summary:	Planner plugin for Kontact
Summary(pl.UTF-8):	plugin Planner dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-planner

%description kontact-plugin-planner
Planner plugin for Kontact.

%description kontact-plugin-planner -l pl.UTF-8
Plugin Planner dla Kontakt.

%package korganizer
Summary:	Calendar and scheduling component of Kontact
Summary(pl.UTF-8):	korganizer
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdelibs >= %{version}

%description korganizer
KOrganizer is the calendar and scheduling component of Kontact, the
integrated personal information manager of KDE.

KOrganizer provides management of events and tasks, alarm
notification, web export, network transparent handling of data, group
scheduling, import and export of calendar files and more. It is able
to work together with a wide variety of groupware servers, for example
Kolab, Open-Xchange, Citadel or OpenGroupware.org.

KOrganizer is fully customizable to your needs and is an integral part
of the KDE PIM suite, which aims to be a complete solution for
organizing your personal data. KOrganizer supports the two dominant
standards for storing and exchanging calendar data, vCalendar and
iCalendar.

%description korganizer -l pl.UTF-8
Korganizer.

%package kontact-plugin-korganizer
Summary:	Korganizer plugin for Kontact
Summary(pl.UTF-8):	plugin korganizer dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Requires:	%{name}-korganizer = %{version}-%{release}
Provides:	kde4-kontact-plugin-korganizer
Obsoletes:	kde4-kontact-plugin-korganizer

%description kontact-plugin-korganizer
Korganizer plugin for Kontact.

%description kontact-plugin-korganizer -l pl.UTF-8
Plugin korganizer dla Kontakt.

%package kmobiletools
Summary:	Make your mobile phone communicate with your PC
Summary(pl.UTF-8):	Narzędzie do komunikacji między telefonem komórkowym a PC
Group:		X11/Applications

%description kmobiletools
Make your mobile phone communicate with your PC.

%description kmobiletools -l pl.UTF-8
Narzędzie do komunikacji między telefonem komórkowym a PC.

%package kontact-plugin-kmobiletools
Summary:	Kmobiletools plugin for Kontact
Summary(pl.UTF-8):	plugin kmobiletools dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kmobiletools = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kmobiletools
Obsoletes:	kde4-kontact-plugin-kmobiletools

%description kontact-plugin-kmobiletools
Kmobiletools plugin for Kontact.

%description kontact-plugin-kmobiletools -l pl.UTF-8
Plugin kmobiletools dla Kontakt.

%package kontact-plugin-summary
Summary:	Summary plugin for Kontact
Summary(pl.UTF-8):	plugin Summary dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-summary
Obsoletes:	kde4-kontact-plugin-summary

%description kontact-plugin-summary
Summary plugin for Kontact.

%description kontact-plugin-summary -l pl.UTF-8
Plugin Summary dla Kontakt.

%package kontact-plugin-specialdates
Summary:	Specialdates plugin for Kontact
Summary(pl.UTF-8):	plugin Specialdates dla Kontakt.
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-specialdates
Obsoletes:	kde4-kontact-plugin-specialdates

%description kontact-plugin-specialdates
Specialdates plugin for Kontact.

%description kontact-plugin-specialdates -l pl.UTF-8
Plugin Specialdates dla Kontakt.

%package kontact-plugin-newsticker
Summary:	Newsticker plugin for Kontact
Summary(pl.UTF-8):	plugin Newsticker dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-newsticker
Obsoletes:	kde4-kontact-plugin-newsticker

%description kontact-plugin-newsticker
Newsticker plugin for Kontact.

%description kontact-plugin-newsticker -l pl.UTF-8
Plugin Newsticker dla Kontakt.

%package akregator
Summary:	News feed reader for the KDE desktop
Summary(pl.UTF-8):	Czytnik newsów dla KDE
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}

%description akregator
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%description akregator -l pl.UTF-8
Czytnik newsów dla KDE.

%package kontact-plugin-akregator
Summary:	Akregator plugin for Kontact
Summary(pl.UTF-8):	plugin Akregator dla Kontakt
Group:		X11/Applications
Requires:	%{name}-akregator = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-akregator
Obsoletes:	kde4-kontact-plugin-akregator

%description kontact-plugin-akregator
Akregator plugin for Kontact.

%description kontact-plugin-akregator -l pl.UTF-8
Plugin Akregator dla Kontakt.

%package kontact-plugin-weather
Summary:	Weather plugin for Kontact
Summary(pl.UTF-8):	plugin Weather dla Kontakt
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-weather
Obsoletes:	kde4-kontact-plugin-weather

%description kontact-plugin-weather
Weather plugin for Kontact.

%description kontact-plugin-weather -l pl.UTF-8
Plugin Weather dla Kontakt.

%package knotes
Summary:	Yellow cards
Summary(pl.UTF-8):	Żółte karteczki
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl.UTF-8
KNotes pozwala umieszczać na pulpicie notatki z opcją wysyłania.
Dodatkowo, aby móc służyć za przypominajkę, KNotes może wysyłać pocztę
i drukować notatki, a także przyjmować przeciąganie nawet ze zdalnych
komputerów.

%package kontact-plugin-knotes
Summary:	Knotes plugin for Kontact
Summary(pl.UTF-8):	plugin Knotes dla Kontakt
Group:		X11/Applications
Requires:	%{name}-knotes = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-knotes
Obsoletes:	kde4-kontact-plugin-knotes

%description kontact-plugin-knotes
Knotes plugin for Kontact.

%description kontact-plugin-knotes -l pl.UTF-8
Plugin Knotes dla Kontakt.

%package devel
Summary:	Development files for KDE pim
Summary(pl.UTF-8):	Pliki nagłówkowe do KDE pim
Summary(ru.UTF-8):	Файлы разработки для kdepim
Summary(uk.UTF-8):	Файли розробки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name}-kleopatra = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
bazujących na kdepim.

%description devel -l uk.UTF-8
Цей пакет містить файли заголовків необхідні для побудови програм,
базованих на kdepim.

%description devel -l ru.UTF-8
Этот пакет содержит файлы заголовков необходимые для построения
программ, основанных на kdepim.

%package kio-groupwise
Summary:	Groupwise protocol service
Summary(pl.UTF-8):	Obsługa protokołu Groupwise
Group:		X11/Libraries
Obsoletes:	kde4-kio-groupwise

%description kio-groupwise
Groupwise protocol service.

%description kio-groupwise -l pl.UTF-8
Obsługa protokołu Groupwise.

%package kio-imap4
Summary:	IMAP4 protocol service
Summary(pl.UTF-8):	Obsługa protokołu IMAP4
Group:		X11/Libraries
Obsoletes:	kde4-kio-imap4
# for PLAIN authentication
Suggests:	cyrus-sasl-plain

%description kio-imap4
IMAP4 protocol service.

%description kio-imap4 -l pl.UTF-8
Obsługa protokołu IMAP4.

%package kalarm
Summary:	A personal alarm scheduler
Summary(pl.UTF-8):	Osobisty program do przypominania
Group:		X11/Libraries
Obsoletes:	kalarm

%description kalarm
KAlarm is a personal alarm message, command and email scheduler. It
lets you set up personal alarm messages which pop up on the screen at
the chosen time, or you can schedule commands to be executed or emails
to be sent. Also includes an alarm daemon.

%description kalarm -l pl.UTF-8
KAlarm to osobisty program do planowania i przypominania poprzez
uruchomienie polecenia lub pocztą elektroniczną. Umożliwia ustawienie
własnej wiadomości alarmowej, która wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie poleceń do wykonania lub poczty do
wysłania. Zawiera także demona obsługującego przypominanie.

%package konsolekalendar
Summary:	A command line ICard tool
Summary(pl.UTF-8):	Narzędzie dostępu do plików kalendarza z linii poleceń
Group:		Applications
Requires:	%{name}-libs = %{version}-%{release}

%description konsolekalendar
KonsoleKalendar is a command line interface to KDE calendars. It lets
you view, insert, remove, or modify calendar events by way of the
command line or from a scripting language. Additionally,
KonsoleKalendar can export a KDE calendar to a variety of other
formats.

Main features of KonsoleKalendar:
- list calendar entries from a start date/time to end date/time
- insert/remove/modify calendar entries
- export calendar entries to other file formats

%description konsolekalendar -l pl.UTF-8
KonsoleKalendar to działający z linii poleceń interfejs do kalendarzy
KDE. Pozwala oglądać, wstawiać, usuwać i modyfikować zdarzenia w
kalendarzu z linii poleceń lub języka skryptowego. Ponadto
KonsoleKalendar potrafi wyeksportować kalendarz KDE do wielu innych
formatów.

Główne możliwości programu KonsoleKalendar:
- wypisywanie wpisów kalendarza od daty początkowej do końcowej
- wstawianie/usuwanie/modyfikowanie wpisów
- eksportowanie wpisów kalendarza do innych formatów plików.

Narzędzie dostępu do plików kalendarza z linii poleceń.

%package korn
Summary:	KDE 'biff' application
Summary(pl.UTF-8):	Wskaźnik skrzynki pocztowej dla KDE
Summary(pt_BR.UTF-8):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl.UTF-8
Programik pokazujący liczbę wiadomości w wybranych folderach
pocztowych.

%description korn -l pt_BR.UTF-8
Miniaplicativo de monitoração da caixa de correio.

%package wizards
Summary:	wizards
Summary(pl.UTF-8):	wizards
Group:		X11/Applications

%description wizards
wizards.

%description wizards -l pl.UTF-8
wizards.

%package plugins
Summary:	plugins
Summary(pl.UTF-8):	plugins
Group:		X11/Applications

%description plugins
plugins.

%description plugins -l pl.UTF-8
plugins.

%package ktnef
Summary:	ktnef
Summary(pl.UTF-8):	ktnef
Group:		X11/Applications

%description ktnef
ktnef.

%description ktnef -l pl.UTF-8
ktnef.

%package kitchensync
Summary:	kitchensync
Summary(pl.UTF-8):	kitchensync
Group:		X11/Applications

%description kitchensync
kitchensync.

%description kitchensync -l pl.UTF-8
kitchensync.

%package kleopatra
Summary:	Kleopatra
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dirmngr

%description kleopatra
Kleopatra.

%package kjots
Summary:	KDE Note taker
Summary(pl.UTF-8):	Notatnik dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description kjots -l pl.UTF-8
KJots to mały program do zapisywania notatek.

%description kjots -l pt_BR.UTF-8
Ferramenta de armazenamento de livros.

%package blogilo
Summary:	A KDE blogging client
Summary(pl.UTF-8):	Program do blogowania dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description blogilo
A KDE blogging client.

%description blogilo -l pl.UTF-8
Program do blogowania dla KDE.

%package libs
Summary:	Shared kdepim libraries
Summary(pl.UTF-8):	Współdzielone biblioteki kdepim
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description libs
Libraries shared between PIM applications in KDE, which include:
libkdenetwork, libkdepim, libkmailprivate, libknodecommon,
libksieve, libmimelib and more

%description libs -l pl.UTF-8
Biblioteki współdzielone pomiędzy aplikacjami PIM w KDE, m.in.
libkdenetwork, libkdepim, libkmailprivate, libknodecommon,
libksieve, libmimelib.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0

%build
install -d build
cd build
%cmake \
	-DKONTACT_ENABLE_MIXEDMODE_SUMMARY_PLUGINS=on \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang akregator --with-kde
#%find_lang kaddressbook --with-kde
#%find_lang kalarm --with-kde
%find_lang kleopatra --with-kde
%find_lang kmail --with-kde
#%find_lang kmobiletools --with-kde
%find_lang knode --with-kde
%find_lang knotes --with-kde
#%find_lang konsolekalendar --with-kde
%find_lang kontact --with-kde
%find_lang korganizer --with-kde
#%find_lang korn --with-kde
%find_lang ktimetracker --with-kde
%find_lang kjots --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig
%post	kalarm	-p /sbin/ldconfig
%postun	kalarm	-p /sbin/ldconfig
%post	kleopatra	-p /sbin/ldconfig
%postun	kleopatra	-p /sbin/ldconfig
%post	korganizer	-p /sbin/ldconfig
%postun	korganizer	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# akonadi
%attr(755,root,root) %{_bindir}/akonadiconsole
%attr(755,root,root) %{_bindir}/akonadi_nepomuk_email_feeder
%attr(755,root,root) %{_bindir}/kincidenceeditor
%attr(755,root,root) %{_bindir}/tasks-mobile
#%attr(755,root,root) %ghost %{_libdir}/libakonadi-kcal_next.so.?
#%attr(755,root,root) %{_libdir}/libakonadi-kcal_next.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi_next.so.?
%attr(755,root,root) %{_libdir}/libakonadi_next.so.*.*.*
%dir %{_libdir}/akonadi
%dir %{_libdir}/akonadi/contact
%dir %{_libdir}/akonadi/contact/editorpageplugins
%attr(755,root,root) %{_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_desktopdir}/kde4/akonadiconsole.desktop
%{_datadir}/apps/akonadiconsole
#
%attr(755,root,root) %{_bindir}/kgpgconf
%attr(755,root,root) %{_bindir}/kwatchgnupg
%{_datadir}/apps/kwatchgnupg
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%{_datadir}/apps/kconf_update/kpgp.upd
### strigi
%attr(755,root,root) %{_libdir}/strigi/strigiea_ics.so
%attr(755,root,root) %{_libdir}/strigi/strigiea_vcf.so
### kresources/slox/
#%attr(755,root,root) %{_libdir}/libkslox.so
#%attr(755,root,root) %{_libdir}/libkabc_slox.so
#%attr(755,root,root) %{_libdir}/kde4/kabc_slox.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_slox.so
#%{_datadir}/kde4/services/kresources/kabc/kabc_slox.desktop
#%{_datadir}/kde4/services/kresources/kabc/kabc_ox.desktop
#%{_datadir}/kde4/services/kresources/kabc/kabc_groupwise.desktop
%dir %{_datadir}/kde4/services/kresources/knotes
### kresources/groupd1av
#%attr(755,root,root) %{_libdir}/libkcal_groupdav.so
#%attr(755,root,root) %{_libdir}/libkabc_groupdav.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_groupdav.so
#%attr(755,root,root) %{_libdir}/kde4/kabc_groupdav.so
#%{_datadir}/kde4/services/kresources/kabc/kabc_groupdav.desktop
#%{_datadir}/kde4/services/kresources/kcal/kcal_groupdav.desktop
#%{_datadir}/kde4/services/kresources/kcal/kcal_groupwise.desktop
#%{_datadir}/kde4/services/kresources/kcal/kcal_ox.desktop
#%{_datadir}/kde4/services/kresources/kcal/kcal_slox.desktop
### kresources/remote
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so
%attr(755,root,root) %{_libdir}/kde4/kcal_remote.so
%{_datadir}/kde4/services/kresources/kcal/remote.desktop
### kresources/kolab
#%attr(755,root,root) %{_libdir}/libkcalkolab.so
#%attr(755,root,root) %{_libdir}/libkabckolab.so
#%attr(755,root,root) %{_libdir}/libknoteskolab.so
#%attr(755,root,root) %{_libdir}/kde4/knotes_kolab.so
#%attr(755,root,root) %{_libdir}/kde4/kabc_kolab.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_kolab.so
#%{_datadir}/kde4/services/kresources/kcal/kolab.desktop
#%{_datadir}/kde4/services/kresources/kabc/kolab.desktop
#%{_datadir}/kde4/services/kresources/knotes/kolabresource.desktop
#%{_datadir}/apps/kconf_update/kolab-resource.upd
#%{_datadir}/apps/kconf_update/upgrade-resourcetype.pl
### kresources/lib
#%attr(755,root,root) %{_libdir}/libkgroupwarebase.so
#%attr(755,root,root) %{_libdir}/libkgroupwaredav.so
### kresources/birthdays
#%attr(755,root,root) %{_libdir}/kde4/kcal_kabc.so
#%{_datadir}/kde4/services/kresources/kcal/kabc.desktop
#%{_datadir}/kde4/services/kresources/kabc/kabc_opengroupware.desktop
#%{_datadir}/kde4/services/kresources/kcal/kcal_opengroupware.desktop
### kresources/blog
%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so
%attr(755,root,root) %{_libdir}/kde4/kcal_blog.so
%{_datadir}/kde4/services/kresources/kcal/blog.desktop

%files blogilo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blogilo
%{_desktopdir}/kde4/blogilo.desktop
%{_datadir}/apps/blogilo
%{_datadir}/config.kcfg/blogilo.kcfg
%{_iconsdir}/hicolor/*x*/apps/blogilo.png
%{_iconsdir}/hicolor/*x*/actions/format*.png
%{_iconsdir}/hicolor/*x*/actions/*-mark.png
%{_iconsdir}/hicolor/*x*/actions/*-link.png
%{_iconsdir}/hicolor/*x*/actions/*-media.png
%{_kdedocdir}/en/blogilo

%files kontact -f kontact.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%attr(755,root,root) %{_libdir}/kde4/kcm_kontact.so
%{_desktopdir}/kde4/Kontact.desktop
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/kde4/services/kontactconfig.desktop
%{_datadir}/apps/kontact
%{_desktopdir}/kde4/kontact-admin.desktop
%{_iconsdir}/*/*/*/kontact*.png
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%lang(en) %{_kdedocdir}/en/kontact-admin

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%attr(755,root,root) %{_libdir}/kde4/kcm_knode.so
%attr(755,root,root) %{_libdir}/kde4/knodepart.so
%{_desktopdir}/kde4/KNode.desktop
%{_datadir}/apps/knode
%{_datadir}/dbus-1/interfaces/org.kde.knode.xml
%{_datadir}/kde4/services/knewsservice.protocol
%{_datadir}/kde4/services/knode_*.desktop
%{_iconsdir}/*/*/apps/knode.png
#%{_iconsdir}/*/*/apps/knode2.png

%files kontact-plugin-knode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_knodeplugin.so
%dir %{_datadir}/kde4/services/kontact
%{_datadir}/kde4/services/kontact/knodeplugin.desktop

%files ktimetracker -f ktimetracker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%attr(755,root,root) %{_bindir}/ktimetracker
%attr(755,root,root) %{_libdir}/kde4/ktimetrackerpart.so
%attr(755,root,root) %{_libdir}/kde4/kcm_ktimetracker.so
%{_desktopdir}/kde4/ktimetracker.desktop
%{_datadir}/apps/ktimetracker
%{_datadir}/dbus-1/interfaces/org.kde.ktimetracker.ktimetracker.xml
%{_datadir}/kde4/services/ktimetrackerpart.desktop
%{_datadir}/kde4/services/ktimetracker_config_behavior.desktop
%{_datadir}/kde4/services/ktimetracker_config_display.desktop
%{_datadir}/kde4/services/ktimetracker_config_storage.desktop
%{_iconsdir}/*/*/apps/ktimetracker.png

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmail-mobile
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/ksendemail
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_libdir}/kde4/kcm_kmail.so
%attr(755,root,root) %{_libdir}/kde4/kmailpart.so
#%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_application_octetstream.so
#%{_desktopdir}/kde4/KMail.desktop
%{_desktopdir}/kde4/kmail_view.desktop
%{_datadir}/apps/kmail
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_datadir}/config.kcfg/kmail.kcfg
#%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/kde4/services/kmail_*.desktop
%{_datadir}/kde4/servicetypes/dbusmail.desktop
#%{_datadir}/kde4/servicetypes/dbusimap.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_datadir}/apps/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-transport.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-signature.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail-*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail-*.sh
%{_datadir}/apps/kmailcvt
%exclude %{_iconsdir}/*/scalable
%{_iconsdir}/*/*/apps/kmail*.png
%{_iconsdir}/oxygen/*/mimetypes/x-mail-distribution-list.*

#%{_iconsdir}/oxygen/*/actions/ldap_lookup.png
%{_iconsdir}/oxygen/*/actions/smallclock.png
%{_iconsdir}/oxygen/*/actions/upindicator.png
%{_iconsdir}/oxygen/*/actions/checkmark.png
# conflicts with kde-icons-oxygen
%{_iconsdir}/oxygen/*/actions/edit-delete-page.png

### libkleo
%attr(755,root,root) %{_libdir}/libkleo.so

%files kontact-plugin-kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kmailsummary.so
%{_datadir}/kde4/services/kontact/kmailplugin.desktop
%{_datadir}/kde4/services/kcmkmailsummary.desktop

%files kontact-plugin-ktimetracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_ktimetrackerplugin.so
%{_datadir}/kde4/services/kontact/ktimetracker_plugin.desktop

%files kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_bindir}/kaddressbook-mobile
#%attr(755,root,root) %{_libdir}/kde4/kaddrbk_*.so
%attr(755,root,root) %{_libdir}/kde4/kcm_ldap.so
%attr(755,root,root) %{_libdir}/kde4/kaddressbookpart.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kabconfig.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kabcustomfields.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kabldapconfig.so
#%attr(755,root,root) %{_libdir}/kde4/ldifvcardthumbnail.so
#%attr(755,root,root) %{_libdir}/libkabcommon.so
#%attr(755,root,root) %{_libdir}/libkabinterfaces.so
%{_desktopdir}/kde4/kaddressbook.desktop
%{_datadir}/apps/kaddressbook
#%{_datadir}/dbus-1/interfaces/org.kde.KAddressbook.Core.xml
#%{_datadir}/kde4/services/kabconfig.desktop
#%{_datadir}/kde4/services/kabcustomfields.desktop
#%{_datadir}/kde4/services/kabldapconfig.desktop
%{_datadir}/kde4/services/kcmldap.desktop
#%{_datadir}/kde4/services/kaddressbook
%{_datadir}/kde4/services/kaddressbookpart.desktop
#%{_datadir}/kde4/services/ldifvcardthumbnail.desktop
#%{_datadir}/kde4/servicetypes/dbusaddressbook.desktop
#%{_datadir}/kde4/servicetypes/kaddressbook_contacteditorwidget.desktop
#%{_datadir}/kde4/servicetypes/kaddressbook_extension.desktop
#%{_datadir}/kde4/servicetypes/kaddressbook_view.desktop
#%{_datadir}/kde4/servicetypes/kaddressbook_xxport.desktop
#%{_datadir}/kde4/servicetypes/kaddressbookimprotocol.desktop
%{_iconsdir}/*/*/apps/kaddressbook.*

%files kontact-plugin-kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_kaddressbookplugin.so
%{_datadir}/kde4/services/kontact/kaddressbookplugin.desktop

%files kontact-plugin-planner
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kontact_plannerplugin.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_planner.so
#%{_datadir}/kde4/services/kontact/plannerplugin.desktop
#%{_datadir}/kde4/services/kcmplanner.desktop

%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer
%attr(755,root,root) %{_bindir}/korganizer-mobile
%attr(755,root,root) %{_libdir}/kde4/kcm_korganizer.so
%attr(755,root,root) %{_libdir}/kde4/korg_*.so
%attr(755,root,root) %{_libdir}/kde4/korganizerpart.so
#%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_core.so.?
%attr(755,root,root) %{_libdir}/libkorganizer_core.so.4.*.*
#%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so
#%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config/korganizer.knsrc
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/kde4/services/korganizer_*.desktop
%{_datadir}/kde4/services/korganizer
%{_datadir}/kde4/services/webcal.protocol
%{_datadir}/kde4/servicetypes/calendardecoration.desktop
%{_datadir}/kde4/servicetypes/calendarplugin.desktop
%{_datadir}/kde4/servicetypes/dbuscalendar.desktop
%{_datadir}/kde4/servicetypes/korganizerpart.desktop
%{_datadir}/kde4/servicetypes/korgprintplugin.desktop
%{_desktopdir}/kde4/korganizer-import.desktop
%{_desktopdir}/kde4/korganizer.desktop
%{_iconsdir}/*/*/apps/korganizer.*

%files kontact-plugin-korganizer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_korganizerplugin.so
%attr(755,root,root) %{_libdir}/kde4/kontact_todoplugin.so
%attr(755,root,root) %{_libdir}/kde4/kontact_journalplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_apptsummary.so
%attr(755,root,root) %{_libdir}/kde4/kcm_todosummary.so
%{_datadir}/kde4/services/kontact/korganizerplugin.desktop
%{_datadir}/kde4/services/kontact/todoplugin.desktop
%{_datadir}/kde4/services/kontact/journalplugin.desktop
%{_datadir}/kde4/services/kcmapptsummary.desktop
%{_datadir}/kde4/services/kcmtodosummary.desktop

#%files kmobiletools -f kmobiletools.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmobiletools
#%attr(755,root,root) %{_libdir}/libkmobiletoolsengineui.so
#%attr(755,root,root) %{_libdir}/libkmobiletoolslib.so
#%attr(755,root,root) %{_libdir}/libkmtaddressbook_service.so
#%attr(755,root,root) %{_libdir}/kde4/kmobiletoolsmainpart.so
#%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_sms.so
#%attr(755,root,root) %{_libdir}/kde4/kmobiletools_fake.so
#%{_desktopdir}/kde4/kmobiletools.desktop
#%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_sms.desktop
#%{_datadir}/apps/kmobiletools
#%{_datadir}/config.kcfg/kmobiletools_devices.kcfg
#%{_datadir}/kde4/services/addressbook_service.desktop
#%{_datadir}/kde4/services/fake_engine.desktop
#%{_datadir}/kde4/services/kmobiletools_mainpart.desktop
#%{_datadir}/kde4/servicetypes/kmobiletoolscoreservice.desktop
#%{_datadir}/kde4/servicetypes/kmobiletoolsengine.desktop
#%{_datadir}/kde4/servicetypes/kmobiletoolsenginexp.desktop
#%{_iconsdir}/*/*/apps/kmobiletools.png
#%{_iconsdir}/*/*/actions/exportsms.png
#%{_iconsdir}/*/*/actions/newsms.png
#%{_iconsdir}/*/*/actions/phonecall.png
#%{_iconsdir}/*/*/actions/simcard.png
#%{_iconsdir}/*/*/actions/closedphone.png
#%{_iconsdir}/*/*/actions/*kmobiletoolsAT.png
#%{_iconsdir}/*/*/actions/*kmobiletoolsG.png
#%{_iconsdir}/*/*/actions/overlaydisc.png
#%{_iconsdir}/*/*/actions/smslist.png

#%files kontact-plugin-kmobiletools
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kontact_kmobiletoolsplugin.so
#%{_datadir}/kde4/services/kontact/kmobiletools.desktop

%files kontact-plugin-summary
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_summaryplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kontactsummary.so
%{_datadir}/kde4/services/kontact/summaryplugin.desktop
%{_datadir}/kde4/services/kcmkontactsummary.desktop
%dir %{_datadir}/apps/kontactsummary
%{_datadir}/apps/kontactsummary/kontactsummary_part.rc

%files kontact-plugin-specialdates
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_specialdatesplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_sdsummary.so
%{_datadir}/kde4/services/kontact/specialdatesplugin.desktop
%{_datadir}/kde4/services/kcmsdsummary.desktop

#%files kontact-plugin-newsticker
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kontact_newstickerplugin.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kontactknt.so
#%{_datadir}/kde4/services/kontact/newstickerplugin.desktop
#%{_datadir}/kde4/services/kcmkontactknt.desktop

%files akregator -f akregator.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/akregatorstorageexporter
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so
%attr(755,root,root) %{_libdir}/kde4/akregator_mk4storage_plugin.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_general.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_appearance.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_archive.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_browser.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_advanced.so
%attr(755,root,root) %{_libdir}/kde4/akregator_config_sharemicroblog.so
%attr(755,root,root) %{_libdir}/kde4/akregator_sharemicroblog_plugin.so
%attr(755,root,root) %{_libdir}/kde4/akregatorpart.so
%{_desktopdir}/kde4/akregator.desktop
%{_datadir}/apps/akregator
%{_datadir}/kde4/services/akregator_*.desktop
%{_datadir}/kde4/services/feed.protocol
%{_datadir}/kde4/servicetypes/akregator_plugin.desktop
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_datadir}/config.kcfg/akregator.kcfg
%{_iconsdir}/*/*/apps/akregator_empty.png
%{_iconsdir}/*/*/apps/akregator.*

%files kontact-plugin-akregator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_akregatorplugin.so
%{_datadir}/kde4/services/kontact/akregatorplugin.desktop

#%files kontact-plugin-weather
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kontact_weatherplugin.so
#%{_datadir}/kde4/services/kontact/weatherplugin.desktop

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%attr(755,root,root) %{_bindir}/notes-mobile
%attr(755,root,root) %{_libdir}/kde4/knotes_local.so
%attr(755,root,root) %{_libdir}/kde4/kcm_knote.so
%{_desktopdir}/kde4/knotes.desktop
%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knoteconfig.kcfg
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/kde4/services/kresources/knotes_manager.desktop
%{_datadir}/kde4/services/kresources/knotes/local.desktop
%{_datadir}/kde4/services/knote_config_action.desktop
%{_datadir}/kde4/services/knote_config_display.desktop
%{_datadir}/kde4/services/knote_config_editor.desktop
%{_datadir}/kde4/services/knote_config_network.desktop
%{_datadir}/kde4/services/knote_config_style.desktop
%{_iconsdir}/*/*/apps/knotes.png

%files kontact-plugin-knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_knotesplugin.so
%{_datadir}/apps/knotes/knotes_part.rc
%{_datadir}/kde4/services/kontact/knotesplugin.desktop

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%attr(755,root,root) %{_libdir}/kde4/kjotspart.so
%attr(755,root,root) %{_libdir}/kde4/kontact_kjotsplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kjots.so
%{_datadir}/kde4/services/kjotspart.desktop
%{_desktopdir}/kde4/Kjots.desktop
%{_datadir}/apps/kjots
%{_datadir}/config.kcfg/kjots.kcfg
%{_datadir}/kde4/services/kontact/kjots_plugin.desktop
%{_datadir}/kde4/services/kjots_config_misc.desktop
%{_iconsdir}/*/*/apps/kjots.png

%files devel
%defattr(644,root,root,755)
#%{_includedir}/kleo
#%{_includedir}/kpgp
#%{_includedir}/libkleopatraclient
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so
#%attr(755,root,root) %{_libdir}/libkalarm_resources.so
%attr(755,root,root) %{_libdir}/libkalarm_calendar.so
%attr(755,root,root) %{_libdir}/libgwsoap.so
#%attr(755,root,root) %{_libdir}/libkabc_groupdav.so
#%attr(755,root,root) %{_libdir}/libkabc_slox.so
#%attr(755,root,root) %{_libdir}/libkabcgroupwise.so
#%attr(755,root,root) %{_libdir}/libkabckolab.so
#%attr(755,root,root) %{_libdir}/libakonadi-kcal_next.so
%attr(755,root,root) %{_libdir}/libakonadi_next.so
#%attr(755,root,root) %{_libdir}/libkcalgroupwise.so
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so
#%attr(755,root,root) %{_libdir}/libkcal_slox.so
#%attr(755,root,root) %{_libdir}/libkcalkolab.so
%attr(755,root,root) %{_libdir}/libkdepim.so
#%attr(755,root,root) %{_libdir}/libkgroupwarebase.so
#%attr(755,root,root) %{_libdir}/libkgroupwaredav.so
#%attr(755,root,root) %{_libdir}/libknoteskolab.so
#%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so
#%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so
#%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so
%attr(755,root,root) %{_libdir}/libkpgp.so
%attr(755,root,root) %{_libdir}/libksieve.so
%attr(755,root,root) %{_libdir}/libmessagecore.so
%attr(755,root,root) %{_libdir}/libmessagelist.so
%attr(755,root,root) %{_libdir}/libmessageviewer.so
#%attr(755,root,root) %{_libdir}/libmimelib.so
#%attr(755,root,root) %{_libdir}/libkcal_groupdav.so
%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so
%attr(755,root,root) %{_libdir}/libkleopatraclientcore.so
%attr(755,root,root) %{_libdir}/libkleopatraclientgui.so
%attr(755,root,root) %{_libdir}/libknodecommon.so
%attr(755,root,root) %{_libdir}/libkorganizer_core.so
%{_datadir}/apps/libkleopatra

%files kio-groupwise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kio_groupwise.so
%attr(755,root,root) %{_libdir}/kde4/kabc_groupwise.so
%attr(755,root,root) %{_libdir}/kde4/kcal_groupwise.so
%{_datadir}/config.kcfg/groupwise.kcfg
%{_datadir}/kde4/services/groupwise.protocol
%{_datadir}/kde4/services/groupwises.protocol

%files kalarm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm
%attr(755,root,root) %{_bindir}/kalarmautostart
%attr(755,root,root) %{_libdir}/kde4/kalarm_*.so
%attr(755,root,root) %ghost %{_libdir}/libkalarm_calendar.so.?
%attr(755,root,root) %{_libdir}/libkalarm_calendar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkalarm_resources.so.?
%attr(755,root,root) %{_libdir}/libkalarm_resources.so.*.*.*
%{_desktopdir}/kde4/kalarm.desktop
%{_datadir}/apps/kalarm
%{_datadir}/autostart/kalarm.autostart.desktop
%attr(755,root,root) %{_datadir}/apps/kconf_update/kalarm-*.pl
%{_datadir}/apps/kconf_update/kalarm.upd
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.*.xml
%dir %{_datadir}/kde4/services/kresources/alarms
%{_datadir}/kde4/services/kresources/alarms/local.desktop
%{_datadir}/kde4/services/kresources/alarms/localdir.desktop
%{_datadir}/kde4/services/kresources/alarms/remote.desktop
%{_datadir}/kde4/services/kresources/kalarm_manager.desktop
%{_iconsdir}/*/*/apps/*kalarm.png
%{_kdedocdir}/en/kalarm

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%attr(755,root,root) %{_bindir}/kabcclient
%{_desktopdir}/kde4/konsolekalendar.desktop
%dir %{_datadir}/apps
#%dir %{_datadir}/apps/konsolekalendar
#%dir %{_datadir}/apps/konsolekalendar/pics
#%{_datadir}/apps/konsolekalendar/pics/*.png
%lang(en) %{_kdedocdir}/en/konsolekalendar
%lang(en) %{_kdedocdir}/en/kabcclient
%{_mandir}/man1/kabcclient.1.*

%files kleopatra -f kleopatra.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kleopatra
%attr(755,root,root) %{_libdir}/kde4/kcm_kleopatra.so
%attr(755,root,root) %ghost %{_libdir}/libkleopatraclientcore.so.?
%attr(755,root,root) %{_libdir}/libkleopatraclientcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkleopatraclientgui.so.?
%attr(755,root,root) %{_libdir}/libkleopatraclientgui.so.*.*.*
%{_datadir}/apps/libkleopatra
%{_datadir}/config/libkleopatrarc
%{_desktopdir}/kde4/kleopatra_import.desktop
%dir %{_datadir}/apps/kleopatra
%dir %{_datadir}/apps/kleopatra/pics
%{_datadir}/apps/kleopatra/kleopatra.rc
%{_datadir}/apps/kleopatra/pics/kleopatra_splashscreen.png
%{_datadir}/apps/kleopatra/pics/kleopatra_splashscreen.svgz
%{_datadir}/apps/kleopatra/pics/kleopatra_wizard.png
%{_datadir}/apps/kleopatra/pics/kleopatra_wizard.svgz
%{_datadir}/apps/kleopatra/pics/gpg4win-compact.png
%{_datadir}/apps/kleopatra/pics/gpg4win.png
%{_datadir}/kde4/services/kleopatra_config_appear.desktop
%{_datadir}/kde4/services/kleopatra_config_dirserv.desktop
#%{_datadir}/kde4/services/kleopatra_config_dnorder.desktop
%{_datadir}/kde4/services/kleopatra_config_gnupgsystem.desktop
%{_datadir}/kde4/services/kleopatra_config_smimevalidation.desktop
%{_datadir}/kde4/services/kleopatra_decryptverifyfiles.desktop
%{_datadir}/kde4/services/kleopatra_decryptverifyfolders.desktop
%{_datadir}/kde4/services/kleopatra_signencryptfiles.desktop
%{_datadir}/kde4/services/kleopatra_signencryptfolders.desktop
#%{_iconsdir}/oxygen/*/apps/kleopatra.png
%{_desktopdir}/kde4/kleopatra.desktop

%files wizards
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/groupwarewizard
#%attr(755,root,root) %{_bindir}/egroupwarewizard
%attr(755,root,root) %{_bindir}/groupwisewizard
#%attr(755,root,root) %{_bindir}/sloxwizard
#%attr(755,root,root) %{_bindir}/kolabwizard
#%attr(755,root,root) %{_bindir}/scalixwizard
#%{_desktopdir}/kde4/groupwarewizard.desktop
#%{_datadir}/config.kcfg/egroupware.kcfg
#%{_datadir}/config.kcfg/slox.kcfg
#%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/groupwise.kcfg
#%{_datadir}/config.kcfg/scalix.kcfg

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/ktexteditorkabcbridge.so
#%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_vcard.so
#%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_calendar.so
#%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_xdiff.so
#%{_datadir}/apps/kmail/plugins/bodypartformatter/text_vcard.desktop
#%{_datadir}/apps/kmail/plugins/bodypartformatter/text_calendar.desktop
#%{_datadir}/apps/kmail/plugins/bodypartformatter/text_xdiff.desktop

%files ktnef
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ktnefviewer
#%{_desktopdir}/kde4/ktnef.desktop
#%{_datadir}/apps/ktnef
#%{_iconsdir}/*/*/apps/ktnef.png

#%files kitchensync
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kitchensync
#%attr(755,root,root) %{_libdir}/libkitchensyncprivate.so.?
#%attr(755,root,root) %{_libdir}/libkitchensyncprivate.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/kitchensyncpart.so
#%attr(755,root,root) %{_libdir}/libqopensync.so
#%{_desktopdir}/kde4/kitchensync.desktop
#%{_datadir}/apps/kitchensync
#%{_iconsdir}/*/*/apps/kitchensync.png
#%{_iconsdir}/*/*/actions/sync-start.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdepim.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdepimwidgets.so
#%attr(755,root,root) %{_libdir}/kde4/kpartsdesignerplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
#%{_datadir}/apps/libkdepim
%{_datadir}/apps/kdepimwidgets
#%{_iconsdir}/*/*/actions/button_more.png
#%{_iconsdir}/*/*/actions/button_fewer.png
%attr(755,root,root) %ghost %{_libdir}/libakregatorinterfaces.so.?
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakregatorprivate.so.?
%attr(755,root,root) %{_libdir}/libakregatorprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwsoap.so.?
%attr(755,root,root) %{_libdir}/libgwsoap.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkabc_groupdav.so.?
#%attr(755,root,root) %{_libdir}/libkabc_groupdav.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkabc_slox.so.?
#%attr(755,root,root) %{_libdir}/libkabc_slox.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkabckolab.so.?
#%attr(755,root,root) %{_libdir}/libkabckolab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabcgroupwise.so.?
%attr(755,root,root) %{_libdir}/libkabcgroupwise.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookprivate.so.?
%attr(755,root,root) %{_libdir}/libkaddressbookprivate.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkcal_groupdav.so.?
#%attr(755,root,root) %{_libdir}/libkcal_groupdav.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcalgroupwise.so.?
%attr(755,root,root) %{_libdir}/libkcalgroupwise.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcal_resourceblog.so.?
%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcal_resourceremote.so.?
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkcal_slox.so.?
#%attr(755,root,root) %{_libdir}/libkcal_slox.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkcalkolab.so.?
#%attr(755,root,root) %{_libdir}/libkcalkolab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdepim.so.?
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkgroupwarebase.so.?
#%attr(755,root,root) %{_libdir}/libkgroupwarebase.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkgroupwaredav.so.?
#%attr(755,root,root) %{_libdir}/libkgroupwaredav.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkleo.so.?
%attr(755,root,root) %{_libdir}/libkleo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmailprivate.so.?
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknodecommon.so.?
%attr(755,root,root) %{_libdir}/libknodecommon.so.4.*.*
#%attr(755,root,root) %ghost %{_libdir}/libknoteskolab.so.?
#%attr(755,root,root) %{_libdir}/libknoteskolab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkontactprivate.so.?
%attr(755,root,root) %{_libdir}/libkontactprivate.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkorg_stdprinting.so.?
#%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkorganizer_calendar.so.?
#%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkorganizer_eventviewer.so.?
#%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_interfaces.so.?
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizerprivate.so.?
%attr(755,root,root) %{_libdir}/libkorganizerprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpgp.so.?
%attr(755,root,root) %{_libdir}/libkpgp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksieve.so.?
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkslox.so.?
#%attr(755,root,root) %{_libdir}/libkslox.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessagecore.so.?
%attr(755,root,root) %{_libdir}//libmessagecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessagelist.so.?
%attr(755,root,root) %{_libdir}//libmessagelist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessageviewer.so.?
%attr(755,root,root) %{_libdir}//libmessageviewer.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libmimelib.so.?
#%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
