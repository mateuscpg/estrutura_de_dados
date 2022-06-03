import random
import numpy as np 

class Listasequencial:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  # O(1) - O(2)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1 
      self.valores[self.ultima_posicao] = valor 

  # O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1

  def pesquisar_indice(self, indice):
    for i in range(self.ultima_posicao + 1):
      if i == indice:
        return self.valores[i]
    return -1

  # O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.ultima_posicao -= 1

  def contagem(self, escolha):
    indice = self.pesquisar(escolha)
    for i in range(escolha):
      if indice == self.ultima_posicao:
        indice = 0
      else:
        indice += 1
    return indice

    

'''Construa um programa em Python de acordo com situação problema descrita:
Um grupo de soldados está cercado e não há esperança de vitória, 
porém existe somente um cavalo disponível para escapar e buscar por reforços.
Para determinar qual soldado deve escapar para encontrar ajuda, eles formam um círculo (Fila Circular)
e sorteiam um número de um chapéu. Começando por um soldado sorteado aleatoriamente,
uma contagem é realizada até o número sorteado. Quando a contagem terminar,
o soldado em que a contagem parou é removido do círculo, um novo número é sorteado e
a contagem recomeça no soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
até que somente um soldado reste e seja escolhido para a tarefa.
'''


while True:
    try:
        qntd = int(input("Insira a quantidade de soldados: "))
        break
    except:
        print("Comando inválido!")
lista = Listasequencial(qntd)

for i in range(qntd):
    while True:
        try:
            sold = int(input(f"Nº do id do {i+1}º soldado: "))
            break
        except:
            print("Comando inválido!")
    lista.insere(sold)



while lista.ultima_posicao > 0:
    esco1 = random.choice(lista.valores)
    print(f'\nSoldado sorteado: Nº {esco1}\n')
    print("Lista de soldados antes da remoção")
    lista.imprime()
    ind_sold_apagado = lista.contagem(esco1)
    sold_apagado = lista.pesquisar_indice(ind_sold_apagado)
    print(f'\nSoldado retirado da lista: {sold_apagado}')
    lista.excluir(sold_apagado)
    print('''
Lista de soldados depois da remoção
Índice - Soldado''')
    lista.imprime()

print(f'\nO soldado ganhador é o soldado Nº {lista.valores[0]}')





    
