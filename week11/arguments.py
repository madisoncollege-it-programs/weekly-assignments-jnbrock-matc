#!/usr/bin/env python3

#Author: Joshua Brock
#Week 11: Argparse lab

import argparse
import sys

ag = argparse.ArgumentParser(description = "This is Josh's script")

#========= Arguments list: ====

ag.add_argument('-m', dest='Basic', help='Basic argument', required=False)
ag.add_argument('-i', '--integer', dest='intvar', help='Creates an integer value', metavar='[integer]', required=False, type=int, default=10)
ag.add_argument('-d', '--float', dest='fltvar', help='Creates a float value', metavar='[float]', required=False, type=float, default=10.0)
ag.add_argument('-s', '--string', dest='strvar', help='Creates a string value', metavar='[string]', required=False, type=str, default="lol")
ag.add_argument('-l', dest='listvar', help='Creates a list (space delimited)', metavar='[list]', required=False, default=[], nargs='+')
ag.add_argument('-t', '--set-true', dest='bool_t', help='Toggle from default False to True', required=False, action="store_true", default=False)
ag.add_argument('-f', '--set-false', dest='bool_f', help='Toggle from default True to False', required=False, action="store_false", default=True)
ag.add_argument('-v', '--version', action="version", help="Show's program's version", version="%(prog)s 1.0")



args = ag.parse_args()

#========= Print the values: ====

print(args.intvar)
print(args.strvar)
print(args.fltvar)
print(args.listvar)
