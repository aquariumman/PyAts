from pyats.aetest import Testcase, main, test
from myfunctions import add

class add_test_cl(Testcase):
    @test
    def add_test(self, a, b):
        if add(a, b) < 0:
            self.failed("The result of adding is less then 0")
        else:
            self.passed("The result is greater then 0.")

if __name__=="__main__":
    main()