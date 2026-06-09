import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from math import atan2

class dsplab2task3:
    def init(self):
        variant = 6
        self.f0 = 1 + (variant % 4)
        self.phi0 = 2*np.pi / (3 + (variant % 4))
        self.N = 128
        self.T = 1 / (3*self.f0 * (variant % 8))
        sign = (-1) ** (variant % 2)
        self.s = sign * (variant % 8)
        self.Ni = 21
        
    def run(self):
        self.init()
    
        fig, axs = plt.subplots(3, 2, figsize=(8, 5))
        fig.tight_layout()
        
        for i in range(2):
            if i == 0:
                s = 0
            else:
                s = self.s
            
            t = np.linspace(0, self.Ni*self.T, self.Ni, endpoint = False) - self.T*(self.Ni//2)
            t1 = t[len(t)//2 - s:]
            sg1 = np.exp(1j * (2 * np.pi * self.f0 * t1 + self.phi0))
            t2 = t[:len(t)//2 - s]
            sg2 = np.exp(1j * (2 * np.pi * self.f0 * t2 + self.phi0))
            #print(len(sg1), len(sg2), len(t1), len(t2))
            #print(t1, t2, sep='\n')
            signal = np.concatenate((sg1, np.zeros(self.N-len(sg1)-len(sg2)), sg2))
            spectre = fftpack.fft(signal)
            A = np.abs(spectre)
            P = np.arctan2(np.imag(spectre), np.real(spectre) + 1e-6)
        
            axs[0, i].set_title(f'Complex signal, shifted {s} left')
            axs[0, i].grid()
            axs[0, i].set_ylabel('Signal ampitude')
            axs[0, i].plot([np.real(s) for s in signal], color='blue')
            axs[0, i].plot([np.imag(s) for s in signal], color='red')
            axs[1, i].set_title('Amplitude spectre')
            axs[1, i].grid()
            axs[1, i].set_ylabel('Spectre magnitude')
            axs[1, i].plot(A, color='blue')
            axs[2, i].set_title('Phase spectre')
            axs[2, i].grid()
            axs[2, i].set_ylabel('Spectre magnitude')
            axs[2, i].plot(P, color='blue')
        
        plt.show()
        
    def __init__(self):
        pass
