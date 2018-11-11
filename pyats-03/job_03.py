import sys
import argparse
from pyats import easypy



def	main():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-user_host', type=str,
    #                     dest='hostname',
    #                     required=True,
    #                     help='We need hostname of the device we are connecting from')
    parser.add_argument('-user_vm',
                        type=str,
                        dest='username_vm',
                        required=False,
                        default='pyast',
                        help='We need user name of the device we are connecting to')

    parser.add_argument('-ip_vm',
                        type=str,
                        dest='ip_vm',
                        required=False,
                        default='192.168.242.44',
                        help='We need ip of the device we are connecting to')
    parser.add_argument('-filename',
                        type=str,
                        dest='filename',
                        required=False,
                        default='test.test',
                        help='We need a name for our testfile')

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    easypy.run(testscript='test_script_03.py',
               # hostname=args.hostname,
               username_vm=args.username_vm,
               ip_vm=args.ip_vm,
               filename=args.filename)
