from pyats.aetest import  Testcase, setup, test, cleanup, main
from pyats.topology.loader import load
from pyats.topology import Testbed


class SmokeTest(Testcase):
    @setup
    def setup(self, testbed):
        self.word=testbed.custom['word']
        print('A setup of smoke test')

    @test
    def test_1(self):
        print(f'Test #1{self.word}')

    @test
    def test_2(self):
        print(f'Test #2 {self.word}')

    @cleanup
    def clenup(self):
        print('A cleanup of smoke test')

if __name__=='__main__':
    testbed = load('testbed.yaml')
    main(testbed=testbed)
