import random
def jogar():
    print("FORCA")

    def escolha_palavra():
        #FAZ A ABERTURA DO ARQUIVO, ONDE ESTÁ AS PALAVRAS SECRETAS, E ESCOLHE UMA ALEATÓRIAMENTE E SELECIONA NO JOGO
        #arq = open("palavras.txt", "r", encoding="utf-8")
        with open("palavras.txt", encoding="utf-8") as arq:
            palavras_arquivo = []
            for i in arq:
                palavras_arquivo.append(i.replace("\n","").upper())
                print(i)
        print(palavras_arquivo)
        palavra_chave = ''.join(random.choices(palavras_arquivo))  #join passa a palavra da lista extraida pra string, unindo todas as palavras em uma
        return palavra_chave

    #print(palavra_secreta)
    #DEFINE AS VARIÁVEIS, E RECRIA A PALAVRA SECRETA, PARA COMPARAR COM A ORIGINAL NO FINAL
    #palavra_secreta = 'banana'.upper()
    palavra_secreta = escolha_palavra()
    palavra_secreta2 = list(palavra_secreta)
    perdeu = False
    erros = 0
    ganhou = False
    count = 0
    letras_certas = []


    #CRIA O CAMPO DA PALAVRA CONFORME O TAMANHO DELA PARA MOSTRAR NA TELA
    for i in range(0,len(palavra_secreta)):
        #print(i)
        letras_certas.append("_")
    print(letras_certas)

    # enquanto não enfoucou e não acertou
    #ABRE O LAÇO DE REPITIÇÃO, ENQUANTO O STATUS DE PERDEU OU GANHOU NÃO ALTERAR, O JOGO SE REPETE
    while not perdeu and not ganhou:
        print("Jogo em andamento...")

        letras = input("Digite uma letra: ").upper().strip()

        #SE A LETRA ESCOLHIDA ESTIVER NA PALAVRA PREENCHE O CAMPO DA PALAVRA
        if letras in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == letras:
                    print(index, ':', letra)
                    letras_certas[index] = letra
            #QUANDO A PALAVRA SECRETA ESTIVER PREENCHIDA, ELA VAI FICAR IGUAL A CÓPIA CRIADA NO INICIO, ASSIM MUDA O STATUS DE GANHOU PRA TRUE E ELE VENCE!
            if letras_certas == palavra_secreta2:
                ganhou = True
                print("Você ganhoooouu, PArabéns!!")
        #SE O JOGADOR COMETER 7 ERROS, O STATUS DE PERDEU MUDA PRA TRUE E SAI DO LAÇO, ELE PERDE!
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
