import Adivinhacao
import Forca

print("*********************************")
print("Bem vindo, escolha o seu jogo")
print("*********************************")



jogo = int(input("Digite (1) para escolher o jogo de Adivinhação ou (2) para o jogo de Forca?: "))

if(jogo == 1):

    Adivinhacao.jogar()
    
else:
    
    Forca.jogar()


