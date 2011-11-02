Name:		texlive-leftidx
Version:	20070108
Release:	1
Summary:	Left and right subscripts and superscripts in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leftidx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Left and right subscripts and superscripts are automatically
raised for better fitting to the symbol they belong to.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
