import numpy as np

class Rae:
    """
    Reputation aggregation engine
    
    Aggregates agents' reputation data and calculates their trustworthiness.
    """

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        else:
            raise Exception("'numer_of_agents' must be a positive integer")
        
        self.__number_of_agents = number_of_agents
        self.__trustworthiness_matrix = np.ones((number_of_agents, number_of_agents)) * initial_reputation

    @staticmethod
    def from_matrix(matrix: np.ndarray):
        if matrix is None:
            raise Exception(f"Attribute 'matrix' can't be None")
        elif matrix.shape[0] != matrix.shape[1]:
            raise Exception(f"Shape of provided matrix has to be a square, but is {matrix.shape} instead.")
        
        r = Rae(0)
        
        r.__number_of_agents = matrix.shape[0]
        r.__trustworthiness_matrix = matrix.copy()

        return r
