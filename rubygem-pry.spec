#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-pry
Version  : 0.10.3
Release  : 9
URL      : https://rubygems.org/downloads/pry-0.10.3.gem
Source0  : https://rubygems.org/downloads/pry-0.10.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-pry-bin
BuildRequires : ruby
BuildRequires : rubygem-coderay
BuildRequires : rubygem-rdoc

%description
[![Build Status](https://img.shields.io/travis/pry/pry.svg)](https://travis-ci.org/pry/pry)
[![Code Climate](https://img.shields.io/codeclimate/github/pry/pry.svg)](https://codeclimate.com/github/pry/pry)
[![Inline docs](http://inch-ci.org/github/pry/pry.svg)](http://inch-ci.org/github/pry/pry)

%package bin
Summary: bin components for the rubygem-pry package.
Group: Binaries

%description bin
bin components for the rubygem-pry package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n pry-0.10.3
gem spec %{SOURCE0} -l --ruby > rubygem-pry.gemspec

%build
gem build rubygem-pry.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
pry-0.10.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/pry-0.10.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/README.md
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/bin/pry
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/code.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/code/code_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/code/code_range.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/code/loc.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/code_object.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/color_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/command_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/amend_line.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/bang.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/bang_pry.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cat.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cat/abstract_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cat/exception_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cat/file_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cat/input_expression_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/cd.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/change_inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/change_prompt.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/code_collector.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/disable_pry.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/disabled_commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/easter_eggs.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/edit.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/edit/exception_patcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/edit/file_and_line_locator.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/exit.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/exit_all.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/exit_program.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/find_method.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/fix_indent.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/gem_cd.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/gem_install.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/gem_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/gem_open.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/gist.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/help.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/hist.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/import_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/install_command.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/jump_to.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/list_inspectors.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/list_prompts.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/globals.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/grep.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/instance_vars.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/interrogatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/jruby_hacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/local_names.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/local_vars.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/ls_entity.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/methods_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ls/self_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/nesting.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/play.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/pry_backtrace.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/pry_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/raise_up.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/reload_code.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/reset.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/ri.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/save_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/shell_command.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/shell_mode.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/show_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/show_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/show_input.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/show_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/simple_prompt.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/stat.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/switch_to.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/toggle_color.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/watch_expression.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/watch_expression/expression.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/whereami.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/commands/wtf.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/config/behavior.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/config/convenience.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/config/default.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/core_extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/editor.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/exceptions.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/base_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/command_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/documentation_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/options_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/table.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/helpers/text.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/history.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/history_array.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/hooks.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/indent.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/input_completer.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/input_lock.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/last_exception.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/method.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/method/disowned.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/method/patcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/method/weird_method_locator.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/module_candidate.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/object_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/output.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/pager.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/plugins.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/prompt.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/pry_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/pry_instance.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/rbx_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/repl.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/repl_file_loader.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/rubygem.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/terminal.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/pry-0.10.3/lib/pry/wrapped_module.rb
/usr/lib64/ruby/gems/2.3.0/specifications/pry-0.10.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/pry
