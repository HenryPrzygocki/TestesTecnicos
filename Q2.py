class Node:
  def __init__(self, id = None, key = None, fruta = None, left = None, right = None):
    self.fruta = fruta
    self.id = id
    self.key = key
    self.left = left
    self.right = right

def createTree(Tree,Frutas):
  # cria dicionario vazio que sera usado para relacionar o parentesco dos nós
  d = {}  
  
  # enumera a lista com o parentesco
  for id, key in enumerate(Tree):
    # cria os nós da árvore, usando o nome da fruta correspondente como valor e uma chave que indica o parentesco
    d[id] = Node(id,key,Frutas[id])

    # se a chave for -1, é a raiz da arvore
    if key == -1:
      root = d[id]
    else:
      # define qual o nó mae deste dado elemento (fruta)
      mae = d[key]

      # define o filho como sendo a fruta do dicionario correspondete ao indice
      if mae.left:
        mae.right = d[id]
      else:
        mae.left = d[id]
  return root

def hasPath(tree, id, key, path):
  # se o nó nao existe ou esta num nivel superior ao desejado, nao há caminho
  if not tree or tree.key > key: 
    return False
  
  path.append(tree.fruta)

  # se é o nó desejado, tem caminho
  if tree.id == id: 
    return True
  # se o nó esquerdo ou direito tem caminho
  if hasPath(tree.right,id,key,path) or hasPath(tree.left,id,key,path): 
    return True

  # caso nenhum dos nós filhos tenha caminho, nó mae nao tem caminho 
  path.pop(-1)
  return False

def searchTree(tree,id,key,path=[]):
  # se exite o caminho, retorna-o como array
  if hasPath(tree,id,key,path): 
    return " -> ".join(path)
  print("Sem caminho para fruta desejada")
  return path


# lista com os das frutas
Frutas = ["maça","morango","pera","goiaba","limao","abacaxi","laranja","banana","cebola"]

# define o parentesco dado pelo indice da lista Frutas, neste caso os elementos 1 e 2  (morango e pera) sao filhos do indice 0 (maça)
Tree = [-1,0,0,1,1,2,5,6,6]
tree = createTree(Tree,Frutas)
#           ________maça____________________________  
#          /                                        \ 
#     __morango__                              ___pera
#    /           \                            /       
# goiaba       limao              _________abacaxi    
#                                /                    
#                           __laranja___              
#                          /            \             
#                       banana       cebola

# Fruta desejada
Buscar = "Goiaba"
index = Frutas.index(Buscar.lower())
key = Tree[index]
path = searchTree(tree,index,key)
print(path)
