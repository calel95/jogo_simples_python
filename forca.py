def jogar():
    print("FORCA")

    palavra_secreta = 'banana'.upper()
    palavra_secreta2 = list(palavra_secreta)
    perdeu = False
    erros = 0
    ganhou = False
    count = 0
    letras_certas = []

    #print(palavra_secreta2)


    for i in range(0,len(palavra_secreta)):
        #print(i)
        letras_certas.append("_")
    print(letras_certas)

    # enquanto não enfoucou e não acertou
    while not perdeu and not ganhou:
        print("Jogo em andamento...")

        letras = input("Digite uma letra: ").upper().strip()

        if letras in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == letras:
                    print(index, ':', letra)
                    letras_certas[index] = letra
            if letras_certas == palavra_secreta2:
                ganhou = True
                print("Você ganhoooouu, PArabéns!!")
        else:
            erros = erros + 1
            palavra_secreta
            print(f"Erros {erros}/7")
            if erros == 7:
                perdeu = True
                print(f"Você perdeu, a palavra secreta era {palavra_secreta}")
            else:
                continue
        print(letras_certas)


if __name__ == "__main__":
    jogar()