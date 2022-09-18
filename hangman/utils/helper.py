from os import name, system


def clean_screen() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def print_hang(word:str,letters:list[str]) -> str:
    return ''.join([l if l in letters else '_' for l in word  ])

def check(word:str,letter: str)-> str and bool:
    if len(letter)== 0:
        return '' ,True
    elif letter in word:
        return f"\nA letra {letter} apareceu {word.count(letter)} vezes nela\n", True
    else :
        return f"\nA letra {letter} não está na nela\n" , False
