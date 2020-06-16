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

import re
from SublimeLinter.lint import Linter, util


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

    root = None
    path = None

    def cmd(self):
        """Set working directory and run 'codeclimate analyze'."""
        if self.context.get('project_root') is None:
            self.defaults['chdir'] = '${folder}' \
                if self.context.get('folder') is not None \
                else '${file_path}'

        root = re.search(r"\{(\w+)\}", self.defaults['chdir']).group(1)
        path = self.filename.replace(self.context.get(root) + '/', '')
        return ['codeclimate', 'analyze', path]
