# 'O Problema é gerado por você mesmo! o problema sempre estará entre o monitor e a cadeira. - Shakuspi'
# Vai Corinthians!
import random

tamanho = random.randint(15, 30)
terreno = [random.randint(0, 100) for _ in range(tamanho)]
posicao_atual = random.randint(0, tamanho-1)
print("===[ GERAÇÃO CONCLUIDA ]===")
print(terreno)
print("\nPosicao inicial:", posicao_atual)
print("Valor inicial:", terreno[posicao_atual])
print("\n=== INÍCIO DO RILL CHIMMBE ===\n")
passo = 1
while True:
    valor_atual = terreno[posicao_atual]
    vizinho_esquerda = None
    vizinho_direita = None
    if posicao_atual > 0:
        vizinho_esquerda = terreno[posicao_atual - 1]

    if posicao_atual < tamanho - 1:
        vizinho_direita = terreno[posicao_atual + 1]

    print(f"Passo {passo}")
    print(f"Posicao atual: {posicao_atual}")
    print(f"Valor atual: {valor_atual}")
    #mostrar vizinho
    if vizinho_esquerda is not None:
        print(f"Vizinho esquerda ({posicao_atual - 1}): {vizinho_esquerda}")
    if vizinho_direita is not None:
        print(f"Vizinho direita ({posicao_atual + 1}): {vizinho_direita}")
    melhor_posicao = posicao_atual
    melhor_valor = valor_atual
    #comparacao a esquerda
    if vizinho_esquerda is not None and vizinho_esquerda > melhor_valor:
        melhor_valor = vizinho_esquerda
        melhor_posicao = posicao_atual - 1
    # comparacao a direita
    if vizinho_direita is not None and vizinho_direita > melhor_valor:
        melhor_valor = vizinho_direita
        melhor_posicao = posicao_atual + 1
    #quem procura acha, achou e encontrou uma MasterClass * * * * *
    if melhor_posicao != posicao_atual:
        if melhor_posicao < posicao_atual:
            print("[DECISAO] subiu à esquerda\n")
        else:
            print("[DECISAO] subiu à direita\n")
        posicao_atual = melhor_posicao
    else:
        print("[DECISAO] Vizinhos vei podi! :b")
        print("Aqui é o MasterClass\n")
        print('SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU')
        break
    passo += 1
valor_encontrado = terreno[posicao_atual]
valor_global = max(terreno)
indice_global = terreno.index(valor_global)
print("===[ RESULTADO ]===")
print(f"posicao encontrada: {posicao_atual}")
print(f"Valor encontrado: {valor_encontrado}")
print(f"\nMasterClass")
print(f"Posicao: {indice_global}")
print(f"Valor limite: {valor_global}")
if valor_encontrado == valor_global:
    print("\nO agente encontrou o *MASTERCLASS!*")
else:
    print("\nCadê o MasterClass???? :/")