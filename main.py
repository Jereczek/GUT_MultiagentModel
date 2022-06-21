from suswa.suswalib.systems.rae import Rae
from suswa.suswalib.systems.policies.default_policy import DefaultPolicy
from suswa.suswalib.systems.constants_data import ConstantsData

def main():
    # |N| i |S|
    liczba_agentow = 1000
    liczba_s_agentow = 250

    # Imin oraz Imax
    i_min = 5
    i_max = 15

    # Dystrybuanty zmiennych losowych A i G
    expo_a = 1
    expo_g = 10

    # Polityka (h- oraz s-polityka)
    policy = DefaultPolicy()

    # "Dobra wola"
    x = 1.0
    y = 1.0
    z = 1.0

    # Współczynnik dyskontowy
    delta = 1

    # Początkowe miary zaufania
    initial_rep = 1.0

    # Kroki czasowe
    t_max = 1000
    
    constants = ConstantsData(x, y, z, policy, expo_a, expo_g, i_min, i_max)

    rae = Rae(liczba_agentow, liczba_s_agentow, constants, initial_rep, delta)

    for t in range(t_max):
        print(f"Krok {t}")
        rae.aggregate()

if __name__ == '__main__':
    main()