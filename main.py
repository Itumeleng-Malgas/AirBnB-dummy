#!/usr/bin/python3
"""
This module is the entry point of the application.

"""
import models.interpreter as cmd
import sys

if __name__ == "__main__":
    if not sys.stdin.isatty():

        # Read commands from stdin (pipe)
        for line in sys.stdin:
            cmd.onecmd(line.strip())

    else:
        # Start the interactive cmdloop
        cmd.cmdloop()
