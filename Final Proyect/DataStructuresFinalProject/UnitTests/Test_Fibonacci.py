import unittest
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Fibonacci import fibonacci
import hypothesis.strategies as st
from hypothesis import given
import math

class TestFibonacci(unittest.TestCase):  
    """
    Check that the fibonacci function raises a "TypeError" if the n entered is 
    a letter
    """
    def test_n_is_letter(self):
        with self.assertRaises(TypeError):
            fibonacci('one')
    
    """
    Check that the fibonacci function raises a "TypeError" if the n entered is 
    a float number
    """
    def test_n_is_float(self):
        with self.assertRaises(TypeError):
            fibonacci(1.1)
            
    """
    Check that the fibonacci function raises a "ValueError" if the n entered 
    is n<0
    """
    def test_n_less_than_0(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
            
    """
    Check that the result of the fibonacci is '0' if 'n == 0' 
    """
    def test_n_is_0(self):
        self.assertEqual(fibonacci(0), 0)

    """
    Check that the result of the fibonacci is '1' if 'n == 1' 
    """
    def test_n_is_1(self):
        self.assertEqual(fibonacci(1), 1)

    """
    Check that the fibonacci function was calculated correctly by using the Binet’s Formula this is a formula that is 
    used to find the nth term of the Fibonacci sequence
    """
    @given(st.integers(min_value=2, max_value=20))
    def test_n_greater_than_1(self,n):
        result = int(((((1 + math.sqrt(5)) / 2) ** (n))-(((1 - math.sqrt(5)) / 2) ** (n)))/(math.sqrt(5)))
        self.assertEqual(fibonacci(n), result)

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)

if __name__ == '__main__':
    unittest.main()
