import matplotlib.pyplot as plt 
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from math import *
import numpy as np
from sklearn import datasets

def orbit(T,M,m,e,theta,phi):
    a=(667E-11*T**2*M/(4*np.pi**2))**(1/3)
    c=a*e
    b=sqrt(a**2-c**2)
    print("a=",a,"b=",b,"c=",c)
    alpha = np.linspace(0, 2 * np.pi, 100)
    x = (a*np.cos(alpha)-c)*np.cos(theta)*np.cos(phi)+b*np.sin(alpha)*np.cos(theta)*np.sin(phi)
    y = -(a*np.cos(alpha)-c)*np.sin(phi)+b*np.sin(alpha)*np.cos(phi)
    z= (a*np.cos(alpha)-c)*np.sin(theta)*np.cos(phi)+b*np.sin(alpha)*np.sin(theta)*sin(phi)
    a_s=m*a/M
    c_s=a_s*e
    b_s = sqrt(a_s ** 2 - c_s ** 2)
    print("a_s=", a_s, "b_s=", b_s, "c_s=", c_s)
    x_s = a_s * np.cos(alpha) * np.cos(theta) * np.cos(phi) +c_s*np.cos(theta)*np.cos(phi)+ b_s * np.sin(alpha) * np.cos(theta) * np.sin(phi)
    y_s = -a_s * np.cos(alpha) * np.sin(phi) -c_s*np.sin(phi)+ b_s* np.sin(alpha) * np.cos(phi)
    z_s = a_s * np.cos(alpha) * np.sin(theta) * np.cos(phi)+c_s*np.sin(theta)*np.cos(phi)+ b_s * np.sin(alpha) * np.sin(theta) * sin(phi)
    return x,y,z,x_s,y_s,z_s


orb1=orbit(1E5,5E5,5E4,0.7,np.pi/10,0)

fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot(orb1[0],orb1[1],orb1[2])
axes.scatter(0,0,0)
axes.plot(orb1[3],orb1[4],orb1[5])
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')
plt.show()


