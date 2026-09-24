#Esse aqui é pra valer, amigos. Esse é o código final, podem atualizar como bem entenderem.

import time
import os
import math
# atualização por pietro: adicionado variaveis para proporcionar flexibilidade
largura = 115
altura = 60
#limpaTela:Limpa o terminal. Importante para compreensão do menu(e o terminal não ter 250 linhas toda vez q um novo comando for executado)
def limpaTela():
    tipoSistema = os.name #cada sistema operacional tem meio q um id de .os, eu acho. Como o comando de terminal do windows é diferentão...
    if tipoSistema == "nt": #Id do windows
        _ = os.system("cls") #É basicamente digitando no cmd direto, mt massa 
    else:
        _ = os.system("clear") #Como o windows é "especial", ele só usa cls. O resto usa clear

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
#caracter é alterável, mas por padrão é o m

#eu tenho que reforçar isso porque deu problema antes: O código NORMALMENTE interpreta Y(0) como o TOPO DO CÓDIGO,ou seja, a altura é invertida por princípio
#isso NÃO É BOM porque a fórmula que a gente usar pra gerar os pontos vai entender 0 como o fundo do gráfico(ou no caso o meio do gráfico)
#Então a gente insere uma fórmula direto na impressão do ponto pra inverter isso. Então agora 0 é o fundo
#isso vai ser problema depois porque o código desce o gráfico pra valores negativos na crista mas detalhe, a gente conserta isso
def alteraPonto(grid, coordX, coordY, caracter="m"):
    if pontoValido(grid, coordX, coordY): #Conferindo pra ver se o ponto escolhido não tá fora do alcance
        grid[len(grid)-1-coordY][coordX] = caracter #A fórmula <ALTURA.GRADE>-1-<POSIÇÃO.ESCOLHIDA>Inverte a coordenada pro índice certo
    else:
        print("Ponto %d, %d fora da grade" % (coordX, coordY))

#Fernando: Seguinte eu to arrancando a função criaponto e linhacentral, considerando que a gente já definiu que a grid vai ser 21X9(Na última reunião) e vamo usar 1 caracter por pixel
#criaPonto: Função capaz de gerar um ponto 2x2 na grade, com o caracter pré-definido. O ponto expande para acima de si e a sua direita.
#linhaCentral: Função que pega a linha do meio da grid e a coloca em outro caractere, para dividir o centro da onda
#Também a ideia do sorrisinho é mta mão, se sobrar tempo a gente deixa pra depois. Pior das hipóteses reverte a versão no git

#imprimeTabela: Auto explicativo né patrão
def imprimeTabela(grid):
    for i in range(len(grid)):
        print(" ".join(grid[i])) #Eu botei um espacinho entre cada ponto pro negócio não ficar tão pequeno
#NÃO É MAIS TESTE, TUDO AQUI PRA BAIXO É PRA VALER

criadores = ["Arthur Andriolo da Rosa", "Arthur Stenert Lopes dos Santos", "Fernando Lindner", "Miguel Fülber Gomes", "Otávio Augusto Freiberger", "Pietro Roldão Figueiró"]
print("Gerador de ondas 20029 super ultra blaster")
print("Feito por:")
for i in range(len(criadores)):
    print(criadores[i])
    time.sleep(0.3)
time.sleep(5)
limpaTela()
#Agora é o momento que o código pede as váriaveis. A gente só precisa de frequência e amplitude
#Eu poderia fazer um loop até um valor correto ser aceito
while True:
    print("Insira a frequência(Números inteiros apenas, sem letras; De 1 a 5 Hz)")
    try:
        frequencia = int(input()) #Se o imbecil que usar o código colocar letras vai pro except
        if 0 < frequencia <= 1000:
            limpaTela()
            print("Frequência de %dHz aceita!" % (frequencia))
            break
        else:
            print("Ok é um número mas o MÍNIMO é 1 e o MÁXIMO é 5")
            time.sleep(5)
    except ValueError as erro: #Então esse "ValueError" é pra ser o código de erro quando alguém coloca letra. Eu vou tacar na variável erro e colocar na mensagem
        print("Deu pau: " + str(erro) + " Relembrando: NÚMERO INTEIRO, SEM LETRAS") #Aparentemente o erro não é uma string mas sim alguma outra coisa, porque me torturas piton
        time.sleep(5)
    limpaTela()
    print("Tenta denovo. Coloca um valor válido dessa vez.")
while True: #É a mesma coisa de antes basicamente
    print("Insira a amplitude(Número apenas; de 1 a 4)")
    try:
        amplitude = int(input())
        if 0 < amplitude <= 500:
            limpaTela()
            print("Amplitude de valor %d aceita!" % (amplitude))
            break
        else:
            print("É um número mas é inválido. O MÍNIMO é 1 e o MÁXIMO é 4")
            time.sleep(5)
    except ValueError as erro:
        print("Deu pau: " + str(erro) + " Relembrando: SEM LETRAS NO INPUT")
        time.sleep(5)
    limpaTela()
    print("Tenta denovo, e não coloca um valor inválido dessa vez")
#Resultado dos while: Testei com tudo que é caso e deu certo, cada while é uma entrada de valor
#ENTRADAS TÃO FEITAS AGORA É PROCESSAR ESSA BESTA
#Ok primeiro de tudo eu vou declarar a grid onde vai acontecer tudo. Eu não sei quais caracteres vamo usar ainda ent deixei o padrão
grafico = geraTabela(largura, altura) #vai gerar um retangulão de 21 por 9 | atualização por pietro: a geração agora é definida pelas variaveis de largura e altura, tornando o codigo mais flexivel
#Agora vem o processamento diabólico que usa a tal de "onda senoidal"
#A fórmula normal seria "Amplitude * sen(ângulo definido)" MAS A GENTE NÃO TEM ÂNGULO A GENTE TEM FREQUÊNCIA ENT COMO Q FICA
#Muitos estudos depois provaram que se a gente fazer "A * math.sin(2 * math.pi * frequencia * (i/20))" num for vai dar certo
#2*math.pi * (i/20) num for de range 21 faz uma subida e descida, o i/20 é cada ponto X no gráfico, multiplicar pela frequencia faz o bagui se espremer pra dar mais voltas
#É alguma magia negra da matemática que eu não sei explicar mas vamo testar
for i in range(largura): #A gente sabe que o comprimento do gráfico é 21 ent n precisa fazer outras coisas | atualização por pietro: o mesmo de casos anteriores, agora é utilizada uma variavel ao invés de numero fixo para maior flexibilidade
    coordenadaX = i
    #A coordenada X não tem segredo, vamo aplicar a magia da coordenada Y agora
    #ETAPA 1: Magia -> vai ser igual a algum valor entre amplitude positiva e amplitude negativa, podendo ser quebrado
    #atualização por pietro: alterei levemente a formula para gerar ondas mais suaves e visiveis dentro da limitação que temos
    coordenadaY = (amplitude * 1.1) * math.sin((frequencia / 3) * 2 * math.pi * (i / 20))
    #ETAPA 2: tem que arredondar pq o nosso bagui n aceita numero quebrado
    coordenadaY = round(coordenadaY)
    #ETAPA 3: a linha zero do nosso gráfico fica no meio dele, que na verdade é a linha 4(no caso é a quinta linha, mas começa no 0)
    #Então a gente pega a coordenada que ele pensa que deve colocar(que vai de 4 até -4, dependendo da amplitude escolhida) e somar 4 pra ele dar o shift certo
    #Se a meta era -4, ele vai pra linha 0, o fundo do gráfico. Se era 0, vai pra 4, o meio. E se a meta era 4, vai pra 8, o topo do gráfico
    #atualização por pietro: agora a linha a baixo não é dependente de +4 apenas, tendo agora um calculo automatizado para centralizar a onda corretamente graças a variavel anteriormente mencionada no inicio do codigo
    coordenadaY += round(altura / 2)
    #AGORA É IMPRIMIR E REZAR PRA DAR CERTO. TO usando o caractere padrão que é o m, mas se vocês achar um melhor a gente troca
    alteraPonto(grafico, coordenadaX, coordenadaY)
#SUPOSTAMENTE ele faz isso 20 vezes e completa nosso gráfico, aí é só imprimir o gráfico usando o imprimeTabela
print("Gerando onda...")
time.sleep(5) #Demorar mais tempo porque é mais legal
limpaTela()
imprimeTabela(grafico)
input("Acabou. Aperte ENTER para sair, e se gostou deixa o like, se inscreva e aperte o sininho para receber as notificações")
#EU FIZ UM TESTE COM FREQUÊNCIA 1 E AMPLITUDE 4 E DEU CERTO TESTAR COM MAIS VALORES DEPOIS VAMOOOOOOOOOOOOOOO
#SUPOSTAMENTE É GG TROPA, SÓ FAZER O ARTIGO, ARRUMAR O QUE CÊS PREFERIR E LIMPAR ESSA BAGUNÇA
print("CÓDIGO ACABOU, SE NADA EXPLODIU ATÉ AGORA É PORQUE DEU CERTO")
