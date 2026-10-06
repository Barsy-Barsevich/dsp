import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import find_peaks

amp = 1 # Максимальная амплитуда сигнала
km = 0.45 # Коэффициент модуляции
f0 = 40 # Несущая частота
fm = 12 # Частота модулирующего сигнала
fs = 500 # Частота дискретизации
N = 500 # Период сигнала в дискретах
T = 1/fs # Период дискретизации
tau = N*T # Период сигнала в секундах

# Пример модулирующего сигнала
At = lambda t: amp * (1 + km * np.cos(2*np.pi*fm*t))

# Оси времени и частоты
tt = np.linspace(0, tau, N, endpoint=False)
ff = np.linspace(0, fs, N, endpoint=False)

# АМ-сигнал
s = At(tt)*np.cos(2*np.pi*f0*tt)

# Амплитудный спектр АМ-сигнала
sft = np.abs(fft(s)) / N

# Поиск пиков
ipeaks, _ = find_peaks(sft, height = 0.1)
for i in range(3):
    print(f"Freq = {ipeaks[i]}, Amp = {sft[ipeaks[i]]}")
print(f"Freq differences: {ipeaks[1]-ipeaks[0]}, {ipeaks[1]-ipeaks[2]}, Hz")
plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.title('AM-signal')
plt.plot(tt, s, label='Result AM-Signal')
plt.plot(tt, At(tt), '--', label='Modulation signal')
plt.xlim([0, tau])
plt.grid(True)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(1, 2, 2)
plt.title('Spectrum')
plt.plot(ff, sft)
plt.plot(ipeaks, sft[ipeaks], 'x')
for i in range(3):
    plt.annotate(ipeaks[i], (ipeaks[i], sft[ipeaks[i]]))
plt.xlim([0, fs/2]) # Ограничение оси до частоты Найквиста (только положительная
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.show()