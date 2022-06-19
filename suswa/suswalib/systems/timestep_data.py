import numpy as np

class TimestepData:
    """
    trustworthiness_vector - V_i(t)
    delta - matrix that represents the number of cycles since the last interaction between agent i and j

    availability - matrix representing the availability of services of agent i to agent j
    gain - matrix representing the quality of receiving services from agent i by agent j

    service_policy - matrix representing the policy of agent i giving services to agent j
    service_receiving_policy - matrix representing the policy of agent j reporting services received by agent i
    """

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        elif number_of_agents < 0:
            raise Exception("'numer_of_agents' must be a positive integer")
        
        self.trustworthiness_vector = np.ones(number_of_agents) * initial_reputation
        self.delta = np.zeros((number_of_agents, number_of_agents))

        self.availability = np.zeros((number_of_agents, number_of_agents))
        self.gain = np.zeros((number_of_agents, number_of_agents))

        self.service_policy = np.zeros((number_of_agents, number_of_agents))
        self.service_receiving_policy = np.zeros((number_of_agents, number_of_agents))

    def __getitem__(self, key):
        return self.trustworthiness_vector[key]
