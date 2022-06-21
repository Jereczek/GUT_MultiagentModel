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

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0, exponent_a: float = 1.0, exponent_g: float = 1.0, i_min: int = 0, i_max: int = 0, rng = None):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        elif number_of_agents < 0:
            raise Exception("'numer_of_agents' must be a positive integer")

        if (i_min == 0 and i_max == 0):
            i_max = number_of_agents

        if (rng is None):
            rng = Generator(MT19937())
        
        self.trustworthiness_vector = np.ones(number_of_agents) * initial_reputation
        self.delta = np.zeros((number_of_agents, number_of_agents))

        self.availability = TimestepData.__get_matrix_with_random_distribution(number_of_agents, exponent_a, rng)
        self.gain = TimestepData.__get_matrix_with_random_distribution(number_of_agents, exponent_g, rng)

        self.choosen_service_providers = TimestepData.__get_service_providers(number_of_agents, i_min, i_max, rng)
        self.service_policy = np.zeros((number_of_agents, number_of_agents))
        self.service_receiving_policy = np.zeros((number_of_agents, number_of_agents))

    @staticmethod
    def __get_matrix_with_random_distribution(number_of_agents: int, exponent: float, rng: Generator):
        m = np.ones((number_of_agents, number_of_agents))

        for i in range(number_of_agents):
            for j in range(number_of_agents):
                m[i][j] = np.power(rng.uniform(0, 1), exponent)

        return m

    @staticmethod
    def __get_service_providers(number_of_agents: int, i_min: int, i_max: int, rng: Generator):
        m = []

        for i in range(number_of_agents):
            number_of_services = int(np.floor(rng.uniform(i_min, i_max)))
            m.append([])
            range_of_agents = [x for x in range(number_of_agents) if x not in [i]]
            rng.shuffle(range_of_agents)
            m[i].append(range_of_agents[0:number_of_services])

        return m

