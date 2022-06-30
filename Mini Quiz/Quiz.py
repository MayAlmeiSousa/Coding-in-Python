#Função: Gerar um pequeno Quiz com 4 Perguntas seguida de 5 alternativas cada
#Etapa1.
#Tela inicial do jogo com uma mesagem de Boas Vindas ao usuário.
nome=input("Para começar a jogar informe o seu nome: ")
print(nome,"Bem Vindo(a) ao Jogo QuizMania. ")
print("------------------------------------------------------------------------------------------")
#Etapa2.
#Mostrar as perguntas na tela e capturar as respostas.
#As resposta são armazenadas em uma variável por meio do comando "Input".
print("                               Pergunta 01                                                ")
print("Qual ator interpretou o personagem dos quadrinhos Capitão América nos filmes da Marvel ?  ")
print("a.Tom Holland    b.Criss Evans      c.Sebastian Stan      d.Jesen Ackles      e.Brad Britt")
resp1=input("Resposta: ")
print("------------------------------------------------------------------------------------------")
print("                                Pergunta 02                                               ")
print("Qual foi o primeiro filme do Universo Compartilhado da Marvel ? ")
print("a.Homem Formiga e a Vespa   b.Guardiões da Galáxia      c.Homem de Ferro      d.Doutor Estranho      e.O Incrível Hulk")
resp2=input("Resposta: ")
print("------------------------------------------------------------------------------------------")
print("                                 Pergunta 03                                              ")
print("Qual é a cidade que o personagem Kratos do jogo God Of War nasceu? ")
print("a.Rodes   b.Athena     c.Esparta      d.Roma      e.Constantinopla")
resp3=input("Resposta: ")
print("------------------------------------------------------------------------------------------")
print("                                 Pergunta 04                                              ")
print("Qual é o nome da cidade em o personagem Batman da DC nasceu? ")
print("a.GothamCity   b.Megacity   c.NovaYork      d.Dakota      e.Kansas")
resp4=input("Resposta: ")
print("------------------------------------------------------------------------------------------")
#Etapa3
#Mostrar se todas as repostas estão corretas ou se alguma se econtra incorreta.
#Uma mesagem é emitida ao usuário.
if resp1=="b" and resp2=="c" and resp3=="c" and resp4=="a":
    print("Parabéns !! ",nome,"todas as respostas estão corretas !!")
else:
    print(nome,"Infelizmente não foi desta vez, pois existem respostas erradas.")
