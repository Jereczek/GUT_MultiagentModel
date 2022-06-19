import unittest
from xmlrpc.client import Boolean
import numpy as np

# pylint: disable=[import-error]

import context

from suswa.suswalib.systems.timestep_data import *

class TimeStampDataUnitTests(unittest.TestCase):

    def test_createObject_invalidNumberOfAgentsProvided_shouldThrowException(self):
        with self.assertRaises(Exception):
            TimestepData(-1, 0)
    
    def test_accessArrayFromMatrix_MatrixContainsOnlyOnes_ShouldReturnRangeOfOnes(self):
        td = TimestepData(3, 1)

        np.testing.assert_array_equal(td.trustworthiness_vector[:], (1, 1, 1))
        
    def test_accessItemFromMatrix_MatrixContainsOnlyOnes_ShouldReturnRangeOfOnes(self):
        td = TimestepData(3, 1)

        self.assertEqual(td.trustworthiness_vector[0], 1)

    def test_createObject_NumberOfAgentsIsFive_FiveByFiveDeltaMatrixWithZerosShouldGetInitialized(self):
        td = TimestepData(5)

        self.assertEqual(td.delta.shape, (5, 5))

    def test_createObject_NumberOfAgentsIsFive_FiveElementVectorShouldGetInitialized(self):
        td = TimestepData(5)

        self.assertEqual(td.trustworthiness_vector.shape, (5,))

    def test_random(self):
        temp_range = np.linspace(1, 1, num=5, dtype=int)
        temp_range = np.array(np.append(temp_range, np.linspace(0, 0, num=2, dtype=int)), dtype='bool')

        np.random.shuffle(temp_range)

        for i in temp_range:
            print(i)