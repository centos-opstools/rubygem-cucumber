%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name cucumber

Summary:        Tool to execute plain-text documents as functional tests
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        2.4.0
Release:        1%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://cukes.info
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildArch:      noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Requires: rubygem(builder) >= 2.1.2
Requires: rubygem(cucumber-core) >= 1.5.0
Requires: rubygem(cucumber-core) < 1.6
Requires: rubygem(cucumber-wire) >= 0.0.1
Requires: rubygem(cucumber-wire) < 0.1
Requires: rubygem(diff-lcs) >= 1.1.3
Requires: rubygem(gherkin) >= 4.0
Requires: rubygem(gherkin) < 5
Requires: rubygem(multi_json) >= 1.7.5
Requires: rubygem(multi_json) < 2.0
Requires: rubygem(multi_test) >= 0.1.2
# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
%{?scl:Requires: %{?scl_prefix}runtime}

%description
Cucumber lets software development teams describe how software should behave
in plain text. The text is written in a business-readable domain-specific
language and serves as documentation, automated tests and development-aid.

%prep
%setup -n %{pkg_name}-%{version} -q -c  -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

rm -f $RPM_BUILD_ROOT%{gem_instdir}/.ruby-gemset
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.ruby-version
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.yardopts
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.gitattributes
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.gitmodules
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/.github
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.coveralls.yml
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.yardopts
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.travis.yml
rm -f $RPM_BUILD_ROOT%{gem_instdir}/Gemfile.lock
rm -f $RPM_BUILD_ROOT%{gem_instdir}/.rspec
find $RPM_BUILD_ROOT%{gem_instdir} -type f | grep '.gitignore' | xargs rm -f

# Remove zero-length documentation files
find $RPM_BUILD_ROOT%{gem_docdir} -empty -delete

%files
%defattr(-,root,root,-)
%{_bindir}/cucumber
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/features
%{gem_instdir}/gem_tasks
%{gem_libdir}
%{gem_instdir}/spec
%{gem_instdir}/cucumber.yml
%{gem_instdir}/cucumber.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/examples
%doc %{gem_docdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/Gemfile
%{gem_cache}
%{gem_spec}

%changelog
* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 2.4.0-1
- update to 2.4.0

* Wed Feb 24 2016 Pavel Valena <pvalena@redhat.com> - 1.3.18-4
- Add scl macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.18-1
- 1.3.18
  ref: https://github.com/cucumber/cucumber/issues/781

* Wed Jun 18 2014 Josef Stribny <jstribny@redhat.com> - 1.3.15-1
- Update to cucumber 1.3.15

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Drop useless build requires.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.2.1-1
- Update cucumber to version 1.2.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.9-1
- Update cucumber to version 1.1.9

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.1-1
- update to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Michal Fojtik <mfojtik@redhat.com> - 0.10.0-1
- Version bump

* Mon Sep 27 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-4
- Fixed JSON version again

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-3
- Fixed JSON version

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-2
- Fixed gherkin version in dependency list

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-1
- Version bump to match upstream
- Fixed dependency issue with new gherkin package

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-4
- Fixed JSON version

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-3
- Removed JSON patch (JSON updated in Fedora)

* Sun Aug 01 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-2
- Patched Rakefile and replaced rspec beta version dependency
- Patched Rakefile and downgraded JSON dependency

* Wed Jun 30 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-1
- Newer release

* Sun Oct 18 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.2-1
- Newer release

* Mon Oct 12 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.0-1
- Newer release

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-2
- Use geminstdir macro where appropriate
- Do not move examples around
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-1
- Package generated by gem2rpm
- Move examples into documentation
- Remove empty files
- Fix up License
