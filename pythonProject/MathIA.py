import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
myFile = np.genfromtxt('SPY3.csv', delimiter=',')
dt = 1
t = np.arange(0, 251, dt)
f = myFile
tl = 0.0067 * t + 273.69
cd = f - tl

# Plot 1
fig, axs = plt.subplots(4, 1)
plt.sca(axs[0])
plt.plot(t, f, color='c', LineWidth=1.5, label='SPY')
plt.plot(t, tl, color='k', LineWidth=1.5, label='Trendline')
plt.title('SPY')
plt.legend()

# Plot 2
plt.sca(axs[1])
plt.plot(t, cd, color='c', LineWidth=1.5, label='Corrected (Normalized with TrendLine)')
plt.legend()

# Compute fft
c = fftpack.rfft(cd)
plt.sca(axs[2])
plt.plot(abs(c), color='r', LineWidth=1.5, label='FFT')
plt.legend()
PSD = abs(c)

# Inverse FFT
indices = PSD > 500
cc = indices * c
print(cc)
ic = fftpack.irfft(cc)
plt.sca(axs[3])
plt.plot(ic, color='k', LineWidth=1.5, label='IFFT of basic harmonics')
plt.legend()

x = [2, 3, 5, 7]
print('Basic Frequencies(Hz per trading year):')
print(x)
plt.show()
