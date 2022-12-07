import unittest
import hypothesis.strategies as st
from hypothesis import given
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Merge_Sort import merge_sort

class TestMergeSort(unittest.TestCase):
    """
    Check that merge sort sorts in ascending order
    """
    @given(st.lists(st.integers(min_value=1, max_value=100), min_size=100))
    def test_merge_sort(self,array):
        self.assertEqual(merge_sort(array), sorted(array))

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)

if __name__ == '__main__':
    unittest.main()
