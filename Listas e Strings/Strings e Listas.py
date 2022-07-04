#Projeto desenvolvido para o entendimento dos conceitos básicos de Strings e Listas.
#Paso1: Inserção do nome.
print("------------ Brincando com Strings --------------")
nome=input("Insira o seu Nome : ")
#Passo2:Mostrar cada letra armazenada na variável.
print("O nome digitado foi:",nome)
print("---------------------------------------------------")
for x in nome:
    print(x)
#Passo3:Mostrar ao usuário a quantidade de letras que o nome possue.
print("A Quantidade de letras é ",len(nome))
#Fim da primeira parte.
#Início da segunda parte com Listas.
#Passo1:Inserção dos nomes dentro das listas.
print("------------ Brincando com Listas --------------------")
Avang_nome=["Steve Rogers","Tony Stark","Peter Parker","Clint Barneers","Thor Odinson","Sam Wilson"]
#Passo2:Mostrar cada nome para o usuário.
for i in Avang_nome:
    print(i)
#Passo3: Mostar a quantidade de elementos da lista, ou seja, o tamanho da lista e não a quantidade de letras de cada nome.
#isto é o que diferencia um função "LEN" da outra.
print("A Quantidade de elementos dentro da Lista é:",len(Avang_nome))