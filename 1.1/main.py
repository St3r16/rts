import numpy as np      # math operations
import matplotlib.pyplot as plt     #graphs

n = 10      # harmonics 
w = 2700    #frequency
N = 256     # discrete calls

signals = np.zeros(N)      #array 
W = w / n

for harmonic in range(n):
    amplitude = np.random.rand()
    phase = np.random.rand()
    
    for t in range(N):
        signals[t] += (amplitude * np.sin(W * t + phase))

    W += W

print('Average: ', np.average(signals))
print('Dispersion: ', np.var(signals))

plt.plot(signals)
plt.title('Random generated signals')
plt.xlabel('time')
plt.ylabel('signal')
plt.show()