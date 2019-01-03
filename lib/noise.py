from  .math      import normalize
import numpy      as     np
from   numpy.fft import rfft, irfft

# https://en.wikipedia.org/wiki/Colors_of_noise#Technical_definitions

def white(sample_count):
    return np.random.randn(sample_count).astype(np.float32)
def pink(sample_count):
    x = white(sample_count)
    X = rfft(x) / sample_count
    S = np.sqrt(np.arange(X.size)+1.)  # +1 to avoid divide by zero
    y = (irfft(X/S)).real[0:sample_count]
    return normalize(y)
def blue(sample_count):
    x = white(sample_count)
    X = rfft(x) / sample_count
    S = np.sqrt(np.arange(X.size))  # Filter
    y = (irfft(X*S)).real[0:sample_count]
    return normalize(y)
def brown(sample_count):
    x = white(sample_count)
    X = rfft(x) / sample_count
    S = (np.arange(X.size)+1)  # Filter
    y = (irfft(X/S)).real[0:sample_count]
    return normalize(y)
def violet(sample_count):
    x = white(sample_count)
    X = rfft(x) / sample_count
    S = (np.arange(X.size))  # Filter
    y = (irfft(X*S)).real[0:sample_count]
    return normalize(y)
colors = [
    'white',
    'pink',
    'blue',
    'brown',
    'violet',
]
functions = {
    'white': white,
    'pink': pink,
    'blue': blue,
    'brown': brown,
    'violet': violet,
}
