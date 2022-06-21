# copy this file to get a basic workint test suite.

import unittest

# pylint: disable=[import-error]

import context

import suswa.suswalib.systems.policies.default_policy_methods

class DefaultPolicyUnitTests(unittest.TestCase):

    availability = 10
    threshold = 2

    def test_default_m_policy(self):
        expected = self.availability * self.threshold

        actual = suswa.suswalib.systems.policies.default_policy_methods.default_m_policy(True, self.availability, self.threshold)

        self.assertEqual(expected, actual)
        
    def test_default_d_policy(self):
        expected = self.threshold

        actual = suswa.suswalib.systems.policies.default_policy_methods.default_d_policy(True, self.availability, self.threshold)

        self.assertEqual(expected, actual)