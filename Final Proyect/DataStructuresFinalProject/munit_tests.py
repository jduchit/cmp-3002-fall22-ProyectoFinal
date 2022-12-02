from DataStructures import Array, Doubly_Linked_List, Singly_Linked_List, Queue, Priority_Queue, Stacks, FactorialRecursion,FactorialMemoization, 
FibonacciRecursion,FibonacciMemoization,MergeSort,QuickSort

from MergeSort import merge_sort
from FactorialRecursion import factorial
from FactorialMemoization import factorial
from FibonacciRecursion import factorial
from FibonacciMemoization import factorial

import unittest
import hypothesis.strategies as st
from hypothesis import given
import math


class TestSort(unittest.TestCase):
    """
    Check that merge sort sorts in ascending order
    """
    @given(st.lists(st.integers(min_value=1, max_value=12), min_size=4))
    def test_merge_sort(self,array):
        self.assertEqual(merge_sort(array), sorted(array))


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
    @given(st.integers(min_value=2, max_value=100))
    def test_n_greater_than_0(self,n):
        result = int(factorial(n) / factorial(n - 1))
        self.assertEqual(n, result)
        

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

if __name__ == '__main__':
    unittest.main()
