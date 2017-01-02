#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Noah Davis
# Copyright (c) 2016 Noah Davis
#
# License: MIT
#

"""This module exports the Codeclimate plugin class."""

from SublimeLinter.lint import Linter, util, persist


class Codeclimate(Linter):
    """Provides an interface to codeclimate."""

    syntax = (
        'ruby on rails',
        'ruby',
        'javascript',
        'python',
        'go',
        'html',
        'css',
        'markdown',
        'php',
        'haskall',
        'java',
        'shellscript'
    )
    executable = "codeclimate"
    regex = r'^(?P<line>\d+)(?:-\d+)?:\s(?P<message>.+)$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {
        'chdir': "${project}"
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        """Construct a cmd to provide a relative path to 'codeclimate analyze'."""
        result = [self.executable_path, 'analyze']
        relative_file_name = None
        for folder in self.view.window().folders():
            if self.filename.find(folder) == 0:
                relative_file_name = self.filename.replace(folder + '/', '')
        result.append(relative_file_name)
        persist.debug(result)
        return result
