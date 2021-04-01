import numpy as np      # math operations
import matplotlib.pyplot as plt     #graphs

n = 10      # harmonics
w = 2700    #frequency
N = 256     # discrete calls

def signalsGenerator(n,w,N):
    signals = np.zeros(N)
    W = w / n

    for harmonic in range(n):
        amplitude = np.random.rand()
        phase = np.random.rand()

        for t in range(N):
            signals[t] += (amplitude * np.sin(W * t + phase))
        W += W
    return signals

def correlFunction(signalFirst, signalSec):

    result = []
    lngth = len(signalFirst) // 2
    mathExpect_1 = np.average(signalFirst)
    mathExpect_2 = np.average(signalSec)
    def_1, def_2 = np.std(signalFirst), np.std(signalSec)     #deflection

    for t in range(lngth):
        cov = 0     #covariance

        for l in range(lngth):
            cov += (signalFirst[l]-mathExpect_1)*(signalSec[l+t]-mathExpect_2) / (lngth)

        result.append((cov / def_1 * def_2))

    return result

def autocorrelFunction(signal):
    return correlFunction(signal, signal)

signal1  = signalsGenerator(n,w,N)
signal2 = signalsGenerator(n,w,N)

print('Average: ', np.average(signal1))
print('Dispersion: ', np.var(signal1))

plt.plot(signal1)
plt.plot(signal2)
plt.title('Random generated signals')
plt.xlabel('time')
plt.ylabel('signal')
plt.figure()

plt.plot(autocorrelFunction(signal1))
plt.title('Autocorrelation')
plt.xlabel('time')
plt.ylabel('corr')
plt.figure()

plt.plot(correlFunction(signal1, signal2))
plt.title('Crosscorrelation')
plt.xlabel('time')
plt.ylabel('corr')
plt.show()