from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # read, text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write, text, + = cria o arquivo
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: # Para linha dentro do arquivo...
            dado = linha.split(';') # Vou criar dado...
            dado[1] = dado[1].replace('\n', '') # remover o \n
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # E mostrá-lo na tela.
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at') # append = colocar coisas no arquivo
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

