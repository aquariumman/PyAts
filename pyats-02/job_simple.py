import sys
import argparse
from pyats.easypy import run

def main():
    parser = argparse.ArgumentParser(description=("Simple parser"))
    parser.add_argument('-a', dest='a', type=float, required=False, default=1, help="we need give a value for testing")
    parser.add_argument('-b', dest='b', type=float, required=False, default=1, help="we need give a value for testing")
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    print('args : ', args)
    run(testscript='add_func.py', a=args.a, b=args.b)
    run(testscript='div_func.py', a=args.a, b=args.b)
    run(testscript='mult_func.py', a=args.a, b=args.b)
    run(testscript='substract_func.py', a=args.a, b=args.b)
