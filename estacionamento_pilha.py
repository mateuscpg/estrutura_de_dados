import numpy as np

class Pilha:
  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.__topo = -1
    self.__valores = np.empty(self.__capacidade, dtype=int)
  
  def __pilha_vazia(self):
    if self.__topo == -1:
      return True
    else:
      return False

  def __pilha_cheia(self):
    if self.__topo == self.__capacidade-1:
      return True
    else:
      return False

  def empilhar(self,valor):
    if self.__pilha_cheia():
      print('A pilha está cheia')
    else:
      self.__topo+=1
      self.__valores[self.__topo]=valor

  def desempilhar(self):
    if self.__pilha_vazia():
      print('A pilha está vazia')
    else:
      self.__topo-=1

  def ver_topo(self):
    if self.__topo != -1:
      return self.__valores[self.__topo]
    else:
      return -1

'''Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação problema: 
Armazene as placas dos carros de luxos (apenas os números) que estão estacionados em um rua sem saída.
 Dado uma placa verifique se o carro está estacionado na rua. 
Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.'''

def principal():

    capacidade = int(input("Quantas placas você deseja armazenar? "))
    pilha = Pilha(capacidade)

    for x in range (capacidade):
        pilha.empilhar(int(input(f" {x+1}ª placa que você deseja empilhar: ")))

    placa = int(input("\nDigite apenas os números da placa do carro que você quer checar: "))
    rua = int(input("\nO carro está estacionado na rua?\n[1] Sim\n[2] Não  "))
    if rua == 1:
        print (f"\nO carro que vai sair é o carro com a placa: {pilha.ver_topo()}")

        while pilha.ver_topo() != placa:
            pilha.desempilhar()
            print (f"\nO carro que vai sair é o carro com a placa: {pilha.ver_topo()}")
    else: 
        print("O carro não está estacionado na rua")
 

  

principal()


