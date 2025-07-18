# TODO:
#
#/usr/lib64/kde4/plugins/accessible/messagevieweraccessiblewidgetfactory.so
#
%define		qtver	4.8.1
%define		orgname	kdepim
Summary:	Personal Information Management (PIM) for KDE
Summary(ko.UTF-8):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl.UTF-8):	Zarządca informacji osobistej (PIM) dla KDE
Summary(ru.UTF-8):	Персональный планировщик (PIM) для KDE
Summary(uk.UTF-8):	Персональный планувальник (PIM) для KDE
Name:		kde4-kdepim
Version:	4.14.10
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	https://download.kde.org/Attic/applications/15.04.3/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a09c9bd838cd71c16e9993e57653a7ad
Patch0:		kdepim-4.11.90-install_kleopatra_headers.patch
Patch1:		%{name}-qt.patch
Patch100:	%{name}-branch.diff
# http://mirrors.ludost.net/gentoo/distfiles/kleopatra-4.4.3-assuan2.patch.bz2
URL:		https://kde.org/
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
#BuildRequires:	kde4-kactivities-devel >= %{version}
BuildRequires:	kde4-baloo-widgets-devel >= 4.14.3
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libassuan-devel
BuildRequires:	libindicate-qt-devel >= 0.2.2
BuildRequires:	libkgapi-devel >= 2.2.0
BuildRequires:	link-grammar-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
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
Obsoletes:	kde4-kdepim-akonadi < 4.3
Obsoletes:	kde4-kdepim-kitchensync < 4.2
Obsoletes:	kde4-kdepim-kpilot < 4.4
Obsoletes:	kde4-kdepim-plugins < 4.10.4-2
Obsoletes:	kde4-kdepim-wizards < 4.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepim jest zestawem aplikacji do zarządzania informacjami osobistymi
(PIM) dla K Desktop Environment (KDE).

%description -l ru.UTF-8
kdepim - это набор утилит для управления персональной информацией для
K Desktop Environment (KDE).

%description -l uk.UTF-8
kdepim - це набір утиліт для керування персональною информацією для K
Desktop Environment (KDE).

%package kontact
Summary:	Kontact Personal Information Management
Summary(pl.UTF-8):	Kontact - zarządca informacji osobistych (PIM)
Group:		X11/Applications
Requires:	kde4-kdepim-runtime
Requires:	pinentry-qt4
Provides:	kde4-kontact
Obsoletes:	kde4-kontact < 4.2
Obsoletes:	kde4-kontact-plugin-ktimetracker < 4.2
Obsoletes:	kde4-kontact-plugin-planner < 4.2
Obsoletes:	kde4-kdepim-kontact-plugin-ktimetracker < 4.10
Obsoletes:	kde4-kdepim-kontact-plugin-planner < 4.8

%description kontact
Kontact Personal Information Management.

%description kontact -l pl.UTF-8
Kontact Personal Information Management - zarządca informacji
osobistych.

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
- support for sending mail via SMTP
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
- obsługę wysyłania poczty poprzez SMTP
- konfigurowalne filtry, fonty i kolory
- pełne punktowanie wiadomości (score)
- wiele więcej...

%description knode -l pt_BR.UTF-8
Leitor de notícias (news) do KDE.

%package kontact-plugin-knode
Summary:	Knode plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Knode dla Kontacta
Group:		X11/Applications
Requires:	%{name}-knode = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Obsoletes:	kde4-kontact-plugin-knode < 4.2

%description kontact-plugin-knode
Knode plugin for Kontact.

%description kontact-plugin-knode -l pl.UTF-8
Wtyczka Knode dla Kontacta.

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
URL:		https://kontact.kde.org/components/kmail.html
# ? Requires:	kde4-kdebase >= %{version}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pinentry-qt4
Obsoletes:	kde4-kdepim-ktnef < 4.8

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
- sprawdzanie pisowni w locie
- import poczty z innych klientów
- wiele więcej...

%description kmail -l pt_BR.UTF-8
Poderoso cliente / leitor de e-mails para o KDE.

%package kontact-plugin-kmail
Summary:	Kmail plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Kmail dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kmail = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kmail
Obsoletes:	kde4-kontact-plugin-kmail < 4.2

%description kontact-plugin-kmail
Kmail plugin for Kontact.

%description kontact-plugin-kmail -l pl.UTF-8
Wtyczka Kmail dla Kontacta.

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
Summary(pl.UTF-8):	Wtyczka Kaddressbook dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kaddressbook = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kaddressbook
Obsoletes:	kde4-kontact-plugin-kaddressbook < 4.2

%description kontact-plugin-kaddressbook
Kaddressbook plugin for Kontact.

%description kontact-plugin-kaddressbook -l pl.UTF-8
Wtyczka Kaddressbook dla Kontacta.

%package korganizer
Summary:	KOrganizer - calendar and scheduling component of Kontact
Summary(pl.UTF-8):	KOrganizer - komponent Kontacta z kalendarzem i planowaniem
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
KOrganizer to komponent Kontacta (zarządcy informacji osobistych KDE)
z kalendarzem i planowaniem zadań.

KOrganizer zapewnia zarządzanie wydarzeniami i zadaniami,
powiadomienia, eksport przez WWW, przezroczystą sieciowo obsługę
danych, planowanie grupowe, import i eksport plików kalendarza itp.
Potrafi współpracować z wieloma serwerami pracy grupowej, jak Kolab,
Open-Xchange, Citadel czy OpenGroupware.org.

KOrganizer jest w pełni konfigurowalny do potrzeb i jest integralną
częścią narzędzi KDE PIM, których celem jest zapewnienie kompletnego
rozwiązania organizowania danych osobistych. KOrganizer obsługuje dwa
dominujące standardy pzechowywania i wymiany danych kalendarza:
vCalendar oraz iCalendar.

%package kontact-plugin-korganizer
Summary:	KOrganizer plugin for Kontact
Summary(pl.UTF-8):	Wtyczka KOrganizer dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Requires:	%{name}-korganizer = %{version}-%{release}
Provides:	kde4-kontact-plugin-korganizer
Obsoletes:	kde4-kontact-plugin-korganizer < 4.2

%description kontact-plugin-korganizer
KOrganizer plugin for Kontact.

%description kontact-plugin-korganizer -l pl.UTF-8
Wtyczka KOrganizer dla Kontacta.

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
Summary(pl.UTF-8):	Wtyczka kmobiletools dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kmobiletools = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-kmobiletools
Obsoletes:	kde4-kontact-plugin-kmobiletools < 4.2

%description kontact-plugin-kmobiletools
Kmobiletools plugin for Kontact.

%description kontact-plugin-kmobiletools -l pl.UTF-8
Wtyczka kmobiletools dla Kontacta.

%package kontact-plugin-summary
Summary:	Summary plugin for Kontact
Summary(pl.UTF-8):	Wtyczka podsumowania dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-summary
Obsoletes:	kde4-kontact-plugin-summary < 4.2

%description kontact-plugin-summary
Summary plugin for Kontact.

%description kontact-plugin-summary -l pl.UTF-8
Wtyczka podsumowania dla Kontacta.

%package kontact-plugin-specialdates
Summary:	Specialdates plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Specialdates dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-specialdates
Obsoletes:	kde4-kontact-plugin-specialdates < 4.2

%description kontact-plugin-specialdates
Specialdates plugin for Kontact.

%description kontact-plugin-specialdates -l pl.UTF-8
Wtyczka Specialdates dla Kontacta.

%package kontact-plugin-newsticker
Summary:	Newsticker plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Newsticker dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-newsticker
Obsoletes:	kde4-kontact-plugin-newsticker < 4.2

%description kontact-plugin-newsticker
Newsticker plugin for Kontact.

%description kontact-plugin-newsticker -l pl.UTF-8
Wtyczka Newsticker dla Kontacta.

%package akregator
Summary:	News feed reader for the KDE desktop
Summary(pl.UTF-8):	Czytnik aktualności dla środowiska KDE
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
Akregator to czytnik aktualności (news feed) dla środowiska KDE.
Pozwala śledzić strony z wiadomościami, blogi oraz inne witryny z
obsługą RSS/Atom bez potrzeby ręcznego sprawdzania uaktualnień przy
użyciu przeglądarki WWW. Akregator jest zaprojektowany jako łatwy w
użyciu, a jednocześnie wystarczająco potężny, by czytać wygodnie
setki źródeł aktualności. Ma integrację z Konquerorem w celu dodawania
nowych źródeł oraz z wewnętrzną przeglądarką w celu łatwego czytania
wiadomości.

%package kontact-plugin-akregator
Summary:	Akregator plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Akregator dla Kontacta
Group:		X11/Applications
Requires:	%{name}-akregator = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-akregator
Obsoletes:	kde4-kontact-plugin-akregator < 4.2

%description kontact-plugin-akregator
Akregator plugin for Kontact.

%description kontact-plugin-akregator -l pl.UTF-8
Wtyczka Akregator dla Kontacta.

%package kontact-plugin-weather
Summary:	Weather plugin for Kontact
Summary(pl.UTF-8):	Wtyczka Weather dla Kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-weather
Obsoletes:	kde4-kontact-plugin-weather < 4.2

%description kontact-plugin-weather
Weather plugin for Kontact.

%description kontact-plugin-weather -l pl.UTF-8
Wtyczka Weather dla Kontacta.

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
Summary(pl.UTF-8):	Wtyczka Knotes dla Kontacta
Group:		X11/Applications
Requires:	%{name}-knotes = %{version}-%{release}
Requires:	%{name}-kontact = %{version}-%{release}
Provides:	kde4-kontact-plugin-knotes
Obsoletes:	kde4-kontact-plugin-knotes < 4.2

%description kontact-plugin-knotes
Knotes plugin for Kontact.

%description kontact-plugin-knotes -l pl.UTF-8
Wtyczka Knotes dla Kontacta.

%package devel
Summary:	Development files for KDE pim
Summary(pl.UTF-8):	Pliki nagłówkowe do KDE pim
Summary(ru.UTF-8):	Файлы разработки для kdepim
Summary(uk.UTF-8):	Файли розробки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name}-kleopatra = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdepim-apidocs < 4.0.61

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
Obsoletes:	kde4-kio-groupwise < 4.2.0

%description kio-groupwise
Groupwise protocol service.

%description kio-groupwise -l pl.UTF-8
Obsługa protokołu Groupwise.

%package kio-imap4
Summary:	IMAP4 protocol service
Summary(pl.UTF-8):	Obsługa protokołu IMAP4
Group:		X11/Libraries
Obsoletes:	kde4-kio-imap4 < 4.2.0
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
Obsoletes:	kalarm < 3

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

%package kleopatra
Summary:	Kleopatra - certificate manager and crypto GUI for KDE
Summary(pl.UTF-8):	Kleopatra - zarządca certyfikatów i graficzny interfejs kryptograficzny dla KDE
Group:		X11/Applications
URL:		https://apps.kde.org/kleopatra/
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dirmngr

%description kleopatra
Kleopatra is a certificate manager and universal crypto GUI for KDE.

%description kleopatra -l pl.UTF-8
Kleopatra to zarządca certyfikatów i uniwersalny graficzny interfejs
kryptograficzny dla KDE.

%package kjots
Summary:	KDE Note taker
Summary(pl.UTF-8):	Notatnik dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kde4-kdebase >= 4.14.3

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
Requires:	kde4-kdebase >= 4.14.3

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
%patch -P0 -p1
%patch -P1 -p1
#%%patch100 -p1

%{__sed} -i -e '1s, /usr/bin/env bash,/bin/bash,' kmail/kconf_update/kmail-*.sh

%build
install -d build
cd build
%cmake .. \
	-DKONTACT_ENABLE_MIXEDMODE_SUMMARY_PLUGINS=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang akregator --with-kde
%find_lang kleopatra --with-kde
%find_lang kmail --with-kde
%find_lang knode --with-kde
%find_lang knotes --with-kde
%find_lang kontact --with-kde
%find_lang korganizer --with-kde
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
%attr(755,root,root) %{_bindir}/kincidenceeditor
%attr(755,root,root) %{_bindir}/sieveeditor
%attr(755,root,root) %{_bindir}/storageservicemanager
%attr(755,root,root) %{_bindir}/tasks-mobile
%{_datadir}/apps/tasks-mobile
%{_desktopdir}/kde4/tasks-mobile.desktop
%{_iconsdir}/*/*/apps/tasks-mobile.*
%dir %{_libdir}/akonadi
%dir %{_libdir}/akonadi/contact
%dir %{_libdir}/akonadi/contact/editorpageplugins
%attr(755,root,root) %{_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_desktopdir}/kde4/akonadiconsole.desktop
%{_desktopdir}/kde4/pimsettingexporter.desktop
%{_desktopdir}/kde4/sieveeditor.desktop
%{_desktopdir}/kde4/storageservicemanager.desktop
%{_datadir}/apps/akonadiconsole
%dir %{_datadir}/apps/sieve
%dir %{_datadir}/apps/sieve/scripts
%dir %{_datadir}/apps/sieve/scripts/copy
%{_datadir}/apps/sieve/scripts/copy/template.desktop
%{_datadir}/apps/sieve/scripts/copy/template.txt
%{_datadir}/apps/sieveeditor
%{_datadir}/apps/storageservicemanager
%{_datadir}/config/kaddressbook_themes.knsrc
%{_datadir}/config/knotes_printing_theme.knsrc
%{_datadir}/config/ksieve_script.knsrc

%{_iconsdir}/hicolor/*x*/apps/akonadiconsole.png
%{_iconsdir}/hicolor/*x*/apps/kdepim-dropbox.png
%{_iconsdir}/hicolor/*x*/apps/kdepim-googledrive.png
#
%attr(755,root,root) %{_bindir}/kgpgconf
%attr(755,root,root) %{_bindir}/kwatchgnupg
%{_datadir}/apps/kwatchgnupg
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%{_datadir}/apps/kconf_update/kpgp.upd
### strigi is not used for Akonadi does not include it
#%attr(755,root,root) %{_libdir}/strigi/strigiea_ctg.so
#%attr(755,root,root) %{_libdir}/strigi/strigiea_ics.so
#%attr(755,root,root) %{_libdir}/strigi/strigiea_vcf.so
#%attr(755,root,root) %{_libdir}/strigi/strigiea_mail.so
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so
%{_datadir}/apps/libmessageviewer
%{_datadir}/apps/messagelist
%{_datadir}/apps/messageviewer
%attr(755,root,root) %{_libdir}/kde4/messageviewer_bodypartformatter_*.so
%attr(755,root,root) %{_libdir}/kde4/kcal_remote.so
%{_datadir}/kde4/services/kresources/kcal/remote.desktop
%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so
%attr(755,root,root) %{_libdir}/kde4/kcal_blog.so
%{_datadir}/kde4/services/kresources/kcal/blog.desktop
%attr(755,root,root) %{_bindir}/pimsettingexporter
%{_datadir}/apps/pimsettingexporter
%{_datadir}/apps/kconf_update/grantleetheme.upd
%{_datadir}/apps/kconf_update/noteglobalsettings.upd
%lang(en) %{_kdedocdir}/en/kwatchgnupg
%lang(en) %{_kdedocdir}/en/pimsettingexporter
%lang(en) %{_kdedocdir}/en/sieveeditor

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
%lang(en) %{_kdedocdir}/en/blogilo

%files kontact -f kontact.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%attr(755,root,root) %{_libdir}/kde4/kcm_kontact.so
%{_desktopdir}/kde4/Kontact.desktop
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/kde4/services/kontactconfig.desktop
%{_datadir}/apps/contactthemeeditor
%{_datadir}/apps/kontact
%{_datadir}/apps/kontact-touch
%{_desktopdir}/kde4/kontact-admin.desktop
%{_iconsdir}/*/*/*/kontact*.*
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%lang(en) %{_kdedocdir}/en/kontact-admin

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%attr(755,root,root) %{_libdir}/kde4/kcm_knode.so
%attr(755,root,root) %{_libdir}/kde4/knodepart.so
%{_desktopdir}/kde4/KNode.desktop
%{_datadir}/apps/knode
%{_datadir}/apps/kconf_update/knode.upd
%{_datadir}/dbus-1/interfaces/org.kde.knode.xml
%{_datadir}/kde4/services/knode_*.desktop
%{_iconsdir}/*/*/apps/knode.*
# XXX: where to package?
%lang(en) %{_kdedocdir}/en/kioslave/news

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
%attr(755,root,root) %{_bindir}/akonadi_archivemail_agent
%attr(755,root,root) %{_bindir}/akonadi_followupreminder_agent
%attr(755,root,root) %{_bindir}/akonadi_mailfilter_agent
%attr(755,root,root) %{_bindir}/importwizard
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmail-mobile
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/ksendemail
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/ktnef
%attr(755,root,root) %{_bindir}/mboximporter
%attr(755,root,root) %{_libdir}/kde4/kcm_kmail.so
%attr(755,root,root) %{_libdir}/kde4/kmailpart.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpimidentities.so

%{_desktopdir}/kde4/KMail2.desktop
%{_desktopdir}/kde4/kmail_view.desktop
%{_desktopdir}/kde4/kmail-mobile.desktop
%{_desktopdir}/kde4/mboximporter.desktop
%{_datadir}/apps/akonadi_archivemail_agent
%{_datadir}/apps/akonadi_mailfilter_agent
%{_datadir}/apps/kmail2
%{_datadir}/apps/kmail-mobile
%{_datadir}/apps/ktnef
%{_datadir}/apps/mobileui
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/apps/kconf_update/mailfilteragent.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/migrate-kmail-filters.pl
%{_datadir}/kde4/services/kmail_*.desktop
%{_datadir}/kde4/services/kcm_kpimidentities.desktop
%{_datadir}/kde4/servicetypes/dbusmail.desktop
%{_datadir}/kde4/services/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_datadir}/akonadi/agents/folderarchiveagent.desktop
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_datadir}/apps/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-transport.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-signature.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail-*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail-*.sh
%{_datadir}/apps/kmailcvt
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/applications/kde4/importwizard.desktop
%{_datadir}/applications/kde4/ktnef.desktop
%{_iconsdir}/*/*/apps/kmail*.*
%{_iconsdir}/*/*/apps/ktnef.*
%{_iconsdir}/*/*/apps/kaddressbook-mobile-harmattan.*
%{_iconsdir}/*/*/apps/korganizer-mobile-harmattan.*
%{_iconsdir}/*/*/apps/notes-mobile-harmattan.*
%{_iconsdir}/*/*/apps/tasks-mobile-harmattan.*
%{_iconsdir}/*/*/actions/ktnef_extract*.*
%{_iconsdir}/oxygen/*/mimetypes/x-mail-distribution-list.*
%{_iconsdir}/oxygen/*/actions/smallclock.*
%{_iconsdir}/oxygen/*/actions/upindicator.*
%{_iconsdir}/oxygen/*/actions/checkmark.*
# conflicts with kde-icons-oxygen
%{_iconsdir}/oxygen/*/actions/edit-delete-page.*
%lang(en) %{_kdedocdir}/en/akonadi_archivemail_agent
%lang(en) %{_kdedocdir}/en/importwizard
%lang(en) %{_kdedocdir}/en/kmailcvt
%lang(en) %{_kdedocdir}/en/ktnef

%attr(755,root,root) %{_bindir}/akonadi_sendlater_agent
%dir %{_datadir}/apps/akonadi_sendlater_agent
%dir %{_datadir}/apps/akonadi_followupreminder_agent
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_datadir}/apps/akonadi_sendlater_agent/akonadi_sendlater_agent.notifyrc
%{_datadir}/apps/akonadi_followupreminder_agent/akonadi_followupreminder_agent.notifyrc
%lang(en) %{_kdedocdir}/en/akonadi_followupreminder_agent
%lang(en) %{_kdedocdir}/en/akonadi_sendlater_agent

%attr(755,root,root) %{_bindir}/contactthemeeditor
%attr(755,root,root) %{_bindir}/headerthemeeditor
%{_datadir}/applications/kde4/contactthemeeditor.desktop
%{_datadir}/applications/kde4/headerthemeeditor.desktop
%dir %{_datadir}/apps/headerthemeeditor
%{_datadir}/apps/headerthemeeditor/headerthemeeditorui.rc
%dir %{_datadir}/apps/composereditor
%{_datadir}/apps/composereditor/composereditorinitialhtml
%lang(en) %{_kdedocdir}/en/contactthemeeditor
%lang(en) %{_kdedocdir}/en/headerthemeeditor

%{_datadir}/config/messageviewer_header_themes.knsrc

%files kontact-plugin-kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kmailsummary.so
%{_datadir}/kde4/services/kontact/kmailplugin.desktop
%{_datadir}/kde4/services/kcmkmailsummary.desktop

%files kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_bindir}/kaddressbook-mobile
%attr(755,root,root) %{_libdir}/kde4/kcm_ldap.so
%attr(755,root,root) %{_libdir}/kde4/kaddressbookpart.so
%{_desktopdir}/kde4/kaddressbook.desktop
%{_desktopdir}/kde4/kaddressbook-importer.desktop
%{_desktopdir}/kde4/kaddressbook-mobile.desktop
%{_datadir}/apps/kaddressbook
%{_datadir}/apps/kaddressbook-mobile
%{_datadir}/kde4/services/kcmldap.desktop
%{_datadir}/kde4/services/kaddressbookpart.desktop
%{_iconsdir}/*/*/apps/kaddressbook.*
%{_iconsdir}/*/*/apps/kaddressbook-mobile.*

%files kontact-plugin-kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_kaddressbookplugin.so
%{_datadir}/kde4/services/kontact/kaddressbookplugin.desktop

%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calendarjanitor
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer
%attr(755,root,root) %{_bindir}/korganizer-mobile
%attr(755,root,root) %{_libdir}/kde4/kcm_korganizer.so
%attr(755,root,root) %{_libdir}/kde4/korg_*.so
%attr(755,root,root) %{_libdir}/kde4/korganizerpart.so
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/korganizer-mobile
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
%{_desktopdir}/kde4/korganizer-import.desktop
%{_desktopdir}/kde4/korganizer.desktop
%{_desktopdir}/kde4/korganizer-mobile.desktop
%{_iconsdir}/*/*/apps/korganizer.*
%{_iconsdir}/*/*/apps/korganizer-mobile.*
%{_iconsdir}/hicolor/*/apps/korg-*.*

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
%{_datadir}/apps/akregator_sharemicroblog_plugin
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

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_notes_agent
%attr(755,root,root) %{_bindir}/knotes
%attr(755,root,root) %{_bindir}/notes-mobile
%attr(755,root,root) %{_libdir}/kde4/kcm_knote.so
%attr(755,root,root) %{_libdir}/kde4/kcm_knotessummary.so
%{_desktopdir}/kde4/knotes.desktop
%{_desktopdir}/kde4/notes-mobile.desktop
%{_datadir}/akonadi/agents/notesagent.desktop
%{_datadir}/apps/akonadi_notes_agent
%{_datadir}/apps/knotes
%{_datadir}/apps/notes-mobile
%{_datadir}/apps/desktoptheme/default/widgets/stickynote.svgz
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/kde4/services/knote_config_action.desktop
%{_datadir}/kde4/services/knote_config_display.desktop
%{_datadir}/kde4/services/knote_config_editor.desktop
%{_datadir}/kde4/services/knote_config_network.desktop
%{_datadir}/kde4/services/kcmknotessummary.desktop
%{_datadir}/kde4/services/knote_config_collection.desktop
%{_datadir}/kde4/services/knote_config_misc.desktop
%{_datadir}/kde4/services/knote_config_print.desktop
#%{_datadir}/kde4/services/knote_config_style.desktop
%{_iconsdir}/*/*/actions/knotes_*.png
%{_iconsdir}/*/*/apps/knotes.*
%{_iconsdir}/*/*/apps/notes-mobile.png
%lang(en) %{_kdedocdir}/en/akonadi_notes_agent

%files kontact-plugin-knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kontact_knotesplugin.so
%{_datadir}/kde4/services/kontact/knotesplugin.desktop

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%attr(755,root,root) %{_libdir}/kde4/kjotspart.so
%attr(755,root,root) %{_libdir}/kde4/kontact_kjotsplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kjots.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_akonotes_list.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_akonotes_note.so
%{_datadir}/kde4/services/kjotspart.desktop
%{_desktopdir}/kde4/Kjots.desktop
%{_datadir}/apps/kjots
%{_datadir}/config.kcfg/kjots.kcfg
%{_datadir}/kde4/services/akonotes_*.desktop
%{_datadir}/kde4/services/kontact/kjots_plugin.desktop
%{_datadir}/kde4/services/kjots_config_misc.desktop
%{_iconsdir}/*/*/apps/kjots.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kleo
%{_includedir}/kpgp
%{_includedir}/libkleopatraclient
%attr(755,root,root) %{_libdir}/libakonadi_next.so
#%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so
%attr(755,root,root) %{_libdir}/libcalendarsupport.so
%attr(755,root,root) %{_libdir}/libcalendarsupportcollectionpage.so
%attr(755,root,root) %{_libdir}/libeventviews.so
%attr(755,root,root) %{_libdir}/libfollowupreminder.so
%attr(755,root,root) %{_libdir}/libgrantleetheme.so
%attr(755,root,root) %{_libdir}/libgrantleethemeeditor.so
%attr(755,root,root) %{_libdir}/libincidenceeditorsng.so
%attr(755,root,root) %{_libdir}/libincidenceeditorsngmobile.so
#%attr(755,root,root) %{_libdir}/libkaddressbookgrantlee.so
#%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so
#%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so
%attr(755,root,root) %{_libdir}/libkdepimdbusinterfaces.so
%attr(755,root,root) %{_libdir}/libkdepimmobileui.so
#%attr(755,root,root) %{_libdir}/libkdepim.so
%attr(755,root,root) %{_libdir}/libkdgantt2.so
%attr(755,root,root) %{_libdir}/libkleo.so
%attr(755,root,root) %{_libdir}/libkleopatraclientcore.so
%attr(755,root,root) %{_libdir}/libkleopatraclientgui.so
%attr(755,root,root) %{_libdir}/libkmanagesieve.so
%attr(755,root,root) %{_libdir}/libknodecommon.so
#%attr(755,root,root) %{_libdir}/libknotesprivate.so
%attr(755,root,root) %{_libdir}/libkorganizer_core.so
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so
%attr(755,root,root) %{_libdir}/libkpgp.so
%attr(755,root,root) %{_libdir}/libksieve.so
%attr(755,root,root) %{_libdir}/libksieveui.so
%attr(755,root,root) %{_libdir}/libmailcommon.so
%attr(755,root,root) %{_libdir}/libmailimporter.so
%attr(755,root,root) %{_libdir}/libmessagecomposer.so
%attr(755,root,root) %{_libdir}/libmessagecore.so
%attr(755,root,root) %{_libdir}/libmessagelist.so
%attr(755,root,root) %{_libdir}/libmessageviewer.so
%attr(755,root,root) %{_libdir}/libnoteshared.so
%attr(755,root,root) %{_libdir}/libpimcommon.so
%attr(755,root,root) %{_libdir}/libtemplateparser.so
%attr(755,root,root) %{_libdir}/libcomposereditorng.so
%attr(755,root,root) %{_libdir}/libsendlater.so

%files kalarm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm
%attr(755,root,root) %{_bindir}/kalarmautostart
%attr(755,root,root) %{_libdir}/kde4/libexec/kalarm_helper
%{_desktopdir}/kde4/kalarm.desktop
%{_datadir}/apps/kalarm
%{_datadir}/autostart/kalarm.autostart.desktop
%attr(755,root,root) %{_datadir}/apps/kconf_update/kalarm-*.pl
%{_datadir}/apps/kconf_update/kalarm.upd
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.*.xml
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
/etc/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_iconsdir}/*/*/apps/*kalarm.*
%lang(en) %{_kdedocdir}/en/kalarm

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%attr(755,root,root) %{_bindir}/kabcclient
%attr(755,root,root) %{_libdir}/kde4/ktexteditorkabcbridge.so
%{_desktopdir}/kde4/konsolekalendar.desktop
%dir %{_datadir}/apps
%{_iconsdir}/hicolor/*x*/apps/konsolekalendar.png
%lang(en) %{_kdedocdir}/en/konsolekalendar
%lang(en) %{_kdedocdir}/en/kabcclient
%{_mandir}/man1/kabcclient.1*

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
%{_datadir}/kde4/services/kleopatra_config_gnupgsystem.desktop
%{_datadir}/kde4/services/kleopatra_config_smimevalidation.desktop
%{_datadir}/kde4/services/kleopatra_config_cryptooperations.desktop
%{_datadir}/kde4/services/kleopatra_decryptverifyfiles.desktop
%{_datadir}/kde4/services/kleopatra_decryptverifyfolders.desktop
%{_datadir}/kde4/services/kleopatra_signencryptfiles.desktop
%{_datadir}/kde4/services/kleopatra_signencryptfolders.desktop
%{_iconsdir}/hicolor/*/apps/kleopatra.*
%{_desktopdir}/kde4/kleopatra.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdepim.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdepimwidgets.so
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_datadir}/apps/kdepimwidgets
# xxx - where is better place for this?
%dir %{_libdir}/kde4/imports
%dir %{_libdir}/kde4/imports/org
%dir %{_libdir}/kde4/imports/org/kde
%{_libdir}/kde4/imports/org/kde/pim
%attr(755,root,root) %ghost %{_libdir}/libakonadi_next.so.?
%attr(755,root,root) %{_libdir}/libakonadi_next.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakregatorinterfaces.so.?
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakregatorprivate.so.?
%attr(755,root,root) %{_libdir}/libakregatorprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalendarsupport.so.?
%attr(755,root,root) %{_libdir}/libcalendarsupport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalendarsupportcollectionpage.so.?
%attr(755,root,root) %{_libdir}/libcalendarsupportcollectionpage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeventviews.so.?
%attr(755,root,root) %{_libdir}/libeventviews.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfollowupreminder.so.?
%attr(755,root,root) %{_libdir}/libfollowupreminder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrantleetheme.so.?
%attr(755,root,root) %{_libdir}/libgrantleetheme.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrantleethemeeditor.so.?
%attr(755,root,root) %{_libdir}/libgrantleethemeeditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libincidenceeditorsng.so.?
%attr(755,root,root) %{_libdir}/libincidenceeditorsng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libincidenceeditorsngmobile.so.?
%attr(755,root,root) %{_libdir}/libincidenceeditorsngmobile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookgrantlee.so.?
%attr(755,root,root) %{_libdir}/libkaddressbookgrantlee.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdepimdbusinterfaces.so.?
%attr(755,root,root) %{_libdir}/libkdepimdbusinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdepimmobileui.so.?
%attr(755,root,root) %{_libdir}/libkdepimmobileui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdgantt2.so.?
%attr(755,root,root) %{_libdir}/libkdgantt2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmanagesieve.so.?
%attr(755,root,root) %{_libdir}/libkmanagesieve.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksieveui.so.?
%attr(755,root,root) %{_libdir}/libksieveui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmailcommon.so.?
%attr(755,root,root) %{_libdir}/libmailcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmailimporter.so.?
%attr(755,root,root) %{_libdir}/libmailimporter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessagecomposer.so.?
%attr(755,root,root) %{_libdir}/libmessagecomposer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnoteshared.so.?
%attr(755,root,root) %{_libdir}/libnoteshared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtemplateparser.so.?
%attr(755,root,root) %{_libdir}/libtemplateparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookprivate.so.?
%attr(755,root,root) %{_libdir}/libkaddressbookprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcal_resourceblog.so.?
%attr(755,root,root) %{_libdir}/libkcal_resourceblog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcal_resourceremote.so.?
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdepim.so.?
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkleo.so.?
%attr(755,root,root) %{_libdir}/libkleo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmailprivate.so.?
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknodecommon.so.?
%attr(755,root,root) %{_libdir}/libknodecommon.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libknotesprivate.so.?
%attr(755,root,root) %{_libdir}/libknotesprivate.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkontactprivate.so.?
%attr(755,root,root) %{_libdir}/libkontactprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_core.so.?
%attr(755,root,root) %{_libdir}/libkorganizer_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_interfaces.so.?
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizerprivate.so.?
%attr(755,root,root) %{_libdir}/libkorganizerprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpgp.so.?
%attr(755,root,root) %{_libdir}/libkpgp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksieve.so.?
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessagecore.so.?
%attr(755,root,root) %{_libdir}//libmessagecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessagelist.so.?
%attr(755,root,root) %{_libdir}//libmessagelist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmessageviewer.so.?
%attr(755,root,root) %{_libdir}//libmessageviewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpimcommon.so.?
%attr(755,root,root) %{_libdir}/libpimcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcomposereditorng.so.?
%attr(755,root,root) %{_libdir}/libcomposereditorng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsendlater.so.?
%attr(755,root,root) %{_libdir}/libsendlater.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpimsettingexporterprivate.so.4
%attr(755,root,root) %{_libdir}/libpimsettingexporterprivate.so.*.*.*

%dir %{_libdir}/kde4/plugins/accessible
%attr(755,root,root) %{_libdir}/kde4/plugins/accessible/messagevieweraccessiblewidgetfactory.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/mailcommonwidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/pimcommonwidgets.so
%dir %{_libdir}/kde4/plugins/grantlee
%dir %{_libdir}/kde4/plugins/grantlee/0.5
%attr(755,root,root) %{_libdir}/kde4/plugins/grantlee/0.5/grantlee_messageheaderfilters.so
