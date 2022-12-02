import unittest
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Sum import sum

class testsum(unittest.TestCase):

    def test_sum(self):
        """
        check sum funtion
        """
        self.assertEqual(sum(5), 15, "incorrect sum")
        """
        check when 0 is entered in the funtion
        """
        self.assertEqual(sum(0), 0, "incorrect sum")
    
    def test_letter_case(self): 
        """
        check if a letter is entered in sum funtion
        """
        with self.assertRaises(TypeError):
            sum('one')

    def test_float_case(self): 
        """
        check if a float number is entered in sum funtion
        """
        with self.assertRaises(TypeError):
            sum(1.1)

    def test_negative_number_case(self): 
        """
        check if a negative_number is entered in sum2 funtion
        """
        with self.assertRaises(ValueError):
            sum(-1)

unittest.main()