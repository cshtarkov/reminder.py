"""
Prints the lines of a file to the status bar as a reminder

This module will read in an arbitrary text file and print out
the contents one by line, separated by a separator.
The intended use is to keep a file e.g. ~/.reminder and to echo
important notes into it, so that it can be visible on your screen
at all times.
Click the component to go to the next set of tasks immediately.

Configuration parameters:
    - reminder_file :   File to read in, defaults to ~/.reminder
    - separator     :   How to separate the lines, defaults to |
    - cache_timeout :   How often to refresh the module, defaults to 60 (seconds)
    - max_lines     :   How many lines to display on the screen at one time, defaults to 2.
                        I've found that 2 is a good value for a 1366x768 screen, you will
                        probably want to increase it for larger screens.

@author Christian Shtarkov christian@shtarkov.net
@license MIT
"""

from os.path import expanduser, join
from time import time

class Py3status:
    reminder_file = join(expanduser("~"), ".reminder")
    separator = "|"
    cache_timeout = 60
    max_lines = 2

    _contents = []
    _last_index = 0

    def _load_file(self):
        with open(self.reminder_file) as f:
            self._contents = list(map(lambda x: x.rstrip(), f.readlines()))
        # Validate index
        if self._last_index >= len(self._contents): self._last_index = 0

    def __init__(self):
        self._load_file()

    def kill(self, i3s_output_list, i3s_config):
        pass

    def on_click(self, i3s_output_list, i3s_config, event):
        self.put_reminder(i3s_output_list, i3s_config)

    def put_reminder(self, i3s_output_list, i3s_config):
        # Reload file on every cache timeout
        self._load_file()

        # TODO: Error handling when missing file
        if len(self._contents) == 0:
            return {}

        full_text = ""
        # Upper bound is either the next `max_lines` lines or the end of the file.
        lower = self._last_index
        upper = self._last_index + self.max_lines if self._last_index + self.max_lines < len(self._contents) else len(self._contents)
        # Join the string
        for line in self._contents[lower:upper]:
            full_text = str.format("{0} {2} {1}", full_text, line, self.separator)
            self._last_index = upper
            if self._last_index == len(self._contents): self._last_index = 0
        # Remove initial separator
        self._full_text = full_text[3:]
        response = {
            'full_text': self._full_text,
            'cached_until': time() + self.cache_timeout
        }
        return response

if __name__ == "__main__":
    from time import sleep
    r = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    while True:
        print(r.put_reminder([], config))
        sleep(1)

