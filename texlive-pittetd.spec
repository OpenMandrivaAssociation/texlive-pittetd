Name:		texlive-pittetd
Version:	15878
Release:	2
Summary:	Electronic Theses and Dissertations at Pitt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pittetd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pittetd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pittetd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pittetd.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class for theses and dissertations. Provides patch
files that enable pittetd to use files prepared for use with
the pittdiss or pitthesis classes. The manual provides a
detailed guide for users who wish to use the class to prepare
their thesis or dissertation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pittetd/pitetd10.clo
%{_texmfdistdir}/tex/latex/pittetd/pitetd11.clo
%{_texmfdistdir}/tex/latex/pittetd/pitetd12.clo
%{_texmfdistdir}/tex/latex/pittetd/pittetd.cls
%doc %{_texmfdistdir}/doc/latex/pittetd/achicago.pit
%doc %{_texmfdistdir}/doc/latex/pittetd/pittdiss.pit
%doc %{_texmfdistdir}/doc/latex/pittetd/pittetd.pdf
%doc %{_texmfdistdir}/doc/latex/pittetd/pitthesis.pit
#- source
%doc %{_texmfdistdir}/source/latex/pittetd/pittetd.dtx
%doc %{_texmfdistdir}/source/latex/pittetd/pittetd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
