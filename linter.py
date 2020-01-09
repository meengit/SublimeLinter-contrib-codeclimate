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

    defaults = {
        'chdir': "${project}",
        'executable': 'codeclimate',
        'selector': (
            'source.css, '
            'source.go, '
            'source.haskall, '
            'source.java, '
            'source.javascript, '
            'source.php, '
            'source.python, '
            'source.ruby, '
            'source.scss, '
            'source.shell, '
            'text.html'
        )
    }
    regex = r'^(?P<line>\d+)(?:-\d+)?:\s(?P<message>.+)$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    word_re = None

    def cmd(self):
        """Construct a cmd to provide a relative path to 'codeclimate analyze'."""
        result = ['codeclimate', 'analyze', '-e', 'structure', '-e', 'duplication']
        relative_file_name = None
        for folder in self.view.window().folders():
            if self.filename.find(folder) == 0:
                relative_file_name = self.filename.replace(folder + '/', '')
        if relative_file_name == None:
            return result
        result.append(relative_file_name)
        persist.debug(result)
        return result
