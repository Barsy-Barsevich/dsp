import numpy as np

Nlist = 6

fs = 25e3 #800 + 2*Nlist
f0 = 3000 #180 + Nlist
deltaf = 1200 #25 + Nlist
N = 8192 #1024
Ni = 1001 #400 + Nlist
A = 0.3 #Nlist / 30
phi0 = np.pi/4 #2*np.pi / Nlist

# fs = 800 + 2*Nlist
# f0 = 180 + Nlist
# deltaf = 25 + Nlist
# N = 1024
# Ni = 400 + Nlist
# A = Nlist / 30
# phi0 = 2*np.pi / Nlist