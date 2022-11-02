from lib.interface import *

def arquivoExiste(nome):
    try:
        file = open(nome, 'rt') # read, text
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        file = open(nome, 'wt+') # write, text, + = cria o arquivo
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        file = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabeçalho('NOTAS CADASTRADAS')
        for linha in file: # Para linha dentro do arquivo...
            dado = linha.split(';') # Vou criar dado...
            dado[1] = dado[1].replace('\n', '') # remover o \n
            print(f'{dado[0]:<30}{dado[1]:>3}') # E mostrá-lo na tela.
    finally:
        file.close()


def cadastrar(arq, dict, cadeira, nota):
    try:
        file = open(arq, 'at') # append = colocar coisas no arquivo
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            file.write(f'{dict[cadeira]};{nota}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Nova nota de {dict[cadeira]} adicionada.')
            file.close()

