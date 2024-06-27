#  you can only succesfully login if BOTH username and password are correct.
#use a single if statement to do this

def login_system(username, password):
    correct_username = "admin"  # do not change line 
    correct_password = "password123"  # do not change line 

    





#do not change the code below , it is simply going to test the code you write above to see it is running properly
import unittest

class TestLoginSystem(unittest.TestCase):
    def test_successful_login(self):
        self.assertEqual(login_system("admin", "password123"), "success")
        
    def test_invalid_username(self):
        self.assertEqual(login_system("user", "password123"), "failure")
        
    def test_invalid_password(self):
        self.assertEqual(login_system("admin", "wrongpassword"), "failure")

if __name__ == '__main__':
    unittest.main()
