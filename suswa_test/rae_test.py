from suswa.suswalib.systems.constants_data import ConstantsData
from suswa.suswalib.systems.policies.default_policy import DefaultPolicy
from suswa.suswalib.systems.policies.policy import BehaviorPolicy
from suswa.suswalib.systems.rae import Rae

import numpy as np

import unittest

# pylint: disable=[import-error]

import context

from suswa.suswalib.agents.agent import *

class RaeUnitTests(unittest.TestCase):

    sample_consts = ConstantsData(1.0, 1.0, 1.0, DefaultPolicy(), 1.0, 1.0, 0, 10)

    def test_selftest(self):
        self.assertTrue(True)


    def test_createObject_NumberOfAgentsIsFive_NumberOfAgentsShouldBeFive(self):
        rae = Rae(5, 2, self.sample_consts)

        self.assertEqual(rae.number_of_agents, 5)
    
    def test_createObject_NumberOfSAgentsIsTwo_NumberOfSAgentsInArrayShouldBeTwo(self):
        rae = Rae(5, 2, self.sample_consts)

        number_of_s_agents = 0

        for i in rae.strategic_agents:
            if(i):
                number_of_s_agents += 1

        self.assertEqual(number_of_s_agents, 2)

    def test_createObject_SetInitialTrustworthiness_InitialTrustworthinessVectorShouldGetAssigned(self):
        number_of_agents = 10
        initial_trustworthiness = np.ones(number_of_agents)

        rae = Rae(number_of_agents, number_of_agents - 1, self.sample_consts, initial_trustworthiness)

        np.testing.assert_array_equal(rae.data[0].trustworthiness_vector, initial_trustworthiness)

    def test_createObject_SetRandomInitialTrustwothiness_InitialTrustworthinessVectorShouldGetAssignedWithRandomVector(self):
        number_of_agents = 5

        rae = Rae(number_of_agents, 2, self.sample_consts, initial_reputation=None)

        self.assertNotEqual(np.sum(rae.data[0].trustworthiness_vector), number_of_agents)

    def test_createObject_SetEqualInitialTrustwothiness_InitialTrustworthinessVectorContainEqualValues(self):
        number_of_agents = 5

        rae = Rae(number_of_agents, 2, self.sample_consts, initial_reputation=1.0)

        self.assertEqual(np.sum(rae.data[0].trustworthiness_vector), number_of_agents)
