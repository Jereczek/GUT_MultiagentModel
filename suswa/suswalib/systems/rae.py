import numpy as np
from suswa.suswalib.systems.timestep_data import TimestepData

class Rae:
    """
    Reputation aggregation engine
    
    Aggregates agents' reputation data and calculates their trustworthiness.
    """

    # __delta = np.empty()

    # trustworthiness_matrix = np.empty()
    # number_of_agents = 0


    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0, discount_factor: int = 1):
        self.__data = [TimestepData(number_of_agents, initial_reputation)]

        self.number_of_agents = number_of_agents
        self.discount_factor = discount_factor
        self.current_timestep = 0

        self.__delta = [np.zeros((number_of_agents, number_of_agents))]
        

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
            sum += self.__data[t][i][j] * np.power(self.discount_factor, self.__delta[t][i][j]) #TODO: - R(t - self.__delta[t])
