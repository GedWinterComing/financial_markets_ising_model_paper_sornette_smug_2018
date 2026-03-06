# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:11:06 2019

@author: Gabriele
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:23:19 2019

@author: Gabriele
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
# definisco la funzione logistica
def ising_mappa(beta, H, s):
    return np.tanh(beta * (s + H))
#%%
# definisco la funzione per plottare la mappa
def disegna_mappa(beta, H, s0, n, ax=None):
    # disegno la funzione e la retta diagonale y=x
    t = np.linspace(-1, 1)  # crea 50 punti equispaziati tra 0 e 1 compresi
    ax.plot(t, ising_mappa(beta, H, t), 'blue', lw=3)  # ln = linewidth
    ax.plot([-1, 1], [-1, 1], 'grey', lw=1)

    # Applico recursivamente y=f(x) e disegno le due linee, però nel caso di x0 deve partire dall'asse x
    # Punti disegnati:
    # (x,0) oppure (x, x) --> (x, y)
    # (x, y) --> (y, y)
    s = s0
    for i in range(n):
        y = ising_mappa(beta, H, s)
        # Disegno le due linee
        if i==0:
            ax.plot([s, s] , [0, y], 'k', lw=1)
            ax.plot([s, y] , [y, y], 'k', lw=1)  # separati
        else:
                ax.plot([s,s,s,y] , [s,y,y,y], 'k', lw=1)  # o tutti assieme
        
        # aumento l'opacità (alpha) del punto ad ogni interazione
        ax.plot([s], [y], 'ok', ms=10, alpha=(i + 1) / n)
        s = y  # preparo per l'interazione successiva

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title('Ising')
    ax.set_xlabel('$s_t$')
    ax.set_ylabel('$s_{t+1}$')
    ax.grid()
#%%
def disegna_generazione(beta, H, s0, n, ax=None):
    # disegno la popolazione rispetto alla generazione
    # generazione = np.linspace(0,anni,anni)  # NON va bene! Non sono numeri interi e poi genera N punti da 0 a N e non da 0 a N-1
    generazione = np.zeros(n)
    popolazione = np.zeros(n)
    
    for i in range(n):
        if i ==0:
            popolazione[i] = s0
        else:
            popolazione[i] = ising_mappa(beta, H, popolazione[i-1])
            generazione[i] = i

    ax.plot(generazione , popolazione, 'green', lw=1)  # figo con lw=3 , però poi il grafico è poco visibile
    ax.set_ylim(-1, 1)
    ax.set_title('Periodo Ising')
    ax.set_xlabel('tempo $t$')
    ax.set_ylabel('opinione $s_t$')
    ax.grid()
#%%
# PER ISING PRIMO SISTEMA DEL PAPER CON UN'UNICA EQUAZIONE

fig, ax = plt.subplots(2, 2, figsize=(14, 14), sharey=True)

s0 = .8
turni = 100

beta1 = 3
H1 = -0.4
beta2 = 1
H2 = 0

# Cuspide per H=0 e beta=1

disegna_mappa(beta1, H1, s0, turni, ax[0, 0])
disegna_generazione(beta1, H1, s0, turni, ax[0, 1])
disegna_mappa(beta2, H2, s0, turni, ax[1, 0])
disegna_generazione(beta2, H2, s0, turni, ax[1, 1])
fig.savefig('Ising mappa.jpg', dpi = 300, transparent = False)
#%%
H = 0
n = 10000
beta = np.linspace(0.0, 4.0, n)  # n punti per r tra 2,5 e 4. Ovvero ho 10000 valori diversi di r
iterations = 1000
last = 100
s = 1e-5 * np.ones(n)  # il punto iniziale per tutti: x_0 = 0.00001
lyapunov = np.zeros(n)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), sharex=True)  # disegno sia il grafico con gli r che quello con l'esponente
for i in range(iterations):
    s = ising_mappa(beta, H, s)  # calcola una iterazione delle mappe dei 10000 r
    # Calcoliamo la somma pariale dell'esponente Lyapunov. Ad ogni ciclo sommo il nuovo esponente calcolato al precedente
    lyapunov += np.log(abs(( 1 - (ising_mappa(beta, H, s))**2)*beta ))  # il logaritmo della derivata della funzione logistica
    # disegno il diagramma delle biforcazioni
    # faccio 1000 iterazioni però per il grafico delle biforcazioni prendo solo le last, cioè 100 quando la mappa si è già fissata
    if i >= (iterations - last):
        ax1.plot(beta, s, ',k', alpha=.25)
ax1.set_xlim(0, 4)  # mostro solo il range di beta interessanti
ax1.set_ylim(-1, 1)
ax1.set_title("Bifurcation diagram")

# Ora invece mostriamo il grafico dello Lyapunov exponent.
# Horizontal line.
ax2.axhline(0, color='k', lw=.5, alpha=.5)  # disegna una retta a y=0 cioè l'asse x
# Negative Lyapunov exponent.
# N.B.: r è un vettore! Per questo c'è r[]
# Prendo tutte le posizioni nel vettore degli r alle quali corrispondono esponenti negativi nel vettore lyapunov. Cioè tutti gli r per i quali ho trovato un lyapunov negativo 
ax2.plot(beta[lyapunov < 0], lyapunov[lyapunov < 0] / iterations, '.k', alpha=.5, ms=.5)
# Positive Lyapunov exponent.
ax2.plot(beta[lyapunov >= 0], lyapunov[lyapunov >= 0] / iterations, '.r', alpha=.5, ms=.5)
ax2.set_xlim(0.0, 4)
ax2.set_ylim(-1, 1)
ax2.set_title("Lyapunov exponent")
plt.tight_layout()
fig.savefig('Ising Biforcazioni ed esponente Lyapunov.jpg', dpi = 300, transparent = False)


#%%
#%%

# il terzo sistema di campo medio del paper
def ising_mappa3(a, b, theta, k, H, s):
    s1 = np.tanh(a * s + b * H)
    H1 = theta*H + (1-theta)*s
    a = a + k
    # a += k  # perchè non sono sicuro che funzioni
    
    s = s1
    H = H1
    #return np.array([s, H, a])
    return s, H, a
#%%
# definisco la funzione per plottare la mappa del terzo sistema del paper
def disegna_mappa3(a, b, theta, k, H, s0, n, ax=None):
    # disegno la funzione e la retta diagonale y=x
    t = np.linspace(-1, 1)  # crea 50 punti equispaziati tra 0 e 1 compresi
    mercato = ising_mappa3(a, b, theta, k, H, t)
    ax.plot(t, mercato[0], 'blue', lw=3)  # ln = linewidth
    ax.plot([-1, 1], [-1, 1], 'grey', lw=1)

    # Applico recursivamente y=f(x) e disegno le due linee, però nel caso di x0 deve partire dall'asse x
    # Punti disegnati:
    # (x,0) oppure (x, x) --> (x, y)
    # (x, y) --> (y, y)
    s = s0
    for i in range(n):
        y = ising_mappa3(a, b, theta, k, H, s)
        # ora però y=(s,H,a) ma io voglio solo s, il primo numero del vettore, perciò
        H = y[1]
        a = y[2]
        y = y[0]
        # Disegno le due linee
        if i==0:
            ax.plot([s, s] , [0, y], 'k', lw=1)
            ax.plot([s, y] , [y, y], 'k', lw=1)  # separati
        else:
                ax.plot([s,s,s,y] , [s,y,y,y], 'k', lw=1)  # o tutti assieme
        
        # aumento l'opacità (alpha) del punto ad ogni interazione
        ax.plot([s], [y], 'ok', ms=10, alpha=(i + 1) / n)
        s = y  # preparo per l'interazione successiva

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title('Ising')
    ax.set_xlabel('$s_t$')
    ax.set_ylabel('$s_{t+1}$')
    ax.grid()
#%%
# definisco la funzione per plottare l'evoluzione nel tempo del terzo sistema del paper
def disegna_generazione3(a, b, theta, k, H, s0, n, ax=None):
    # disegno la magnetizzazione del mercato rispetto al tempo
    generazione = np.zeros(n)
    popolazione = np.zeros(n)
    
    for i in range(n):
        if i ==0:
            popolazione[i] = s0
        else:
            y = ising_mappa3(a, b, theta, k, H, popolazione[i-1])
            # ora però y=(s,H,a) ma io voglio solo s, il primo numero del vettore, perciò
            H = y[1]
            a = y[2]
            popolazione[i] = y[0]
            generazione[i] = i

    ax.plot(generazione , popolazione, 'green', lw=1)  # figo con lw=3 , però poi il grafico è poco visibile
    ax.set_ylim(-1, 1)
    ax.set_title('Periodo Ising')
    ax.set_xlabel('tempo $t$')
    ax.set_ylabel('opinione $s_t$')
    ax.grid()
#%%
# PER ISING TERZO SISTEMA DEL PAPER CON 3 EQUAZIONI

fig, ax = plt.subplots(2, 2, figsize=(14, 14), sharey=True)

# devi indicare (a, b, theta, k, H, s, n, ax)
# se vuoi usare beta allora devi fare che:  a = b = beta
# e per il caso semplice della prima equazione: k=0, theta=0, H_(t+1) = H_t = H_0

turni = 200

s0 = .5
H0 = -0.5

theta = 0.50
#theta=0.99
#theta=0.00
k = 0
#k = 0.04


a1 = -4.17
b1 = -8.53
#a1=-2
#b1=-1
#b1=-1  # caso (1) b)
#a1=-1 + b1*((1-theta)/(1+theta))  # caso (1) b)



a2 = 4
b2 = -2.8
#a2=-1.5
#b2=1
#b2=-1  # caso (1) c)
#a2=(1+b2*(1-theta))/(theta)  # caso (1) c)


disegna_mappa3(a1, b1, theta, k, H0, s0, turni, ax[0, 0])
disegna_generazione3(a1, b1, theta, k, H0, s0, turni, ax[0, 1])
disegna_mappa3(a2, b2, theta, k, H0, s0, turni, ax[1, 0])
disegna_generazione3(a2, b2, theta, k, H0, s0, turni, ax[1, 1])
fig.savefig('Ising terza mappa.jpg', dpi = 300, transparent = False)
#%%












# TUTTO SBAGLIATO DA QUA IN POI
punti_biforcazioni = 10000
a_lyapunov_bif = np.linspace(-12.0, 5.0, punti_biforcazioni)
b_lyapunov_bif = a_lyapunov_bif  # perchè qua è come se usassi solo beta quindi a=b cioè sto facendo il secondo sistema
n = 100  # dopo provare anche con 1000 ma troppo lungo
theta_ly = 0.50
H = -0.5
H_bifurc = -0.5
k_lyapunov = 0
a_lyapunov = np.linspace(-12.0, 5.0, n)  # n punti per r tra 2,5 e 4. Ovvero ho 10000 valori diversi di r
b_lyapunov = a_lyapunov  # perchè qua è come se usassi solo beta quindi a=b cioè sto facendo il secondo sistema
iterations = 1000 # dopo provare anche con 1000
last = 100 # dopo provare anche con 100
s = 0.5 # per ora, perchè c'è un errore, in quanto in questa versione del codice s non è un array perchè ne faccio una alla volta
s_bifurc = s * np.ones(punti_biforcazioni)  # il punto iniziale per tutti: x_0 = 0.00001
lyapunov3 = np.zeros((n,n))  #ci vuole la doppia parentesi perchè le dimensioni della matrice vanno tra parentesi
fig = plt.figure()

for i in range(iterations):
    s_bifurc = ising_mappa3(a_lyapunov_bif, b_lyapunov_bif, theta_ly, k_lyapunov, H_bifurc, s_bifurc)  # calcola una iterazione delle mappe dei 10000 r
    H_bifurc = s_bifurc[1]
    # a = s[2]
    s_bifurc = s_bifurc[0]
    for riga in range(n):
            for colonna in range(n):                    
                    derivata = ising_mappa3(a_lyapunov[riga], b_lyapunov[colonna], theta_ly, k_lyapunov, H, s)
                    s = derivata[0]
                    calcolo_derivata = ising_mappa3(a_lyapunov[riga], b_lyapunov[colonna], theta_ly, k_lyapunov, H, s)
                    # perchè devi calcolare la mappa e poi col suo risultato lo usi come s della derivata della mappa
                    # l'H che devi usare è quello della prima volta
                    H = derivata[1]

                    # Calcoliamo la somma pariale dell'esponente Lyapunov. Ad ogni ciclo sommo il nuovo esponente calcolato al precedente
                    # però poi serve solo la tanh cioè il primo elemento del vettore derivata
                    lyapunov3[riga,colonna] += np.log(abs(( 1 - (calcolo_derivata[0])**2)*a_lyapunov[riga]))  # il logaritmo della derivata della funzione logistica
    if i >= (iterations - last):
        # disegno il diagramma delle biforcazioni
        # faccio 1000 iterazioni però per il grafico delle biforcazioni prendo solo le last, cioè 100 quando la mappa si è già fissata
        plt.plot(a_lyapunov_bif, s_bifurc, ',k', alpha=75)
plt.title("Bifurcation diagram secondo sistema")
plt.xlim(-12, 5)  # mostro solo il range di beta interessanti
plt.ylim(-1, 1)
plt.tight_layout()
fig.savefig('Ising biforcazioni seconda mappa.jpg', dpi = 300, transparent = False)

fig = plt.figure()
lyapunov3 = lyapunov3/(1-theta_ly)  # lo scalo
plt.imshow(lyapunov3,cmap='gray')
#plt.xlim(0, n)
#plt.ylim(n, 0)
plt.colorbar()
plt.title("Lyapunov exponent secondo sistema")
fig.savefig('Ising esponente Lyapunov seconda mappa.jpg', dpi = 300, transparent = False)



#%%
# ALCUNI GRAFICI:
#%%
theta_co = 0.99
# theta_co = 0.50
# theta_co = 0.001
b_co = np.linspace(-3,3,100)
a_co_one1 = np.zeros(100)
a_co_one2 = np.zeros(100)
a_co_one3 = np.zeros(100)
a_co_one1 = -b_co + 1
a_co_one2 = (b_co*(1-theta_co))/(1+theta_co) - 1
a_co_one3 = (1 + b_co*(1-theta_co))/theta_co
plt.plot(a_co_one1,b_co, 'black')
plt.plot(a_co_one2,b_co, 'red')
plt.plot(a_co_one3,b_co, 'green')
plt.xlim(-4, 4) 
plt.ylim(-3,3)
#%%
# SBAGLIATO
from mpl_toolkits import mplot3d

fig = plt.figure()
axco = plt.axes(projection='3d')
axco.set_xlabel('a')
axco.set_ylabel('b')
axco.set_zlabel('theta')


range_theta_co_two = 100
b_co_two1 = np.zeros(range_theta_co_two)
b_co_two2 = np.zeros(range_theta_co_two)
b_co_two3 = np.zeros(range_theta_co_two)
a_co_two1 = np.zeros(range_theta_co_two)
a_co_two2 = np.zeros(range_theta_co_two)
a_co_two3 = np.zeros(range_theta_co_two)
theta_co_two = np.linspace(0,1,range_theta_co_two)

for i in range(range_theta_co_two):
    a_co_two1[i] = -theta_co_two[i] + 2
    b_co_two1[i] = theta_co_two[i] - 1
    
    a_co_two2[i] = -theta_co_two[i]
    b_co_two2[i] = theta_co_two[i] +1
    
    a_co_two3[i] = -theta_co_two[i] - 2
    b_co_two3[i] = (theta_co_two[i] + 1)**2/(theta_co_two[i] - 1)
    
    #axco.plot_surface(a_co_two1[i], b_co_two1[i], theta_co_two[i])
    #axco.plot_surface(a_co_two2[i], b_co_two2[i], theta_co_two[i])
    #axco.plot_surface(a_co_two3[i], b_co_two3[i], theta_co_two[i])
    
axco.plot_wireframe(a_co_two1, b_co_two1, theta_co_two, color='black')
axco.plot_wireframe(a_co_two2, b_co_two2, theta_co_two, color='green')
axco.plot_wireframe(a_co_two3, b_co_two3, theta_co_two, color='red')

yy, zz = np.meshgrid(range(2), range(2))
xx = yy*0
axco.plot_surface(xx, yy, zz, color='red')
axco.set_title('Codimensional-2 bifurcations')
#plt.savefig('Lorenz Attractor plot.jpg', dpi=550, transparent=False)
#plt.plot([a_co_two1,a_co_two2,a_co_two3],[b_co_two1,b_co_two2,b_co_two3], '.k')
#plt.plot(a_co_two1,b_co_two1, 'black')
#plt.plot(a_co_two2,b_co_two2, 'red')
#plt.plot(a_co_two3,b_co_two3, 'green')
plt.xlim(-5, 5) 
plt.ylim(-5,5)


#%%  FINE!