#Agora que já exercitou os conceitos faça um programa capaz de realizar: (g ° f), (g ° g), (f° f) e (f ° g). Para quaisquer f(x) e g(x) que forem dados como entrada.

#Para testar com outras f(x) e g(x) é necessário alterar dentro dessas 4 funções
def gof(x):
  f=2*x
  g=3*x
  return 3*f

def gog(x):
  f=2*x
  g=3*x
  return 3*g

def fof(x):
  f=2*x
  g=3*x
  return 2*f
  
def fog (x):
  f=2*x
  g=3*x
  return 2*g

#Apresentando na tela o menu, para o usuario selecionar oq quer calcular
print("-- MENU --")
print("1 - gof")
print("2 - gog")
print("3 - fof")
print("4 - fog")
funcao = int(input("Escolha um dos números: "))

#Aqui calculamos as funções de acordo com a opção escolhida
if funcao == 1:
  #Aqui é possível alterar o valor de x, dentro do parenteses
  print(gof(1))

if funcao == 2:
  print(gog(1))

if funcao == 3:
  print(fof(1))
  
if funcao == 4:
  print(fog(1))
    

