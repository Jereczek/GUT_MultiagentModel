from suswa.suswalib.systems.policies.policy import BehaviorPolicy

class ConstantsData():

    def __init__(
        self,
        x: float,
        y: float,
        z: float,
        policy: BehaviorPolicy,
        expo_a: float,
        expo_g: float,
        i_min: int,
        i_max: int
        ):

        self.x = x
        self.y = y
        self.z = z
        self.policy = policy

        self.expo_a = expo_a
        self.expo_g = expo_g

        if(i_min > i_max):
            raise Exception("'i_min' should be lower or equal to 'i_max'.")
        if(i_min < 0 or i_max < 0):
            raise Exception("'i_min' and 'i_max' should be greater or equal 0.")

        self.i_min = i_min
        self.i_max = i_max