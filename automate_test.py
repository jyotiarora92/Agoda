import ChangePassword
import unittest

class TestPlan(unittest.TestCase):
    def testcase1(self):
        print("TEST   CASE1:  Test to see length shorter than 18 charaters is not valid.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456",""))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABCDEF1234#"))

    def testcase2(self):
        print("TEST  CASE2:  Test to see atleast 1 lowercase is required.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "ABCDEFGHIJKL123457#$"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "ABCDEFGHI123457#$@!"))

    def testcase3(self):
        print("TEST  CASE3:  Test to see atleast 1 uppercase is required.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefgh123457#$"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdeg12309hY457#$@!"))
    
    def testcase4(self):
        print("TEST  CASE4:  Test to see similarity between old and new passwords.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABC@12890"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABCDEF!@#$klmnqw"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABCDEF!@klmnqw12"))

    def testcase5(self):
        print("TEST  CASE5:  Test to see atleast 1 numeric is required.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABC!@#$&*HHJUY"))

    def testcase6(self):
        print("TEST  CASE6:  Test to see atleast 1 special char is required.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "abcdefABC0986453HHJUY"))

    def testcase7(self):
        print("TEST  CASE7:  Test to see extra special char is not accepted.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456","qwerrtyABCDEF@!#1-"))

    def testcase8(self):
        print("TEST  CASE8:  Test to see string with space is not accepeted.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456","qwerrtyABC DEF@!#1"))

    def testcase9(self):
        print("TEST  CASE9:  Test to see no duplicate repeat characters more than 4 are accepted.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456","qwerrrrtyABCDEF@!#1"))

    def testcase10(self):
        print("TEST  CASE10:  Test to see no more than 4 special characters are accepted.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456","qwerrtyABCDEF@!##*"))

    def testcase11(self):
        print("TEST  CASE11:  Test to see 50% of the password should not be a number.")
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456", "AbxVGTQW@!#$0987572"))
        print(ChangePassword.changePassword("abcdefABCDEF!@#$123456","qwerrtyAB@0987652109"))

    
    

if __name__ == "__main__":
    unittest.main()
