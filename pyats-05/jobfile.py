import sys
import argparse
from	pyats.topology.loader	import	load
from pyats.easypy import run



def main():
    run(testscript='rabbit.py')
