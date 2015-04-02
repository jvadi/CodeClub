import unittest
import week2 as functions

class TestFunctions(unittest.TestCase):

    #remove tests
    def test_remove1_lastelement(self):
        testlist = [1,2,3,4,5]
        functions.remove(testlist,2)
        self.assertEqual(testlist, [2,3,4,5])

    def test_remove2_firstelement(self):
        testlist = [5,4,3,2,1]
        functions.remove(testlist,2)
        self.assertEqual(testlist, [5,4,3,2])

    def test_remove3_severalelements(self):
        testlist = [3,5,1,4,2]
        functions.remove(testlist,4)
        self.assertEqual(testlist, [5,4])

    def test_remove4_nomatches(self):
        testlist = [1,2,3,4,5]
        functions.remove(testlist,1)
        self.assertEqual(testlist, [1,2,3,4,5])

    def test_remove5_allmatches(self):
        testlist = [1,2,3,4,5]
        functions.remove(testlist,6)
        self.assertEqual(testlist, [])

    #copy under tests
    def test_copyunder1_lastelement(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(testlist,2)
        self.assertEqual(testlist, [1])

    def test_copyunder2_firstelement(self):
        original = [5,4,3,2,1]
        teslist = functions.copyElementsUnder(testlist,2)
        self.assertEqual(testlist, [1])

    def test_copyunder3_severalelements(self):
        original = [3,5,1,4,2]
        testlist = functions.copyElementsUnder(testlist,4)
        self.assertEqual(testlist, [3,1,2])

    def test_copyunder4_nomatches(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(testlist,1)
        self.assertEqual(testlist, [])

    def test_copyunder5_allmatches(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(testlist,6)
        self.assertEqual(testlist, [1,2,3,4,5])

    def test_copyunder6_isgenuinecopy(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(testlist,3)
        self.assertEqual(original, [1,2,3,4,5])
    



        

if __name__ == '__main__':
    unittest.main()
