%global packname  tree
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.35
Release:          2
Summary:          Classification and regression trees

Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/tree_1.0-35.tar.gz
Requires:         R-grDevices R-graphics R-stats 
Requires:         R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-grDevices R-graphics R-stats
BuildRequires:    R-MASS 

%description
Classification and Regression Trees.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
# %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po

