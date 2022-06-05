import numpy as np

class TimestepData:

    def __init__(self, number_of_agents: int, initial_reputation: float = 1.0):
        if number_of_agents == 0:
            pass # 0 will be treated as a special value for static initalization methods
        elif number_of_agents < 0:
            raise Exception("'numer_of_agents' must be a positive integer")
        
        self.trustworthiness_matrix = np.ones((number_of_agents, number_of_agents)) * initial_reputation

    def __getitem__(self, key):
        return self.trustworthiness_matrix[key]
