"""
Novidades:
    - help(print) no console -> definir sep=" " e end="\n"
    - "texto {}".format(variável)
    - "R$ {:7.2f}.format(1.7)           # formata a saida em números de caracteres iguais
    - "R$ {:07.2f}.format(2.6)          # preenche com zeros
    - "Data: {:02d}.format(2)           # preenche com zeros, sendo inteiro
"""

import random as rand


def jogar():
    print("****************************************")
    print("* BEM VINDO(A) AO JOGO DE ADIVINHAÇÃO! *")
    print("****************************************")

    numero_secreto = rand.randrange(1, 101)
    total_tentativas = 0
    pontos = 500

    print("Qual o nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil")
    nivel = int(input("Digite sua escolha: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    # while rodada <= total_tentativas:
    for rodada in range(1, total_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite o seu palpite (entre 1 e 100): "))
        if chute < 1 or chute > 100:
            print("Número invalido!")
            continue

        isCerto = numero_secreto == chute
        isMaior = chute > numero_secreto
        isMenor = chute < numero_secreto

        if isCerto:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if isMaior:
                print("Você errou. O seu chute foi maior que o número secreto.")
            if isMenor:
                print("Você errou. O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


if __name__ == "__main__":
    jogar()
