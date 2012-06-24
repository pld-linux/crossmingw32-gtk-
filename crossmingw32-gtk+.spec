%define		realname	gtk+
%define		snap	20030115
Summary:	The Gimp Toolkit - Ming32 cross version
Summary(cs):	Sada n�stroj� pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(es):	Conjunto de herramientas Gimp
Summary(fi):	Gimp-ty�kalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit - wersja skro�na dla Ming32
Summary(pt_BR):	Kit de ferramentas Gimp
Summary(tr):	Gimp ToolKit aray�z kitapl���
Name:		crossmingw32-%{realname}
Version:	1.3.0
Release:	0.%{snap}.2
License:	LGPL
Group:		Libraries
Source0:	http://www.gimp.org/~tml/gimp/win32/gtk+-dev-%{version}-%{snap}.zip
# Source0-md5:	56eff0fac89da0166b71901813775e86
URL:		http://www.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	crossmingw32-glib2 >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs
Knihovny X p�vodn� psan� pro GIMP, kter� nyn� pou��v� tak� �ada jin�ch
program�.

%description -l da
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de
Die X-Libraries, die urspr�nglich f�r GIMP geschrieben wurden und
mittlerweile f�r eine ganze Reihe anderer Programme benutzt werden.

%description -l fr
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
k�ytet��n nyt my�s useissa muissakin ohjelmissa.

%description -l it
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl
GTK+, kt�ra to biblioteka sta�a si� podstaw� programu Gimp, zawiera
funkcje do tworzenia graficznego interfejsu u�ytkownika pod X Window.
By�a tworzona z za�o�eniem �eby by�a ma�a, efektywna i wygodna. GTK+
jest napisane w C z podej�ciem zorientowanym bardzo obiektowo. GDK
(cz�� GTK+) jest warstw� po�redni� pomi�dzy Xlib i reszt� toolkitu
zapewniaj�c� prac� niezale�nie od g��bi koloru (ilo�ci bit�w na
piksel). GTK (druga cz�� GTK+) jest natomiast ju� zbiorem r�nego
rodzaju kontrolek s�u��cych do tworzenia interfejsu u�ytkownika.

%description -l pt_BR
Bibliotecas X originalmente escritas para o GIMP, que agora est�o
sendo tamb�m usadas por v�rios outros programas.

%description -l tr
Ba�lang��ta GIMP i�in yaz�lm�� X kitapl�klar�. �u anda ba�ka
programlarca da kullan�lmaktad�r.

%prep
install -d gtk
cd gtk && rm * -rf ; unzip %{SOURCE0} && cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}

cp -rf gtk/* $RPM_BUILD_ROOT%{arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*
%{arch}/lib/*
