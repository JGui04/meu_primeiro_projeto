"""
Programa: Jogo de adivinhação
Autor: J. Guilherme
licença: GNU
Data: 2024/06/14
Versão: v1
Descrição: Este programa terá como proposta fazer com que o usuário acerte qual o número que foi sorteado pelo programa.
"""

import random
opcoes = 1

numero = random.randint(1,100)

escolha = 0
tentativas = 0
opcao = 1

while opcao == 1:

    numero = random.randint(1,100)

    escolha = 0
    tentativas = 0

    while tentativas < 10 and escolha != numero:

        escolha = int(input("Entre com um número de 1 até 100:\n"))

        tentativas +=1

        while escolha < 0 or escolha > 100:
            print('ERRO - Número não está entre 0 e 100')
            escolha = int(input("\nEntre com um número de 1 até 100:\n"))

        if (escolha < numero):
            print(f"\nO número é {escolha}, é menor que o sorteado !!!")
            print(f"Tentativas {tentativas} de 10 !!!\n")
        elif (escolha > numero):
            print(f"\nO número {escolha}, é maior que o sorteado !!!")
            print(f"Tentativas {tentativas} de 10 !!!\n")
        else:
            print(f"\nO número {escolha} foi sorteado !!!")
            print(f"Você acertou Parabens!!!\n")
            break

        if(tentativas == 10):
            print(f"\nVocê Não acertou !!!\n")
            break

    opcao = int(input('Você deseja jogar novamente ?\n1 - Sim\n2 - Não\n'))

    while opcao < 1 or opcao > 2:
        print('ERRO - Digite novamente a sua opcão')
        opcao = int(input('Você deseja jogar novamente ?\n1 - Sim\n2 - Não\n'))

else:
    print('Obrigado por jogar !!! :)')
