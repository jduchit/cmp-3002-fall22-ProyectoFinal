import unittest
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Factorial import factorial
import hypothesis.strategies as st
from hypothesis import given

class TestFactorial(unittest.TestCase):  
    """
    Check that the factorial function raises a "TypeError" if the n entered is 
    a letter
    """
    def test_n_is_letter(self):
        with self.assertRaises(TypeError):
            factorial('one')
    
    """
    Check that the factorial function raises a "TypeError" if the n entered is 
    a float number
    """
    def test_n_is_float(self):
        with self.assertRaises(TypeError):
            factorial(1.1)
            
    """
    Check that the factorial function raises a "ValueError" if the n entered 
    is n<0
    """
    def test_n_less_than_0(self):
        with self.assertRaises(ValueError):
            factorial(-1)
            
    """
    Check that the result of the factorial is '1' if 'n == 0' 
    """
    def test_n_is_0(self):
        self.assertEqual(factorial(0), 1)

    """
    Check that the factorial function was calculated correctly by using the 
    definition that says the factorial of a number divided by the factorial of 
    that number minus one is the original number
    """
    @given(st.integers(min_value=2, max_value=500))
    def test_n_greater_than_0(self,n):
        result = int(factorial(n) / factorial(n - 1))
        self.assertEqual(n, result)
        
if __name__ == '__main__':
    unittest.main()