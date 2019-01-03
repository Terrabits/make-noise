import numpy as np

def ms(x):
    return (np.abs(x)**2.0).mean()
def normalize(x):
    return x * np.sqrt(1.0 / ms(x))
