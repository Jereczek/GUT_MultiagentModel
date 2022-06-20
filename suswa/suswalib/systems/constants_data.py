from suswa.suswalib.systems.policies.policy import BehaviorPolicy

class ConstantsData():

    def __init__(self, x: float, y: float, z: float, policy: BehaviorPolicy, expo_a: float, expo_g: float):
        self.x = x
        self.y = y
        self.z = z
        self.policy = policy

        self.expo_a = expo_a
        self.expo_g = expo_g