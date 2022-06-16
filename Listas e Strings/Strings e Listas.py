#Projeto desenvolvido para o entendimento dos conceitos básicos de Strings e Listas.
#Paso1: Inserção do nome.
print("------------ Brincando com Strings --------------")
nome=input("Insira o seu Nome : ")
#Passo2:Mostrar cada letra armazenada na variável.
#Limitação: Só funcinará com nomes que possuem 6 letras.
print("O nome digitado foi:",nome)
print("---------------------------------------------------")
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
#Passo3:Mostrar ao usuário a quantidade de letras que o nome possue.
print("A Quantidade de letras é ",len(nome))
#Fim da primeira parte.
#Início da segunda parte com Listas.
#Passo1:Inserção dos nomes dentro das listas.
#Limitação: A mesma da primeira parte só funcionará com a quantidade pré formatada.
print("------------ Brincando com Listas --------------------")
Avang_nome=["Steve Rogers","Tony Stark","Peter Parker","Clint Barneers","Thor Odinson","Sam Wilson"]
#Passo2:Mostrar cada nome para o usuário.
print(Avang_nome[0])
print(Avang_nome[1])
print(Avang_nome[2])
print(Avang_nome[3])
print(Avang_nome[4])
print(Avang_nome[5])
#Passo3: Mostar a quantidade de elementos da lista, ou seja, o tamanho da lista e não a quantidade de letras de cada nome.
#isto é o que diferencia um função "LEN" da outra.
print("A Quantidade de elementos é ",len(Avang_nome))
