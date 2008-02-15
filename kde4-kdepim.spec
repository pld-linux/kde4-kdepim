# Conditional build:
%bcond_without	apidocs			# do not prepare API documentation
%bcond_without	hidden_visibility	# don't use gcc hidden visibility
#
%define		_state		unstable

%define	orgname	kdepim
Summary:	Personal Information Management (PIM) for KDE
Summary(ko.UTF-8):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl.UTF-8):	Zarządca informacji osobistej (PIM) dla KDE
Summary(ru.UTF-8):	Персональный планировщик (PIM) для KDE
Summary(uk.UTF-8):	Персональный планувальник (PIM) для KDE
Name:		kde4-kdepim
Version:	4.0.62
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	dc319aa9f2e9941601adbaf7afddc939
BuildRequires:	bison
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-bind-devel
BuildRequires:	boost-type_traits-devel
BuildRequires:	cmake
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-dtd42-xml
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gpgme-devel >= 1:1.0.0
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libassuan-devel
BuildRequires:	libgnokii-devel
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	libopensync-devel < 1:0.30
BuildRequires:	libopensync-devel >= 1:0.22
BuildRequires:	lockdev-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pilot-link-devel >= 0.12.1
%{?with_apidocs:BuildRequires:	qt4-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%description -l ru.UTF-8
kdepim - это набор утилит для управления
персональной информацией для K Desktop
Environment (KDE).

%description -l uk.UTF-8
kdepim - це набір утиліт для керування
персональною информацією для K Desktop
Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl.UTF-8):	Pliki nagłówkowe do KDE pim
Summary(ru.UTF-8):	Файлы разработки для kdepim
Summary(uk.UTF-8):	Файли розробки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
bazujących na kdepim.

%description devel -l uk.UTF-8
Цей пакет містить файли заголовків
необхідні для побудови програм,
базованих на kdepim.

%description devel -l ru.UTF-8
Этот пакет содержит файлы заголовков
необходимые для построения программ,
основанных на kdepim.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):	Dokumentacja API
Group:		Documentation
Requires:	kde4-kdelibs >= %{version}

%description apidocs
Annotated reference of libkdepim, libkdenetwork, libkmailprivate,
libknodecommon and the other kdepim's programming interfaces':
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsów programowania libkdepim, libkdenetwork,
libkmailprivate, libknodecommon i innych z kdepim wraz z przypisami:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)

%package -n kde4-kio-groupwise
Summary:	Groupwise protocol service
Summary(pl.UTF-8):	Obsługa protokołu Groupwise
Group:		X11/Libraries

%description -n kde4-kio-groupwise
Groupwise protocol service.

%description -n kde4-kio-groupwise -l pl.UTF-8
Obsługa protokołu Groupwise.

%package -n kde4-kio-imap4
Summary:	IMAP4 protocol service
Summary(pl.UTF-8):	Obsługa protokołu IMAP4
Group:		X11/Libraries

%description -n kde4-kio-imap4
IMAP4 protocol service.

%description -n kde4-kio-imap4 -l pl.UTF-8
Obsługa protokołu IMAP4.

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
uruchomienie polecenia lub pocztą elektroniczną. Umożliwia
ustawienie własnej wiadomości alarmowej, która wyskoczy na ekranie
o wybranym czasie albo zaszeregowanie poleceń do wykonania lub poczty
do wysłania. Zawiera także demona obsługującego przypominanie.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl.UTF-8):	Program do komunikacji między PC a tel. komórkowym
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl.UTF-8
Kandy umożliwia dostęp do telefonu komórkowego i pozwala na
synchronizację danych z telefonu z danymi na PC.

%package karm
Summary:	Personal timetracker
Summary(pl.UTF-8):	Osobisty czasomierz
Group:		X11/Applications

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl.UTF-8
KArm (nazwa pochodzi od słowa "praca" w języku punjambi) śledzi
czas spędzony na różnych zajęciach. Jest przydatny przy obliczaniu
godzin do wystawiania rachunków wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl.UTF-8):	Program pocztowy KDE
Summary(pt_BR.UTF-8):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
URL:		http://kmail.kde.org/
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdebase-core >= %{version}
Requires:	kde4-kio-imap4 >= %{version}-%{release}
Requires:	kde4-kio-pop3 >= %{version}
Requires:	kde4-kio-smtp >= %{version}

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
- ściąganie na żądanie lub usuwanie bez ściągania dużych
  listów z serwera POP3
- pełną obsługę listów we wszystkich językach i zestawach
  znaków obsługiwanych przez Qt
- przeszukiwanie wiadomości z prezentacją w wirtualnych folderach
- usuwanie powtórzonych listów
- wątkowanie wiadomości
- kontrolę pisowni w locie
- import poczty z innych klientów
- wiele więcej...

%description kmail -l pt_BR.UTF-8
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl.UTF-8):	Czytnik newsów dla KDE
Summary(pt_BR.UTF-8):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kdebase-core >= %{version}
Requires:	kde4-kio-nntp >= %{version}

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
KNode to czytnik newsów zgodny ze specyfikacją GKNSA przeznaczony
dla środowiska KDE. Jego możliwości obejmują:
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
Dodatkowo, aby móc służyć za przypominajkę, KNotes może
wysyłać pocztę i drukować notatki, a także przyjmować
przeciąganie nawet ze zdalnych komputerów.

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
KonsoleKalendar to działający z linii poleceń interfejs do
kalendarzy KDE. Pozwala oglądać, wstawiać, usuwać i modyfikować
zdarzenia w kalendarzu z linii poleceń lub języka skryptowego.
Ponadto KonsoleKalendar potrafi wyeksportować kalendarz KDE do wielu
innych formatów.

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
Requires:	kde4-kdebase-desktop >= %{version}

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl.UTF-8
Programik pokazujący liczbę wiadomości w wybranych folderach
pocztowych.

%description korn -l pt_BR.UTF-8
Miniaplicativo de monitoração da caixa de correio.

%package kpilot
Summary:	A sync tool for palmtops
Summary(pl.UTF-8):	Narzędzie do synchronizacji z palmtopami
Group:		X11/Applications
Requires:	pilot-link

%description kpilot
KPilot is an equivalent for the Palm Desktop software from Palm Inc,
which makes your Palm/Palm Pilot/Visor computer capable of exchanging
information with your KDE powered computer. KPilot doesn't replace the
Palm Desktop all by itself. It connects and integrates a number of
fine KDE 3.x applications into a package that can do everything the
Palm Desktop can, and more.

KPilot has plugins that can exchange information between your Palm and
other applications like KOrganizer or POP3/SMTP mail servers. In
KPilot you can display and edit your contacts, write notes or install
new programs on your Palm.

It supports:
- Palm Pilot, m100, m500, Zire, Tungsten series
- Handspring Visor and Treo series
- Sony Clié series (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c,
  T675c, 665c)
- and Garmin iQue 3600
- others might work, but have not been tested

%description kpilot -l pl.UTF-8
KPilot to odpowiednik oprogramowania Palm Desktop firmy Palm Inc,
umożliwiający wymianę informacji między urządzeniami Palm, Palm
Pilot i Visor a komputerem z KDE. KPilot jako taki nie zastępuje Palm
Desktop - łączy i integruje wiele aplikacji KDE 3.x w pakiet,
którym można zrobić tyle samo, a nawet więcej, co przy użyciu
Palm Desktop.

KPilot ma wtyczki do wymiany informacji między Palmem a innymi
aplikacjami, takimi jak KOrganizer albo serwery POP3/SMTP. W KPilocie
można wyświetlać i modyfikować kontakty, pisać notatki lub
instalować nowe programy na Palmie.

Obsługuje urządzenia serii:
- Palm Pilot, m100, m500, Zire, Tungsten
- Handspring Visor i Treo
- Sony Clié (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c, T675c,
  665c)
- Garmin iQue 3600
- mogą działać także inne, ale nie były testowane.

%description kpilot -l ru.UTF-8
утилита для синхронизации с 3com Palm Pilots
и совместимыми с ними устройствами,

%description kpilot -l uk.UTF-8
утиліта для синхронізації з 3com Palm Pilots
та сумісними з ними пристроями.

%package libs
Summary:	Shared kdepim libraries
Summary(pl.UTF-8):	Współdzielone biblioteki kdepim
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description libs
Libraries shared between PIM applications in KDE, which include:
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib and more

%description libs -l pl.UTF-8
Biblioteki współdzielone pomiędzy aplikacjami PIM w KDE, m.in.
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib.

%prep
%setup -q -n %{orgname}-%{version}

%build
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs			-p /sbin/ldconfig
%postun	libs			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.Kolab
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/*groupwarewizard
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/kode
%attr(755,root,root) %{_bindir}/kolabwizard
%attr(755,root,root) %{_bindir}/kontact
%attr(755,root,root) %{_bindir}/kxml_compiler
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/sloxwizard

#### AKONADI ???
%attr(755,root,root) %{_bindir}/akonadi
%attr(755,root,root) %{_bindir}/akonadi_control
%attr(755,root,root) %{_bindir}/akonadi_ical_resource
%attr(755,root,root) %{_bindir}/akonadi_knut_resource
%attr(755,root,root) %{_bindir}/akonadi_localbookmarks_resource
%attr(755,root,root) %{_bindir}/akonadi_maildir_resource
%attr(755,root,root) %{_bindir}/akonadi_mailthreader_agent
%attr(755,root,root) %{_bindir}/akonadi_nepomuk_feeder
%attr(755,root,root) %{_bindir}/akonadi_nntp_resource
%attr(755,root,root) %{_bindir}/akonadi_strigi_feeder
%attr(755,root,root) %{_bindir}/akonadi_vcard_resource
%attr(755,root,root) %{_bindir}/akonadiconsole
%attr(755,root,root) %{_bindir}/akonadictl
%attr(755,root,root) %{_bindir}/akonadiserver
%attr(755,root,root) %{_bindir}/akonamail
%attr(755,root,root) %{_bindir}/kabcclient
%attr(755,root,root) %{_bindir}/kabceditor
%attr(755,root,root) %{_bindir}/kabcviewer
%attr(755,root,root) %{_bindir}/kagenda
%attr(755,root,root) %{_bindir}/kcontactmanager
%attr(755,root,root) %{_bindir}/kmobiletools
%attr(755,root,root) %{_bindir}/ktimetracker
%attr(755,root,root) %{_bindir}/kung
%attr(755,root,root) %{_bindir}/kwsdl_compiler
%attr(755,root,root) %{_bindir}/kxforms
%attr(755,root,root) %{_bindir}/scalixadmin
%attr(755,root,root) %{_bindir}/scalixwizard
%attr(755,root,root) %{_bindir}/schematest
%attr(755,root,root) %{_bindir}/thememain
%attr(755,root,root) /usr/lib/kde4/akonadi_serializer_addressee.so
%attr(755,root,root) /usr/lib/kde4/akonadi_serializer_bookmark.so
%attr(755,root,root) /usr/lib/kde4/akonadi_serializer_kcal.so
%attr(755,root,root) /usr/lib/kde4/akonadi_serializer_mail.so
%attr(755,root,root) /usr/lib/kde4/akonadi_serializer_sms.so
##################

#%attr(755,root,root) %{_libdir}/kde4/conduit_memofile.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_notepad.so
%attr(755,root,root) %{_libdir}/kde4/kabc_groupdav.so
#%attr(755,root,root) %{_libdir}/kde4/kabc_groupwise.so
%attr(755,root,root) %{_libdir}/kde4/kabc_kolab.so
#%attr(755,root,root) %{_libdir}/kde4/kabc_newexchange.so
%attr(755,root,root) %{_libdir}/kde4/kabc_slox.so
%attr(755,root,root) %{_libdir}/kde4/kabc_xmlrpc.so
%attr(755,root,root) %{_libdir}/kde4/kcal_groupdav.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_groupwise.so
%attr(755,root,root) %{_libdir}/kde4/kcal_kabc.so
%attr(755,root,root) %{_libdir}/kde4/kcal_kolab.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_local.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_localdir.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_newexchange.so
%attr(755,root,root) %{_libdir}/kde4/kcal_remote.so
#%attr(755,root,root) %{_libdir}/kde4/kcal_resourcefeatureplan.so
%attr(755,root,root) %{_libdir}/kde4/kcal_slox.so
%attr(755,root,root) %{_libdir}/kde4/kcal_xmlrpc.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kmailsummary.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kontact.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kontactknt.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kontactsummary.so
%attr(755,root,root) %{_libdir}/kde4/kcm_korganizer.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_korgsummary.so
%attr(755,root,root) %{_libdir}/kde4/kcm_sdsummary.so
#%attr(755,root,root) %{_libdir}/kde4/kded_networkstatus.so
#%attr(755,root,root) %{_libdir}/kde4/kfile_ics.so
#%attr(755,root,root) %{_libdir}/kde4/libakregatorpart.so*
#%attr(755,root,root) %{_libdir}/kde4/libexchangewizard.so
#%attr(755,root,root) %{_libdir}/kde4/libgroupwisewizard.so*
#%attr(755,root,root) %{_libdir}/kde4/libakregator_mk4storage_plugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkitchensyncpart.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_akregator.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_journalplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_kaddressbookplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_karm.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_kmailplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_knodeplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_knotesplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_korganizerplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_todoplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_kpilotplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_newstickerplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_specialdatesplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_summaryplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkontact_weatherplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkorg_*.so
#%attr(755,root,root) %{_libdir}/kde4/libkorganizerpart.so
#%attr(755,root,root) %{_libdir}/kde4/libegroupwarewizard.so*
#%attr(755,root,root) %{_libdir}/kde4/libkolabwizard.so*
#%attr(755,root,root) %{_libdir}/kde4/libsloxwizard.so*
#%attr(755,root,root) %{_libdir}/kde4/resourcecalendarexchange.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdepimwidgets.so
#%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kpartsdesignerplugin.so
%{_datadir}/apps/akregator
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/kdepimwidgets
#%{_datadir}/apps/kgantt
#%{_datadir}/apps/kitchensync
%{_datadir}/apps/kontact
%{_datadir}/apps/kontactsummary
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
#%{_datadir}/apps/kdepim
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/egroupware.kcfg
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config.kcfg/memofileconduit.kcfg
#%{_datadir}/config.kcfg/mk4config.kcfg
#%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/slox.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg

#%{_datadir}/services/akregator_mk4storage_plugin.desktop
#%{_datadir}/services/akregator_part.desktop
#%{_datadir}/services/feed.protocol
#%{_datadir}/services/kcmkmailsummary.desktop
#%{_datadir}/services/kcmkontactknt.desktop
#%{_datadir}/services/kcmkontactsummary.desktop
#%{_datadir}/services/kcmkorgsummary.desktop
#%{_datadir}/services/kcmsdsummary.desktop
#%{_datadir}/services/kded/networkstatus.desktop
#%{_datadir}/services/kfile_ics.desktop
#%{_datadir}/services/kontact
#%{_datadir}/services/kontactconfig.desktop
#%{_datadir}/services/korganizer
#%{_datadir}/services/korganizer_*.desktop
#%{_datadir}/services/kresources/kabc/imap.desktop
#%{_datadir}/services/kresources/kabc/kabc_groupdav.desktop
#%{_datadir}/services/kresources/kabc/kabc_groupwise.desktop
#%{_datadir}/services/kresources/kabc/kabc_newexchange.desktop
#%{_datadir}/services/kresources/kabc/kabc_opengroupware.desktop
#%{_datadir}/services/kresources/kabc/kabc_slox.desktop
#%{_datadir}/services/kresources/kabc/kabc_xmlrpc.desktop
#%{_datadir}/services/kresources/kabc/kolab.desktop
#%{_datadir}/services/kresources/kabc/kabc_ox.desktop
#%{_datadir}/services/kresources/kcal
#%{_datadir}/services/kresources/kcal_manager.desktop
#%{_datadir}/services/webcal.protocol
#%{_datadir}/servicetypes/akregator_plugin.desktop
#%{_datadir}/servicetypes/calendardecoration.desktop
#%{_datadir}/servicetypes/calendarplugin.desktop
#%{_datadir}/servicetypes/dcopcalendar.desktop
#%{_datadir}/servicetypes/kaddressbookimprotocol.desktop
#%{_datadir}/servicetypes/kontactplugin.desktop
#%{_datadir}/servicetypes/korganizerpart.desktop
#%{_datadir}/servicetypes/korgprintplugin.desktop
#%{_desktopdir}/kde/Kontact.desktop
#%{_desktopdir}/kde/akregator.desktop
#%{_desktopdir}/kde/korganizer.desktop
#%{_desktopdir}/kde/kitchensync.desktop
#%{_desktopdir}/kde/groupwarewizard.desktop
%{_iconsdir}/*/*/apps/akregator*
%{_iconsdir}/*/*/*/korganizer*.png
#%{_iconsdir}/*/*/*/kitchensync.png
%{_iconsdir}/*/*/apps/kontact.png
#%{_iconsdir}/*/*/actions/kontact_*.png
#%{_iconsdir}/*/*/actions/*rss*
#%{_iconsdir}/crystalsvg/22x22/actions/button_fewer.png
#%{_iconsdir}/crystalsvg/22x22/actions/button_more.png

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/indexlib-config
%{_includedir}/*.h
%{_includedir}/kleo
%{_includedir}/kmail
%{_includedir}/kontact
%{_includedir}/kpgp
%{_includedir}/kpilot
%{_includedir}/ksieve
%{_includedir}/libakonadi
%{_includedir}/libkmobiletools
%{_includedir}/libkmobiletoolsengineui
%{_includedir}/akregator
%{_includedir}/kaddressbook

#%{_libdir}/libgpgme++.so
%{_libdir}/libkabc_groupdav.so
#%{_libdir}/libindex.so
#%{_libdir}/libkabc_groupwise.so
#%{_libdir}/libkabc_newexchange.so
%{_libdir}/libkabc_slox.so
%{_libdir}/libkabc_xmlrpc.so
%{_libdir}/libkabckolab.so
%{_libdir}/libkabinterfaces.so
%{_libdir}/libkaddressbook.so
#%{_libdir}/libkcal.so
#%{_libdir}/libkcal_groupdav.so
#%{_libdir}/libkcal_groupwise.so
#%{_libdir}/libkcal_newexchange.so
%{_libdir}/libkcal_resourcefeatureplan.so
%{_libdir}/libkcal_resourceremote.so
%{_libdir}/libkcal_slox.so
%{_libdir}/libkcal_xmlrpc.so
%{_libdir}/libkcalkolab.so
%{_libdir}/libkdepim.so
#%{_libdir}/libkgantt.so
%{_libdir}/libkgroupwarebase.so
%{_libdir}/libkgroupwaredav.so
%{_libdir}/libkholidays.so
#%{_libdir}/libkitchensync.so
#%{_libdir}/libkleopatra.so
#%{_libdir}/libkmime.so
%{_libdir}/libknotes_xmlrpc.so
%{_libdir}/libknoteskolab.so
%{_libdir}/libkocorehelper.so
%{_libdir}/libkode.so
%{_libdir}/libkontact.so
#%{_libdir}/libkorganizer.so
%{_libdir}/libkorganizer_eventviewer.so
%{_libdir}/libkorganizer_calendar.so
%{_libdir}/libkorg_stdprinting.so
%{_libdir}/libkpgp.so
%{_libdir}/libkpilot.so
#%{_libdir}/libkpimexchange.so
#%{_libdir}/libkpimidentities.so
%{_libdir}/libkpinterfaces.so
%{_libdir}/libksieve.so
#%{_libdir}/libktnef.so
%{_libdir}/libmimelib.so
#%{_libdir}/libqgpgme.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
#%{_kdedocdir}/en/%{name}-apidocs
%endif

%files -n kde4-kio-imap4
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kio_imap4.so
#%{_datadir}/services/imap4.protocol
#%{_datadir}/services/imaps.protocol

%files -n kde4-kio-groupwise
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kio_groupwise.so
%{_datadir}/config.kcfg/groupwise.kcfg
#%{_datadir}/services/groupwise.protocol
#%{_datadir}/services/groupwises.protocol

%files kaddressbook
%defattr(644,root,root,755)
#-f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_libdir}/kde4/kcm_kabconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kabcustomfields.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kabldapconfig.so
%attr(755,root,root) %{_libdir}/kde4/ldifvcardthumbnail.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_bookmark_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_cardview.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_cryptosettings.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_csv_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_distributionlist.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_eudora_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_gmx_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_gnokii_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_iconview.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_kde2_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_ldif_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_opera_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_pab_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_resourceselection.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_tableview.so
%attr(755,root,root) %{_libdir}/kde4/kaddrbk_vcard_xxport.so
%attr(755,root,root) %{_libdir}/kde4/kaddressbookpart.so


%{_datadir}/apps/kaddressbook
/usr/share/kde4/services/kaddressbook/aimprotocol.desktop
/usr/share/kde4/services/kaddressbook/bookmark_xxport.desktop
/usr/share/kde4/services/kaddressbook/cardview.desktop
/usr/share/kde4/services/kaddressbook/cryptosettings.desktop
/usr/share/kde4/services/kaddressbook/csv_xxport.desktop
/usr/share/kde4/services/kaddressbook/distributionlist.desktop
/usr/share/kde4/services/kaddressbook/distributionlistng.desktop
/usr/share/kde4/services/kaddressbook/eudora_xxport.desktop
/usr/share/kde4/services/kaddressbook/gaduprotocol.desktop
/usr/share/kde4/services/kaddressbook/gmx_xxport.desktop
/usr/share/kde4/services/kaddressbook/gnokii_xxport.desktop
/usr/share/kde4/services/kaddressbook/groupwiseprotocol.desktop
/usr/share/kde4/services/kaddressbook/iconview.desktop
/usr/share/kde4/services/kaddressbook/icqprotocol.desktop
/usr/share/kde4/services/kaddressbook/ircprotocol.desktop
/usr/share/kde4/services/kaddressbook/jabberprotocol.desktop
/usr/share/kde4/services/kaddressbook/kde2_xxport.desktop
/usr/share/kde4/services/kaddressbook/ldif_xxport.desktop
/usr/share/kde4/services/kaddressbook/meanwhileprotocol.desktop
/usr/share/kde4/services/kaddressbook/msnprotocol.desktop
/usr/share/kde4/services/kaddressbook/opera_xxport.desktop
/usr/share/kde4/services/kaddressbook/pab_xxport.desktop
/usr/share/kde4/services/kaddressbook/resourceselection.desktop
/usr/share/kde4/services/kaddressbook/skypeprotocol.desktop
/usr/share/kde4/services/kaddressbook/smsprotocol.desktop
/usr/share/kde4/services/kaddressbook/tableview.desktop
/usr/share/kde4/services/kaddressbook/vcard_xxport.desktop
/usr/share/kde4/services/kaddressbook/yahooprotocol.desktop
/usr/share/applications/kde4/kaddressbook.desktop

/usr/share/kde4/servicetypes/kaddressbook_contacteditorwidget.desktop
/usr/share/kde4/servicetypes/kaddressbook_extension.desktop
/usr/share/kde4/servicetypes/kaddressbook_view.desktop
/usr/share/kde4/servicetypes/kaddressbook_xxport.desktop
/usr/share/kde4/servicetypes/kaddressbookimprotocol.desktop

/usr/share/kde4/services/addressbook_service.desktop
%{_iconsdir}/*/*/*/kaddressbook.png
/usr/share/dbus-1/interfaces/org.kde.KAddressbook.Core.xml

%files kalarm
%defattr(644,root,root,755)
#-f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
#%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*.desktop
%{_desktopdir}/kde4/kalarm.desktop
%{_desktopdir}/kde4/kalarmd.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
/usr/lib/libkalarm_resources.so
/usr/lib/libkalarm_resources.so.4
/usr/lib/libkalarm_resources.so.4.1.0
/usr/share/apps/kconf_update/kalarm-1.2.1-general.pl
/usr/share/apps/kconf_update/kalarm-1.9.5-defaults.pl
/usr/share/apps/kconf_update/kalarm-version.pl
/usr/share/apps/kconf_update/kalarm.upd
/usr/share/config.kcfg/kalarmconfig.kcfg
/usr/share/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
/usr/share/dbus-1/interfaces/org.kde.kalarm.kalarmd.Daemon.xml
/usr/share/dbus-1/interfaces/org.kde.kalarm.notify.xml
/usr/lib/kde4/kalarm_local.so
/usr/lib/kde4/kalarm_localdir.so
/usr/lib/kde4/kalarm_remote.so

%files kandy
%defattr(644,root,root,755)
#-f kandy.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kandy*
#%{_datadir}/apps/kandy
#%{_datadir}/config.kcfg/kandy.kcfg
#%{_desktopdir}/kde/kandy.desktop

%files karm
%defattr(644,root,root,755)
#-f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%attr(755,root,root) %{_libdir}/kde4/kontact_karm.so
#%attr(755,root,root) %{_libdir}/kde4/libkarmpart.so
#%{_datadir}/apps/karm
%{_datadir}/apps/karmpart
#%{_datadir}/services/karm_part.desktop
#%{_desktopdir}/kde/karm.desktop
#%{_iconsdir}/*/*/*/karm.png
/usr/lib/kde4/karmpart.so
/usr/share/kde4/services/kontact/karmplugin.desktop

%files kmail
%defattr(644,root,root,755)
#-f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%attr(755,root,root) %{_bindir}/kmailcvt
#%attr(755,root,root) %{_bindir}/kleopatra
#%attr(755,root,root) %{_bindir}/kwatchgnupg
#
%attr(755,root,root) %{_libdir}/libkmailprivate.so.4
%attr(755,root,root) %{_libdir}/libkmailprivate.so.4.1.0
#
%attr(755,root,root) %{_libdir}/kde4/kcm_kmail.so
%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_application_octetstream.so
%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_vcard.so
%attr(755,root,root) %{_libdir}/kde4/kmail_bodypartformatter_text_xdiff.so
%attr(755,root,root) %{_libdir}/kde4/kmailpart.so
%attr(755,root,root) %{_libdir}/kde4/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/libkleo.so
%attr(755,root,root) %{_libdir}/libkleo.so.4
%attr(755,root,root) %{_libdir}/libkleo.so.4.1.0
#%attr(755,root,root) %{_libdir}/kde4/kcm_kleopatra.so
#%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_application_octetstream.so
#%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_calendar.so
#%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_vcard.so
#%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_xdiff.so
#%attr(755,root,root) %{_libdir}/kde4/libkmailpart.so*
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.sh
%{_datadir}/apps/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-signature.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-transport.pl
#%{_datadir}/apps/kleopatra
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
#%{_datadir}/apps/kwatchgnupg
%{_datadir}/apps/libkleopatra
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_datadir}/config/libkleopatrarc
%{_datadir}/config.kcfg/kmail.kcfg
/usr/share/kde4/services/kcmkmailsummary.desktop
%{_datadir}/kde4/services/kmail_config_accounts.desktop
%{_datadir}/kde4/services/kmail_config_appearance.desktop
%{_datadir}/kde4/services/kmail_config_composer.desktop
%{_datadir}/kde4/services/kmail_config_identity.desktop
%{_datadir}/kde4/services/kmail_config_misc.desktop
%{_datadir}/kde4/services/kmail_config_security.desktop
/usr/share/kde4/services/kontact/kmailplugin.desktop
#%{_datadir}/services/kleopatra_config_appear.desktop
#%{_datadir}/services/kleopatra_config_dirserv.desktop
#%{_datadir}/services/kleopatra_config_dnorder.desktop
#%{_datadir}/servicetypes/dcopimap.desktop
#%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde4/KMail.desktop
#%{_desktopdir}/kde/kmail_view.desktop
# hidden (todo)
#%{_desktopdir}/kde/kleopatra_import.desktop
#%{_iconsdir}/*/*/apps/kmail.*
#%{_iconsdir}/*/*/apps/kmailcvt.*
#%{_iconsdir}/*/*/apps/kmaillight.*
# TODO
#%{_iconsdir}/*/*/apps/gpg.png
#%{_iconsdir}/*/*/apps/gpgsm.png
%{_iconsdir}/*/*x*/apps/kmail.png
%{_iconsdir}/*/scalable/apps/kmail.svgz
%{_iconsdir}/*/*x*/apps/kmailcvt.png
# kio-mbox
#%attr(755,root,root) %{_libdir}/kde4/kio_mbox.so
#%{_datadir}/services/mbox.protocol
# kio-sieve
#%attr(755,root,root) %{_libdir}/kde4/kio_sieve.so
#%{_datadir}/services/sieve.protocol
# ktnef
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_desktopdir}/kde4/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png
/usr/share/dbus-1/interfaces/org.kde.kmail.kmail.xml
/usr/share/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
/usr/share/dbus-1/interfaces/org.kde.kmail.mailcomposer.xml

%files knode
%defattr(644,root,root,755)
#-f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%attr(755,root,root) %{_libdir}/kde4/kcm_knode.so
#%attr(755,root,root) %{_libdir}/kde4/libknodepart.so*
%{_datadir}/apps/knode
#%{_datadir}/services/knewsservice.protocol
#%{_datadir}/services/knode_config_accounts.desktop
#%{_datadir}/services/knode_config_appearance.desktop
#%{_datadir}/services/knode_config_cleanup.desktop
#%{_datadir}/services/knode_config_identity.desktop
#%{_datadir}/services/knode_config_post_news.desktop
#%{_datadir}/services/knode_config_privacy.desktop
#%{_datadir}/services/knode_config_read_news.desktop
#%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png

%files knotes
%defattr(644,root,root,755)
#-f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%attr(755,root,root) %{_libdir}/kde4/knotes_kolab.so
%attr(755,root,root) %{_libdir}/kde4/knotes_local.so
%attr(755,root,root) %{_libdir}/kde4/knotes_xmlrpc.so
#%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knoteconfig.kcfg
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
#%dir %{_datadir}/services/kresources/knotes
#%{_datadir}/services/kresources/knotes/imap.desktop
#%{_datadir}/services/kresources/knotes/local.desktop
#%{_datadir}/services/kresources/knotes/knotes_xmlrpc.desktop
#%{_datadir}/services/kresources/knotes/kolabresource.desktop
#%{_datadir}/services/kresources/knotes_manager.desktop
#%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png

%files konsolekalendar
%defattr(644,root,root,755)
#-f konsolekalendar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
#%{_desktopdir}/kde/konsolekalendar.desktop
#%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png

%files korn
%defattr(644,root,root,755)
#-f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
#%{_libdir}/kconf_update_bin/korn-3-4-config_change
%{_datadir}/apps/kconf_update/korn-*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/korn-3-5*.pl
#%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png

%files kpilot
%defattr(644,root,root,755)
#-f kpilot.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/kpilot*
#%attr(755,root,root) %{_libdir}/kde4/conduit_address.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_doc.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_knotes.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_popmail.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_mal.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_sysinfo.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_time.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_todo.so
#%attr(755,root,root) %{_libdir}/kde4/conduit_vcal.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpilot.so
#%attr(755,root,root) %{_libdir}/kde4/kfile_palm.so
#%{_datadir}/apps/kconf_update/kpalmdoc.upd
%{_datadir}/apps/kconf_update/kpilot.upd
%{_datadir}/apps/kpilot
#%{_datadir}/config.kcfg/abbrowserconduit.kcfg
#%{_datadir}/config.kcfg/docconduit.kcfg
#%{_datadir}/config.kcfg/knotesconduit.kcfg
#%{_datadir}/config.kcfg/kpalmdoc.kcfg
%{_datadir}/config.kcfg/kpilot.kcfg
%{_datadir}/config.kcfg/kpilotlib.kcfg
#%{_datadir}/config.kcfg/malconduit.kcfg
%{_datadir}/config.kcfg/popmail.kcfg
#%{_datadir}/config.kcfg/sysinfoconduit.kcfg
%{_datadir}/config.kcfg/timeconduit.kcfg
%{_datadir}/config.kcfg/vcalconduitbase.kcfg
#%{_datadir}/services/kfile_palm.desktop
#%{_datadir}/services/kpilot_config.desktop
#%{_datadir}/services/*conduit.desktop
#%{_datadir}/servicetypes/kpilotconduit.desktop
#%{_desktopdir}/kde/kpalmdoc.desktop
#%{_desktopdir}/kde/kpilot*.desktop
#%{_iconsdir}/*/*/apps/kpalmdoc.png
%{_iconsdir}/[!l]*/*/*/kpilot*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakregatorprivate.so
/usr/lib/libkaddressbook.so.4
#%attr(755,root,root) %{_libdir}/libindex.so.*.*.*
#%attr(755,root,root) %{_libdir}/libgpgme++.so.*.*.*
#%attr(755,root,root) %{_libdir}/libgwsoap.so.*.*.*
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_groupdav.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkabc_groupwise.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkabc_newexchange.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_slox.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabckolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkcal.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_groupdav.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkcal_groupwise.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkcal_newexchange.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_resourcefeatureplan.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_slox.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcalkolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
%attr(755,root,root) %{_libdir}/libkgroupwarebase.so.*.*.*
%attr(755,root,root) %{_libdir}/libkgroupwaredav.so.*.*.*
%attr(755,root,root) %{_libdir}/libkholidays.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkitchensync.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkleopatra.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmailprivate.so
#%attr(755,root,root) %{_libdir}/libkmime.so.*.*.*
%attr(755,root,root) %{_libdir}/libknodecommon.so
%attr(755,root,root) %{_libdir}/libknotes_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libknoteskolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkocorehelper.so.*.*.*
%attr(755,root,root) %{_libdir}/libkode.so.*.*.*
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpgp.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkpimidentities.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
%attr(755,root,root) %{_libdir}/libksieve.so.4
%attr(755,root,root) %{_libdir}/libkslox.so.*.*.*
#%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
#%attr(755,root,root) %{_libdir}/libqopensync.so.*.*.*
#%attr(755,root,root) %{_libdir}/libqgpgme.so.*.*.*
#%{_datadir}/apps/libical
%{_datadir}/apps/libkdepim
%{_datadir}/apps/libkholidays
