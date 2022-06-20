import numpy as np
from numpy.random import Generator, MT19937

class TimestepData:
    """
    trustworthiness_vector - V_i(t)
    delta - matrix that represents the number of cycles since the last interaction between agent i and j

    availability - matrix representing the availability of services of agent i to agent j
    gain - matrix representing the quality of receiving services from agent i by agent j

    service_policy - matrix representing the policy of agent i giving services to agent j
    service_receiving_policy - matrix representing the policy of agent j reporting services received by agent i
    """

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0, exponent_a: float = 1.0, exponent_g: float = 1.0):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        elif number_of_agents < 0:
            raise Exception("'numer_of_agents' must be a positive integer")

        rng = Generator(MT19937())
        
        self.trustworthiness_vector = np.ones(number_of_agents) * initial_reputation
        self.delta = np.zeros((number_of_agents, number_of_agents))

        self.availability = TimestepData.__get_matrix_with_random_distribution(number_of_agents, exponent_a, rng)
        self.gain = TimestepData.__get_matrix_with_random_distribution(number_of_agents, exponent_g, rng)

        self.service_policy = np.zeros((number_of_agents, number_of_agents))
        self.service_receiving_policy = np.zeros((number_of_agents, number_of_agents))

    @staticmethod
    def __get_matrix_with_random_distribution(number_of_agents: int, exponent: float, rng: Generator):
        m = np.ones((number_of_agents, number_of_agents))

        for i in range(number_of_agents):
            for j in range(number_of_agents):
                m[i][j] = np.power(rng.uniform(0, 1), exponent)

        return m

