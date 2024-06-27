
# this functoin shd tell if a is bigger or b, and incase they are same , return equal!
# If both numbers are equal, any of them can be returned.

def compare_numbers(a, b):
    #code here 









#do not change the code below , it is simply going to test the code you write above to see it is running properly

import unittest

class TestCompareNumbers(unittest.TestCase):
    def test_a_greater_than_b(self):
        self.assertEqual(compare_numbers(10, 5), "a is bigger")
        
    def test_a_less_than_b(self):
        self.assertEqual(compare_numbers(5, 10), "b is bigger")
        
    def test_a_equal_b(self):
        self.assertEqual(compare_numbers(5, 5), "a and b are equal.")

if __name__ == '__main__':
    unittest.main()