import os  # para executar comandos no terminal
import random  # gerar numero aleatório
import time  # colocar para dormir

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

def verifica_numero(numero: int, count: int = 1) -> None:
    """
    verifica_numero : verifica se o numero chutado bate com o que foi gerado

    Arguments:
        numero -- numero a ser adivinhado

    Keyword Arguments:
        count -- numero de tentativas (default: {1})
    """
    time.sleep(0.5)
    if (chute := int(input(f"{green('Qual o número gerado ?')}   ")) ) == numero:
        time.sleep(1.5)
        print(f"Parabéns!! Você acerto o numero com {cyan(str(count))} tentativas!\n")
    elif 1 > chute or chute > 100 :
        print(f"Número fora to intervalo entre {red('1')} e {red('100')}, favor chute novamente")
        verifica_numero(numero=numero, count=count+1)
    elif chute < numero:
        print(f"Número {red('menor')} que o esperado, chute novamente um {green('maior')}")
        verifica_numero(numero=numero, count=count+1)
    else :
        print(f"Número {red('maior')} que o esperado, chute novamente um {green('menor')}")
        verifica_numero(numero=numero, count=count)


def guess() -> None:
    """
    guess : Inicia o jogo
    """
    print(f"Um numero foi gerado automaticamente entre 1 e 100 ")
    verifica_numero(numero = number())
    time.sleep(0.5)
    if input(f"Deseja jogar novamente? Digite 's' caso sim, qualquer outro valor caso não \n") in ('s','sim','S','SIM'):
        time.sleep(0.5)
        print(f"{cyan('Reiniciando ...')}")
        time.sleep(1)
        os.system("cls")
        guess()
    else:
        time.sleep(0.5)
        print(f"{green('Muito obrigado pro jogar conosco!!')}")
        time.sleep(0.5)
        print(f"{red('Finalizando...')}")
        time.sleep(3)

if __name__ == '__main__':
    guess()
