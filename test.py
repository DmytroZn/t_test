# target = __import__('my_sum.py')
# sum = target.sum

import unittest

from fractions import Fraction
from my_sum import sum 

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        the that it can sum 
    a list of integer
        '''

        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        '''
        the that it can sum 
    a list of fracc
        '''
        data = [Fraction(1,4), Fraction(1, 4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

if __name__ == '__main__':
    unittest.main()