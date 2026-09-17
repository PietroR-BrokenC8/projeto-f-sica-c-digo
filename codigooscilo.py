import math


def desenhar_onda(dados, largura=40, altura=50, char="*"):
    """
    Desenha uma representação em ASCII de uma lista de valores numéricos.

    dados: lista de números (ex: [0, 1, 2, 1, 0, -1, -2, -1, 0])
    largura: quantas colunas a onda vai ocupar (os dados são reamostrados para essa largura)
    altura: quantas linhas de altura o gráfico terá
    char: caractere usado para desenhar a onda
    """
    if not dados:
        print("Nenhum dado fornecido.")
        return

    # Reamostra os dados para caber na largura desejada
    n = len(dados)
    indices = [int(i * (n - 1) / (largura - 1)) if largura > 1 else 0 for i in range(largura)]
    amostra = [dados[i] for i in indices]

    minimo, maximo = min(amostra), max(amostra)
    intervalo = maximo - minimo if maximo != minimo else 1

    # Normaliza os valores para a altura do gráfico (linhas de 0 a altura-1)
    linhas = []
    for valor in amostra:
        pos = round((valor - minimo) / intervalo * (altura - 1))
        linhas.append(pos)

    # Monta o grid, linha por linha, de cima para baixo
    grid = [[" " for _ in range(largura)] for _ in range(altura)]
    for coluna, linha in enumerate(linhas):
        grid[altura - 1 - linha][coluna] = char

    for linha in grid:
        print("".join(linha))


def gerar_onda_seno(pontos=100, ciclos=2, amplitude=1):
    """Gera dados de exemplo: uma onda senoidal."""
    return [amplitude * math.sin(2 * math.pi * ciclos * i / pontos) for i in range(pontos)]


if __name__ == "__main__":
    print("Onda senoidal de exemplo:\n")
    dados = gerar_onda_seno(pontos=200, ciclos=3)
    desenhar_onda(dados, largura=60, altura=60, char="█")

    print("\nOnda a partir de dados manuais:\n")
    dados_manuais = [0, 2, 4, 6, 4, 2, 0, -2, -4, -6, -4, -2, 0, 3, 5, 2, -1, -3, 0]
    desenhar_onda(dados_manuais, largura=88, altura=27, char="*")
    