import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

# Create f data
myFile = np.genfromtxt('SPY2.csv', delimiter=',')
dt = 1
t = np.arange(0, 335, dt)
f = myFile
# f = np.sin(2*np.pi*50*t)
tl = 0.6291*t + 36.461
cd = f - tl

# Plot f
fig, axs = plt.subplots(4, 1)
plt.sca(axs[0])
plt.plot(t, f, color='c', LineWidth=1.5, label='SPY')
plt.plot(t, tl, color='k', LineWidth=1.5, label='trend')
plt.xlim(t[0], t[-1])
plt.legend()

# corrected
plt.sca(axs[1])
plt.plot(t, cd, color='c', LineWidth=1.5, label='Corrected')
plt.xlim(t[0], t[-1])
plt.legend()

# Compute fft
n = len(t)
fhat = np.fft.fft(cd, n)
#PSD = fhat * np.conj(fhat) / n
PSD = abs(fhat)
freq = (1 / (dt * n)) * np.arange(n)
L = np.arange(1, np.floor(n / 2), dtype='int')
plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label='PSD')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()
plt.show()

# IFFT
indices = PSD > 100
PSDclean = PSD * indices
print(PSDclean)
fhat = indices * fhat
ffilt = np.fft.ifft(fhat)
PSDN = ffilt * np.conj(ffilt) / n
print(ffilt)
plt.sca(axs[3])
plt.plot(t, PSDclean, color='c', LineWidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()
plt.show()
