import pandas as pd
from pandas import DataFrame, Series
import unittest
import numpy as np

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # set up some variables here
        self.frame = pd.DataFrame({'key1' : ['a', 'b', 'c'], 'key2': [1,2,3]})
        self.my_val = 'a'

    def test_frame(self):
        # write some asserts here
        self.assertEquals(self.frame.ix[0,0],'a')
        # self.assertEquals(self.seq[2], 2)
        self.assertEquals(self.my_val, 'a')
        self.assertEquals(len(self.my_val), 1)

    def test_fails(self):
        # write some asserts here
        self.assertEquals(self.my_val, 'a')

if __name__ == '__main__':
    unittest.main()
