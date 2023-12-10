
from queue import PriorityQueue
from pyamaze import maze, agent



def h_score(atual):
    x_atual = atual[0]
    y_atual = atual[1]

    x_destino = 1
    y_destino = 1

    return abs(x_atual - x_destino) + abs(y_atual - y_destino)  

def melhor_caminho(caminho, origem):
    melhor = {}
    chave = (1,1)

    while chave != origem:
        valor = caminho[chave]
        melhor[valor] = chave
        chave = valor
    
    return melhor


def aestrela(l):
    destino = (1, 1)
    fila = PriorityQueue()

    origem = (labirinto.rows, labirinto.cols)

    g_score = {}
    caminho = {}

    #celulas com valor inicial infinito com exceção do origem
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score[origem] = 0
    f_score[origem] = g_score[origem] + h_score(origem)

    #caminhar explorando caminhos
    item = (f_score[origem], h_score(origem), origem)
    fila.put(item)

    while not fila.empty():
        atual = fila.get()[2]

        if atual == destino:
            break

        for direcao in "NSEW":
            x_atual = atual[0]
            y_atual = atual[1]

            #verifica se o a direcao esta no dicionario de opcoes de caminho possiveis
            if l.maze_map[atual][direcao] == 1: 
                if direcao == 'N':
                    proxima = (x_atual-1, y_atual)
                elif direcao == 'S':
                    proxima = (x_atual+1, y_atual)
                elif direcao == 'E':
                    proxima = (x_atual, y_atual+1)
                elif direcao == 'W':
                    proxima = (x_atual, y_atual-1)

                proxima_g_score = g_score[atual] + 1
                proxima_h_score = h_score(proxima)
                proxima_f_score = proxima_g_score + proxima_h_score

                if proxima_f_score < f_score[proxima]:
                    f_score[proxima] = proxima_f_score
                    g_score[proxima] = proxima_g_score
                    proximo_item = (proxima_f_score, proxima_h_score, proxima)
                    fila.put(proximo_item)
                    caminho[proxima] = atual

    #Refaz o caminho do destino até a origem para selecionar apenas as celulas do caminho final
    caminho = melhor_caminho(caminho, origem)

    return caminho


labirinto = maze(100,100)

labirinto.CreateMaze()
agente = agent(labirinto, filled =True, footprints=True )
caminho = aestrela(labirinto)
labirinto.tracePath({agente: caminho}, delay=30)
labirinto.run()