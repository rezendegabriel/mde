# -*- coding: utf-8 -*-

"""
Trabalho Método da Rigidez
Mecânica das Estruturas - MAC023

Discentes: Gabriel Rezende
           Pedro Henrique Eveling
           
Doscentes: Prof. Afonso Lemonge
           Prof.(a) Patricia Hallak
"""

import numpy as np

class No: 
    def __init__(self, id, x, y, z, rx, ry, rz, px, py, pz):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.px = px
        self.py = py
        self.pz = pz
        self.dx = 0
        self.dy = 0
        self.dz = 0
    
    def getId(self):
        return self.id
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    def getRx(self):
        return self.rx
    
    def getRy(self):
        return self.ry
    
    def getRz(self):
        return self.rz
    
    def getPx(self):
        return self.px
    
    def getPy(self):
        return self.py
    
    def getPz(self):
        return self.pz
    
    def getDx(self):
        return self.dx
    
    def getDy(self):
        return self.dy
    
    def getDz(self):
        return self.dz
    
    def setId(self, id):
        self.id = id
        
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def setZ(self, z):
        self.z = z
        
    def setRx(self, rx):
        self.Rx = rx
        
    def setRy(self, ry):
        self.Ry = ry
        
    def setRz(self, rz):
        self.Rz = rz
        
    def setPx(self, px):
        self.px = px
        
    def setPy(self, py):
        self.py = py
        
    def setPz(self, pz):
        self.pz = pz
        
    def setDx(self, dx):
        self.dx = dx
        
    def setDy(self, dy):
        self.dy = dy
        
    def setDz(self, dz):
        self.dz = dz
   
class Material():  
    def __init__(self, id, A, J, E, G):
        self.id = id
        self.A = A
        self.J = J
        self.E = E
        self.G = G
        
    def getId(self):
        return self.id
    
    def getA(self):
        return self.A
    
    def getJ(self):
        return self.J
    
    def getE(self):
        return self.E
    
    def getG(self):
        return self.G
    
    def setId(self, id):
        self.id = id
    
    def setA(self, A):
        self.A = A
    
    def setJ(self, J):
        self.J = J
    
    def setE(self, E):
        self.E = E
    
    def setG(self, G):
        self.G = G
     
class Elemento():
    def __init__(self, id, n1, n2, material):
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.material = material
        
        self.l = 0
        self.cx = 0
        self.cy = 0
        self.vetorLM = [] #vetor LM
        self.matrizKG = np.zeros((4,4), dtype = np.float64) #matriz de rigidez no referncial global
        
    def getId(self):
        return self.id
    
    def getN1(self):
        return self.n1
    
    def getN2(self):
        return self.n2
    
    def getL(self):
        return self.l
    
    def getCx(self):
        return self.cx
    
    def getCy(self):
        return self.cy
    
    def getMaterial(self):
        return self.material
    
    def getVetorLM(self):
        return self.vetorLM
    
    def getMatrizKG(self):
        return self.matrizKG
    
    def setId(self, id):
        self.id = id
        
    def setN1(self, n1):
        self.n1 = n1
        
    def setN2(self, n2):
        self.n2 = n2
        
    def setL(self, l):
        self.l = l
        
    def setCx(self, cx):
        self.cx = cx

    def setCy(self, cy):
        self.cy = cy
        
    def setMaterial(self, material):
        self.material = material
        
    def setVetorLM(self):
        self.vetorLM.append(self.n1.getDx())
        self.vetorLM.append(self.n1.getDy())
        self.vetorLM.append(self.n2.getDx())
        self.vetorLM.append(self.n2.getDy())
        
    def setMatrizKG(self):
        cos_2 = self.cx**2
        sen_2 = self.cy**2
        
        sencos = self.cx*self.cy
        
        self.matrizKG[0][0] = cos_2
        self.matrizKG[0][1] = sencos
        self.matrizKG[0][2] = -cos_2
        self.matrizKG[0][3] = -sencos
        
        self.matrizKG[1][0] = sencos
        self.matrizKG[1][1] = sen_2
        self.matrizKG[1][2] = -sencos
        self.matrizKG[1][3] = -sen_2
        
        self.matrizKG[2][0] = -cos_2
        self.matrizKG[2][1] = -sencos
        self.matrizKG[2][2] = cos_2
        self.matrizKG[2][3] = sencos
        
        self.matrizKG[3][0] = -sencos
        self.matrizKG[3][1] = -sen_2
        self.matrizKG[3][2] = sencos
        self.matrizKG[3][3] = sen_2
        
        self.matrizKG = ((self.material.getE()*self.material.getA())/self.l)*self.matrizKG
        
class Estrutura():
    def __init__(self):
        self.nos = []
        self.materiais = []
        self.elementos = []
        
    def criarNo(self, id, x, y, z, rx, ry, rz, px, py, pz):
        if self.buscarNo(id) is None:
            self.nos.append(No(id, x, y, z, rx, ry, rz, px, py, pz))
        
    def buscarNo(self, id):
        for i in self.nos:
            if id == i.getId():
                return i
            
        return None
    
    def criarMaterial(self, id, A, J, E, G):
        if self.buscarMaterial(id) is None:
            self.materiais.append(Material(id, A, J, E, G))
        
    def buscarMaterial(self, id):
        for i in self.materiais:
            if id == i.getId():
                return i
            
        return None
    
    def criarElemento(self, id, n1, n2, tipo_elemento):
        if self.buscarElemento(id) is None:
            self.elementos.append(Elemento(id, n1, n2, tipo_elemento))
        
    def buscarElemento(self, id):
        for i in self.elementos:
            if id == i.getId():
                return i
            
        return None
    
    def criarVetoresLM(self):
        deslocamentos = []
        
        d = 1
        while d <= 2*len(self.nos):
            deslocamentos.append(d)
            
            d+=1
            
        #deslocamentos desconhecidos
        for i in self.nos:
            if i.getRx() == 0:
                i.setDx(deslocamentos.pop(0))
            if i.getRy() == 0:
                i.setDy(deslocamentos.pop(0))
                
        #deslocamentos conhecidos
        for i in self.nos:
            if i.getRx() == 1:
                dx = deslocamentos.pop(0)
                i.setDx(dx)
            if i.getRy() == 1:
                i.setDy(deslocamentos.pop(0))
           
        #atualiza o vetor LM
        for i in self.elementos:
            i.setVetorLM()
            
    def criarMatrizesKG(self):
        for i in self.elementos:
            #atualiza o tamanho do elemento
            i.setL(((i.getN2().getX() - i.getN1().getX())**2+(i.getN2().getY() - i.getN1().getY())**2)**0.5)
            #atualiza o Cx do elemento
            i.setCx((i.getN2().getX() - i.getN1().getX())/i.getL())
            #atualiza o Cy do elemento
            i.setCy((i.getN2().getY() - i.getN1().getY())/i.getL())
            #atualiza a matriz de rigidez no referencial global
            i.setMatrizKG()
            
def leitura(nome_arquivo, estrutura):
    num_nos = 0
    num_materiais = 0
    
    try:
        arquivo = open(nome_arquivo, 'r')
    except:
        return False
    
    i = 0
    for linha in arquivo:
        #leitura das informações de controle
        if i == 2:
            info_controle = linha.split()
            num_nos = int(info_controle[0])
            num_materiais = int(info_controle[1])
    
        #leitura das informações dos nós  
        if 4 < i < (5+num_nos):
            info_nos = linha.split()
            estrutura.criarNo(info_nos[0], float(info_nos[1]), float(info_nos[2]), float(info_nos[3]), float(info_nos[4]), float(info_nos[5]), float(info_nos[6]), float(info_nos[7]), float(info_nos[8]), float(info_nos[9]))
    
        #leitura das informações dos materiais           
        if (6+num_nos) < i < (7+num_nos+num_materiais):
            info_materiais = linha.split()
            estrutura.criarMaterial(info_materiais[0], float(info_materiais[1]), float(info_materiais[2]), float(info_materiais[3]), float(info_materiais[4]))
        
        #leitura dos elementos
        if i > (8+num_nos+num_materiais):
            info_elementos = linha.split()
            estrutura.criarElemento(info_elementos[0], estrutura.buscarNo(info_elementos[1]), estrutura.buscarNo(info_elementos[2]), estrutura.buscarMaterial(info_elementos[3]))
        
        i+=1
        
    arquivo.close()
    
    return True
    
def menu():
    print("**********Mecânica das Estruturas - Método da Rigidez**********")
    
    estrutura = Estrutura()
    
    nome_arquivo = input("Arquivo de entrada: ")
    
    while leitura(nome_arquivo, estrutura) == False:
        nome_arquivo = input("Arquivo inexistente! Digite novamente: ")
        
    print("Estrutura criada com sucesso!")
    
    estrutura.criarVetoresLM()
    estrutura.criarMatrizesKG()
    
menu()