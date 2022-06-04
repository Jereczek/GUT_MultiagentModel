import numpy as np

class Rae:
    """
    Reputation aggregation engine
    
    Aggregates agents' reputation data and calculates their trustworthiness.
    """

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0):
        self.__number_of_agents = number_of_agents
        self.__trustworthiness_matrix = np.ones((number_of_agents, number_of_agents)) * initial_reputation
        pass

    