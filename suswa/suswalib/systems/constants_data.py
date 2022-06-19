from suswa.suswalib.systems.policies.policy import BehaviorPolicy

class ConstantsData():

    def __init__(self, x: float, y: float, z: float, policy: BehaviorPolicy):
        self.x = x
        self.y = y
        self.z = z
        self.policy = policy