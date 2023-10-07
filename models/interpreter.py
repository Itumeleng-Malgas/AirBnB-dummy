#!/usr/bin/python3
"""
This modules defines the application Interpreter, it extends the built-in cmd
module and uses its cmdloop to create the interactive command prompt

"""

# User defined modules
import models

# Built-in modules
import cmd
import sys

class Interpreter(cmd.Cmd):
    """ Interpreter class implementation """
    prompt = "> "

    def do_quit(self, args):
        """Exit the application."""
        return True

    def emptyline(self):
        """Take no action"""
        pass

# Inintialize Interpreter class
interpreter = Interpreter()
