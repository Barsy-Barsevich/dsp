import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import find_peaks

# Параметры сигнала
amp = 1
fs = 500 # Частота дискретизации, Гц

f0 = 100 # Несущая частота, Гц
fm = 10 # Частота модуляции, Гц
N = 1000 # Отсчетов в периоде сигнала
T = 1/fs # Период дискретизации
tau = N*T # Период сигнала в секундах

# Модулирующий сигнал
Pt = lambda t: 2*np.pi*fm*t

# Оси времени и частоты
tt = np.linspace(0, tau, N, endpoint=False)
ff = np.linspace(0, fs, N, endpoint=False)

# FМ-сигнал
s = amp*np.cos(2*np.pi*f0*tt + Pt(tt))

# Амплитудный спектр FМ-сигнала
sft = np.abs(fft(s)) / N

# Поиск пиков
ipeaks, _ = find_peaks(sft, height = 0.07)
plt.figure(figsize=(16, 16))
plt.subplot(3, 2, 1)
plt.title('FM-signal')
plt.plot(tt, s)
plt.xlim([0, tau])
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(3, 2, 2)
plt.title('Spectrum')
plt.plot(ff, sft)
plt.plot(ff[ipeaks], sft[ipeaks], 'x')
plt.annotate(('f0+fm = %d Hz'%ff[ipeaks[0]]), (ff[ipeaks[0]], sft[ipeaks[0]]))
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

# Снятие с несущей частоты
s_demod = s * np.cos(2*np.pi*f0*tt)

# Идеальный ФНЧ в часотной области
lowpass = np.ones(N)
fc = 150 # Частота среза
Nc = int(np.round(fc*N/fs))
lowpass[Nc:N-Nc] = 0

# Спектры сигнала до фильтра и после
spec = fft(s_demod)
spec_lowpass = spec * lowpass
aspec = np.abs(spec) / N
aspec_lowpass = np.abs(spec_lowpass) / N
s_demod_lowpass = ifft(spec_lowpass)

# Поиск пиков
ipeaks, _ = find_peaks(aspec_lowpass, height = 0.07)

plt.subplot(3, 2, 3)
plt.title('Demodulated signal')
plt.plot(tt, s_demod)
plt.xlim([0, tau])
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(3, 2, 4)
plt.title('Spectrum')
plt.plot(ff, aspec, label='Demod. signal spectrum')
plt.plot(ff, lowpass*np.max(aspec)*0.95, 'b--', label='Lowpass filter spectrum')
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.legend()
plt.subplot(3, 2, 5)
plt.title('Demodulated filtered signal')
plt.plot(tt, np.real(s_demod_lowpass), label='real')
plt.plot(tt, np.imag(s_demod_lowpass), label='imag')
plt.xlim([0, tau])
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.subplot(3, 2, 6)
plt.title('Spectrum')
plt.plot(ff, aspec_lowpass)
plt.plot(ff[ipeaks], aspec_lowpass[ipeaks], 'x')
plt.annotate(('fm = %d Hz'%ff[ipeaks[0]]), (ff[ipeaks[0]], aspec_lowpass[ipeaks[0]]))
plt.grid(True)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.show()