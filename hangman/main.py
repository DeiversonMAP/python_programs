from sys import exit

from utils.helper import check, clean_screen, print_hang
from utils.words import *


def main()-> None:
    # colocar um try aqui para levantar exceção pra caso seja inserido tipo errado
    dificuldade:int = int( input(f"""|{'='*60}|
|{' Bem vindo(a) ao jogo da forca ':=^60}|
|{'='*60}|
|{'Digite um numero entre 3 a 15 para escolher':^60}|
|{'o tamanho da palavra (3,4,...,13,14,15).':^60}|
|{'Vale lembrar que você poderá errar a letra':^60}| 
|{'apenas 5 vezes, na sexta vez perderá o jogo.':^60}|
|{'='*60}|
    Ensira o tamanho desejado: """))

    hangman(word =word(num = dificuldade),erros=0,letters=[],comment='')


def hangman(word:str, erros:int = 0 , letters:list[str] = [],comment:str='') -> None:
    secret:str
    if (secret:=print_hang(word,letters))== word:
        result(word,True)
    clean_screen()        
    # Criar modo de imprimir a forca na tela sem repetir a tela 
    chute:str = input(f'''\r
A palavra {word}
A palavra contém {len(word)} letras.
Você ja errou {erros} vezes (máximo 5).
Letras já tentadas: {", ".join(letters)}
{comment}
Palavra a ser adivinhada:
{secret}

chute apenas uma letra por vez:
                                ''').lower()

    if chute not in letters:
        comment:str 
        b:bool
        comment,b = check(word,letter=chute)
        if not b:
            erros+=1
        if erros <= 5:
            letters.append(chute)
            hangman(word = word,erros = erros,letters = letters ,comment = comment)
        else:
            result(word,False)

def result(word:str, finished:bool=False) -> None:
    if not finished:
        print(f""""
Infelizmente você perdeu.
A palavra é : {word.upper()}

|{'='*60}|""")
    else:
        print(f"""|{'='*60}|
|{"Parabéns, você adivinhou a palavra !!!":^60}|
|{'='*60}|""")

    decisao = input(f"""
Deseja jogar de novo? S/N
""")
    if decisao.lower()[0] =='s':
        clean_screen()
        main()
    else:
        clean_screen()
        print(f'Obrigado por jogar comigo!!!')
        exit(0)

if __name__ == '__main__':
    main()
