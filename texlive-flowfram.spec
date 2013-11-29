# revision 28238
# category Package
# catalog-ctan /macros/latex/contrib/flowfram
# catalog-date 2012-11-11 10:25:17 +0100
# catalog-license lppl
# catalog-version 1.14
Name:		texlive-flowfram
Version:	1.14
Release:	1
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
%{_texmfdistdir}/scripts/flowfram/flowfram.perl
%{_texmfdistdir}/tex/latex/flowfram/flowfram.sty
%doc %{_texmfdistdir}/doc/latex/flowfram/CHANGES
%doc %{_texmfdistdir}/doc/latex/flowfram/README
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguide.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguide.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/ffuserguideidx.ist
%doc %{_texmfdistdir}/doc/latex/flowfram/flowfram.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/egg.eps
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/egg.png
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-article.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-article.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-blanks.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-brochure.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-brochure.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-news.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-news.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-news2.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-news2.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-pages.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-pages.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-poster.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-poster.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-rot.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample-rot.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample1.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample1.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample2.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample2.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample3.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sample3.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sampleRL.pdf
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sampleRL.tex
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sheep.eps
%doc %{_texmfdistdir}/doc/latex/flowfram/samples/sheep.png
#- source
%doc %{_texmfdistdir}/source/latex/flowfram/flowfram.dtx
%doc %{_texmfdistdir}/source/latex/flowfram/flowfram.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
