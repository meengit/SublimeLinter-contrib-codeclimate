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
import logging
import os
from SublimeLinter.lint import Linter, util


logger = logging.getLogger('SublimeLinter.plugin.eslint')


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
    regex = r'^(?P<line>\d+)(?:-\d+)?:\s(?P<message>.+)$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    word_re = None

    def cmd(self):
        """Set command and run 'codeclimate analyze'."""
        abs_path = self.filename
        working_dir = self.get_working_dir()

        msg = 'You try to lint the file %s from outside of SublimeText\'s ' \
              'working directory (%s), which is not supported by this ' \
              'SublimeLinter plugin at this time. You can do either:\n' \
              '* You open the directory containing the current file in' \
              'a new window. You may have to add a customized ' \
              '`.codeclimate.yml` configuration to that directory ' \
              'as well;\n' \
              '* You change the working directory of the linter plugin in ' \
              ' the global or the Project\'s settings;\n' \
              '* You disable the linter plugin in the global or the ' \
              'Project\'s settings.\n\n' \
              'Please visit https://github.com/codeclimate/' \
              'SublimeLinter-contrib-codeclimate for examples.' \
              '\n' % (abs_path, working_dir)

        if not (abs_path.startswith(os.path.abspath(working_dir) + os.sep)):
            logger.info(msg)
            return None

        file = os.path.relpath(abs_path, working_dir)
        return ['codeclimate', 'analyze', '${args}', file, '${xoo}']
