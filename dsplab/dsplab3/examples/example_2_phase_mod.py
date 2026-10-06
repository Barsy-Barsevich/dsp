import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import find_peaks

amp = 1 # Максимальная амплитуда сигнала
km = 10 # Коэффициент модуляции
f0 = 30 # Несущая частота
fm = 5 # Частота модулирующего сигнала
fs = 500 # Частота дискретизации
N = 500 # Период сигнала в дискретах
T = 1/fs # Период дискретизации
tau = N*T # Период сигнала в секундах

# Пример модулирующего сигнала
Pt = lambda t: km / fm * np.sin(2*np.pi*fm*t)

# Оси времени и частоты
tt = np.linspace(0, tau, N, endpoint=False)
ff = np.linspace(0, fs, N, endpoint=False)

# FМ-сигнал
s = amp*np.cos(2*np.pi*f0*tt + Pt(tt))

# Амплитудный спектр FМ-сигнала
sft = np.abs(fft(s)) / N

# Поиск пиков
ipeaks, _ = find_peaks(sft, height = 0.07)
for i in range(5):
    print(f"Freq = {ipeaks[i]}, Amp = {sft[ipeaks[i]]}")
print(f"Freq differences: {ipeaks[1]-ipeaks[0]}, {ipeaks[1]-ipeaks[2]}, Hz")
plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.title('FM-signal')
plt.plot(tt, s, label='Result FM-Signal')
plt.plot(tt, Pt(tt), '--', label='Modulation signal')
plt.xlim([0, tau])
plt.grid(True)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(1, 2, 2)
plt.title('Spectrum')
plt.plot(sft)
plt.plot(ipeaks, sft[ipeaks], 'x')
for i in range(5):
    plt.annotate(ipeaks[i], (ipeaks[i], sft[ipeaks[i]]))
plt.xlim([0, fs/2]) # Ограничение оси до частоты Найквиста (только положительная
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.show()