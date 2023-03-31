Name:		texlive-leftidx
Version:	15878
Release:	2
Summary:	Left and right subscripts and superscripts in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leftidx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Left and right subscripts and superscripts are automatically
raised for better fitting to the symbol they belong to.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/leftidx/leftidx.sty
%doc %{_texmfdistdir}/doc/latex/leftidx/README
%doc %{_texmfdistdir}/doc/latex/leftidx/leftidx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/leftidx/Makefile
%doc %{_texmfdistdir}/source/latex/leftidx/leftidx.dtx
%doc %{_texmfdistdir}/source/latex/leftidx/leftidx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
