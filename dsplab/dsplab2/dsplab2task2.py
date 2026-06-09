import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

class dsplab2task2:
    def init(self):
        self.A1 = 2
        self.A2 = 3
        self.f01 = 6
        self.f02 = 1
        self.phi01 = 3*np.pi/4
        self.phi02 = 2*np.pi/6
        self.fs = 64
        self.tau = 1
        self.Anoise = 2
        self.K = 0.25 * 7
        self.phi = np.linspace(0, self.fs, self.fs, endpoint = False)
        self.sg1 = self.A1*np.cos(self.phi01 + self.phi * (self.f01*2*np.pi / self.fs))
        self.sg2 = self.A2*np.cos(self.phi02 + self.phi * (self.f02*2*np.pi / self.fs))
        self.sgsum = self.sg1 + self.sg2
    
    def test_sg(self):
        self.init()
        plt.plot(self.phi, self.sg1)
        plt.plot(self.phi, self.sg2)
        plt.grid()
        plt.show()
    
    def run(self):
        self.init()
        fig, axs = plt.subplots(4, 2, figsize=(8, 5))
        #fig.tight_layout(rect=[0, 0, 1, 0.995], pad=3.0)
        random_vector = self.Anoise * np.random.rand(len(self.sgsum))
        for row in range(4):
            if row == 0:
                signal = self.sgsum
            elif row == 1:
                signal = self.sgsum + random_vector
            elif row == 2:
                signal = self.sgsum + random_vector + self.K
            else:
                signal = np.concatenate((self.sgsum, np.zeros(512-len(self.sgsum))))
            
            spectre = fftpack.fft(signal)
            A = np.abs(spectre)
            P = np.arctan2(np.imag(spectre), np.real(spectre))
            
            axs[row, 0].set_title('Amplitude spectre')
            axs[row, 0].grid(True)
            axs[row, 0].set_ylabel('Spectre magnitude')
            axs[row, 0].stem(A)
            axs[row, 1].set_title('Phase spectre')
            axs[row, 1].grid(True)
            axs[row, 1].set_ylabel('Spectre phase, pi')
            axs[row, 1].stem(P*1/np.pi)
        plt.show()
    
    def __init__(self):
        pass
