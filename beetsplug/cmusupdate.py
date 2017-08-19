# Copyright 2017, Nate Bogdanowicz
import os.path
import subprocess as sp
from beets import config
from beets.plugins import BeetsPlugin


class CmusUpdatePlugin(BeetsPlugin):
    def __init__(self):
        super(CmusUpdatePlugin, self).__init__()
        self.register_listener('database_change', self.on_db_change)

    def on_db_change(self, lib, model):
        self.register_listener('cli_exit', self.update)

    def update(self, lib):
        self._log.info('Adding music to cmus')
        music_dir = os.path.expanduser(config['directory'].get())
        command = f'add -l {music_dir}'
        sp.call(['cmus-remote', '-C', command])
