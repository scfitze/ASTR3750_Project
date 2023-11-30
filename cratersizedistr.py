import matplotlib.pyplot as plt
import numpy as np
import random

def N():
    return 50*(np.linspace(10, 150))**(-1.8)

def random_crater_size():
    size = np.round(((N())/50)**(-1/1.8))
    return random.choice(size)