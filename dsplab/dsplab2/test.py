from matplotlib import pyplot as plt
from scipy import fftpack
import numpy as np

f0 = 1 + (6 % 4)
phi0 = 2 * np.pi / (3 + (6 % 4))
N = 128
T = 1 / (3 * f0 * (1 + 6 % 8))
s = (-1 * (6 % 2)) * (6 % 8)

import math
Ni = 29
fs = 20
T = 1/fs
ts = [i for i in range(N)]
tsi = [i for i in range(Ni)]

#t = np.linspace(0, (Ni-1)*T, Ni, endpoint = False)
#signal = np.exp(1j * (2 * np.pi * f0 * t + phi0))
#sig1 = signal[:(Ni-1)//2]
#sig2 = signal[(Ni-1)//2:(Ni-1)]
#print(len(signal), len(sig1), len(sig2), len(t))
#x = np.concatenate((sig1, np.zeros(N-len(sig1)-len(sig2)), sig2))
t = np.linspace(0, (Ni)*T, Ni, endpoint = False) - T*(Ni//2)
t1 = t[len(t)//2:]
sig1 = np.exp(1j * (2 * np.pi * f0 * t1 + phi0))
t2 = t[:len(t)//2]
sig2 = np.exp(1j * (2 * np.pi * f0 * t2 + phi0))
print(len(sig1), len(sig2), len(t1), len(t2))
print(t1, t2, sep='\n')
signal = np.concatenate((sig1, np.zeros(N-len(sig1)-len(sig2)), sig2))

f = fftpack.fftfreq(len(signal)) * fs
X = fftpack.fft(signal)
A = np.abs(X)

P = [math.atan2(np.imag(i), np.real(i) + 1e-6) for i in X]

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))
axes[0].plot(ts, np.real(signal))
axes[0].plot(ts, np.imag(signal))
axes[0].stem(ts, np.real(signal), markerfmt='o')
axes[0].stem(ts, np.imag(signal), markerfmt='o')
axes[0].grid(True)
axes[0].set_xlabel('Chips')
axes[0].set_ylabel('Signal amplitude')
axes[0].set_xlim(0, N)

axes[1].grid(True)
axes[1].plot(f, A)
axes[1].set_xlabel('Frequency [Hz]')
axes[1].set_ylabel('Spectrum Magnitude')
axes[1].set_xlim(-fs/2, fs/2)

axes[2].grid(True)
axes[2].plot(f, P)
axes[2].set_xlabel('Frequency [Hz]')
axes[2].set_ylabel('Phase / pi')
axes[2].set_xlim(-fs / 2, fs/ 2)
axes[2].set_ylim(-np.pi, np.pi)

fig.tight_layout()
plt.show()

