import numpy as np

# Note: is_s_agent is unused in this case, however expected by BehaviorPolicy
def default_m_policy(is_s_agent, availability: float, threshold: float) -> float:
    return availability * threshold

# Note: is_s_agent is unused in this case, however expected by BehaviorPolicy
def default_d_policy(is_s_agent, availability: float, threshold: float) -> float:
    return np.minimum(availability, threshold)

def default_service_policy(is_s_agent, y: float, x: float, trustworthiness: float) -> float:
    if(is_s_agent):
        return y
    
    if(trustworthiness > 1 - x):
        return 1.0

    return 0

def default_service_receiving_policy(is_s_agent, z: float, x: float, trustworthiness: float) -> float:
    return default_service_policy(is_s_agent, z, x, trustworthiness) # symetric approach
