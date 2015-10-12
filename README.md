## reminder.py - py3status module

*reminder.py* functions as a reminder to do stuff when used with py3status / i3bar.

## Documentation
Prints the lines of a file to the status bar as a reminder.
                         
This module will read in an arbitrary text file and print out
the contents one by line, separated by a separator.
The intended use is to keep a file e.g. `~/.reminder` and to echo
important notes into it, so that it can be visible on your screen
at all times.

Configuration parameters:

* `reminder_file` : File to read in, defaults to ~/.reminder
* `separator` : How to separate the lines, defaults to |
* `cache_timeout` : How often to refresh the module

