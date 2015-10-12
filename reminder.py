"""
Prints the lines of a file to the status bar as a reminder

This module will read in an arbitrary text file and print out
the contents one by line, separated by a separator.
The intended use is to keep a file e.g. ~/.reminder and to echo
important notes into it, so that it can be visible on your screen
at all times.

Configuration parameters:
    - reminder_file : File to read in, defaults to ~/.reminder
    - separator : How to separate the lines, defaults to |
    - cache_timeout : How often to refresh the module

@author Christian Shtarkov christian@shtarkov.net
@license MIT
"""

from os.path import expanduser, join
from time import time

class Py3status:
    reminder_file = join(expanduser("~"), ".reminder")
    cache_timeout = 5

    def __init__(self):
        pass

    def kill(self, i3s_output_list, i3s_config):
        pass

    def put_reminder(self, i3s_output_list, i3s_config):
        with open(self.reminder_file) as f:
            full_text = ""
            contents = f.readlines()
            for line in contents:
                line = line.rstrip()
                full_text = str.format("{0} | {1}", full_text, line)
            full_text = full_text[3:]
            response = {
                'full_text': full_text,
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

