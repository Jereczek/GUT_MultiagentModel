from asyncio import constants
from select import select
import numpy as np
from numpy.random import Generator, MT19937
from suswa.algorithms.kmeans import TwoMeans
from suswa.suswalib.systems.constants_data import ConstantsData
from suswa.suswalib.systems.policies.policy import BehaviorPolicy

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

    def __init__(self,
        number_of_agents: int,
        number_of_s_agents: int,
        constants: ConstantsData,
        initial_reputation: float = 1.0,
        discount_factor: int = 1
        ):
        self.__data = [TimestepData(number_of_agents, initial_reputation, constants.expo_a, constants.expo_g)]
        
        self.initial_reputation = initial_reputation

        self.number_of_agents = number_of_agents
        self.number_of_s_agents = number_of_s_agents
        self.discount_factor = discount_factor
        self.current_timestep = 0

        self.strategic_agents = self.__get_vector_of_s_agents()

        self.constants = constants

        self.clusterizing = TwoMeans()

    def __get_vector_of_s_agents(self):
        """
        Creates a shuffeled array of True/False values, where True ocurrs 'number_of_s_agent' times - True symbolizes an s-agent.
        """
        if self.number_of_s_agents > self.number_of_agents:
            raise Exception("'number_of_s_agents' must be lower or equal to 'number_of_agents'")

        temp_range = np.linspace(1, 1, num=self.number_of_s_agents, dtype=int)
        temp_range = np.array(np.append(temp_range, np.linspace(0, 0, num=self.number_of_agents - self.number_of_s_agents, dtype=int)), dtype='bool')

        np.random.shuffle(temp_range)

        return temp_range

    def aggregate(self):
        r_i_avg = []

        for n in range(self.number_of_agents):
            r_i_avg.append(self.__aggregate_for(n))

        
        n_high, n_low = self.clusterize(r_i_avg)

        high_avg = self.get_avg_of_cluster(r_i_avg, n_high)
        low_avg = self.get_avg_of_cluster(r_i_avg, n_low)

        new_timestep_data = TimestepData(self.number_of_agents, self.initial_reputation, self.constants.expo_a, self.constants.expo_g)

        self.set_multiple(new_timestep_data.trustworthiness_vector, n_high, high_avg / high_avg)
        self.set_multiple(new_timestep_data.trustworthiness_vector, n_low, low_avg / high_avg)

        self.__data.append(new_timestep_data)

        pass

    def clusterize(self, r_averages):
        current_clusters = self.clusterizing.fit(r_averages)

        n_1 = []
        n_2 = []

        n_1_sum = 0
        n_2_sum = 0

        for i in len(current_clusters):
            if current_clusters[i] == 0:
                n_1.append(i)
                n_1_sum += r_averages[i]
            else:
                n_2.append(i)
                n_2_sum += r_averages[i]

        if n_1_sum < n_2_sum:
            return (n_2, n_1)
        
        return (n_1, n_2)

    def get_avg_of_cluster(self, r_i_avg, cluster):
        sum = 0.0

        for i in cluster:
            sum += r_i_avg[i]

        return sum / float(len(cluster))

    def set_multiple(self, array, indecies, value):
        for i in indecies:
            array[i] = value

    def __aggregate_for(self, i: int):
        """
        Implementation of R_i,avg(t) reputation data aggregation formula for a single agent (i)
        """
        r = [x for x in range(self.number_of_agents) if x not in [i]]
        t = self.current_timestep

        sum = 0.0

        for j in r:
            t_minus_delta_t = t - self.__data[t].delta[i][j]
            sum += self.__data[t][i][j] * np.power(self.discount_factor, self.__data[t].delta[i][j]) - self.__R(i, j, t_minus_delta_t) 
        
        return sum

    def __R(self, i, j, t):
        return BehaviorPolicy.apply_service_receiving_policy_static(
                self.constants,
                self.strategic_agents[j],
                self.__data[t].gain[i][j] * BehaviorPolicy.apply_service_policy_static(
                    self.constants,
                    self.strategic_agents[i],
                    self.__data[t].availability[i][j],
                    self.__data[t].trustworthiness_vector[j]),
                self.__data[t].trustworthiness_vector[i])
