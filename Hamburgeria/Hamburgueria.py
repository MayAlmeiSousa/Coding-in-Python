#Criação das Funções para o menu ou cardápio.
def menu_hambuguer():
  
  print("         Menu         ")  
  print("-"*30)
  print(" [1] X-Burguer ")
  print(" [2] X- Egg ")
  print(" [3] X-Bacon ")
  print(" [4] Natural ")
  
def menu_bebida(): 
  
  print("         Bebidas         ")
  print("-"*30)
  print(" [1] Refrigerante")
  print(" [2] Suco Natural")  
  print(" [3] Chopp de Vinho")
  print(" [4] Milkshake")
  print(" [5] Nenhuma")

#Declaração da variável de controle do Loopy.
novo_pedido=1
pagamento=""

#ínicio do Loop.
while novo_pedido == 1:
  
  print("Ben Vindo(a) Hamburgueria Sabor Único")
  nome=input("Insira o seu nome: ")
  menu_hambuguer()
  print("-"*30)
  hamb=input(" Escolha: " )
  print("-"*30)
  menu_bebida()
  print("-"*30)
  bebi=input(" Escolha: " )
  print("-"*30)
  
#Comando para inserir o valor e o nome do hamburguer escolhido pelo usuário.
  if int(hamb)==1:
    nome_hamb="X-Burguer" 
    valor_hamb=5.00
  elif int(hamb)==2:
    nome_hamb="X-Egg"
    valor_hamb=4.50
  elif int(hamb)==3:
    nome_hamb="X-Bacon"
    valor_hamb=6.00
  else:
    nome_hamb="Natural"
    valor_hamb=7.00
  
#Comando para inserir o valor e o nome doa bebida escolhido pelo usuário.
  if int(bebi)==1:
    nome_bebida="Refrigerante"
    valor_bebida=3.00
    tot_pedidos=valor_hamb+valor_bebida
  elif int(bebi)==2:
     nome_bebida="Suco Natural"
     valor_bebida=4.00
     tot_pedidos=valor_hamb+valor_bebida    
  elif int(bebi)==3:
    nome_bebida="Chopp de Vinho"
    valor_bebida=5.00
    tot_pedidos=valor_hamb+valor_bebida
  else:
    nome_bebida="Nenhuma"
    valor_bebida=0.00
    tot_pedidos=valor_hamb+valor_bebida
    
#Status do Pedido:   
  print("-"*30)
  print("         Status         ")
  print("Pedido:",nome)
  print("Nome Hamburguer:",nome_hamb)
  print("Nome Bebida:",nome_bebida)
  print("Total do Pedido:",tot_pedidos,"R$")
  print("-"*30) 
  
#Simulação do pagamento:  
  print("Qual vai ser a forma de pagamento ?")
  print("Dinheiro [1] ou Cartão [2]")
  pagamento=input("Escolha: ")
  
  if pagamento=="1":
    print("Processando o pagamento aguarde.")
    print("Pagamento realizado com sucesso !!")
  elif pagamento=="2":
    print("Processando o pagamento aguarde.")
    print("Pagamento realizado com sucesso !!")
    
#Pagamento aprovado continuação do sistema:
  print("Deseja resalizar outro pedido:")
  print("[1] Sim     [2] Não")
  novo_pedido=int(input("Escolha: "))

else:
  print("Pedido Realizado com Sucesso !!")
  print("Obrigada pela sua preferência.")
  print("Volte Sempre !!")

#fim do Loop e fim do sistema.