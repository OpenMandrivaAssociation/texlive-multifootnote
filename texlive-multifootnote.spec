%global tl_name multifootnote
%global tl_revision 70745

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Multiple numbers for the same footnote
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multifootnote
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multifootnote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multifootnote.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides several commands for generating footnotes which
correspond to multiple footnote numbers (resp. marks). In some cases,
you may wish for certain footnotes to correspond to several places in
your text. The traditional solution usually involves writing the same
footnote mark multiple times at the corresponding places. However, this
approach makes it difficult to see at once how many times a footnote has
been referred to. Therefore, the current package proposes another
method: writing the footnote marks in linear order, and allowing a
footnote text to match several of these marks.

