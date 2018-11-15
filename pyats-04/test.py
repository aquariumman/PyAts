from pyats.aetest import main, Testcase, setup, loop, test
import sys
import argparse

""" 
Run this test with commands:

python test.py --letter a
python test.py --letter b
python test.py --letter c

"""

mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


class Test(Testcase):

    @setup
    def setup(self, letter):
        if letter in mapping.keys():
            loop.mark(self.check, uids=mapping[letter])
        else:
            self.aborted('wrong key was given!')

    @test
    def check(self, section):
        print(f"Current section: {section.uid}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--letter', type=str, dest='letter', required=True,
                        help='We need to specify key with --letter one of [a, b, c]')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(letter=args.letter)

