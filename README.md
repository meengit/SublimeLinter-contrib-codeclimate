SublimeLinter-contrib-codeclimate
=================================

[![Build Status](https://travis-ci.com/meengit/SublimeLinter-contrib-codeclimate.svg?branch=main)](https://travis-ci.com/meengit/SublimeLinter-contrib-codeclimate)

This SublimeLinter plugin provides an interface to the [codeclimate CLI][codeclimate]. Code Climate supports a variety of languages through standardized Docker images known as static analysis engines.

## Dependencies

**SublimeLinter** and the **codeclimate CLI** must be installed to use this plugin. 

* If you haven't installed **SublimeLinter** yet, please follow the instructions [here][sublimelinter-installation].
* If you haven't installed the **codeclimate CLI** yet, please follow the instructions [here][codeclimate].

It is recommended to add the `codeclimate` executable to your `$PATH` variable. You can find some [help for this step][sublimelinter-troubleshooting] in the SublimeLinter documentation. Besides, it is also possible to set a custom path to the `codeclimate` executable in the SublimeLinter settings (*[see Settings](#settings)*).

## Plugin installation

Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available.

Within Sublime Text, bring up the [Command Palette][cmd] and type *install*. Select `Package Control: Install Package` and wait a few seconds while Package Control fetches the list of the available plugins.

When the plugin list appears, type *codeclimate* and select `SublimeLinter-contrib-codeclimate`.

## How it works

* If the opened folder in SublimeText contains a `.codeclimate.yml` configuration file in its root, `codeclimate` will recognize this file's settings. Otherwise, it will automatically run the default inspections of `structure` and `duplication`.
* If you have a `.codeclimate.yml` configuration file in a different folder, you can set SublimeLinter's `working_dir` setting (*[see Settings](#settings)*).

There are some use cases SublimeLinter can't run `codeclimate`. For instance: if you open a single file beside already opened folders in the same view. In that case, the linter will fail and print a warning because the single file has no working directory (which is required by `codeclimate`).

## Limitations

***This plugin may cause performance problems if many projects and documents are open in SublimeText.***

I recommend deactivating the plugin globally by default and then activating it depending on your opened folders or as part of a SublimeText Project. 

## Settings

To see how SublimeLinter's settings works, please see [settings][sublimelinter-settings] and (generic) [linter settings][sublimelinter-linter-settings] in SublimeLinter's documentation.

### Examples

Here I try to give you some examples of everyday use cases.

### Disable/enable this plugin

```json
{
  "linters": {
    "codeclimate": {
      "disable": true
    }
  }
}
```

For SublimeLinter's global settings, go to *Preferences > Package Settings > SublimeLinter > Settings*.

#### Set executable

You can set the path to the `codeclimate` executable in the global SublimeLinter settings or your project settings:

```json
{
  "linters": {
    "codeclimate": {
      "executable": "/usr/local/bin/codeclimate"
    }
  }
}
```

#### Pass arguments to the codeclimate CLI

If you want to ignore the configuration of a `.codeclimate.yml`, for instance, to run a subset of codeclimate engines, you can set linter arguments in the global SublimeLinter settings or your project settings:

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

#### Customize the working directory

Suppose you use a `.codeclimate.yml`-configuration file. In that case, the `codeclimate` CLI needs to be executed in your configuration file's directory. Otherwise, it can't detect your configuration and runs only the default analyzes.

SublimeLinter takes the current file's root folder in SublimeText's sidebar as the working directory for executing its linter commands. You can change this behavior by setting the working directory of execution:

```json
{
  "linters": {
    "codeclimate": {
      "working_dir": "/path/to/working/dir"
    }
  }
}
```

*Hint: Make sure the working directory is in the path of the file you want to lint!*

#### Set associated file types

You can set the associated file types in the global SublimeLinter settings or your project settings:

```json
{
  "linters": {
    "codeclimate": {
      "selector": "source.php, source.python"
    }
  }
}
```

> *To find out what selector to use for given file type, use the "Tools > Developer > Show Scope Name" menu entry. ([SublimeLinter documenation][sublimelinter-selector])*

## Contributing

If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Do your changes on a separate topic branch created from the latest `main`.
3. Commit and push the topic branch.
4. Make a pull request.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you very much for helping out!

## License

[MIT, see LICENSE][license]

[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[codeclimate]: https://github.com/codeclimate/codeclimate
[docs]: http://sublimelinter.readthedocs.org
[license]: https://github.com/meengit/SublimeLinter-contrib-codeclimate/blob/main/LICENSE
[pc]: https://sublime.wbond.net/installation
[sublimelinter-installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[sublimelinter-linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[sublimelinter-selector]: http://www.sublimelinter.com/en/stable/linter_settings.html#selector
[sublimelinter-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[sublimelinter-troubleshooting]: http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable
