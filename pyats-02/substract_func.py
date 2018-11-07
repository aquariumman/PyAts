from pyats.aetest import Testcase, main, test
from myfunctions import substr

class substr_test_cl(Testcase):
    @test
    def substr_test(self, a, b):
        if substr(a, b) < 0:
            self.failed("The result of substraction is less then 0")
        else:
            self.passed("The result of substraction is greater then 0.")

if __name__=="__main__":
    main()