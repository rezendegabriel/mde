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
        self.matrizRT = np.zeros((4,4), dtype = np.float64) #matriz de rotação
        self.matrizKL = np.zeros((4,4), dtype = np.float64) #matriz de rigidez no referncial local
        self.matrizKG = np.zeros((4,4), dtype = np.float64) #matriz de rigidez no referncial global
        self.deslocamentos = [] #vetor deslocamento
        self.acoesExtremidadeBarras = [] #ações de extremidade das barras
        
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
    
    def getMatrizRT(self):
        return self.matrizRT
    
    def getMatrizKL(self):
        return self.matrizKL
    
    def getMatrizKG(self):
        return self.matrizKG
    
    def getDeslocamentos(self):
        return self.deslocamentos
    
    def getAcoesExtremidadeBarras(self):
        return self.acoesExtremidadeBarras
    
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
        
    def setMatrizRT(self):
        cos = self.cx
        sen = self.cy
        
        self.matrizRT[0][0] = cos
        self.matrizRT[0][1] = sen
        self.matrizRT[1][0] = -sen
        self.matrizRT[1][1] = cos
        
        self.matrizRT[2][2] = cos
        self.matrizRT[2][3] = sen
        self.matrizRT[3][2] = -sen
        self.matrizRT[3][3] = cos
        
    def setMatrizKL(self):
        EAx_L = ((self.material.getE()*self.material.getA())/self.l)
        
        self.matrizKL[0][0] = EAx_L
        self.matrizKL[0][2] = -EAx_L
        self.matrizKL[2][0] = -EAx_L
        self.matrizKL[2][2] = EAx_L
        
        
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
        
    def setDeslocamentos(self, deslocamentos):
        self.deslocamentos = deslocamentos
        
    def setAcoesExtremidadeBarras(self, acoesExtremidadeBarras):
        self.acoesExtremidadeBarras = acoesExtremidadeBarras
        
class Estrutura():
    def __init__(self):
        self.num_equacoes = 0
        self.matrizK = 0
        self.matrizKRD = 0
        
        self.nos = []
        self.materiais = []
        self.elementos = []
        self.vetorFD = []
        self.deslocamentos = []
        self.vetorFR = []
        
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
        d = 1
        
        #deslocamentos desconhecidos
        for i in self.nos:
            if i.getRx() == 0:
                i.setDx(d)
                
                self.num_equacoes += 1 #atualiza o número de equações
                d+=1    
            if i.getRy() == 0:
                i.setDy(d)
                
                self.num_equacoes += 1 #atualiza o número de equações
                d+= 1
        #deslocamentos conhecidos
        for i in self.nos:
            if i.getRx() == 1:
                i.setDx(d)
                
                d+=1
            if i.getRy() == 1:
                i.setDy(d)
                
                d+=1
           
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
            
    def criarMatrizK(self):
        #atualiza a matriz K
        self.matrizK = np.zeros((2*len(self.nos),2*len(self.nos)), dtype = np.float64)
        
        #percorre os elementos e armazena os vetores LM e a matriz KG
        for k in self.elementos:
            vetorLM = k.getVetorLM()
            matrizKG = k.getMatrizKG()
            
            #percorre os índices do vetor LM correspondentes aos índices da matriz K da estrutura
            for i in vetorLM:
                for j in vetorLM:
                    self.matrizK[i-1][j-1] += matrizKG[vetorLM.index(i)][vetorLM.index(j)]
                    
    def criarVetorFD(self):
        #cargas nodais em nós com deslocamento desconhecido
        for i in self.nos:
            if i.getDx() <= self.num_equacoes:
                self.vetorFD.append(i.getPx())
            if i.getDy() <= self.num_equacoes:
                self.vetorFD.append(i.getPy())
                
    def calcularDeslocamentos(self):
        #inicializa matriz K de tamanho igual ao número de deslocamentos desconhecidos
        matrizK = np.zeros((self.num_equacoes, self.num_equacoes), dtype = np.float64)
        
        for i in range(self.num_equacoes):
            for j in range(self.num_equacoes):
                matrizK[i][j] = self.matrizK[i][j]
                
        #calcula os deslocamentos desconhecidos
        self.deslocamentos = np.linalg.solve(matrizK, self.vetorFD)
        
        print(self.deslocamentos)
        
    def calcularAcoesExtremidadeBarras(self):
        for i in self.elementos:
            deslocamentos = []
            vetorLM = i.getVetorLM()
            
            #atualiza o vetor deslocamento
            l = 0
            for k in vetorLM:
                if k > self.num_equacoes:
                    deslocamentos.append(0)
                else:
                    deslocamentos.append(self.deslocamentos[l])
                    l += 1
                    
            i.setDeslocamentos(deslocamentos)
            #atualiza a matriz de rotação
            i.setMatrizRT()
            #atualiza a matriz de rigidez no referencial local
            i.setMatrizKL()
            #calcula as ações da extremidade das barras
            i.setAcoesExtremidadeBarras(np.dot((np.dot(i.getMatrizKL(), i.getMatrizRT())), deslocamentos))
            
            print(i.getAcoesExtremidadeBarras())
            
    def criarMatrizKRD(self):
        num_deslocamentos = 2*len(self.nos)
        num_linhas_KRD = num_deslocamentos-self.num_equacoes
        num_colunas_KRD = self.num_equacoes
        
        coeficientes_matrizKRD = []
        
        #inicializa matriz KRD, em que o número de linhas equivale à quantidade de deslocamentos desconhecidos e o número de colunas à quantidade de deslocamentos conhecidos
        self.matrizKRD = np.zeros((num_linhas_KRD, num_colunas_KRD), dtype = np.float64)
        
        for i in range(num_deslocamentos):
            for j in range(num_deslocamentos):
                if i >= self.num_equacoes and j < self.num_equacoes:
                    coeficientes_matrizKRD.append(self.matrizK[i][j])
        
        #cria a matriz KRD
        for i in range(num_linhas_KRD):
            for j in range(num_colunas_KRD):
                self.matrizKRD[i][j] = coeficientes_matrizKRD.pop(0)

    def calcularReacoesApoio(self):
        #calcula as reações de apoio
        self.vetorFR = np.dot(self.matrizKRD, self.deslocamentos)
        
        print(self.vetorFR)
                
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
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("**********Mecânica das Estruturas - Método da Rigidez**********")

estrutura = Estrutura()

nome_arquivo = input("Arquivo de entrada: ")

while leitura(nome_arquivo, estrutura) == False:
    nome_arquivo = input("Arquivo inexistente! Digite novamente: ")
    
print("Estrutura criada com sucesso!")

estrutura.criarVetoresLM()
estrutura.criarMatrizesKG()
estrutura.criarMatrizK()
estrutura.criarVetorFD()
estrutura.criarMatrizKRD()

opcao = 0

while opcao != "4":
    print("***************Menu***************")
    print("1) Calcular deslocamentos")
    print("2) Calcular ações da extremidade das barras")
    print("3) Calcular reações de apoio")
    print("4) Sair")
    
    opcao = input("O que deseja fazer? ")

    if opcao == "1":
        estrutura.calcularDeslocamentos()
        
    if opcao == "2":
        estrutura.calcularAcoesExtremidadeBarras()
        
    if opcao == "3":
        estrutura.calcularReacoesApoio()