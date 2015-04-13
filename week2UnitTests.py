import unittest
import week2 as functions
from hypothesis import *


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
        testlist = functions.copyElementsUnder(original,2)
        self.assertEqual(testlist, [1])

    def test_copyunder2_firstelement(self):
        original = [5,4,3,2,1]
        testlist = functions.copyElementsUnder(original,2)
        self.assertEqual(testlist, [1])

    def test_copyunder3_severalelements(self):
        original = [3,5,1,4,2]
        testlist = functions.copyElementsUnder(original,4)
        self.assertEqual(testlist, [3,1,2])

    def test_copyunder4_nomatches(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(original,1)
        self.assertEqual(testlist, [])

    def test_copyunder5_allmatches(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(original,6)
        self.assertEqual(testlist, [1,2,3,4,5])

    def test_copyunder6_isgenuinecopy(self):
        original = [1,2,3,4,5]
        testlist = functions.copyElementsUnder(original,3)
        self.assertEqual(original, [1,2,3,4,5])

    def test_rbl1_nomatch(self):
        original = [1,2,3,4,5]
        remove   = [6,7,8]
        functions.removeByList(original,remove)
        self.assertEqual(original, [1,2,3,4,5])

    def test_rbl2_matches(self):
        original = [1,2,3,4,5]
        remove   = [1, 3, 5]
        functions.removeByList(original,remove)
        self.assertEqual(original, [2,4])    

    def test_rdup1_none(self):
        original = [5,2,3,4,1]
        copy = functions.removeDuplicates(original)
        self.assertEqual(copy, [1,2,3,4,5])

    def test_rdup2_dups(self):
        original = [5,2,3,4,1,5,2,3,4]
        copy = functions.removeDuplicates(original)
        self.assertEqual(copy, [1,2,3,4,5])

    def test_listover_1_nolap(self):
        lst1 = [1,2,3,4,5]
        lst2 = [6,7,8,9]
        lst3 = functions.listOverlap(lst1, lst2)
        self.assertEqual(lst3, [])

    def test_listover_2_olap(self):
        lst1 = [1,2,3,4,5]
        lst2 = [1,3,5]
        lst3 = functions.listOverlap(lst1, lst2)
        self.assertEqual(lst3, [1,3,5])

    def test_listover2_1_nolap(self):
        lst1 = [1,2,3,4,5]
        lst2 = [6,7,8,9]
        lst3 = functions.listOverlap2(lst1, lst2)
        self.assertEqual(lst3, [])

    def test_listover2_2_olap(self):
        lst1 = [1,2,3,4,5]
        lst2 = [1,3,5]
        lst3 = functions.listOverlap2(lst1, lst2)
        self.assertEqual(lst3, [1,3,5])
            
    def test_sss_up(self):
        expected = [0,1,2,3,4]
        actual = functions.createList(0,5,1)
        self.assertEqual(expected, actual)

    def test_sss_down(self):
        expected = [5,4,3,2,1]
        actual = functions.createList(5,0,-1)
        self.assertEqual(expected, actual)

    def test_sss_step(self):
        expected = [0,3,6,9,12]
        actual = functions.createList(0,13,3)
        self.assertEqual(expected, actual)

    def test_clubentry_enter(self):
        guestlist = {"Jamie": True,
                     "Bob" : False}        
        expected = True
        actual = functions.clubEntry("Jamie", guestlist)
        self.assertEqual(expected, actual)

    def test_clubentry_onlistfalse(self):
        guestlist = {"Jamie": True,
                     "Bob" : False}
        expected = False
        actual = functions.clubEntry("Bob", guestlist)
        self.assertEqual(expected, actual)

    def test_clubentry_notonlist(self):
        guestlist = {"Jamie": True,
                     "Bob" : False}
        expected = False
        actual = functions.clubEntry("Steven", guestlist)
        self.assertEqual(expected, actual)
        
    def test_factorial_negative(self):
        self.assertEqual(False, functions.factorial(-1))

    def test_factorial_zero(self):
        self.assertEqual(1, functions.factorial(0))

    def test_factorial_one(self):
        self.assertEqual(1, functions.factorial(1))

    def test_factorial_two(self):
        self.assertEqual(2, functions.factorial(2))

    def test_factorial_three(self):
        self.assertEqual(6, functions.factorial(3))

    def test_factorial_four(self):
        self.assertEqual(24, functions.factorial(4))

    def test_fibSequence_negative(self):
        self.assertEqual(False, functions.fibSequence(-1))

    def test_fibSequence_zero(self):
        self.assertEqual([1], functions.fibSequence(0))

    def test_fibSequence_one(self):
        self.assertEqual([1, 1], functions.fibSequence(1))

    def test_fibSequence_two(self):
        self.assertEqual([1, 1, 2], functions.fibSequence(2))

    def test_fibSequence_hundred(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                    144, 233, 377, 610, 987, 1597, 2584,
                    4181, 6765, 10946, 17711, 28657, 46368,
                    75025, 121393, 196418, 317811, 514229,
                    832040, 1346269, 2178309, 3524578, 5702887,
                    9227465, 14930352, 24157817, 39088169, 63245986,
                    102334155, 165580141, 267914296, 433494437, 701408733,
                    1134903170, 1836311903, 2971215073, 4807526976, 7778742049,
                    12586269025, 20365011074, 32951280099, 53316291173, 86267571272,
                    139583862445, 225851433717, 365435296162, 591286729879, 956722026041,
                    1548008755920, 2504730781961, 4052739537881, 6557470319842,
                    10610209857723, 17167680177565, 27777890035288, 44945570212853,
                    72723460248141, 117669030460994, 190392490709135, 308061521170129,
                    498454011879264, 806515533049393, 1304969544928657, 2111485077978050,
                    3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221,
                    23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497,
                    160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258,
                    1100087778366101931, 1779979416004714189, 2880067194370816120,
                    4660046610375530309, 7540113804746346429, 12200160415121876738,
                    19740274219868223167, 31940434634990099905, 51680708854858323072,
                    83621143489848422977, 135301852344706746049, 218922995834555169026,
                    354224848179261915075, 573147844013817084101]
        self.assertEqual(expected, functions.fibSequence(100))

    def test_hanoi_negative(self):
        self.assertEqual(False, functions.hanoi(-1))

    def test_hanoi_zero(self):
        self.assertEqual(False, functions.hanoi(0))

    def test_hanoi_one(self):
        self.assertEqual(1, functions.hanoi(1))

    def test_hanoi_two(self):
        self.assertEqual(3, functions.hanoi(2))

    def test_hanoi_three(self):
        self.assertEqual(7, functions.hanoi(3))

    def test_hanoi_four(self):
        self.assertEqual(15, functions.hanoi(4))

    def test_hanoi_fourty(self):
        self.assertEqual(1099511627775, functions.hanoi(40))

    def test_encode(self):
        expected = "0001020304050607080910"
        actual = functions.encode("AbCdEfGhIjK")
        self.assertEqual(expected, actual)

    def test_decode(self):
        expected = "abcdefghijk"
        actual = functions.decode("0001020304050607080910")
        self.assertEqual(expected,actual)

    def test_decode_badcode(self):
        expected = False
        actual = functions.decode("1")
        self.assertEqual(expected, actual)

    def test_encrypt_complexkey(self):
        original = "AbCdEfGhIjK"
        key  = "1234"
        expected = "0103050705070911091113"
        actual = functions.encrypt(original, key)
        self.assertEqual(expected, actual)

    def test_encrypt_singlekey(self):
        original = "AbCdEfGhIjK"
        key  = "1"
        expected = "0102030405060708091011"
        actual = functions.encrypt(original, key)
        self.assertEqual(expected, actual)

    def test_decrypt_complexkey(self):
        original = "0103050705070911091113" 
        key  = "1234"
        expected = "abcdefghijk"
        actual = functions.encrypt(original, key)
        self.assertEqual(expected, actual)


    def test_decrypt_singlekey(self):
        original = "0102030405060708091011"
        key  = "1"
        expected = "abcdefghijk"
        actual = functions.encrypt(original, key)
        self.assertEqual(expected, actual)

    def test_decrypt_encyrypt(self):
        word = "AbCdEfGhIjK"
        key = "1234"
        self.assertEqual(word.lower(), functions.decrypt(functions.encrypt(word, key),key))
        

    def test_papersize_A000(self):
        self.assertEqual((1682, 2378), functions.paperSize("A000"))
        
    def test_papersize_A00(self):
        self.assertEqual((1189, 1682), functions.paperSize("A00"))

    def test_papersize_A0(self):
        self.assertEqual((841, 1189), functions.paperSize("A0"))

    def test_papersize_A1(self):
        self.assertEqual((594, 841), functions.paperSize("A1"))

    def test_papersize_A2(self):
        self.assertEqual((420, 594), functions.paperSize("A2"))

    def test_papersize_A3(self):
        self.assertEqual((297, 420), functions.paperSize("A3"))



if __name__ == '__main__':
    unittest.main()
