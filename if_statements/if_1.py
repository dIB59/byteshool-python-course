
#the code in function check_nuber is not complete
#it checks if a number is bigger then 0 , smaller then 0 or equal to 0
def check_number(number):
    if number > 0:
        return "The number is positive."
    elif 



#do not change the code below , it is simply going to test the code you write above to see it is running properly
import unittest

class TestCheckNumber(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(check_number(10), "The number is positive.")
        
    def test_negative(self):
        self.assertEqual(check_number(-5), "The number is negative.")
        
    def test_zero(self):
        self.assertEqual(check_number(0), "The number is zero.")

if __name__ == '__main__':
    unittest.main()
