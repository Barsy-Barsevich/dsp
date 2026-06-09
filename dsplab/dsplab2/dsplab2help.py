import numpy as np
import scipy.integrate as spi

class dsplab2help:
    def __init__(self):
        pass
    
    # Расчет интеграла от комплексной функции
    def integral_complex(self, func, a, b, **kwargs):
        def real_func(x):
            return np.real(func(x))
        def imag_func(x):
            return np.imag(func(x))
        real_integral = spi.quad(real_func, a, b, **kwargs)
        imag_integral = spi.quad(imag_func, a, b, **kwargs)
        integral = (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])
        return integral
    
    # Вычисление коэффициентов ряда Фурье c[-N/2],.., c[0], .., c[N/2-1] (всего N)
    def fourier_coeffs(self, func, N, T):
        result = []
        N1 = -int(N/2)
        N2 = int((N-1)/2)
        for k in range(N1, N2+1):
            ck = (1./T) * self.integral_complex(lambda x: func(x) * np.exp(-1j * 2 *  np.pi * k * x / T), 0,T)[0]
            result.append(ck)
        return np.array(result)
    
    # Аппроксимация (восстановление) функции f(x) при помощи коэффициентов c[k]
    def fourier_fit(self, x, c, T):
        result = 0. + 0.j
        N = len(c)
        N1 = -int(N/2)
        N2 = int((N-1)/2)
        for k in range(N1, N2+1):
            result += c[k+int(N/2)] * np.exp(1j * 2. * np.pi * k * x / T)
        return result
