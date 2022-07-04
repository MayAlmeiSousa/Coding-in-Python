#Funçao realizar as operações matemáticas de acordo com a escolha do usuário. 
#Etapa1:
#Mostar uma tela inicial e pedir ao usuário que digite o seu nome e os dois números.
print('-------------------------------------')
print('       Operações Matemáticas         ')
print('-------------------------------------')
num1=input('Digite o Primeiro Número: ')
num2=input('Digite o Segundo Número:  ')
#Etapa2:
#Mostar ao usuário o Menu de opções e registrar a esolha do mesmo.
print('-------------------------------------')
print('              Menu                   ')
print('-------------------------------------')
print('[1] Soma')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] divisão')
print('[5] Potência')
print('-------------------------------------')
resp=input('Insira aqui a sua escolha: ')
#Etapa3:
#Efetuar a operação escolhida pelo usuário.
if int(resp)==1:
    soma=int(num1) + int(num2)
elif int(resp)==2:
    subtra= int(num1) - int(num2)
elif int(resp)==3:
    multi= int(num1) * int(num2)
elif int(resp)==4:
    divi= int(num1) / int(num2)
    float(divi)
else: 
    pot=int(num1)**int(num2)
#Etapa5:
#Mostrar o Rsultado final com o resultado da operação escolhida.       
print('-------------------------------------')
print('         Resultado Final             ')
print('-------------------------------------')
if int(resp)==1:
    print('O resultado da soma é:',soma)
elif int(resp)==2:
    print('O resultado da subtração é:',subtra)
elif int(resp)==3:
    print('O resultado da multiplicação é:',multi)
elif int(resp)==4:
    print('O resultado da divisão é:',divi)
else: 
    print('O resultado da soma é:',pot)