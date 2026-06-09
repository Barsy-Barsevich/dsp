import numpy as np
import matplotlib.pyplot as plt
import dsplab2help

class dsplab2task1:
    def f(self, x):
        x %= 2*np.pi
        x = np.abs(x)
        return np.where(np.pi/2 < x, np.where(x <= 3*np.pi/2, 1, -1), -1)
        
    ## Test of f(x)
    #a = []
    #b = []
    #for i in range(1000):
    #    b.append(i*2/1000)
    #    a.append(f(i*2*np.pi/1000))
    #plt.plot(b, a)
    #plt.show()

    def init(self):
        self.dsplabhelp = dsplab2help.dsplab2help()
        # Исходные данные
        self.T = 2*np.pi # Период
        self.x1 = np.pi  # Нижняя граница области определения функции
        self.x2 = -np.pi # Верхняя граница области определения функции
        self.Nx = 100    # Дискретизация по оси X
        # Ось X
        self.x_range = np.linspace(self.x1, self.x2, self.Nx)
        # Эталонные кривые исходной функции f(x)
        self.y_true = self.f(self.x_range)
        self.y_true_real = [y.real for y in self.y_true]
        self.y_true_imag = [y.imag for y in self.y_true]
    
    # Вычисление коэффициентов, аппроксимация, построение графиков при разных N
    def run(self):
        N_all = [1, 3, 7, 15]        
        fig, axs = plt.subplots(len(N_all), 2, figsize=(8, 5))
        fig.tight_layout(rect=[0, 0, 1, 0.95], pad=3.0)
        row = 0
        for N in N_all:
            C = self.dsplabhelp.fourier_coeffs(self.f, N, self.T)
            print(f'Fourier coeffs for N=={N}: ', end='')
            for elem in C: print(f'{np.real(elem):.3f}, ', end='')
            print('')
            y_approx = self.dsplabhelp.fourier_fit(self.x_range, C, self.T)
            y_approx_real = [y.real for y in y_approx]
            y_approx_imag = [y.imag for y in y_approx]
            axs[row, 0].set_title('real part, case N=' + str(N))
            axs[row, 1].set_title('imag part, case N=' + str(N))
            axs[row, 0].grid(True)
            axs[row, 1].grid(True)
            axs[row, 0].scatter(self.x_range, self.y_true_real, color='blue', s=1, marker='.')
            axs[row, 0].scatter(self.x_range, y_approx_real, color='red', s=2, marker='.')
            axs[row, 1].scatter(self.x_range, self.y_true_imag, color='blue', s=1, marker='.')
            axs[row, 1].scatter(self.x_range, y_approx_imag, color='red', s=2, marker='.')
            row += 1
        plt.show()
    
    def __init__(self):
        pass

