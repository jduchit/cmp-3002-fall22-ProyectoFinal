import time
import unittest
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest import Merge_arrs

## Testing class
class TestMergeSortedArrays(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #setea elementos para todos los tests

        cls.merge_arrays = Merge_arrs.merge_sorted_arrays

        cls.arr1_emp = []
        cls.arr2_emp = []

        cls.arr1_large = [i for i in range(1, 10000, 2)] # Array with odds nums
        cls.arr2_large = [i for i in range(0, 10000, 2)] # Array with even nums
        cls.corr_arr = cls.arr1_large+cls.arr2_large
        cls.corr_arr.sort()
        cls.totest_arr = [i for i in range(0, 10000)]

    def test_empty_first_ll(self):
        self.assertEqual(self.merge_arrays(self.arr1_emp, self.arr2_large), self.arr2_large)

    def test_empty_sec_ll(self):
        self.assertEqual(self.merge_arrays(self.arr1_large, self.arr2_emp), self.arr1_large)

    def test_empty_both(self):
        self.assertEqual(self.merge_arrays(self.arr1_emp, self.arr2_emp), [])

    def test_large_ll(self):   
        self.assertEqual(self.merge_arrays(self.arr1_large, self.arr2_large), self.totest_arr)
    

if __name__ == "__main__":
    unittest.main()