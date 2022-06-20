# copy this file to get a basic workint test suite.

import unittest

# pylint: disable=[import-error]

import context
from suswa.suswalib.systems.constants_data import ConstantsData

from suswa.suswalib.systems.policies.policy import BehaviorPolicy
from suswa.suswalib.systems.policies.default_policy_methods import *

class PolicyUnitTests(unittest.TestCase):

    def test_createObject_usingDefaultPolicies_ShouldPass(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )

    def test_applyServicePolicyTest_usingSomeConstantParams_shouldPass(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )

        self.assertIsNotNone(policy.apply_service_policy(0.1, False, 0.2, 0.3, 0.4))
        self.assertIsNotNone(policy.apply_service_policy(0.1, True, 0.2, 0.3, 0.4))

    def test_applyServiceReceivingPolicyTest_usingSomeConstantParams_shouldPass(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )

        self.assertIsNotNone(policy.apply_service_receiving_policy(0.1, False, 0.2, 0.3, 0.4))
        self.assertIsNotNone(policy.apply_service_receiving_policy(0.1, True, 0.2, 0.3, 0.4))

    def test_defautlServicePolicyTest_ExpectedMinValueShouldGetReturnedForSAgent(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )
        a = 1
        expected = 0.5 # min(a, expected)

        actual = policy.apply_service_policy(a, True, expected, 0, 0)

        self.assertEqual(expected, actual)

    def test_defautlServiceReceivingPolicyTest_ExpectedMinValueShouldGetReturnedForSAgent(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )
        a = 1
        expected = 0.5 # min(a, expected)

        actual = policy.apply_service_receiving_policy(a, True, expected, 0, 0)

        self.assertEqual(expected, actual)

    def test_staticServicePolicy_shouldYieldSameResultAsNonStaticVersion(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )
        data = ConstantsData(0.1, 0.2, 0.3, policy, 1.0, 1.0)
        a = 1
        trustworthiness = 1
        is_a_agent = False
        expected = policy.apply_service_policy(a, is_a_agent, data.y, data.x, trustworthiness)

        actual = BehaviorPolicy.apply_service_policy_static(data, is_a_agent, a, trustworthiness)

        self.assertEqual(expected, actual)

    def test_staticServiceReceivingPolicy_shouldYieldSameResultAsNonStaticVersion(self):
        policy = BehaviorPolicy(
            default_m_policy,
            default_m_policy,
            default_service_policy,
            default_service_receiving_policy
        )
        data = ConstantsData(0.1, 0.2, 0.3, policy, 1.0, 1.0)
        a = 1
        trustworthiness = 1
        is_a_agent = False
        expected = policy.apply_service_receiving_policy(a, is_a_agent, data.y, data.x, trustworthiness)

        actual = BehaviorPolicy.apply_service_receiving_policy_static(data, is_a_agent, a, trustworthiness)

        self.assertEqual(expected, actual)
