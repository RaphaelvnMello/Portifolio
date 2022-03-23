import random

def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    arquivo = open(r'D:\Biblioteca de Projetos\Programação\Python\Jogo\Jogoteca\palavras.txt')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print("São:", len(letras_acertadas), "letras \n",letras_acertadas)
    erro = 0
    enforcou = False
    acertou = False
   

    while (not acertou and not enforcou):

        index = 0
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra       
                index = index + 1

        else:
              erro += 1  
              print("Você errou, restam {} tentativas" .format(7 - erro))
              desenha_forca(erro)
        
        if(erro == 7):
            print("Você perdeu, a palavra secreta era : {}" .format(palavra_secreta))
            enforcou = True
       
        if("_" not in letras_acertadas):
            print("Parabéns você ganhou!")
            acertou = True

        print(letras_acertadas) 

    print("Fim do jogo")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()