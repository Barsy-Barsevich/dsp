import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

class dsplab3:
	def init(self):
		self.fs = 812
		self.f0 = 186
		self.deltaT = 31
		self.N = 1024
		self.Ni = 406
		self.A = 0.2
		self.phi0 = np.pi / 3
		self.T = 1 / self.fs

	def form_lfm_2_1_1(self):
		a = self.deltaT * self.T / self.Ni
		b = 2 * self.f0 * self.T
		self.n = np.array([i for i in range(-self.Ni//2, self.Ni//2+1)])
		self.s = np.cos(np.pi * (a*self.n**2 + b*self.n))

	def test_lfm_time_zone(self):
		plt.plot(n, s)
		plt.grid()
		plt.show()

	def test_lfm_freq_zone(self):
		S = np.abs(fft(self.s))
		plt.plot(S)
		plt.grid()
		plt.show()

lab = dsplab3()
lab.init()
lab.form_lfm_2_1_1()
lab.test_lfm_freq_zone()
