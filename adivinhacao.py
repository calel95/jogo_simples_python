import random

def jogar():

    numero_seceto = random.randrange(101)

    valor = 0
    maior = 0
    menor = 999999999999

    nivel = 0

    print("Escolha o nível do desafio:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    dificuldade = int(input())

    if dificuldade == 1:
        nivel = 9
    elif dificuldade == 2:
        nivel = 6
    elif dificuldade == 3:
        nivel = 3

    for i in range(1,nivel + 1):
        valor = int(input("Digite valor: "))
        if valor == numero_seceto:
            print("Parabéns, você acetou")
            break
        elif valor > numero_seceto:
            print("o numero é menor")
        elif valor < numero_seceto:
            print("o número é maior")

    print("Fim do jogo!")

if __name__ == '__main__':
    jogar()