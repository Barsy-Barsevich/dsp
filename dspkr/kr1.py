import matplotlib.pyplot as plt
import numpy as np

def vkf(sig_f, base_f, N):
    R = []
    for mu in range(-N+1, N):
        r = 0
#        if mu >= 0:
#            for i in range(mu, N):
#                r += sig_f[i] * base_f[i-mu]
#        else:
#            for i in range(0, N-(-mu)):
#                r += sig_f[i] * base_f[i-mu]
        for i in range(N):
            r += sig_f[i] * base_f[(i-mu)%N]
        R.append(r)
    return R




m1 = [-1,  1, -1,  1,  1, -1, -1]
m2 = [-1,  1,  1, -1,  1, -1, -1]
sm = [ 0,  2,  0,  0,  0,  0, -2]

R = vkf(sm, m1, 7)
print(np.correlate(m1, sm))

plt.plot(R)
plt.grid()
plt.show()
