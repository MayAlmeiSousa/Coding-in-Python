#// Média da Turma.
#// Função: Efetuar o calculo da média de uma turma de 10 Alunos. 

print("-"*50)
print(" Colégio Estadual Guilherme Santos ")
print("-"*50)

def media_aluno (a,b:float):
    m_aluno=(a+b)/2
    return(m_aluno)

def media_turma (a:float):
    m_turma=a/10
    return(m_turma)

aluno_nome=[]
n1=""
n2=""
nota1=0.0
nota2=0.0
aluno_media=[]
soma_m=0.0

for x in range(0,10):
     aluno_nome.append(input("Digite o nome do aluno: "))
     
     n1=input("Digite a primeira nota: ")
     nota1=float(n1)
     n2=input("Digite a segunda nota: ")
     nota2=float(n2)
   
     result_m=media_aluno(nota1,nota2)
     
     aluno_media.append(result_m)
     
     soma_m=result_m+soma_m
       
turma_m=media_turma(soma_m)
      
print(f"A média dos alunos da turma é de {turma_m:.2f}") #//Formatação para mostrar na tela o resultado com dois números decimais depois da vírgula. 
