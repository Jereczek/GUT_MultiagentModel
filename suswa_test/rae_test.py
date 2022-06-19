from suswa.suswalib.systems.rae import Rae

import unittest

# pylint: disable=[import-error]

import context

from suswa.suswalib.agents.agent import *

class RaeUnitTests(unittest.TestCase):

    def test_selftest(self):
        self.assertTrue(True)


    def test_createObject_NumberOfAgentsIsFive_NumberOfAgentsShouldBeFive(self):
        rae = Rae(5, 2, None)

        self.assertEqual(rae.number_of_agents, 5)
    
    def test_createObject_NumberOfSAgentsIsTwo_NumberOfSAgentsInArrayShouldBeTwo(self):
        rae = Rae(5, 2, None)

        number_of_s_agents = 0

        for i in rae.strategic_agents:
            if(i):
                number_of_s_agents += 1

        self.assertEqual(number_of_s_agents, 2)
