class BehaviorPolicy():

    def __init__(self, service_policy, service_receiving_policy, service_policy_threshold, service_receiving_policy_threshold):
        self.service_policy = service_policy
        self.service_receiving_policy = service_receiving_policy
        self.service_policy_threshold = service_policy_threshold
        self.service_receiving_policy_threshold = service_receiving_policy_threshold

    @staticmethod
    def apply_service_policy_static(configuration, is_s_agent, cant_think_of_a_good_name: float, trustworthiness: float) -> float:
        return configuration.policy.apply_service_policy(
            cant_think_of_a_good_name,
            is_s_agent,
            configuration.y,
            configuration.x,
            trustworthiness
        )

    @staticmethod
    def apply_service_receiving_policy_static(configuration, is_s_agent, cant_think_of_a_good_name: float, trustworthiness: float) -> float:
        return configuration.policy.apply_service_receiving_policy(
            cant_think_of_a_good_name,
            is_s_agent,
            configuration.z,
            configuration.x,
            trustworthiness
        )

    def apply_service_policy(self, cant_think_of_a_good_name: float, is_s_agent, y: float, x: float, trustworthiness: float) -> float:
        return self.service_policy(
            is_s_agent,
            cant_think_of_a_good_name,
            self.service_policy_threshold(is_s_agent, y, x, trustworthiness))

    def apply_service_receiving_policy(self, cant_think_of_a_good_name: float, is_s_agent, z: float, x: float, trustworthiness: float) -> float:
        return self.service_receiving_policy(
            is_s_agent,
            cant_think_of_a_good_name,
            self.service_receiving_policy_threshold(is_s_agent, z, x, trustworthiness))
