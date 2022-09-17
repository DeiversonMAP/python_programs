import random  # gerar numero aleatório
from os import name, system  # para executar comandos no terminal
from time import sleep  # colocar para dormir

import colorama as color  # alterar cores dos textos


def red(texto: str)-> str:
    """
    red Colore texto em vermelho

    Arguments:
        texto -- texto a ser colorido

    Returns:
        Texto na cor vermelha
    """
    return f'{color.Fore.RED}{texto}{color.Fore.RESET}'

def green(texto: str)-> str:
    """
    green Colore texto em verde

    Arguments:
        texto -- texto a ser colorido

    Returns:
        texto na cor verde
    """
    return f'{color.Fore.GREEN}{texto}{color.Fore.RESET}'

def cyan(texto: str)-> str:
    """
    cyan Colore texto em ciano

    Arguments:
        texto -- Texto a ser colorido

    Returns:
        texto na cor ciano
    """
    return f'{color.Fore.CYAN}{texto}{color.Fore.RESET}'

def number() -> int:
    """
    number 
        Gera numero aleatório entre 1 e 100
    Returns:
        int
    """
    return random.randint(1, 101)

def clean_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def verifica_numero(numero: int, count: int = 1) -> None:
    """
    verifica_numero : verifica se o numero chutado bate com o que foi gerado

    Arguments:
        numero -- numero a ser adivinhado

    Keyword Arguments:
        count -- numero de tentativas (default: {1})
    """
    sleep(0.5)
    chute : int
    if (chute := int(input(f"{green('Qual o número que pensei ?')}   ")) ) == numero:
        sleep(1.5)
        print(f"\nParabéns!! Você acertou o número com {cyan(str(count))} tentativas!\n")
    elif 1 > chute or chute > 100 :
        print(f"Número {red(str(chute))} está fora do intervalo entre {red('1')} e {red('100')}, favor chute novamente")
        verifica_numero(numero=numero, count=count)
    elif chute < numero:
        print(f"Número {red(str(chute))} é {red('menor')} que o esperado, chute novamente um {green('maior')}")
        verifica_numero(numero=numero, count=count+1)
    else :
        print(f"Número {red(str(chute))} é {red('maior')} que o esperado, chute novamente um {green('menor')}")
        verifica_numero(numero=numero, count=count+1)

def guess() -> None:
    """
    guess : Inicia o jogo
    """
    print(f"Pensei em um número entre entre 1 e 100 ")
    verifica_numero(numero = number())
    sleep(0.5)
    if input(f"Deseja jogar novamente? Digite 's' caso sim, qualquer outro valor caso não \n").upper() in ('S','SIM','Y','YES'):
        sleep(0.5)
        print(f"{cyan('Reiniciando ...')}")
        sleep(1)
        clean_screen()
        guess()
    else:
        sleep(1)
        print(f"{green('Muito obrigado pro jogar comigo!!')}")
        sleep(1)
        print(f"{red('Tchau !!!')}")
        sleep(3)
        clean_screen()

if __name__ == '__main__':
    print(f"""
{green('#')* 40}
{green(f"{' Jogo do chute ':#^40}")}
{green('#')* 40}
            """)
    guess()
