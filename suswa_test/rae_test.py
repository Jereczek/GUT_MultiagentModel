from suswa.suswalib.systems.rae import Rae

import unittest

# pylint: disable=[import-error]

import context

from suswa.suswalib.agents.agent import *

class RaeUnitTests(unittest.TestCase):

    def test_selftest(self):
        self.assertTrue(True)


    def test_createObject_NumberOfAgentsIsFive_NumberOfAgentsShouldBeFive(self):
        rae = Rae(5, 2)

        self.assertEqual(rae.number_of_agents, 5)