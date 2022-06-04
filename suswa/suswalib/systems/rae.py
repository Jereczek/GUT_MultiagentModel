import numpy as np

class Rae:
    """
    Reputation aggregation engine
    
    Aggregates agents' reputation data and calculates their trustworthiness.
    """

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0, discount_factor: int = 1,):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        elif number_of_agents < 0:
            raise Exception("'numer_of_agents' must be a positive integer")
        
        self.number_of_agents = number_of_agents
        self.trustworthiness_matrix = np.ones((number_of_agents)) * initial_reputation

        self.__delta = np.zeros((number_of_agents, number_of_agents))

    @staticmethod
    def from_matrix(array: np.ndarray):
        if array is None:
            raise Exception(f"Attribute 'matrix' can't be None")
        
        r = Rae(0)
        
        r.number_of_agents = len(array)
        r.trustworthiness_matrix = array.copy()

        return r
