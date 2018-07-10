Name:		texlive-flowfram
Version:	1.17
Release:	2
Summary:	Create text frames for posters, brochures or magazines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flowfram
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowfram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowfram.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowfram.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The flowfram package enables you to create frames in a document
such that the contents of the document environment flow from
one frame to the next in the order in which they were defined.
This is useful for creating posters or magazines, indeed any
form of document that does not conform to the standard one or
two column layout.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/flowfram
%{_texmfdistdir}/tex/latex/flowfram
%doc %{_texmfdistdir}/doc/latex/flowfram
#- source
%doc %{_texmfdistdir}/source/latex/flowfram

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
