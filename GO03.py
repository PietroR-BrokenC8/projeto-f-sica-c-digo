import time
import os
import math
#limpaTela:Limpa o terminal. Importante para compreensão do menu(e o terminal não ter 250 linhas toda vez q um novo comando for executado)
def limpaTela():
    tipoSistema = os.name #cada sistema operacional tem meio q um id de .os, eu acho. Como o comando de terminal do windows é diferentão...
    if tipoSistema == "nt": #Id do windows
        os.system("cls") #É basicamente digitando no cmd direto, mt massa 
    else:
        os.system("clear") #Como o windows é "especial", ele só usa cls. O resto usa clear

#geraTabela: prepara uma grade pra nós, uma lista de listas
#caracter é alterável, mas por padrão é o .
def geraTabela(quantiaCaracteres, quantiaLinhas, caracter="."):
    tabelaRetornada = []
    for i in range(quantiaLinhas):
        linha = []
        for i in range(quantiaCaracteres):
            linha.append(caracter) 
        tabelaRetornada.append(linha)
    return tabelaRetornada
#pontoValido: Recebe grid, coordenada X e coordenada Y, retorna True se esse ponto está na grade
def pontoValido(grid, coordX, coordY):
    if coordX>=len(grid[0]) or coordY>=len(grid):
        return False
    else:
        return True

#alteraPonto:Escolhe um ponto de uma grade e o altera. Essa função já está adaptada ao fato q coordy=0 seria o topo, e o converte para q coordy=0 seja o fundo
#Função simples, de ser utilizada em funções compostas. Pode ser utilizada pra debugging
#caracter é alterável, mas por padrão é o m
def alteraPonto(grid, coordX, coordY, caracter="m"): #Se não escolher um cara
    if pontoValido(grid, coordX, coordY): #Conferindo pra ver se o ponto escolhido não tá fora do alcance
        grid[len(grid)-1-coordY][coordX] = caracter #A fórmula <ALTURA.GRADE>-1-<POSIÇÃO.ESCOLHIDA>Inverte a coordenada pro índice certo
    else:
        print("Ponto %d, %d fora da grade" % (coordX, coordY))
    
#criaPonto: Função capaz de gerar um ponto 2x2 na grade, com o caracter pré-definido. O ponto expande para acima de si e a sua direita.
#Caso uma parte do ponto fique para fora da grade, ele irá alterar apenas as partes que consegue alterar
def criaPonto(grid, coordX, coordY, caracter="m"):
    alteraPonto(grid, coordX, coordY, caracter)
    alteraPonto(grid, (coordX + 1), coordY, caracter)
    alteraPonto(grid, coordX, (coordY + 1), caracter)
    alteraPonto(grid, (coordX + 1), (coordY + 1), caracter)

#linhaCentral: Função que pega a linha do meio da grid e a coloca em outro caractere, para dividir o centro da onda
#Por motivos de debugging pode usar pra mudar o caractere de uma linha inteira
#Toda tabela DEVE SER ÍMPAR. Se for par o bagui arredonda pra baixo
def linhaCentral(grid, caracter="1", linha=-1):
    if linha == -1: #Verificador de debugging, se você definir a linha ele vai tentar alterar aquela linha
        if pontoValido(grid, 0, linha):
            for i in range(len(grid[linha])):
                grid[linha][i] = caracter
        else:
            print("linha %d fora da grade", linha)
    else:
        if len(grid)%2==0:
            metadeGrid = len(grid)/2-1
        else:
            metadeGrid = len(grid)/2-0.5


#TESTE
#Tabela do sorrisinho
gridSmile = [
    ["0","0","1","1","1","1","1","0","0"],
    ["0","1","0","0","0","0","0","1","0"],
    ["1","0","0","1","0","1","0","0","1"],
    ["1","0","0","0","0","0","0","0","1"],
    ["1","0","0","0","0","0","0","0","1"],
    ["1","0","0","0","0","0","0","0","1"],
    ["1","0","0","0","0","0","0","0","1"],
    ["0","1","0","0","0","0","0","1","0"],
    ["0","0","1","1","1","1","1","0","0"],
]
criadores = ["Arthur Andriolo da Rosa", "Arthur Stenert Lopes dos Santos", "Fernando Lindner", "Miguel Fülber Gomes", "Otávio Augusto Freiberger", "Pietro Roldão Figueiró"]
print("Gerador de ondas 20029 super ultra blaster")
print("Feito por:")
for i in range(len(criadores)):
    print(criadores[i])
    time.sleep(0.3)
print("Carregando ondas...")
time.sleep(5)
for i in range(len(gridSmile)):
    print("".join(gridSmile[i]))
    time.sleep(0.03)
time.sleep(2)
limpaTela()
