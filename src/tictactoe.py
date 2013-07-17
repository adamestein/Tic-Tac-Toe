#!/usr/bin/python

"""DESCRIPTION OF SCRIPT
Interactively play the game of Tic-Tac-Toe against a human player and never lose.
"""

from optparse import OptionParser
import os
import sys

__author__    = "Adam Stein"
__copyright__ = "Copyright 2013"
__email__     = "adam@csh.rit.edu"
__version__   = "1.0"

def parse_args():
    """Parse command line options"""

    program = os.path.basename(sys.argv[0])

    parser = OptionParser(
        usage = "%s [-1] [-h] [--version]" % program,
        version = "%prog v" + __version__,
        description = """\
Interactively play the game of Tic-Tac-Toe against a human player and never lose.
"""
    )

    parser.add_option(
        "-1", "--humanstart",
        action = "store_true",
        default = False,
        dest = "humanstart",
        help = "Human makes the first move instead of the computer"
    )

    (options, args) = parser.parse_args()

    return (options, args)

if __name__ == "__main__":
    # Parse command line options
    (options, args) = parse_args()

    sys.exit(0)


