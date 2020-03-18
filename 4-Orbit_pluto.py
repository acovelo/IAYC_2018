import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from math import *
import numpy as np
from sklearn import datasets
from scipy.optimize import fsolve


def orbit(T,M,m,e,theta,phi):
    a=(667E-11*T**2*M/(4*np.pi**2))**(1/3)
    c=a*e
    b=sqrt(a**2-c**2)
    print("a=",a,"b=",b,"c=",c)
    alpha = np.linspace(0,2*np.pi, 100)
    beta=np.linspace(0,2*np.pi,100)
    x = (a*np.cos(alpha)-c)*np.cos(theta)*np.cos(phi)+b*np.sin(alpha)*np.cos(theta)*np.sin(phi)
    y = -(a*np.cos(alpha)-c)*np.sin(phi)+b*np.sin(alpha)*np.cos(phi)
    z= (a*np.cos(alpha)-c)*np.sin(theta)*np.cos(phi)+b*np.sin(alpha)*np.sin(theta)*sin(phi)
    a_s=m*a/M
    c_s=a_s*e
    b_s = sqrt(a_s ** 2 - c_s ** 2)
    print("a_S=", a_s, "b_s=", b_s, "c_s=", c_s)
    x_s = a_s * np.cos(beta) * np.cos(theta) * np.cos(phi) +c_s*np.cos(theta)*np.cos(phi)+ b_s * np.sin(beta) * np.cos(theta) * np.sin(phi)
    y_s = -a_s * np.cos(beta) * np.sin(phi) -c_s*np.sin(phi)+ b_s* np.sin(beta) * np.cos(phi)
    z_s = a_s * np.cos(beta) * np.sin(theta) * np.cos(phi)+c_s*np.sin(theta)*np.cos(phi)+ b_s * np.sin(beta) * np.sin(theta) * sin(phi)
    return x,y,z,x_s,y_s,z_s

orbcharon1=orbit(6.387230,1305,158.7,0.0022,0.001*(np.pi/180),0)
orbstyx1= orbit(20.16155,1305,0.00075,0.0058,0.81*np.pi/180,0)
orbnix1=orbit(24.85463,1305,0.005,0.002036,0.133*np.pi/180,0)
orbkerberos1=orbit(32.16756,1305,0.0016,0.00328,0.389*np.pi/180,0)
orbhydra1=orbit(38.20177,1305,0.005,0.005862,0.242*np.pi/180,0,)





def plotting(ax,orba,orbb,orbc,orbd,orbe):
    ax.plot(orba[3] + orbb[3] + orbc[3] + orbd[3] + orbe[3], orba[4] + orbb[4] + orbc[4] + orbd[4] + orbe[4],
            orba[5] + orbb[5] + orbc[5] + orbd[5] + orbe[5],label='Pluto')
    ax.plot(orba[0], orba[1], orba[2],label='Charon')
    ax.plot(orbb[0],orbb[1],orbb[2],label='Styx')
    ax.plot(orbc[0],orbc[1],orbc[2],label='Nix')
    ax.plot(orbd[0],orbd[1],orbd[2],label='Kerberos')
    ax.plot(orbe[0],orbe[1],orbe[2],label='Hydra')
    ax.scatter([0], [0], [0])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set(title="Pluto")


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, projection='3d')
plotting(ax1, orbcharon1, orbstyx1,orbnix1,orbkerberos1,orbhydra1)


plt.legend(loc=2)
plt.show()