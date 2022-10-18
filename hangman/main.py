from sys import exit

from utils.helper import check, clean_screen, print_hang
from utils.words import *


def main()-> None:
    # colocar um try aqui para levantar exceção pra caso seja inserido tipo errado
    try:
        dificuldade:int = int( input(f"""|{'='*60}|
|{' Bem vindo(a) ao jogo da forca ':=^60}|
|{'='*60}|
|{'Digite um numero entre 3 a 15 para escolher':^60}|
|{'o tamanho da palavra (3,4,...,13,14,15).':^60}|
|{'Vale lembrar que você poderá errar a letra':^60}| 
|{'apenas 5 vezes, na sexta vez perderá o jogo.':^60}|
|{'='*60}|
    Ensira o tamanho desejado: """))
        w: str = word(num = dificuldade)
    except ValueError:
        clean_screen()
        print(f"""|{'='*60}|
|{"Favor inserir um numero válido":^60}|""")
        main()
    except IndexError:
        clean_screen()
        print(f"""|{'='*60}|
|{"Favor inserir um numero válido dentro do limite especificado":^60}|""")
        main()
    else:
        hangman(word = 'parâmetro' #w
                ,erros=0,letters=[],comment='')
    

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

chute apenas uma letra por vez: ''').lower()[0]
    try:        #tratamento de erro para nao aceitar caracteres numéricos
        i:int = int(chute)
    except ValueError:
        if chute not in letters:
            b:bool
            comment,b = check(word= word,letter= chute)  # type: ignore
            letters.append(chute)
            if not b:
                erros+=1
            if erros <= 5:
                hangman(word = word,erros = erros,letters = letters ,comment = comment)
            else:
                result(word,False)
        else:
            hangman(word = word,erros = erros,letters = letters ,comment = comment)
    else:
        hangman(word = word,erros = erros,letters = letters ,comment = comment)

def result(word:str, finished:bool=False) -> None:
    clean_screen()
    if not finished:
        print(f""""
Infelizmente você perdeu.
A palavra é : {word.upper()}

|{'='*60}|""")
    else:
        print(f"""|{'='*60}|
|{' '+word+' ':=^60}|
|{'='*60}|
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
    clean_screen()
    main()
