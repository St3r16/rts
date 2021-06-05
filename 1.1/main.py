import numpy as np      # math operations
import matplotlib.pyplot as plt     #graphs
import time

n = 10      # harmonics 
w = 2700    #frequency
N = 256     # discrete calls

signals = np.zeros(N)      #array 
W = w / n
time_list = []
start_time = time.time()
for harmonic in range(n):
    amplitude = np.random.rand()
    phase = np.random.rand()
    
    for t in range(100,10001, 100):
        signals=np.zeros(t+1)
        signals[t] += (amplitude * np.sin(W * t + phase))
        end_time = time.time()

    res = end_time - start_time
    time_list.append(res)

    W += W
print(time_list)
#print('Average: ', np.average(signals))
#print('Dispersion: ', np.var(signals))

#plt.plot(signals)
#plt.title('Random generated signals')
#plt.xlabel('time')
#plt.ylabel('signal')
#plt.show()
plt.plot(time_list, [100,200,300,400,500,600,700,800,900,1000])
plt.title('Random generated signals')
plt.xlabel('time')
plt.ylabel('signal')
plt.show()