import unittest
import hypothesis.strategies as st
from hypothesis import given
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Insertion_Sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    """
    Check that merge sort sorts in ascending order
    """
    @given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=10000))
    def test_merge_sort(self,array):
        self.assertEqual(insertion_sort(array), sorted(array))

if __name__ == '__main__':
    unittest.main()
