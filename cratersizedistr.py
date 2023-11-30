import matplotlib.pyplot as plt
import numpy as np
import random

def N():
    return 50*(np.linspace(10, 150, 30))**(-1.8)

def Size():
    return np.round(((N())/50)**(-1/1.8)).astype(int)

def random_crater_size():
    pdf = N() / np.sum(N()) # Normalize
    return np.random.choice(Size(), p=pdf)

def uniform_crater_size():
    return 30
