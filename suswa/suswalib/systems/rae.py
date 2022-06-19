from select import select
import numpy as np
from numpy.random import Generator, MT19937

from suswa.suswalib.systems.timestep_data import TimestepData

class Rae:
    """
    Reputation aggregation engine
    
    Aggregates agents' reputation data and calculates their trustworthiness.
    """

    # __delta = np.empty()

    # trustworthiness_matrix = np.empty()
    # number_of_agents = 0

    rng = Generator(MT19937())

    def __init__(self, number_of_agents: int, number_of_s_agents, initial_reputation: float = 1.0, discount_factor: int = 1):
        self.__data = [TimestepData(number_of_agents, initial_reputation)]
        
        self.number_of_agents = number_of_agents
        self.number_of_s_agents = number_of_s_agents
        self.discount_factor = discount_factor
        self.current_timestep = 0

        self.__strategic_agents = self.__get_vector_of_s_agents()

    def __get_vector_of_s_agents(self, number_of_s_agents: int):
        """
        Creates a shuffeled array of True/False values, where True ocurrs 'number_of_s_agent' times - True symbolizes an s-agent.
        """
        if self.number_of_s_agents > self.number_of_agents:
            raise Exception("'number_of_s_agents' must be lower or equal to 'number_of_agents'")

        temp_range = np.linspace(1, 1, num=number_of_s_agents, dtype=int)
        temp_range = np.array(np.append(temp_range, np.linspace(0, 0, num=self.number_of_agents - self.number_of_s_agents, dtype=int)), dtype='bool')

        np.random.shuffle(temp_range)

        return temp_range

    def aggregate(self):
        pass

    def __aggregate_for(self, i: int):
        """
        Implementation of R_i,avg(t) reputation data aggregation formula for a single agent (i)
        """
        r = [x for x in range(self.number_of_agents) if x not in [i]]
        t = self.current_timestep

        sum = 0.0

        for j in r:
            sum += self.__data[t][i][j] * np.power(self.discount_factor, self.__data.delta[t][i][j]) #TODO: - R(t - self.__data[t].delta[i][j])
