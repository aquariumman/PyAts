from pyats.aetest import Testcase, main, test
from myfunctions import mult

class mult_test_cl(Testcase):
    @test
    def mult_test(self, a, b):
        if mult(a, b) < 0:
            self.failed("The result of multiplication is less then 0")
        else:
            self.passed("The result of multiplication is greater then 0.")

if __name__=="__main__":
    main()