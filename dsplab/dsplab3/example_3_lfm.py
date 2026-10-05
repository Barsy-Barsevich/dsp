import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import find_peaks

amp = 10 # Максимальная амплитуда сигнала
f0 = 10 # Несущая частота
F = 20 # Полоса сигнала
fs = 500 # Частота дискретизации
N = 500 # Период сигнала в дискретах
T = 1/fs # Период дискретизации
tau = N*T # Период сигнала в секундах

# Пример модулирующего сигнала
Pt = lambda t: np.pi * F / tau * t**2

# Оси времени и частоты
tt = np.linspace(0, tau, N, endpoint=False)
ff = np.linspace(0, fs, N, endpoint=False)

# ЛЧМ-сигнал
s = amp*np.cos(2*np.pi*f0*tt + Pt(tt))

# Амплитудный спектр FМ-сигнала
sft = np.abs(fft(s)) / N
plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.title('LFM-signal')
plt.plot(tt, s)
plt.xlim([0, tau])
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(1, 2, 2)
plt.title('Spectrum')
plt.plot(sft)
plt.plot([f0,f0],[0, np.max(sft)], 'r--')
plt.plot([f0+F,f0+F],[0, np.max(sft)], 'r--')
plt.plot([f0,f0+F],[np.max(sft) / 2, np.max(sft) / 2], 'r--')
plt.annotate((' F=%d'%F), (f0+F, np.max(sft) / 2))
plt.xlim([0, fs/2]) # Ограничение оси до частоты Найквиста (только положительная
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.show()