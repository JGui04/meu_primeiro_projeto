"""
Programa: Jogo de adivinhação
Autor: J. Guilherme
licença: GNU
Data: 2024/06/24
Versão: v1.1.1
Descrição: Este programa terá como proposta fazer com que o usuário acerte qual o número que foi sorteado pelo programa.
"""

# Importando biblioteca que irá sortear um número
import random

# Para iniciar o jogo caso a opção seja jogar de novo ou começar o jogo
opcao = 1

# Um Loop de repetição para que o jogo continue caso seja escolhido para jogar de novo
while opcao == 1:

    # Onde será sorteado o número de 1 a 100
    numero = random.randint(1,100)

    # Número de escolha
    escolha = 0

    # Se não for digitado um número inteiro
    try:
        
        # Onde será digitado o número do nível em que o usuário deseja jogar
        tentativas = int(input('Escolha seu nível\n1 - Fácil\n2 - Médio\n3 - Difícil\n'))

        # Caso a escolha não esteja entre 1 a 3, aparecerá na tela que não existe o nível escolhido e repetirá para que o usuário escolha o nível
        while tentativas < 1 or tentativas > 3:
            print('Nível não existe, escolha novamente.\n')
            tentativas = int(input('Escolha seu nível\n1 - Fácil\n2 - Médio\n3 - Difícil\n'))

        # Caso seja escolhido o nível fácil
        if tentativas == 1:
            chances = 10
            nivel = 10

        # Nível médio
        elif tentativas == 2:
            chances = 5
            nivel = 5

        # Nível difícil
        else:
            chances = 3
            nivel = 3
    # Caso o usuário não tenha digitado um número inteiro
    except:
        print('Isso não é um número inteiro positivo. Tente novamente')
        
        # Voltará para o início para o usuário escolher o nível
        continue
  
    # Um Loop para o caso de a escolha não tenha sido a certa ou as chances não tenham chegado continuar
    while chances > 0 and escolha != numero:

        # Se o usuário não digitar um número inteiro
        try:

            # Onde o usuário fará a escolha de número do 1 a 100
            escolha = int(input("Entre com um número de 1 até 100:\n"))

            # Vai diminuuindo as chances até zero independente do nível escolhido
            chances -=1

            # Caso o número escolhido seja não esteja entre 1 a 100, aparecerá na tela que deu um erro e para digitar novamente e pedirá para digitar novamente.
            while escolha < 0 or escolha > 100:
                print('ERRO - Número não está entre 0 e 100')
                escolha = int(input("\nEntre com um número de 1 até 100:\n"))

            # Caso o número seja menor que o sorteado aparacerá na tela e também quantas chances o usuário ainda tem.
            if (escolha < numero):
                print(f"\nO número é {escolha}, é menor que o sorteado !!!")
                print(f"Tentativas {chances} de {nivel} !!!\n")

            # Caso o número seja maior que o sorteado aparacerá na tela e também quantas chances o usuário ainda tem.
            elif (escolha > numero):
                print(f"\nO número {escolha}, é maior que o sorteado !!!")
                print(f"Tentativas {chances} de {nivel} !!!\n")

            # Se  usuário acetar o número sorteado aparecerá na tela e que ele acertou.
            else:
                print(f"\nO número {escolha} foi sorteado !!!")
                print(f"Você acertou Parabens!!!\n")
                break
        
        # Caso o que for digitado não seja um número inteiro, aparecerá na tela o erro e para escolher novamente.
        except:
            print('Isso não é um número inteiro. Escolha novamente.')

            # Para que volte onde o usuário possa escolher o número
            continue

        # Caso o usuário atinja o limite das chances e elas cheguem a ZERO, imprimirá na tela que ele não acertou.
        if(chances == 0):
            print(f"\nVocê Não acertou !!!\n")

            # Irá para o programa após isso.
            break

    # Se a opção escolhida nao for um número inteiro
    try:

        # No final mesmo que o usuário ganhe ou perca aparecerá essas opção para o caso dele (usuário) queira jogar novamente ou não.
        opcao = int(input('Você deseja jogar novamente ?\n1 - Sim\n2 - Não\n'))

        # Caso o usuário digite um numero que não for 1 ou 2, terá um Erro e pedirá para que digite novamente.
        while opcao < 1 or opcao > 2:
            print('ERRO - Digite novamente a sua opcão')
            opcao = int(input('Você deseja jogar novamente ?\n1 - Sim\n2 - Não\n'))

    # Se a opção escolhida não foi um número inteiro, aparecerá esse ERRO e vai perguntar novamente.
    except:
        print('Isso não é uma das opções disponíveis. Escolha novamente')
        continue

# Caso a opção escolhida seja o número 2, o programa se encerrará e imprimirá na tela um agradecimento 
else:
    print('Obrigado por jogar !!! :)')
