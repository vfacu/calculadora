import os


def clear():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # ? clear_console()
    print('\n--- Menu de Operación---')
    print('+')
    print('-')
    print('*')
    print('/')
    print('0')
