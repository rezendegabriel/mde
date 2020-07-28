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

#%%

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

#%%
  
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
  
#%%   
    
class Elemento():
    def __init__(self, id, n1, n2, material, tipo_estrutura):
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.material = material
        self.tipo_estrutura = tipo_estrutura
        
        self.l = 0
        self.cx = 0
        self.cy = 0
        
        self.vetorLM = [] #vetor LM
        self.deslocamentos = [] #vetor deslocamento
        self.acoesExtremidadeBarra = [] #ações de extremidade das barras
        
        if self.tipo_estrutura == "TRELIÇA 2D":
            self.matrizR_T = np.zeros((4,4), dtype = np.float64) #matriz de rotação
            self.matrizK_L = np.zeros((4,4), dtype = np.float64) #matriz de rigidez no referncial local
            self.matrizK_G = np.zeros((4,4), dtype = np.float64) #matriz de rigidez no referncial global
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.matrizR_T = np.zeros((6,6), dtype = np.float64) #matriz de rotação
            self.matrizK_L = np.zeros((6,6), dtype = np.float64) #matriz de rigidez no referncial local
            self.matrizK_G = np.zeros((6,6), dtype = np.float64) #matriz de rigidez no referncial global

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
    
    def getTipoEstrutura(self):
        return self.tipo_estrutura
    
    def getVetorLM(self):
        return self.vetorLM
    
    def getMatrizR_T(self):
        return self.matrizR_T
    
    def getMatrizK_L(self):
        return self.matrizK_L
    
    def getMatrizK_G(self):
        return self.matrizK_G
    
    def getDeslocamentos(self):
        return self.deslocamentos
    
    def getAcoesExtremidadeBarra(self):
        return self.acoesExtremidadeBarra
    
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
        
    def setTipoEstrutura(self, tipo_estrutura):
        self.tipo_estrutura = tipo_estrutura
        
    def setVetorLM(self):
        if self.tipo_estrutura == "TRELIÇA 2D":
            self.vetorLM.append(self.n1.getDx())
            self.vetorLM.append(self.n1.getDy())
            self.vetorLM.append(self.n2.getDx())
            self.vetorLM.append(self.n2.getDy())
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.vetorLM.append(self.n1.getDx())
            self.vetorLM.append(self.n1.getDy())
            self.vetorLM.append(self.n1.getDz())
            self.vetorLM.append(self.n2.getDx())
            self.vetorLM.append(self.n2.getDy())
            self.vetorLM.append(self.n2.getDz())
            
        
    def setMatrizR_T(self):
        cos = self.cx
        sen = self.cy
        
        self.matrizR_T[0][0] = cos
        self.matrizR_T[0][1] = sen
        self.matrizR_T[1][0] = -sen
        self.matrizR_T[1][1] = cos
        
        if self.tipo_estrutura == "TRELIÇA 2D":    
            self.matrizR_T[2][2] = cos
            self.matrizR_T[2][3] = sen
            self.matrizR_T[3][2] = -sen
            self.matrizR_T[3][3] = cos
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.matrizR_T[2][2] = 1
            
            self.matrizR_T[3][3] = cos
            self.matrizR_T[3][4] = sen
            self.matrizR_T[4][3] = -sen
            self.matrizR_T[4][4] = cos
            
            self.matrizR_T[5][5] = 1
        
    def setMatrizK_L(self):
        EAx_L = ((self.material.getE()*self.material.getA())/self.l)
        
        if self.tipo_estrutura == "TRELIÇA 2D":
            self.matrizK_L[0][0] = EAx_L
            self.matrizK_L[0][2] = -EAx_L
            self.matrizK_L[2][0] = -EAx_L
            self.matrizK_L[2][2] = EAx_L
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            EIz_L = (self.material.getE()*self.material.getJ()/self.l)
            EIz_L2 = (self.material.getE()*self.material.getJ()/self.l**2)
            EIz_L3 = (self.material.getE()*self.material.getJ()/self.l**3)
            
            
            self.matrizK_L[0][0] = EAx_L
            self.matrizK_L[0][3] = -EAx_L
            
            self.matrizK_L[1][1] = 12*EIz_L3
            self.matrizK_L[1][2] = 6*EIz_L2
            self.matrizK_L[1][4] = -12*EIz_L3
            self.matrizK_L[1][5] = 6*EIz_L2
            
            self.matrizK_L[2][1] = 6*EIz_L2
            self.matrizK_L[2][2] = 4*EIz_L
            self.matrizK_L[2][4] = -6*EIz_L2            
            self.matrizK_L[2][5] = 2*EIz_L
            
            self.matrizK_L[3][0] = -EAx_L
            self.matrizK_L[3][3] = EAx_L
            
            self.matrizK_L[4][1] = -12*EIz_L3
            self.matrizK_L[4][2] = -6*EIz_L2
            self.matrizK_L[4][4] = 12*EIz_L3
            self.matrizK_L[4][5] = -6*EIz_L2
            
            self.matrizK_L[5][1] = 6*EIz_L2
            self.matrizK_L[5][2] = 2*EIz_L
            self.matrizK_L[5][4] = -6*EIz_L2
            self.matrizK_L[5][5] = 4*EIz_L
        
    def setMatrizK_G(self):
        self.matrizK_G = np.dot(np.transpose(self.matrizR_T), np.dot(self.matrizK_L, self.matrizR_T))
        
    def setDeslocamentos(self, deslocamentos):
        self.deslocamentos = deslocamentos
        
    def setAcoesExtremidadeBarra(self, acoesExtremidadeBarra):
        self.acoesExtremidadeBarra = acoesExtremidadeBarra

#%%

class Carga():
    def __init__(self, id, elemento, px, py, pz, q, rt, a, b):
        self.id = id
        self.elemento = elemento
        
        #carga pontual
        self.px = px
        self.py = py
        self.pz = pz
        
        #carga distribuída
        self.q = q
        self.rt = rt
        
        #posição
        self.a = a
        self.b = b
        
    def getId(self):
        return self.id
    
    def getElemento(self):
        return self.elemento
    
    def getPx(self):
        return self.px
    
    def getPy(self):
        return self.py
    
    def getPz(self):
        return self.pz
    
    def getQ(self):
        return self.q
    
    def getRT(self):
        return self.rt
    
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def setId(self, id):
        self.id = id
        
    def setElemento(self, elemento):
        self.elemento = elemento
        
    def setPx(self, px):
        self.px = px
    
    def setPy(self, py):
        self.py = py
        
    def setPz(self, pz):
        self.pz = pz
    
    def setQ(self, q):
        self.q = q

    def setRT(self, rt):
        self.rt = rt
    
    def setA(self, a):
        self.a = a
    
    def setB(self, b):
        self.b = b

#%%
 
class Estrutura():
    def __init__(self, tipo_estrutura):
        self.tipo_estrutura = tipo_estrutura
        
        #número de deslocamentos desconhecidos
        self.num_equacoes = 0
        
        #informações das classes
        self.nos = []
        self.materiais = []
        self.elementos = []
        self.cargas = []
        
        #vetores de deslocamentos
        self.d = []
        self.d_coordenadas = []
        self.d_conhecidos_coordenadas = []
        
        #vetores de forças
        self.vetorF_N = []
        self.vetorF_E = []
        self.vetorF = []
        self.vetorF_R = []
        self.vetorF_RL = []
        
        #matrizes notáveis
        self.matrizK = 0
        self.matrizA_ML = 0
        self.matrizK_RD = 0
        
    def getTipoEstrutura(self):
        return self.tipo_estrutura
        
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
    
    def criarElemento(self, id, n1, n2, material, tipo_estrutura):
        if self.buscarElemento(id) is None:
            self.elementos.append(Elemento(id, n1, n2, material, tipo_estrutura))
        
    def buscarElemento(self, id):
        for i in self.elementos:
            if id == i.getId():
                return i
            
        return None
    
    def criarCarga(self, id, elemento, px, py, pz, q, rt, a, b):
        if self.buscarCarga(id) is None:
            self.cargas.append(Carga(id, elemento, px, py, pz, q, rt, a, b))
        
    def buscarCarga(self, id):
        for i in self.cargas:
            if id == i.getId():
                return i
            
        return None
    
    def criarVetoresLM(self):
        d = 1
        
        #deslocamentos desconhecidos
        for i in self.nos:
            if i.getRx() == 0:
                i.setDx(d)
                self.d_coordenadas.append("x")

                
                self.num_equacoes += 1 #atualiza o número de equações
                d+=1
                
            if i.getRy() == 0:
                i.setDy(d)
                self.d_coordenadas.append("y")
                
                self.num_equacoes += 1 #atualiza o número de equações
                d+= 1
                
            if self.tipo_estrutura == "PÓRTICO 2D":
                if i.getRz() == 0:
                    i.setDz(d)
                    self.d_coordenadas.append("z")
                    
                    self.num_equacoes += 1 #atualiza o número de equações
                    d+= 1

        #deslocamentos conhecidos
        for i in self.nos:
            if i.getRx() == 1:
                i.setDx(d)
                self.d_conhecidos_coordenadas.append(str(i.getId()) + "_x")
                
                d+=1
                
            if i.getRy() == 1:
                i.setDy(d)
                self.d_conhecidos_coordenadas.append(str(i.getId()) + "_y")
                
                d+=1
            
            if self.tipo_estrutura == "PÓRTICO 2D":
                if i.getRz() == 1:
                    i.setDz(d)
                    self.d_conhecidos_coordenadas.append(str(i.getId()) + "_z")
                    
                    d+=1
           
        #atualiza o vetor LM
        for i in self.elementos:
            i.setVetorLM()
            
    def criarMatrizesK_G(self):
        for i in self.elementos:
            #atualiza o tamanho do elemento
            i.setL(((i.getN2().getX() - i.getN1().getX())**2+(i.getN2().getY() - i.getN1().getY())**2)**0.5)
            #atualiza o Cx do elemento
            i.setCx((i.getN2().getX() - i.getN1().getX())/i.getL())
            #atualiza o Cy do elemento
            i.setCy((i.getN2().getY() - i.getN1().getY())/i.getL())
            #atualiza a matriz de rotação
            i.setMatrizR_T()
            #atualiza a matriz de rigidez no referencial local
            i.setMatrizK_L()
            #atualiza a matriz de rigidez no referencial global
            i.setMatrizK_G()
            
    def criarMatrizK(self):
        #atualiza a matriz K
        if self.tipo_estrutura == "TRELIÇA 2D":
            self.matrizK = np.zeros((2*len(self.nos),2*len(self.nos)), dtype = np.float64)
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.matrizK = np.zeros((3*len(self.nos),3*len(self.nos)), dtype = np.float64)
        
        #percorre os elementos e armazena os vetores LM e a matriz KG
        for k in self.elementos:
            vetorLM = k.getVetorLM()
            matrizK_G = k.getMatrizK_G()
            
            #percorre os índices do vetor LM correspondentes aos índices da matriz K da estrutura
            for i in vetorLM:
                for j in vetorLM:
                    self.matrizK[i-1][j-1] += matrizK_G[vetorLM.index(i)][vetorLM.index(j)]
                    
    def criarVetorF_N(self):
        #cargas nodais em nós com deslocamento desconhecido
        for i in self.nos:
            if i.getDx() <= self.num_equacoes:
                self.vetorF_N.append(i.getPx())
                
            if i.getDy() <= self.num_equacoes:
                self.vetorF_N.append(i.getPy())
            
            if self.tipo_estrutura == "PÓRTICO 2D":
                if i.getDz() <= self.num_equacoes:
                    self.vetorF_N.append(i.getPz())
         
        #cargas nodais em nós com deslocamento conhecidos
        if self.tipo_estrutura == "PÓRTICO 2D":
            for i in self.nos:
                if i.getDx() > self.num_equacoes:
                    self.vetorF_N.append(i.getPx())
                
                if i.getDy() > self.num_equacoes:
                    self.vetorF_N.append(i.getPy())
            
                if i.getDz() > self.num_equacoes:
                    self.vetorF_N.append(i.getPz())
                
    def criarMatrizA_ML(self):
        num_linhas_AEP = len(self.elementos)
        
        #atualiza a matriz AEP
        self.matrizA_ML = np.zeros((num_linhas_AEP, 6), dtype = np.float64)
        
        #percorrer as cargas
        for i in self.cargas:
            elemento = i.getElemento()
            k = int(elemento.getId())
            L = elemento.getL()
            
            a = i.getA()
            b = i.getB()
            
            #carga horizontal
            if i.getPx() != 0:              
                P = i.getPx()
                
                self.matrizA_ML[k-1][0] += P*a/L
                self.matrizA_ML[k-1][3] += P*b/L
                
            #carga vertical
            if i.getPy() != 0:
                P = i.getPy()
                
                self.matrizA_ML[k-1][1] += P*(b**2)*(3*a+b)/(L**3)
                self.matrizA_ML[k-1][2] += P*a*(b**2)/(L**2)
                self.matrizA_ML[k-1][4] += P*(a**2)*(a+3*b)/(L**3)
                self.matrizA_ML[k-1][5] += -P*b*(a**2)/(L**2)
                
            #carga momento
            if i.getPz() != 0:
                M = i.getPz()
                
                self.matrizA_ML[k-1][1] += 6*M*a*b/(L**3)
                self.matrizA_ML[k-1][2] += M*b(2*a-b)/(L**2)
                self.matrizA_ML[k-1][4] += -6*M*a*b/(L**3)
                self.matrizA_ML[k-1][5] += M*a(2*b-a)/(L**2)
                
            #carga distribuída
            if i.getQ() != 0:
                q = i.getQ()
                
                #retangular e distribuída em toda a barra
                if i.getRT() == "R" and a == 0:
                    self.matrizA_ML[k-1][1] += q*L/2
                    self.matrizA_ML[k-1][2] += q*(L**2)/12
                    self.matrizA_ML[k-1][4] += q*L/2
                    self.matrizA_ML[k-1][5] += -q*(L**2)/12
                
                #retangular e distribuída em parte da barra
                if i.getRT() == "R" and 0 < a < L:
                    self.matrizA_ML[k-1][1] += q*a*(2*(L**3)-2*(a**2)*L+(a**3))/(2*L**3)
                    self.matrizA_ML[k-1][2] += q*(a**2)*(6*(L**2)-8*a*L+3*(a**2))/(12*L**2)
                    self.matrizA_ML[k-1][4] += q*(a**3)*(2*L-a)/(2*L**3)
                    self.matrizA_ML[k-1][5] += -q*(a**3)*(4*L-3*a)/(12*L**2)
                
                #triangular
                if i.getRT() == "T":
                    self.matrizA_ML[k-1][1] += 3*q*L/20
                    self.matrizA_ML[k-1][2] += q*(L**2)/30
                    self.matrizA_ML[k-1][4] += 7*q*L/20
                    self.matrizA_ML[k-1][5] += -q*(L**2)/20
                    
    def criarVetorF_E(self):
        #inicializa o vetor FE
        for i in range(3*len(self.nos)):
            self.vetorF_E.append(0)
            
        for i in self.elementos:
            k = int(i.getId())
            cos = i.getCx()
            sen = i.getCy()
            vetorLM = i.getVetorLM()
                       
            #verifica se o elemento está no referncial global
            if cos == 1 and sen == 0:
                self.vetorF_E[vetorLM[0]-1] += -self.matrizA_ML[k-1][0] #x_1
                self.vetorF_E[vetorLM[1]-1] += -self.matrizA_ML[k-1][1] #y_1
                self.vetorF_E[vetorLM[2]-1] += -self.matrizA_ML[k-1][2] #z_1
                self.vetorF_E[vetorLM[3]-1] += -self.matrizA_ML[k-1][3] #x_2
                self.vetorF_E[vetorLM[4]-1] += -self.matrizA_ML[k-1][4] #y_2
                self.vetorF_E[vetorLM[5]-1] += -self.matrizA_ML[k-1][5] #z_2
                
            #verifica se o elemento, fora do referencial global, está na posição vertical (rotação anti-horária)
            if cos == 0 and sen == 1:
                self.vetorF_E[vetorLM[0]-1] += -self.matrizA_ML[k-1][1]*(-sen) #y_1
                self.vetorF_E[vetorLM[1]-1] += -self.matrizA_ML[k-1][0] #x_1
                self.vetorF_E[vetorLM[2]-1] += -self.matrizA_ML[k-1][2] #z_1
                self.vetorF_E[vetorLM[3]-1] += -self.matrizA_ML[k-1][4]*(-sen) #y_2
                self.vetorF_E[vetorLM[4]-1] += -self.matrizA_ML[k-1][3] #x_2
                self.vetorF_E[vetorLM[5]-1] += -self.matrizA_ML[k-1][5] #z_2
                
            #verifica se o elemento, fora do referncial global, está inclinado (rotação anti-horária)
            if 0 < np.abs(cos) < 1 and 0 < sen < 1:
                self.vetorF_E[vetorLM[0]-1] += -self.matrizA_ML[k-1][1]*(-sen) #x_1
                self.vetorF_E[vetorLM[1]-1] += -self.matrizA_ML[k-1][1]*cos #y_1
                self.vetorF_E[vetorLM[2]-1] += -self.matrizA_ML[k-1][2] #z_1
                self.vetorF_E[vetorLM[3]-1] += -self.matrizA_ML[k-1][4]*(-sen) #x_2
                self.vetorF_E[vetorLM[4]-1] += -self.matrizA_ML[k-1][4]*cos #y_2
                self.vetorF_E[vetorLM[5]-1] += -self.matrizA_ML[k-1][5] #z_2
                
    def criarVetorF(self):
        #cria vetor de forças para o cálculo do deslocamento
        for i in range(self.num_equacoes):
            self.vetorF.append(self.vetorF_E[i]+self.vetorF_N[i])
                
    def calcularDeslocamentos(self):
        #inicializa matriz K de tamanho igual ao número de deslocamentos desconhecidos
        matrizK = np.zeros((self.num_equacoes, self.num_equacoes), dtype = np.float64)
        
        for i in range(self.num_equacoes):
            for j in range(self.num_equacoes):
                matrizK[i][j] = self.matrizK[i][j]
        
        #calcula os deslocamentos desconhecidos
        if self.tipo_estrutura == "TRELIÇA 2D":
            self.d = np.linalg.solve(matrizK, self.vetorF_N)
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.d = np.linalg.solve(matrizK, self.vetorF)
        
        #saída dos deslocamentos
        if self.tipo_estrutura == "TRELIÇA 2D":
            for i in range(len(self.d)):
                print("Deslocamento " + str(i+1) + ": " + str(self.d[i]) + " m")
                
        if self.tipo_estrutura == "PÓRTICO 2D":
            for i in range(len(self.d)):
                if self.d_coordenadas[i] == "x" or self.d_coordenadas[i] == "y":
                    print("Deslocamento " + str(i+1) + ": " + str(self.d[i]) + " m")
                else:
                    print("Deslocamento " + str(i+1) + ": " + str(self.d[i]) + " rad")
    
    def calcularAcoesExtremidadeBarras(self):
        for i in self.elementos:
            k = int(i.getId())
            
            deslocamentos = []
            vetorAML = []
            vetorLM = i.getVetorLM()
            
            if self.tipo_estrutura == "PÓRTICO 2D":
                for n in range(6):
                    vetorAML.append(self.matrizA_ML[k-1][n])
            
            #atualiza o vetor deslocamento
            for j in vetorLM:
                if j > self.num_equacoes:
                    deslocamentos.append(0)
                else:
                    deslocamentos.append(self.d[j-1])
                    
            i.setDeslocamentos(deslocamentos)
            
            #calcula as ações da extremidade das barras
            if self.tipo_estrutura == "TRELIÇA 2D":
                i.setAcoesExtremidadeBarra(np.dot((np.dot(i.getMatrizK_L(), i.getMatrizR_T())), deslocamentos))
            
            if self.tipo_estrutura == "PÓRTICO 2D":
                i.setAcoesExtremidadeBarra(vetorAML + np.dot((np.dot(i.getMatrizK_L(), i.getMatrizR_T())), deslocamentos))
            
            #saída das ações de extremidade das barras
            print("Barra " + str(i.getId()) + ":")
            
            acoesExtremidadeBarra = i.getAcoesExtremidadeBarra()
            n1 = i.getN1().getId()
            n2 = i.getN2().getId()
            
            if self.tipo_estrutura == "TRELIÇA 2D":
                for a in range(len(acoesExtremidadeBarra)):
                    if(a == 0):
                        print(" N_" + str(n1) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                    
                    if(a == 2):
                        print(" N_" + str(n2) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                        
            if self.tipo_estrutura == "PÓRTICO 2D":
                for a in range(len(acoesExtremidadeBarra)):
                    if(a == 0):
                        print(" N_" + str(n1) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                    if(a == 1):
                        print(" V_" + str(n1) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                    if(a == 2):    
                        print(" M_" + str(n1) + ": " + str(acoesExtremidadeBarra[a]) + " N.m")
                    if(a == 3):
                        print(" N_" + str(n2) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                    if(a == 4):
                        print(" V_" + str(n2) + ": " + str(acoesExtremidadeBarra[a]) + " N")
                    if(a == 5):    
                        print(" M_" + str(n2) + ": " + str(acoesExtremidadeBarra[a]) + " N.m")
                        
      
    def criarVetorF_RL(self):
        for i in range(len(self.vetorF_E)):
            if i >= self.num_equacoes:
                self.vetorF_RL.append(-self.vetorF_E[i])                
        
    def criarMatrizK_RD(self):
        if self.tipo_estrutura == "TRELIÇA 2D":
            num_deslocamentos = 2*len(self.nos)
            
        if self.tipo_estrutura == "PÓRTICO 2D":
            num_deslocamentos = 3*len(self.nos)
            
        num_linhas_KRD = num_deslocamentos-self.num_equacoes
        num_colunas_KRD = self.num_equacoes
        
        coeficientes_matrizK_RD = []
        
        #inicializa matriz KRD, em que o número de linhas equivale à quantidade de deslocamentos conhecidos e o número de colunas à quantidade de deslocamentos desconhecidos
        self.matrizK_RD = np.zeros((num_linhas_KRD, num_colunas_KRD), dtype = np.float64)
        
        for i in range(num_deslocamentos):
            for j in range(num_deslocamentos):
                if i >= self.num_equacoes and j < self.num_equacoes:
                    coeficientes_matrizK_RD.append(self.matrizK[i][j])
        
        #cria a matriz KRD
        for i in range(num_linhas_KRD):
            for j in range(num_colunas_KRD):
                self.matrizK_RD[i][j] = coeficientes_matrizK_RD.pop(0)

    def calcularReacoesApoio(self):
        #calcula as reações de apoio
        if self.tipo_estrutura == "TRELIÇA 2D": 
            self.vetorF_R = np.dot(self.matrizK_RD, self.d)
            
            #saída das reações de apoio
            for i in range(len(self.vetorF_R)):
                print(self.d_conhecidos_coordenadas[i] + ": " + str(self.vetorF_R[i]) + " N")
        
        #calcula as reações de apoio
        if self.tipo_estrutura == "PÓRTICO 2D":
            self.vetorF_R = self.vetorF_RL + np.dot(self.matrizK_RD, self.d)
            
            #saída das reações de apoio
            for i in range(len(self.vetorF_R)):
                d = self.d_conhecidos_coordenadas[i]
                
                if d[2] == "x" or d[2] == "y":
                    print(self.d_conhecidos_coordenadas[i] + ": " + str(self.vetorF_R[i]) + " N")
                if d[2] == "z":
                    print(self.d_conhecidos_coordenadas[i] + ": " + str(self.vetorF_R[i]) + " N.m")
                
#%%                
                
def leitura(nome_arquivo, estrutura, opcao_estrutura):
    num_nos = 0
    num_materiais = 0
    num_elementos = 0
    
    i = 0
    for linha in arquivo:
        #leitura do tipo de estrutura
        if i == 0:
            tipo_estrutura = linha.split()
            if opcao_estrutura != (str(tipo_estrutura[0]) + " " + str(tipo_estrutura[1])):
                return False #erro no tipo de estrutura
        
        #leitura das informações de controle
        if i == 4:
            info_controle = linha.split()
            num_nos = int(info_controle[0])
            num_materiais = int(info_controle[1])
            num_elementos = int(info_controle[2])
    
        #leitura das informações dos nós  
        if 7 < i < (8+num_nos):
            info_nos = linha.split()
            estrutura.criarNo(info_nos[0], float(info_nos[1]), float(info_nos[2]), float(info_nos[3]), float(info_nos[4]), float(info_nos[5]), float(info_nos[6]), float(info_nos[7]), float(info_nos[8]), float(info_nos[9]))
    
        #leitura das informações dos materiais           
        if (10+num_nos) < i < (11+num_nos+num_materiais):
            info_materiais = linha.split()
            estrutura.criarMaterial(info_materiais[0], float(info_materiais[1]), float(info_materiais[2]), float(info_materiais[3]), float(info_materiais[4]))
        
        #leitura dos elementos
        if (13+num_nos+num_materiais) < i < (14+num_nos+num_materiais+num_elementos):
            info_elementos = linha.split()
            estrutura.criarElemento(info_elementos[0], estrutura.buscarNo(info_elementos[1]), estrutura.buscarNo(info_elementos[2]), estrutura.buscarMaterial(info_elementos[3]), opcao_estrutura)
        
        #leitura das cargas
        if i > (16+num_nos+num_materiais+num_elementos):        
            info_cargas = linha.split()
            estrutura.criarCarga(info_cargas[0], estrutura.buscarElemento(info_cargas[1]), float(info_cargas[2]), float(info_cargas[3]), float(info_cargas[4]), float(info_cargas[5]), info_cargas[6], float(info_cargas[7]), float(info_cargas[8]))
            
        i+=1
        
    arquivo.close()
    
    return True
    
#%%

print("**********Mecânica das Estruturas - Método da Rigidez**********")

nome_arquivo = input("Arquivo de entrada: ")

arquivo_aberto = False
while arquivo_aberto == False:
    try:
        arquivo = open(nome_arquivo, 'r', encoding = "utf8")
        
        arquivo_aberto = True
    except:
        nome_arquivo = input("Arquivo inexistente! Digite novamente: ")

opcao = 0
while opcao != 3:
    print("\nMenu")
    print(" 1) Pórtico 2D")
    print(" 2) Treliça 2D")
    print(" 3) Sair")
    
    opcao = input("Tipo de estrutura: ")
    
    opcao_estrutura = ""
    
    if opcao == str(1):
        opcao_estrutura = "PÓRTICO 2D"
    if opcao == str(2):
        opcao_estrutura = "TRELIÇA 2D"
    if opcao == str(3):
        print("Finalizando a aplicação...")
        
        break
        
    estrutura = Estrutura(opcao_estrutura)

    if leitura(nome_arquivo, estrutura, opcao_estrutura) == False:
        print("Erro na leitura do arquivo! Verifique o arquivo de entrada.")
        
        break

    print("Estrutura criada com sucesso!")
    
    estrutura.criarVetoresLM()
    estrutura.criarMatrizesK_G()
    estrutura.criarMatrizK()
    estrutura.criarVetorF_N()
    
    if opcao_estrutura == "PÓRTICO 2D":
        estrutura.criarMatrizA_ML()
        estrutura.criarVetorF_E()
        estrutura.criarVetorF()
    
    print("\nCalculando deslocamentos...")
    
    estrutura.calcularDeslocamentos()
    
    print("\nCalculando Ações de Extremidade das Barras...")
    estrutura.calcularAcoesExtremidadeBarras()
    
    print("\nCalculando Reações de Apoio...")
    if opcao_estrutura == "PÓRTICO 2D":
        estrutura.criarVetorF_RL()
    
    estrutura.criarMatrizK_RD()
    estrutura.calcularReacoesApoio()
    
    opcao = 3