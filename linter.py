#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Noah Davis
# Copyright (c) 2016 Noah Davis
#
# Updated by Schuyler Jager & Andreas for SublimeLinter 4
# Copyright (c) 2020 Schuyler Jager & Andreas
# License: MIT
#

"""This module exports the Codeclimate plugin class."""
import os
from SublimeLinter.lint import Linter, PermanentError, util


class Codeclimate(Linter):
    """Provides an interface to codeclimate."""
    defaults = {
        'selector': (
            'source.css, '
            'source.go, '
            'source.haskell, '
            'source.java, '
            'source.javascript, '
            'source.js, '
            'source.php, '
            'source.python, '
            'source.ruby, '
            'source.scss, '
            'source.shell, '
            'text.html'
        )
    }

    regex = r'^== ((?P<filename>.*)(?= \(\d+ issue\) ==))( \(\d+ issue\) ==\n(?P<line>\d+))(?:-\d+)?:\s(?P<message>.+)$'
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    word_re = None

    def cmd(self):
        """Set command and run 'codeclimate analyze'."""
        abs_path = self.filename
        working_dir = self.get_working_dir()

        msg = 'The file \'%s\' is not part of the working dir (%s). ' \
              'Please see the Linter\'s README.md to get further ' \
              'instructions.' % (abs_path, working_dir)

        if not (abs_path.startswith(os.path.abspath(working_dir) + os.sep)):
            self.notify_unassign()
            raise PermanentError(msg)

        file = os.path.relpath(abs_path, working_dir)
        return ['codeclimate', 'analyze', '${args}', file, '${xoo}']
