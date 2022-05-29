import random

'''Construa um programa em Python de acordo com situação problema descrita:
Um grupo de fila_circular está cercado e não há esperança de vitória, 
porém existe somente um cavalo disponível para escapar e buscar por reforços.
Para determinar qual soldado deve escapar para encontrar ajuda, eles formam um círculo (Fila Circular)
e sorteiam um número de um chapéu. Começando por um soldado sorteado aleatoriamente,
uma contagem é realizada até o número sorteado. Quando a contagem terminar,
o soldado em que a contagem parou é removido do círculo, um novo número é sorteado e
a contagem recomeça no soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
até que somente um soldado reste e seja escolhido para a tarefa.
'''

fila_circular = {1: 'Mateus', 2: 'Lucas', 3: 'Joao', 4: 'Luan', 5: 'Marcos', 6: 'Josias'}
chapeu = [1, 2, 3, 4, 5, 6]

print(fila_circular)
print("\n")

i = 0
while i <= len(fila_circular)+2:
    esco = random.choice(chapeu)
    print(f'O chapéu escolhido foi o {esco}, sobrou: ')
    chapeu.remove(esco)
    fila_circular.pop(esco)
    print(fila_circular)
    print("\n")
    i += 1
ganhador = [*fila_circular.values()]

print(f"O soldado {ganhador} ganhou o sorteio, ele pegará o cavalo")




