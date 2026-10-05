import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import find_peaks

from example_3_lfm import *

# Зависимости частоты от времени
ft_s = f0-F/2+F/tau*tt
tt_h = np.linspace(tau, 0, N, endpoint=False)
ft_h = f0-F/2+F/tau*tt_h

# Комплексный ЛЧМ
ss = amp*np.exp(1j*(2*np.pi*f0*tt + Pt(tt)))

# ИХ ЛЧМ-сигнала
h = np.cos(2*np.pi*f0*tt_h + Pt(tt_h))
hh = np.exp(-1j*(2*np.pi*f0*tt_h + Pt(tt_h)))

# Отображение
plt.figure(figsize=(20, 10))
plt.subplot(2, 3, 1)
plt.title('f(t) for LFM signal')
plt.plot(tt, ft_s)
plt.plot([0, tau], [f0, f0], 'r--')
plt.annotate((' f0=%d Hz'%f0), (tau/3, 1.025*f0))
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.subplot(2, 3, 2)
plt.title('LFM signal')
plt.plot(tt, s)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(2, 3, 3)
plt.title('LFM impulse response')
plt.plot(tt, h)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(2, 3, 4)
plt.title('f(t) for impulse response')
plt.plot(tt, ft_h)
plt.plot([0, tau], [f0, f0], 'r--')
plt.annotate((' f0=%d Hz'%f0), (2*tau/3, 1.025*f0))
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.subplot(2, 3, 5)
plt.title('LFM signal')
plt.plot(tt, np.real(ss), label='real')
plt.plot(tt, np.imag(ss), label='imag')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.subplot(2, 3, 6)
plt.title('LFM impulse response')
plt.plot(tt, np.real(hh), label='real')
plt.plot(tt, np.imag(hh), label='imag')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.show()