%global tl_name leftidx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Left and right subscripts and superscripts in math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/leftidx
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leftidx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Left and right subscripts and superscripts are automatically raised for
better fitting to the symbol they belong to.

