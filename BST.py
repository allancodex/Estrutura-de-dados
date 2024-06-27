#1.definindo a árvore
import collections


class Node:
  def __init__(self, dados):
    self.esquerda = None
    self.direita = None
    self.dados = dados

  #é importante lembrar que a função rodará várias vezes com valores diferentes, criando a árvore
  def inserirNode(self, dados):
    if self.dados is None:
      self.dados = dados
    else:
      if dados < self.dados:
        if self.esquerda is None:
          self.esquerda = Node(dados)
        else:
          self.esquerda.inserirNode(dados)
      
      elif dados > self.dados:
        if self.direita is None:
          self.direita = Node(dados)
        else:
          self.direita.inserirNode(dados)

def print_em_ordem(root):
  if root is None:
    return
  else:
    print_em_ordem(root.esquerda)
    print(root.dados,end =' ')
    print_em_ordem(root.direita)

def print_em_preordem(root):
  if root is None:
    return
  else:
    print(root.dados, end = ' ')
    print_em_preordem(root.esquerda)
    print_em_preordem(root.direita)
    
def print_em_posordem(root):
  if root is None:
    return
  else:
    print(root.dados, end = ' ')
    print_em_posordem(root.direita)
    print_em_posordem(root.esquerda)  

def fazerlista(root):
  if root is None:
    return
  else:
    dicionario[root.dados] = []
    fazerlista(root.esquerda)
    if root.esquerda:
      dicionario[root.dados].append(root.esquerda.dados)
    if root.direita:
      dicionario[root.dados].append(root.direita.dados)
    fazerlista(root.direita)
  return dicionario

def bfs(al):
  fila = collections.deque('g')
  visitado = []

  while fila:
    node = fila.popleft()
    visitado.append(node)
    [fila.append(x) for x in al[node]]
  print(visitado)
  
if __name__ == '__main__':
  root = Node('g')
  root.inserirNode('c')
  root.inserirNode('b')
  root.inserirNode('a')
  root.inserirNode('e')
  root.inserirNode('d')
  root.inserirNode('f')
  root.inserirNode('i')
  root.inserirNode('h')
  root.inserirNode('j')
  root.inserirNode('k')

  dicionario = {}
  aList = fazerlista(root)
  
#print_em_ordem(root)
#print_em_preordem(root)
#print_em_posordem(root)
  #bfs(aList)
