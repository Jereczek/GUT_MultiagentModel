from suswa.suswalib.systems.policies.policy import BehaviorPolicy
from suswa.suswalib.systems.policies.default_policy_methods import *

class DefaultPolicy(BehaviorPolicy):

    def __init__(self):
        self.service_policy = default_m_policy
        self.service_receiving_policy = default_m_policy
        self.service_policy_threshold = default_service_policy
        self.service_receiving_policy_threshold = default_service_receiving_policy
