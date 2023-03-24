import adivinhacao
import forca

def jogos():
    print("1 - adivinhacao")
    print("2 - forca")
    opcao = int(input("Escolha um dos jogos\n"))

    if opcao == 1:
        print("jogo adivinhacao")
        adivinhacao.jogar()
    elif opcao == 2:
        print("jogo forca")
        forca.jogar()

if __name__ == "__main__":
    jogos()