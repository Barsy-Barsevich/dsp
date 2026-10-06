import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

import dsplab3_param as param

# Time of 1 sample
sample_time = 1 / param.fs

a = param.deltaf * sample_time / param.Ni
b = 2 * param.f0 * sample_time
lfm_s = lambda n: np.cos(np.pi * (b*n + a*n*n))

# Forming LFM impulse, plot spectrums
# counter = 0
# frequency_array = []
# for i in range(-param.N//2, param.N//2):
#     if (i >= -(param.Ni-1)//2) and (i < (-param.Ni-1)//2+param.Ni):
#         n = i
#         s.append(lfm_s(n))
#     else:
#         s.append(0)
#     frequency_array.append(param.fs / param.N * counter)
#     counter += 1

# Make frequency array
counter = 0
frequency_array = []
time_array = []
for i in range(param.N):
    frequency_array.append(param.fs / param.N * counter)
    time_array.append(sample_time * counter)
    counter += 1

s = []
for i in range(param.N):
    if i > param.N/2:
        n = i - param.N
    else:
        n = i
    if (n >= -(param.Ni-1)//2) and (n < (-param.Ni-1)//2+param.Ni):
        s.append(lfm_s(n))
    else:
        s.append(0)

plt.plot(s)
plt.title('LFM signaali, ajanalue')
plt.show()

S = np.fft.fft(s)

plt.figure(figsize=(20, 5))
plt.subplot(1, 2, 1)
plt.title('LFM Amplitude spectrum')
plt.plot(frequency_array, np.abs(S))
plt.grid()
plt.legend()
plt.xlabel('Frequency, Hz')
plt.ylabel('A*Ni, V')
theoretical_magnitude = 1 / 2 * np.sqrt(param.Ni / param.deltaf / sample_time)
plt.plot([param.f0-param.deltaf/2, param.f0-param.deltaf/2], [0, np.max(np.abs(S))], 'r--')
plt.plot([param.f0+param.deltaf/2, param.f0+param.deltaf/2], [0, np.max(np.abs(S))], 'r--')
plt.plot([param.f0-param.deltaf/2, param.f0+param.deltaf/2], [theoretical_magnitude, theoretical_magnitude], 'r--')
plt.annotate((' f0=%d'%param.f0), (param.f0+param.deltaf/2, np.max(np.abs(S)) / 2))
plt.subplot(1, 2, 2)
plt.title('LFM Phase spectrum')
plt.plot(frequency_array, np.angle(S))
plt.grid()
plt.xlabel('Frequency, Hz')
plt.ylabel('Phase offset, rad')
plt.show()

# Forming reflected LFM impulse
c = param.phi0 / np.pi
lfm_s_ref = lambda n: param.A * np.cos(np.pi * (b*n + a*n*n + c))

s_ref = []
# for i in range(param.N):
#     if i > param.N/2:
#         n = i - param.N
#     else:
#         n = i
#     if (n >= -(param.Ni-1)//2) and (n < (-param.Ni-1)//2+param.Ni):
#         s_ref.append(lfm_s_ref(n))
#     else:
#         s_ref.append(0)

for i in range(-param.N//2, param.N//2):
    if (i >= -(param.Ni-1)//2) and (i < (-param.Ni-1)//2+param.Ni):
        n = i
        s_ref.append(lfm_s_ref(n))
    else:
        s_ref.append(0)

plt.plot(s_ref)
plt.title('Vastettu LFM signaali, ajanalue')
plt.show()

S_ref = np.fft.fft(s_ref)

plt.figure(figsize=(20, 5))
plt.subplot(1, 2, 1)
plt.title('LFM Amplitude spectrum')
plt.plot(frequency_array, np.abs(S_ref))
plt.grid()
plt.legend()
plt.xlabel('Frequency, Hz')
plt.ylabel('A*Ni, V')
theoretical_magnitude = param.A / 2 * np.sqrt(param.Ni / param.deltaf / sample_time)
plt.plot([param.f0-param.deltaf/2, param.f0-param.deltaf/2], [0, np.max(np.abs(S_ref))], 'r--')
plt.plot([param.f0+param.deltaf/2, param.f0+param.deltaf/2], [0, np.max(np.abs(S_ref))], 'r--')
plt.plot([param.f0-param.deltaf/2, param.f0+param.deltaf/2], [theoretical_magnitude, theoretical_magnitude], 'r--')
plt.annotate((' f0=%d'%param.f0), (param.f0+param.deltaf/2, np.max(np.abs(S_ref)) / 2))
plt.subplot(1, 2, 2)
plt.title('LFM Phase spectrum')
plt.plot(frequency_array, np.angle(S_ref))
plt.grid()
plt.xlabel('Frequency, Hz')
plt.ylabel('Phase offset, rad')
plt.show()

# Decoding reflected signal
lfm_s_dec = lambda n: lfm_s_ref(n) * np.e**(-1j * 2 * np.pi * param.f0 * n * sample_time)

s_dec = []
# for i in range(param.N):
#     if i > param.N/2:
#         n = i - param.N
#     else:
#         n = i
#     if (n >= -(param.Ni-1)//2) and (n < (-param.Ni-1)//2+param.Ni):
#         s_dec.append(lfm_s_dec(n))
#     else:
#         s_dec.append(0)

for i in range(-param.N//2, param.N//2):
    if (i >= -(param.Ni-1)//2) and (i < (-param.Ni-1)//2+param.Ni):
        n = i
        s_dec.append(lfm_s_dec(n))
    else:
        s_dec.append(0)

S_dec = np.fft.fft(s_dec)

plt.figure(figsize=(20, 5))
plt.subplot(1, 2, 1)
plt.title('Decoded LFM signal')
plt.plot(time_array, np.real(s_dec))
plt.plot(time_array, np.imag(s_dec))
plt.grid()
plt.legend()
plt.xlabel('Time, s')
plt.ylabel('A, V')
plt.subplot(1, 2, 2)
plt.title('Decoded LFM Amplitude spectrum')
plt.plot(frequency_array, np.abs(S_dec))
plt.grid()
plt.xlabel('Frequency, Hz')
plt.ylabel('A*Ni, V')
plt.show()

# Process signal via ideal low-pass filter
fc = param.f0 #3000
lowpass = np.ones(param.N)
Nc = int(np.round(fc * param.N/param.fs))
lowpass[Nc:param.N-Nc] = 0

S_dec_filtered = S_dec * lowpass
s_filtered = np.fft.ifft(S_dec_filtered)

plt.plot(time_array, s_filtered)
plt.title('Suodettu LFM signaali, ajanalue')
plt.show()

# Form impulse response
h_n = lambda n: np.e**(-1j * np.pi * a * n**2)
h = []
# for i in range(param.N):
#     if i > param.N/2:
#         n = i - param.N
#     else:
#         n = i
#     if (n >= -(param.Ni-1)//2) and (n < (-param.Ni-1)//2+param.Ni):
#         h.append(h_n(n))
#     else:
#         h.append(0)

for i in range(-param.N//2, param.N//2):
    if (i >= -(param.Ni-1)//2) and (i < (-param.Ni-1)//2+param.Ni):
        n = i
        h.append(h_n(n))
    else:
        h.append(0)

H = np.fft.fft(h)

plt.figure(figsize=(20, 5))
plt.subplot(1, 3, 1)
plt.title('LFM impulse response')
plt.plot(time_array, np.real(h))
plt.plot(time_array, np.imag(h))
plt.grid()
plt.legend()
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.subplot(1, 3, 2)
plt.title('LFM impulse response Amplitude spectrum')
plt.plot(frequency_array, np.abs(H))
plt.grid()
plt.xlabel('Frequency, Hz')
plt.ylabel('Magnitude')
plt.subplot(1, 3, 3)
plt.title('LFM impulse response Phase spectrum')
plt.plot(frequency_array, np.angle(H))
plt.grid()
plt.xlabel('Frequency, Hz')
plt.ylabel('Magnitude')
plt.show()

# Form compressed
s_compressed = np.fft.ifft(S_dec_filtered * H)

plt.plot(time_array, np.real(s_compressed), label='real')
plt.plot(time_array, np.imag(s_compressed), label='imag')
plt.plot(time_array, np.abs(s_compressed), label='abs')
plt.legend()
plt.grid()
plt.show()