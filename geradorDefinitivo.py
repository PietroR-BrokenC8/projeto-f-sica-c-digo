#Esse aqui é pra valer, amigos. Esse é o código final, podem atualizar como bem entenderem.

import time
import sys, os
import math
if os.name == 'nt':  # Verifica se é Windows
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Obtém o identificador da saída padrão (STD_OUTPUT_HANDLE = -11)
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        # Lê o modo atual do console e ativa o bit 0x0004 (ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
# atualização por pietro: adicionado variaveis para proporcionar flexibilidade
largura = 101
altura = 41
continuar = True
criadores_cabecalho = ["Programadores principais:\n\n", "Programadores secundários:\n\n", "Responsáveis pelo artigo:\n\n", "Créditos especiais:\n\n"]
Criadores = ["- Fernando Lindner\n- Pietro Roldão Figueiró", "- Arthur Andriolo da Rosa\n- Arthur Stenert Lopes dos Santos\n- Miguel Fülber Gomes\n- Otávio Augusto Freiberger", "- Arthur Stenert Lopes dos Santos", "- prof Ione - professora que conduziu o projeto e pesquisa\n- prof Frederico - professor  professor que idealizou e iniciou o projeto\n- prof Graziano - professor que conduziu e auxiliou no código"]
#limpaTela:Limpa o terminal. Importante para compreensão do menu(e o terminal não ter 250 linhas toda vez q um novo comando for executado)
def limpaTela():
    print("\033[3J\033[2J\033[H", end="", flush=True)
#caracter é alterável, mas por padrão é o .
def geraTabela(quantiaCaracteres, quantiaLinhas, caracter="\033[31m.\033[0m", caracter2="-", caracter3="|"):
    tabelaRetornada = []
    # Descobre os índices centrais de linha e coluna
    linha_central = quantiaLinhas // 2
    coluna_central = quantiaCaracteres // 2
    for i in range(quantiaLinhas):
        linha = []
        for j in range(quantiaCaracteres):
            # 1. Verifica se está em algum dos cantos externos para colocar os números
            if i == 0 and j == quantiaCaracteres - 1:
                linha.append("\033[32m1\33[0m")  # Canto superior direito
            elif i == 0 and j == 0:
                linha.append("\033[32m2\33[0m")  # Canto superior esquerdo
            elif i == quantiaLinhas - 1 and j == 0:
                linha.append("\033[32m3\33[0m")  # Canto inferior esquerdo
            elif i == quantiaLinhas - 1 and j == quantiaCaracteres - 1:
                linha.append("\033[32m4\33[0m")  # Canto inferior direito
            # 2. Se não for um canto, aplica as regras das linhas e colunas centrais
            elif i == linha_central:
                linha.append(caracter2)
            elif j == coluna_central:
                linha.append(caracter3)
            else:
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
def alteraPonto(grid, coordX, coordY, caracter="\033[34mm\033[0m"):
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
    frame = "\n".join(" ".join(grid[i]) for i in range(len(grid))) + "\n"
    sys.stdout.buffer.write(frame.encode("utf-8"))
    #NÃO É MAIS TESTE, TUDO AQUI PRA BAIXO É PRA VALER

criadores = ["Arthur Andriolo da Rosa", "Arthur Stenert Lopes dos Santos", "Fernando Lindner", "Miguel Fülber Gomes", "Otávio Augusto Freiberger", "Pietro Roldão Figueiró"]
print("Gerador de ondas 20029 super ultra blaster")
print("Feito por:")
for i in range(len(criadores)):
    print(criadores[i])
    time.sleep(0.3)
time.sleep(5) #O próximo input tinha um erro de digitação(animaç~eos), arrumei :)
input("aviso rápido, o código era pra ter algumas animaçõeszinhas disponiveis para todos os sistemas operacionais, mas devido a limitações do windows as animações estão disponíveis apenas para linux.\n entrer para continuar pro código.")
limpaTela()
#Agora é o momento que o código pede as váriaveis. A gente só precisa de frequência e amplitude
#Eu poderia fazer um loop até um valor correto ser aceito
while continuar == True:
    while True:
        print("Insira a frequência(Números inteiros apenas, sem letras; De 1 a 100 Hz)")
        try:
            frequencia = int(input()) #Se o imbecil que usar o código colocar letras vai pro except
            if 0 < frequencia <= 100:
                limpaTela()
                print("Frequência de %dHz aceita!" % (frequencia))
                break
            else:
                print("Ok é um número mas o MÍNIMO é 1 e o MÁXIMO é 100")
                time.sleep(5)
        except ValueError as erro: #Então esse "ValueError" é pra ser o código de erro quando alguém coloca letra. Eu vou tacar na variável erro e colocar na mensagem
            print("Deu pau: " + str(erro) + " Relembrando: NÚMERO INTEIRO, SEM LETRAS") #Aparentemente o erro não é uma string mas sim alguma outra coisa, porque me torturas piton
            time.sleep(5)
        limpaTela()
        print("Tenta denovo. Coloca um valor válido dessa vez.")
    while True: #É a mesma coisa de antes basicamente
        print("Insira a amplitude(Número apenas; de 1 a 18)")
        try:
            amplitude = int(input())
            if 0 < amplitude <= 18:
                limpaTela()
                print("Amplitude de valor %d aceita!" % (amplitude))
                break
            else:
                print("É um número mas é inválido. O MÍNIMO é 1 e o MÁXIMO é 18")
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
    #2*math.pi * (i/20) num for de range 21 faz uma subida e descida, o i/20 é cada ponto X no gráfico, multiplicar pela frequencia faz o bagui se espremer pra dar mais voltas
    #É alguma magia negra da matemática que eu não sei explicar mas vamo testar
    if os.name == "posix":
        for i in range(5):
            textosleep = ["Gerando onda"]
            for j in range(4):
                print("".join(textosleep))
                textosleep.append(".")
                time.sleep(0.25)
                limpaTela()
    else:
        print("Gerando onda...")
        time.sleep(5)
        limpaTela()
    for i in range(largura): #A gente sabe que o comprimento do gráfico é 21 ent n precisa fazer outras coisas | atualização por pietro: o mesmo de casos anteriores, agora é utilizada uma variavel ao invés de numero fixo para maior flexibilidade
        for k in range(altura): #atualização por pietro: fiz uma alteração signficativa no calculo e seleção dos pontos mas que resolveram a questão dos espaçamentos
            ponto_atual=(i+k / altura) / (largura-1)
            coordenadaY = round((amplitude*1.1)*math.sin((frequencia/3)*2*math.pi*ponto_atual))
            coordenadaX = round(i+k/altura)
            alteraPonto(grafico, i, coordenadaY + altura //2)
            if os.name == "posix":
                print("\033[H")
                imprimeTabela(grafico)
            #o stennert deu a ideia fe fazer a onda ser colorida ao invés de branca, tipo azul, ou verde sla
        #AGORA É IMPRIMIR E REZAR PRA DAR CERTO. TO usando o caractere padrão que é o m, mas se vocês achar um melhor a gente troca
    #SUPOSTAMENTE ele faz isso 20 vezes e completa nosso gráfico, aí é só imprimir o gráfico usando o imprimeTabela
    if os.name == "nt":
        imprimeTabela(grafico)
    
    if input("Acabou. se quiser gerar mais uma onda digite \033[32m1\033[0m, que tiver enjoado dessas ondas, digite qualquer outra coisa ai\n") == "1":
        continuar = True
        limpaTela()
    else:
        continuar = False
        limpaTela()
        print("se gostou deixa o \033[32mlike\033[0m, se \033[31minscreve\033[0m e ativa o \033[33msininho\033[0m!")
    #EU FIZ UM TESTE COM FREQUÊNCIA 1 E AMPLITUDE 4 E DEU CERTO TESTAR COM MAIS VALORES DEPOIS VAMOOOOOOOOOOOOOOO
    #SUPOSTAMENTE É GG TROPA, SÓ FAZER O ARTIGO, ARRUMAR O QUE CÊS PREFERIR E LIMPAR ESSA BAGUNÇA
limpaTela()
print("é isso, vlw, flw, rola os créditos aí")
for i in range(len(criadores_cabecalho)):
    print(criadores_cabecalho[i])
    time.sleep(1)
    print(Criadores[i])
    time.sleep(2)
    limpaTela()
