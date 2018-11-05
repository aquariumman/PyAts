"""

   You can run the script in a terminal in two ways
   1) python hw1.py
   2) python hw1.py -num1 sume_number -num2 some_number

"""


from pyats.aetest import Testcase, main, test
import sys
import argparse
from calculation import add, divide



class My_test(Testcase):


    @test
    def div_test(self, num1, num2, steps):

        with steps.start('It is whole test step') as wstep:

            with wstep.start('Check to ZeroDivisionError') as zerodiv:
                try:
                    divide(num1, num2)
                except ZeroDivisionError:
                    self.passx(from_exception=ZeroDivisionError('We can not divide to zero!'))
                else:
                    self.passed('Test passed because another requirements is satisfied')

            with wstep.start('Check if the result is less then 0') as lesthen0:
                if divide(num1, num2) < 0:
                    self.skipped('Test is skipped because of the result of the divide(num1, num2) less then 0.')
                else:
                    self.passed('Test passed because another requirements is satisfied')


    @test
    def add_test(self, num1, num2):
        if add(num1, num2) < 0:
            self.skipped('Test is skipped because of the result of the add(num1, num2) less then 0.')
        else:
            self.passed('Test passed because another requirements is satisfied!')



if __name__=='__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=3)
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=0)

    args, unknown= parser.parse_known_args()

    main(num1=args.num1, num2=args.num2)


