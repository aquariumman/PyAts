from pyats.aetest import Testcase, main, test
from myfunctions import div

class div_test_cl(Testcase):
    @test
    def div_test(self, a, b):
        try:
            result = div(a, b)
            if result < 0:
                self.failed("The result of dividing is less then 0")
        except ZeroDivisionError:
            self.passx(from_exception=ZeroDivisionError('We can not divide to zero!'))
        else:
            self.passed('The result of dividing is greater then 0.')


if __name__=="__main__":
    main()