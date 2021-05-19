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


#  Discrete Fourier Transform Coefficient
def fCoeff(pk, N):
    exp = 2*np.pi*pk/N
    return complex(np.cos(exp), -np.sin(exp))


# Discrete Fourier Transform
def fTransform(signals):
    N = len(signals)
    spect=[]
    for p in range (N):
        sum = 0
        for k in range(N):
            sum+= signals[k] * fCoeff(p*k, N)
        spect.append(abs(sum))

    return spect


signal  = signalsGenerator(n,w,N)


plt.plot(signal)
plt.title('Random generated signals')
plt.xlabel('time')
plt.ylabel('signal')
plt.figure()

plt.plot(fTransform(signal))
plt.title('Descrete Fourier Transform')
plt.xlabel('p')
plt.ylabel('F(p)')
plt.show()

