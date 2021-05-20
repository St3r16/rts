import numpy as np      # math operations
import matplotlib.pyplot as plt     #graphs

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


def fCoeff(pk, N):
    exp = 2*np.pi*pk/N
    return complex(np.cos(exp), -np.sin(exp))


# Fast  Fourier Transform
def ffTransform(signals):
    N = len(signals)
    l = int(N/2)
    spect = [0] * N

    if N ==1:
        return signals
    evens = ffTransform(signals[::2])
    odds = ffTransform(signals[1::2])

    for k in range(l):
        spect[k] = evens[k] + odds[k] * fCoeff(k, N)
        spect[k + l] = evens[k] - odds[k] * fCoeff(k, N)

    return spect


signal  = signalsGenerator(n,w,N)


plt.plot(signal)
plt.title('Random generated signals')
plt.xlabel('time')
plt.ylabel('signal')
plt.figure()

plt.plot(ffTransform(signal))
plt.title('Fast Fourier Transform')
plt.xlabel('p')
plt.ylabel('F(p)')
plt.show()

