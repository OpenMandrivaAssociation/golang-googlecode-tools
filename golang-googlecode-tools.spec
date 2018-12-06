# https://github.com/golang/tools
%global forgeurl        https://github.com/golang/tools
%global goipath         golang.org/x/tools
%global commit          ce871d178848e3eea1e8795e5cfb74053dde4bb9

Version:        0

%gometa -i

%global x_name          golang-golangorg-tools

%global go_arch %(go env GOHOSTARCH)
%global go_root %(go env GOROOT)

%global commands benchcmp callgraph digraph eg godex godoc goimports gorename gotype html2article present ssadump stringer goyacc

Name:           golang-googlecode-tools
Release:        23.1%{?dist}
Summary:        Supplementary tools and packages for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package -n golang-godoc
Summary:        Documentation tool for the Go programming language
Provides:       golang(%{goipath}/cmd/godoc) = %{version}-%{release}
Epoch:          1

%description -n golang-godoc
Godoc extracts and generates documentation for Go programs.
Obsoletes:      golang-godoc = 1.1.2

%package -n golang-gotype
Summary:        Go programming language source code analysis tool
Provides:       golang(%{goipath}/cmd/gotype) = %{version}-%{release}

%description -n golang-gotype
The gotype command does syntactic and semantic analysis of Go files and
packages like the front-end of a Go compiler. Errors are reported if the
analysis fails; otherwise gotype is quiet.


%package -n golang-html2article
Summary:        Tool for creating articles from HTML files
Provides:       golang(%{goipath}/cmd/html2article) = %{version}-%{release}
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)

%description -n golang-html2article
This program takes an HTML file and outputs a corresponding article file
in present format. See: code.google.com/p/go.tools/present

%package        callgraph
Summary:        Tool for reporting the call graph of a Go program
Provides:       golang(%{goipath}/cmd/callgraph) = %{version}-%{release}

%description    callgraph
Tool for reporting the call graph of a Go program.

%package        digraph
Summary:        Tool performs queries over unlabelled directed graphs represented in text form
Provides:       golang(%{goipath}/cmd/digraph) = %{version}-%{release}

%description    digraph
The digraph command performs queries over unlabelled directed graphs represented in text form.

%package        gorename
Summary:        Tool for reporting the call graph of a Go program
Provides:       golang(%{goipath}/cmd/gorename) = %{version}-%{release}

%description    gorename
Tool for reporting the call graph of a Go program.

%package        stringer
Summary:        Tool to automate the creation of methods that satisfy the fmt.Stringer interface
Provides:       golang(%{goipath}/cmd/stringer) = %{version}-%{release}

%description    stringer
tool to automate the creation of methods that satisfy the fmt.Stringer interface.

%package        godex
Summary:        Dump exported information for Go programming language
Provides:       golang(%{goipath}/cmd/godex) = %{version}-%{release}

%description    godex
%{summary}.

See http://godoc.org/code.google.com/p/go.tools/cmd/godex for more information.


%package        benchcmp
Summary:        Displays performance changes between benchmarks for the Go programming language
Provides:       golang(%{goipath}/cmd/benchcmp) = %{version}-%{release}

%description    benchcmp
%{summary}.

See http://godoc.org/code.google.com/p/go.tools/cmd/benchcmp for more information.


%package        eg
Summary:        Example-based refactoring for the Go programming language
Provides:       golang(%{goipath}/cmd/eg) = %{version}-%{release}

%description    eg
%{summary}.

See `eg -help` for more information.


%package        goimports
Summary:        Go programming language import line formatter
Provides:       golang(%{goipath}/cmd/goimports) = %{version}-%{release}

%description    goimports
%{summary}.

See http://godoc.org/code.google.com/p/go.tools/cmd/goimports for more information.


%package        present
Summary:        Slide and Article Presentation
Provides:       golang(%{goipath}/cmd/present) = %{version}-%{release}

%description    present
%{summary}.

See http://godoc.org/code.google.com/p/go.tools/cmd/present for more information.


%package        ssadump
Summary:        Display and interpreting SSA form of Go programs
Provides:       golang(%{goipath}/cmd/ssadump) = %{version}-%{release}

%description    ssadump
%{summary}.

%package        goyacc
Summary:        Goyacc is a version of yacc for Go
Provides:       golang(%{goipath}/cmd/goyacc) = %{version}-%{release}

%description    goyacc
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/goyacc for more information.

%package -n %{x_name}-devel
Summary:        Libraries of supplementary Go tools

BuildRequires:   golang-docs

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go tools libraries with golang.org/x/ imports.

%prep
%gosetup -q

%build
%gobuildroot
for cmd in %commands; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
install -d %{buildroot}%{_bindir}
for cmd in %commands; do
	install -p -m 755 _bin/$cmd %{buildroot}%{_bindir}
done

# source codes for building projects
files="$(find . -name 'testdata' -type d)"
%goinstall $files

%check
%gochecks -d go/gcimporter15

%files -n golang-godoc
%{_bindir}/godoc

%files -n golang-gotype
%{_bindir}/gotype

%files -n golang-html2article
%{_bindir}/html2article

%files    godex
%{_bindir}/godex

%files    callgraph
%{_bindir}/callgraph

%files    digraph
%{_bindir}/digraph

%files    gorename
%{_bindir}/gorename

%files    stringer
%{_bindir}/stringer

%files    eg
%{_bindir}/eg

%files    benchcmp
%{_bindir}/benchcmp

%files    goimports
%{_bindir}/goimports

%files    present
%{_bindir}/present

%files    ssadump
%{_bindir}/ssadump

%files    goyacc
%{_bindir}/goyacc

%files -n %{x_name}-devel -f devel.file-list
%license LICENSE PATENTS
%doc AUTHORS CONTRIBUTORS README.md

%changelog
* Wed May 09 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0-23.1.gitce871d1
- Package goyacc
  resolves: #1576672

* Wed Apr 04 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-22.1.gitce871d1
- Update to go spec 3.0

* Mon Feb 19 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-21.1.20180214gitce871d1
- Autogenerate some parts using the new macros

* Thu Feb 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-20.1.20180214gitce871d1
- Bump to upstream ce871d178848e3eea1e8795e5cfb74053dde4bb9 

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-15.1.git9deed8c
- Polish the spec file
  related: #1279381

* Wed Sep 07 2016 jchaloup <jchaloup@redhat.com> - 0-14.1.git9deed8c
- Bump to upstream 9deed8c6c1c89e0b6d68d727f215de8e851d1064
  resolves: #1373868

* Fri Aug 26 2016 jchaloup <jchaloup@redhat.com> - 0-13.1.git1cdaff4
- Include missing templates and static directories
  resolves: #1370456

* Fri Aug 05 2016 jchaloup <jchaloup@redhat.com> - 0-12.1.git1cdaff4
- Do not ship vet and cover binaries anymore, they are shipped via golang-bin
  resolves: #1268206

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-11.1.git1cdaff4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Apr 27 2016 jchaloup <jchaloup@redhat.com> - 0-10.1.git1cdaff4
- Bump to upstream 1cdaff4a02c554c9fb39dda0b56241c5f0949d91
  related: #1279381

* Wed Apr 13 2016 jchaloup <jchaloup@redhat.com> - 0-9.1.git997b354
- Run tests only on golang architectures

* Thu Mar 03 2016 jchaloup <jchaloup@redhat.com>
- Polish spec file
  don't check go/importer on ppc

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.1.git997b354
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 10 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-6.1.git997b354
- Update to golang_arches

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.0.git997b354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 jchaloup <jchaloup@redhat.com> - 0-5.0.git997b354
- Update a list of provided packages

* Thu Oct 15 2015 jchaloup <jchaloup@redhat.com> - 0-4.0.git997b354
- Bump to upstream 997b3545fd86c3a2d8e5fe6366174d7786e71278

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.0.hga7e14835e46b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 jchaloup <jchaloup@redhat.com> - 0-2.0.hga7e14835e46b
- Bump to a7e14835e46bb13da10fa8b9c9c5e7f2f378f568
- Add new tools presented in the commit
- Change import paths to new prefix schema golang.org/x/...
- Add new subpackage and keep the only one for back-compatibility
  resolves: #1199617

* Tue Aug 19 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-1.0.hgd32b5854c941
- updating to the current latest go.tools

* Tue Aug 19 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-0.9.hg17c8fe23290a
- setting an epoch for godoc to fix bz1099074

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.hg17c8fe23290a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Vincent Batts <vbatts@redhat.com> 0-0.7.hg17c8fe23290a
- fix bz1129281 and cleanup file ownership

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.hg17c8fe23290a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Vincent Batts <vbatts@redhat.com> 0-0.5.hg17c8fe23290a
- working on the arch dependencies
- clean up file ownership

* Thu Dec 05 2013 Vincent Batts <vbatts@redhat.com> 0-0.4.hg17c8fe23290a
- golang-godoc to obsolete the package from golang 1.1.2

* Tue Nov 12 2013 Vincent Batts <vbatts@redhat.com> 0-0.3.hg17c8fe23290a
- removing conflicting directory ownership

* Tue Nov 12 2013 Vincent Batts <vbatts@redhat.com> 0-0.2.hg17c8fe23290a
- adding subpackages for all available commands

* Sun Nov 10 2013 Vincent Batts <vbatts@redhat.com> 0-0.1.hg17c8fe23290a
- initial build
