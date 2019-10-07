# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:23:28 2019

@author: pedro
"""
import numpy as np

class no:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX():
        return x
    def getY():
        return y
    def setX():
        self.x=x
    def setY():
        self.y=y
    

class matrix: # tad matrix para gerar e guardar a matriz do problema.
    
    def __init__(self,i,j):
        self.matriz = np.zeros((i,j), dtype=np.float64) #inicializa matriz com zero
        self.i=i
        self.j=j
    def setIndice(self,i,j,v):
        self.matriz[i][j]=v
    def getIndice(self,i,j):
        return self.matriz[i][j]
        
class barrra:
    def __init__(self,n1,n2,L,EA):
        self.n1 = n1
        self.n2 = n2
        self.EA = EA
        self.L = ((n1[0]-n2[0])**2+(n1[1]-n2[1])**2)**0.5
        self.cx = (n2[0]-n1[0])/L
        self.cy = (n2[1]-n1[1])/L
        self.cz = (n2[2]-n1[2])/L
        self.matriz[0][0]=self.cos**2*EA/L
        self.matriz[1][1]=self.sen**2*EA/L
        
    def setEA(x):
        self.EA=x    
        
    
x=int(input("Quantidade de nos"))


noL=[]
for i in range(x): # [x,y,z (coordenadas x,y,z)]
   no=[input("Desloca em x? "),input("desloca em y? "),input("desloca em z? "),(input("coordenada x "),input("coordenada y "),input("coordenada z "))]    
   noL.append(no)
       