SublimeLinter-contrib-codeclimate
=================================

> Please note: This was originally a fork of [codeclimate/SublimeLinter-contrib-codeclimate][codeclimate-origin] to make it compatible for SublimeLinter 4.

[![Build Status](https://travis-ci.org/codeclimate/SublimeLinter-contrib-codeclimate.svg?branch=master)](https://travis-ci.org/codeclimate/SublimeLinter-contrib-codeclimate)

This linter plugin for [SublimeLinter][docs] provides an interface to [codeclimate](https://github.com/codeclimate/codeclimate). Code Climate supports a variety of languages through standardized Docker images known as static analysis engines.

## Installation
SublimeLinter 4 must be installed in order to use this plugin. If SublimeLinter 4 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `codeclimate` is installed on your system. Please see the `codeclimate` documentation, specifically [Prerequisites](https://github.com/codeclimate/codeclimate#prerequisites) and [Installation](https://github.com/codeclimate/codeclimate#installation)

### Linter configuration
In order for `codeclimate` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in ["Finding a linter executable"](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through "Validating your PATH" in the documentation.

Once you have installed and configured `codeclimate`, you can proceed to install the SublimeLinter-contrib-codeclimate plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

When the plugin list appears, type `codeclimate`. Among the entries you should see `SublimeLinter-contrib-codeclimate`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## How it works

The linter is first looking for a SublimeText Project. If a `*.sublime-project` is given, it executes `codeclimate` in the project root directory. If no project is given, it tries to execute `codeclimate` in the first opened folder of the folder pane.

If the SublimeText project folder or the first opened folder in the folder pane contains a `.codeclimate.yml` configuration file, `codeclimate` will recognise its settings. If no configuration file can be evaluated, `codeclimate` will automatically run the defaults of `structure` and `duplication` at this time.

## Linter Configuration

To specify the path to executable, please use the SublimeLinter settings:

```json
{
  "linters": {
    "executable": "/usr/local/bin/codeclimate"
  }
}
```


If your `.codeclimate.yml` does not live in the project root folder, you can set also the `working_dir` of SublimeLinter:

```json
{
  "working_dir": "${folder:$file_path}"
}
```

If you want to ignore the configuration in a `.codeclimate.yml`, for instance, to run a subset of codeclimate engines, you can configure this by setting the linter arguments either in the global SublimeLinter settings or in your project settings. In the global settings, this could look like this:

```json
{
  "linters": {
    "codeclimate": {
      "args": [
          "-e",
          "structure",
          "-e",
          "duplication"
        ]
    }
  }
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.
5. Be patient.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[codeclimate-origin]: https://github.com/codeclimate/SublimeLinter-contrib-codeclimate
[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
