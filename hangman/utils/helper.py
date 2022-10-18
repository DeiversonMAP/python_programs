from os import name, system
from typing import List


def clean_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def print_hang(word:str,letters:List[str]) -> str:#NÃO EATÁ CONCATENANDO OS CARACTERES ESPECIAIS
    # return ''.join([l if l in letters else '_' for l in word  ])
    retorno : str=''
    for l in word:
        try:
            b:bool = acentos[l] in letters  
        except KeyError:
            b = False
        
        if l in letters or b :
            retorno += l
        # elif l in acentos and b:
            
        #     retorno += acentos[l]
        else:
            retorno +='_'
    return retorno            

def check(word:str,letter: str)-> str and bool:
    if len(letter)== 0:
        return '' ,True  # type: ignore
    elif check_especial(word= word,letter=letter) or letter in word :
        return f"\nA letra {letter} apareceu {word.count(letter)} vezes \n", True  # type: ignore #ARRUMAR O CONTADOR PARA QUANDO TIVER CARACTERE ESPECIAL
    else :
        return f"\nA letra {letter} não existe na palavra\n" , False  # type: ignore

def check_especial(word:str,letter: str)-> bool:
    if letter in aux:
        for l in word:
            if l in aux[letter] :
                print(l)
                for i in aux[letter]:
                    if i == l:
                        return True
    return False 


acentos = {
    'á':'a',
    'à':'a',
    'â':'a',
    'â':'a',
    'é':'e',
    'ê':'e',
    'í':'i',
    'ó':'o',
    'ô':'o',
    'ô':'o',
    'ú':'u',
    'ç':'c'
    }
aux = {
    'a': ['a','á','à','â','ã'],
    'e':['e','é','ê'],
    'i':['i','í'],
    'o':['o','ó','ô','ô'],
    'u':['u','ú'],
    'c':['c','ç']
    }

