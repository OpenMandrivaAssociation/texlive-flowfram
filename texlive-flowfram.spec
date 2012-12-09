# revision 16806
# category Package
# catalog-ctan /macros/latex/contrib/flowfram
# catalog-date 2010-01-23 14:06:53 +0100
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-flowfram
Version:	1.13
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
%{_texmfdistdir}/tex/latex/flowfram/flowfram.sty
%doc %{_texmfdistdir}/doc/latex/flowfram/CHANGES
%doc %{_texmfdistdir}/doc/latex/flowfram/README
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguide.html
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguide.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguide.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/flowfram.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/brochure.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/brochure.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/egg.eps
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/egg.png
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/news.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/news.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/news2.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/news2.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/poster.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/poster.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sheep.eps
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sheep.png
#- source
%doc %{_texmfdistdir}/source/latex/flowfram/flowfram.dtx
%doc %{_texmfdistdir}/source/latex/flowfram/flowfram.ins
%doc %{_texmfdistdir}/source/latex/flowfram/flowfram.perl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.13-2
+ Revision: 751935
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.13-1
+ Revision: 718464
- texlive-flowfram
- texlive-flowfram
- texlive-flowfram
- texlive-flowfram

