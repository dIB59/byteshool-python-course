#the code below will give a different grade depending on the score.
#if above or equal to 90 , u get A
#if above or equal to 80 , u get B
#if above or equal to 70 , u get C
#if above or equal to 60 , u get D
#if below 60 , u get F

def get_grade(score):
    #write code here inside function





#do not need to change the code below , it is simply going to test the code you write above to see it is running properly
import unittest

class TestGradingSystem(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(get_grade(95), 'A')
        
    def test_grade_B(self):
        self.assertEqual(get_grade(85), 'B')
        
    def test_grade_C(self):
        self.assertEqual(get_grade(75), 'C')
        
    def test_grade_D(self):
        self.assertEqual(get_grade(65), 'D')
        
    def test_grade_F(self):
        self.assertEqual(get_grade(55), 'F')

if __name__ == '__main__':
    unittest.main()
