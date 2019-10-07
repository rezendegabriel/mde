# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:23:28 2019

@author: pedro
"""
import numpy as np

class No:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.deslocamentos()
    def deslocamentos(self):
        self.desX=int(input("deslocamento em x "))
        self.desY=int(input("deslocamento em y "))
        self.desZ=int(input("deslocamento em z "))
    def getX():
        return x
    def getY():
        return y
    def setX():
        self.x=x
    def setY():
        self.y=y
    def setZ():
        self.z=z
    def getZ():
        return self.z
    

class Matrix: # tad matrix para gerar e guardar a matriz do problema.
    
    def __init__(self,i,j):
        self.matriz = np.zeros((i,j), dtype=np.float64) #inicializa matriz com zero
        self.i=i
        self.j=j
    def setIndice(self,i,j,v):
        self.matriz[i][j]=v
    def getIndice(self,i,j):
        return self.matriz[i][j]
        
class Barrra:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
                
    def criarCs():
        self.cx = (n2[0]-n1[0])/L
        self.cy = (n2[1]-n1[1])/L
        self.cz = (n2[2]-n1[2])/L
    def getL():
        self.L = ((n1[0]-n2[0])**2+(n1[1]-n2[1])**2)**0.5
    def matrizRigidezTrelica():
        self.matriz[0][0] = self.cx**2*self.EA/self.L
        self.matriz[0][1] = self.cy*self.cx*self.EA/self.L
        self.matriz[0][2] = self.cz*self.cx*self.EA/self.L
        self.matriz[0][3] = -self.cx*self.cx*self.EA/self.L
        self.matriz[0][4] = -self.cy*self.cx*self.EA/self.L
        self.matriz[0][5] = -self.cz*self.cx*self.EA/self.L
        
        self.matriz[1][0] = self.cx*self.cy*self.EA/self.L
        self.matriz[1][1] = self.cy*self.cy*self.EA/self.L
        self.matriz[1][2] = self.cz*self.cy*self.EA/self.L
        self.matriz[1][3] = -self.cx*self.cx*self.EA/self.L
        self.matriz[1][4] = -self.cy*self.cx*self.EA/self.L
        self.matriz[1][5] = -self.cz*self.cx*self.EA/self.L
        
        
    def setEA(x):
        self.EA=x
        
    
x=int(input("Quantidade de nos"))


noL=[]
for i in range(x): # [x,y,z (coordenadas x,y,z)]
   no= No(int(input("coordenada x ")),int(input("coordenada y ")),int(input("coordenada z ")))    
   noL.append(no)