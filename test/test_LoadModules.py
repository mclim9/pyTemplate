###############################################################################
### Purpose: Import Library-->Create Object-->Catch obvious typos.
###############################################################################
import unittest
import sys

class TestGeneral(unittest.TestCase):
    def setUp(self):                                #Run before each test
        sys.path.append('../')
        print("",end="")

    def tearDown(self):                             #Run after each test
        pass

###############################################################################
### <Test>
###############################################################################
    def test_Covid_Class(self):
        from src.covid import covid
        self.baz = covid()
        self.assertEqual(self.baz.foo,'N')          # Check default value

    def test_Spam_Class(self):
        from src.spam import spam
        self.eggs = spam()
        self.assertEqual(self.eggs.ham,'ham')       # Check default value

###############################################################################
### </Test>
###############################################################################
if __name__ == '__main__':                          # pragma: no cover
    # unittest.main()     #Run w/o test names
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneral)
    unittest.TextTestRunner(verbosity=2).run(suite)
