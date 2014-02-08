# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/leftidx
# catalog-date 2007-01-08 22:21:56 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-leftidx
Version:	20070108
Release:	3
Summary:	Left and right subscripts and superscripts in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leftidx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070108-2
+ Revision: 753242
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070108-1
+ Revision: 718844
- texlive-leftidx
- texlive-leftidx
- texlive-leftidx
- texlive-leftidx

