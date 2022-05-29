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
      return print(self.__valores[self.__topo])
    else:
      return -1
    
    
def principal():
  capacidade = int(input("Quantos números você deseja informar para a pilha :"))
  pilha = Pilha(capacidade)
  
  for x in range (capacidade):
    pilha.empilhar(int(input(f" {x+1}º número que você deseja empilhar: ")))

  print("A ordem inversa dessa pilha será:")
  for x in range(capacidade):
    pilha.ver_topo()
    pilha.desempilhar()
    

principal()
