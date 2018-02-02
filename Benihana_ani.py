import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import lstsq
from matplotlib.colors import LogNorm
import matplotlib.animation as animation
import time

fig = plt.figure(figsize=(11,9))
ax = fig.add_subplot(111, projection='3d')


benihana = pd.read_csv('/Users/natalienie/Desktop/benihana2.csv')
x =  benihana['advertise'].tolist()
y = benihana['B_size'].tolist()
z = benihana['Profit'].tolist()
data = np.c_[x, y, z]
mn = np.min(data, axis=0)
mx = np.max(data, axis=0)
X,Y = np.meshgrid(np.linspace(mn[0], mx[0], 30), np.linspace(mn[1], mx[1], 20))
A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
XX = X.flatten()
YY = Y.flatten()
C,_,_,_ = lstsq(A, data[:,2])

Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)

def animate(i):

    '''
    benihana = pd.read_csv('/Users/natalienie/Desktop/benihana2.csv')
    x =  benihana['advertise'].tolist()
    y = benihana['B_size'].tolist()
    z = benihana['Profit'].tolist()
    data = np.c_[x, y, z]
    mn = np.min(data, axis=0)
    mx = np.max(data, axis=0)
    X,Y = np.meshgrid(np.linspace(mn[0], mx[0], 30), np.linspace(mn[1], mx[1], 20))
    A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
    XX = X.flatten()
    YY = Y.flatten()
    C,_,_,_ = lstsq(A, data[:,2])

    Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)
    '''

    ax.clear()


    ax.plot_surface(X, Y, Z, norm=LogNorm(), rstride=1, cstride=1, alpha=0.5, cmap=plt.cm.jet)


    ax.scatter(x[:i+1], y[:i+1], z[:i+1])
    #fig = plt.figure(figsize=(9,7))
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x, y, z)
    #ax.plot_surface(X, Y, Z, norm=LogNorm(), rstride=1, cstride=1, alpha=0.5, cmap=plt.cm.jet)
    ax.set_xlabel('advertise')
    ax.set_ylabel('bar size')
    ax.set_zlabel('Nightly_profit')

ani = animation.FuncAnimation(fig, animate, interval=60)

plt.show()
