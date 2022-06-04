from numpy.random import Generator, MT19937

if __name__ == '__main__':
    rng = Generator(MT19937())

    print(rng.random())

    # Uniformy distributed randomnes:
    print(rng.uniform(20, 30))
