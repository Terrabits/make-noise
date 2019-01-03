import numpy as     np
from   lib   import noise

def create_noise(color, sample_freq, seconds):
    sample_count = int(sample_freq*seconds)
    color = color.lower()
    return (noise.functions[color](sample_count) * 32768 / 8).astype(np.int16)
