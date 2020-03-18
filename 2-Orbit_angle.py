import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from math import *
import numpy as np
from sklearn import datasets

def orbit(T,M,m,e,theta,phi,ang):
    a=(667E-11*T**2*M/(4*np.pi**2))**(1/3)
    c=a*e
    b=sqrt(a**2-c**2)
    print("a=",a,"b=",b,"c=",c)
    r = a * (1 - e ** 2) / (1 + e * np.cos(ang))
    v = sqrt((2 * 6.67E-11 * M / r) - (6.67E-11 * M / a))
    E = np.arccos((e + np.cos(ang)) / (1 + e * np.cos(ang)))
    if ang<=np.pi:
        t = T * (E - e * np.sin(E)) / (2 * np.pi)
    else:
        t=T-(T * (E - e * np.sin(E)) / (2 * np.pi))
    print("r=", r, "v=", v, "t=", t)
    angc=np.arccos((e+np.cos(ang))/(1+e*cos(ang)))
    if ang>np.pi:
        angc=2*np.pi-angc
    alpha = np.linspace(0,angc, 100)
    beta=np.linspace(np.pi,angc+np.pi,100)
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
    r_s = m*r/M
    v_s = m*v/M
    print("r_s=", r_s, "v_s=", v_s)
    return x,y,z,x_s,y_s,z_s,r,r_s,v,v_s,t

orb1=orbit(365,1.9E15,3E14,0.7,0,0,0.25*np.pi)
orb2=orbit(365,1.9E15,3E14,0.7,0,0,0.5*np.pi)
orb3=orbit(365,1.9E15,3E14,0.7,0,0,0.75*np.pi)
orb4=orbit(365,1.9E15,3E14,0.7,0,0,np.pi)
orb5=orbit(365,1.9E15,3E14,0.7,0,0,1.25*np.pi)
orb6=orbit(365,1.9E15,3E14,0.7,0,0,1.5*np.pi)
orb7=orbit(365,1.9E15,3E14,0.7,0,0,1.75*np.pi)
orb8=orbit(365,1.9E15,3E14,0.7,0,0,2*np.pi)

def plotting(ax,orb):
    ax.plot(orb[0], orb[1], orb[2])
    ax.plot(orb[3], orb[4], orb[5])
    ax.scatter([0], [0], [0])
    ax.set(xlim=[-6000, 2000], ylim=[-2000, 3500], zlim=[-0.02, 0.02])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set(title="t=" '%d' %orb[10])
    ax.text(0,0,0.015,"v=" '%d' %orb[8],color='blue')
    ax.text(-6000,0,-0.02,"r=" '%d' %orb[6],color='blue')



fig = plt.figure()
ax1 = fig.add_subplot(2, 4, 1, projection='3d')
plotting(ax1, orb1)
ax2 = fig.add_subplot(2, 4, 2, projection='3d')
plotting(ax2, orb2)
ax3 = fig.add_subplot(2, 4, 3, projection='3d')
plotting(ax3, orb3)
ax4 = fig.add_subplot(2, 4, 4, projection='3d')
plotting(ax4, orb4)
ax5 = fig.add_subplot(2, 4, 5, projection='3d')
plotting(ax5, orb5)
ax6 = fig.add_subplot(2, 4, 6, projection='3d')
plotting(ax6, orb6)
ax7 = fig.add_subplot(2, 4, 7, projection='3d')
plotting(ax7, orb7)
ax8 = fig.add_subplot(2, 4, 8, projection='3d')
plotting(ax8, orb8)
plt.show()