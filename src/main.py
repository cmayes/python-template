# !/usr/bin/env python

from typing import List, Any

import sample
from sample.appcode import appfun
import sys
import argparse

"""
Module docstring.
"""

__author__ = 'cmayes'


# COMMANDS = ['daily']

def warning(*objs: Any) -> None:
    """Writes a message to stderr."""
    print("WARNING: ", *objs, file=sys.stderr)


def parse_cmdline(argv: List[str]):
    """
    Returns the parsed argument list and return code.
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = argparse.ArgumentParser()
    # parser.add_argument("-i", "--input_rates", help="The location of the input rates file",
    #                     default=DEF_IRATE_FILE, type=read_input_rates)
    # parser.add_argument("command", metavar='COMMAND',
    #                    help=f"The command to run (one of {','.join(COMMANDS)})")
    args = None
    try:
        args = parser.parse_args(argv)
    except IOError as e:
        warning("Problems reading file:", e)
        parser.print_help()
        return args, 2

    return args, 0


def main(argv=None) -> int:
    args, ret = parse_cmdline(argv)

    print("Hello World!", sample.__version__)
    print(appfun("1"))

    if ret != 0:
        return ret
    return 0  # success


if __name__ == '__main__':
    status = main()
    sys.exit(status)
