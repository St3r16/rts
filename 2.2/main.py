import numpy as np      # math operations
import time
from dft import dft

n = 10      # harmonics
w = 2700    #frequency
N = 256     # discrete calls

def signalsGenerator(n,w,N):
    signals = np.zeros(N)
    W = w / n
    for _ in range(n):
        for t in range(N):
            amplitude = np.random.rand()
            phase = np.random.rand()
            signals[t] += (amplitude * np.sin(W * t + phase))
        W += W
    return signals


def fCoeff(k, N):
    exp = 2.0 * np.pi * k / N
    return complex(np.cos(exp), -np.sin(exp))


# Fast  Fourier Transform
def ffTransform(signals):
    N = len(signals)
    if N == 1 :
        return signals
    spectrum = [0] * N

    evens = ffTransform(signals[::2])
    odds = ffTransform(signals[1::2])

    l = int(N/2)
    for k in range(l):
        exp = odds[k] * fCoeff(k, N)

        spectrum[k] = evens[k] + exp
        spectrum[k + l] = evens[k] - exp

    return spectrum


sigs = signalsGenerator(n, w, N)

start = time.time()
dft(sigs)
print("discrete Fourier transform time: {}".format(time.time() - start))


start = time.time()
ffTransform(sigs)
print("fast Fourier transform time: {}".format(time.time() - start))


