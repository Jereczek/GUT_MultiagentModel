from suswa.suswalib.systems.rae import Rae

import unittest

# pylint: disable=[import-error]

import context

from suswa.suswalib.agents.agent import *

class RaeUnitTests(unittest.TestCase):

    def test_selftest(self):
        self.assertTrue(True)

    def test_exists(self):
        rae = Rae(0)
        pass

    def test_createObject_NumberOfAgentsIsFive_FiveByFiveMatrixWithOnesShouldGetInitialized(self):
        rae = Rae(5)

        self.assertEqual(rae.trustworthiness_matrix.shape, (5,))

    def test_createObject_NumberOfAgentsIsFive_NumberOfAgentsShouldBeFive(self):
        rae = Rae(5)

        self.assertEqual(rae.number_of_agents, 5)