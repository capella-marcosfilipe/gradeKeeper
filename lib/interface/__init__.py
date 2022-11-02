def leiaInt(msg):
    while True:
        try: # Tente fazer isso aqui.
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m\nO usuário preferiu não digitar este número\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

def menuCadeiras(dict):
    cabeçalho('CADEIRAS DE 2022.2')
    for key, value in dict.items():
        print(f'\033[33m{key}\033[m - \033[34m{value}\033[m')
    print(linha())
    opc = leiaInt('\033[33mSua opção: \033[m')
    return opc