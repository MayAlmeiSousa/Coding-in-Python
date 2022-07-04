#Etapa 1:
#Mostrar uma tela inicial com a mensagem para o usuário sobre a tabuada que deve ser mostrada pelo programa.
print("-"*40)
print("           Tabuada              ")
print("-"*40)
print("Qual tabuada deve ser mostrada:")
resp=input("resposta: ")
#Etapa2:
#Mostrar o Loop com a tabuada escolhida pelo usuário.
print("-"*40)
for x in range (1,11):  
    result=int(resp)*x
    print(resp," X ",x," = ",result)
print("-"*40)