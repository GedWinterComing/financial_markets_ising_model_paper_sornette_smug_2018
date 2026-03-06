# -*- coding: utf-8 -*-
"""
Created on Fri May 17 19:40:17 2019

@author: Gabriele
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
# definisco l'autovalore
def autovalore1(a,b, theta):
    return (a + theta + np.sqrt((a - theta)**2 + 4*b*(1 - theta)))/2

def autovalore2(a,b, theta):
    return (a + theta - np.sqrt((a - theta)**2 + 4*b*(1 - theta)))/2

n= 1000
a = np.linspace(-5, 5, n)
b = np.linspace(-10, 2, n)
enne=1000
elle1 = np.zeros((n, n))
elle2 = np.zeros((n, n))
for riga in range(n):
    for colonna in range(n):
        elle1[riga,colonna] = np.log2((1/enne)*autovalore1(a[riga],b[colonna],0.50)**enne)
        elle2[riga,colonna] = np.log2((1/enne)*autovalore2(a[riga],b[colonna],0.50)**enne)
#lyapunov3[riga,colonna] += np.log(abs(( 1 - (calcolo_derivata[0])**2)*a_lyapunov[riga]))  # il logaritmo della derivata della funzione logistica
#%%
fig = plt.figure()
scaloelle1 = elle1/(1 - 0.50)  # lo scalo
scaloelle2 = elle2/(1 - 0.50)  # lo scalo
plt.imshow(scaloelle1,cmap='gray')
#plt.xlim(0, n)
#plt.ylim(n, 0)
plt.colorbar()
plt.title("Lyapunov exponent secondo sistema")
fig.savefig('prova Lyapunov.jpg', dpi = 300, transparent = False)
#%%