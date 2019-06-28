Summary:	Opus codec tools
Name:		opus-tools
Version:	0.2
Release:	1
License:	BSD
Group:		Sound
Url:		http://opus-codec.org/
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libopusenc)

%description
This packages provides various tools to decode & encode files with the Opus
codec.
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*
