from lib.interface import *
from lib.arquivo import *
from time import sleep

# Criar o arquivo texto caso não exista.
arq = 'notasFADIC.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver notas do semestre', 'Cadastrar nova nota', 'Sair do Sistema'])
    match resposta:
        case 1:
            # Opção de listar o conteúdo de um arquivo
            lerArquivo(arq)
        case 2:
            # Opção de cadastrar uma nova nota
            cabeçalho('NOVO CADASTRO')
            cadeirasPrimeiroPeríodo = {1: 'Matemática Discreta (MAT)',
                                       2: 'Programação Básica (PGB)',
                                       3: 'Ambiente Computacional (AMB)',
                                       4: 'Introdução à ESW (IES)'                                       
                                       }
            cadeira = menuCadeiras(cadeirasPrimeiroPeríodo)
            nota = float(input(f'{cadeirasPrimeiroPeríodo[cadeira]} - Nota: '))
            cadastrar(arq, cadeirasPrimeiroPeríodo, cadeira, nota)
        case 3:
            cabeçalho('Saindo do sistema... Até logo!')
            break
        case _:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
