#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class ALXCommand(cmd.Cmd):
    """Class for the command interpreter."""
    pass


if __name__ == '__main__':
    ALXCommand().cmdloop()
