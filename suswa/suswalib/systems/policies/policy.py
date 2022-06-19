class Policy():

    def __init__(self, Pt, Rt, p, r):
        self.Pt = Pt
        self.Rt = Rt
        self.p = p
        self.r = r

    def apply_service_policy(self, cant_think_of_a_good_name: float, is_s_agent, y: float, x: float, trustworthiness: float) -> float:
        self.Pt(is_s_agent, cant_think_of_a_good_name, self.p(y, x, trustworthiness))

    def apply_service_receiving_policy(self, cant_think_of_a_good_name: float, is_s_agent, z: float, x: float, trustworthiness: float) -> float:
        self.Rt(is_s_agent, cant_think_of_a_good_name, self.r(is_s_agent, z, x, trustworthiness))
