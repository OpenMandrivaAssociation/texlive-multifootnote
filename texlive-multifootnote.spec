Name:		texlive-multifootnote
Version:	63456
Release:	2
Summary:	Multiple numbers for the same footnote
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multifootnote
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multifootnote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multifootnote.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides several commands for generating footnotes
with multiple numbers (resp. marks).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/multifootnote
%doc %{_texmfdistdir}/doc/latex/multifootnote

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
