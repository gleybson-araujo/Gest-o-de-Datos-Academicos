import re
from Validacoes import Validacoes

class Estudante():
    proxima_matricula = 1
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        self.matricula = Estudante.proxima_matricula
        Estudante.proxima_matricula += 1
        # self.idade = idade
        # self.ano_letivo = ano_letivo
    
    @staticmethod
    def incluir(menu_operacoes):
        while True:
                cpf = input('\nPara voltar ao menu, digite 0.\n\nInsira o CPF do estudante: ')
                if cpf == '0':
                    print('\nVoltando para o menu de operações...')
                    return
                elif not Validacoes.validar_cpf(cpf):
                    print('\nCPF inválido, tente novamente!')    
                elif Validacoes.cpf_ja_existe(cpf, menu_operacoes):
                    print('\nJá existe um estudante cadastrado com este CPF! Tente novamente!')    
                else:
                    break
        while True:
            nome = input('\nPara voltar ao menu, digite 0.\n\nInsira o nome do estudante: ')
            if nome == '0':
                print('\nVoltando para o menu de operações...')
                return
            elif not re.match("^[A-Za-z ]+$", nome):
                print('\nNome inválido, o nome só pode conter letras sem acentuação.')
            else:  
                break
        return Estudante(cpf, nome)
    
    @staticmethod
    def listar(menu_operacoes):
        if not menu_operacoes.dados_estudantes:
                print('\nNenhum estudante matriculado até o momento!')
        else:
            print('\n**** LISTA DE ALUNOS ****')
            for estudante in menu_operacoes.dados_estudantes:
                    print(f'\nMatricula: {estudante.matricula}\nAluno: {estudante.nome.upper()}\nCPF: {estudante.cpf}')       
    
    @staticmethod
    def atualizar(menu_operacoes):
        if not menu_operacoes.dados_estudantes:
            print('\nNenhum estudante matriculado até o momento!')
            return
        try:
            matricula = int(input('\nPara voltar ao menu, digite 0.\nQual aluno você deseja atualizar?\nDigite o nº da matricula: '))
            if matricula == 0:
                print('\nVoltando para o menu de operações...')
                return
            else:
                for estudante in menu_operacoes.dados_estudantes:
                    if estudante.matricula == matricula:
                        while True:
                            buffer = estudante.cpf
                            estudante.cpf = 0
                            novo_cpf = input('\nPara voltar ao menu, digite 0.\n\nInsira o CPF do estudante: ')
                            if novo_cpf == '0':
                                print('\nVoltando para o menu de operações...')
                                return
                            elif not Validacoes.validar_cpf(novo_cpf):
                                print('\nCPF inválido, tente novamente!')
                                estudante.cpf = buffer
                            elif Validacoes.cpf_ja_existe(novo_cpf, menu_operacoes):
                                print('\nJá existe um estudante cadastrado com este CPF! Tente novamente!')
                                estudante.cpf = buffer
                            else:
                                estudante.cpf = novo_cpf
                                break
                        while True:
                            novo_nome = input('\nPara voltar ao menu, digite 0.\n\nInsira o nome do estudante: ')
                            if novo_nome == '0':
                                print('\nVoltando para o menu de operações...')
                                return
                            elif not re.match("^[A-Za-z ]+$", novo_nome):
                                print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                            else:  
                                estudante.nome = novo_nome
                                break
                print('\nDados do aluno atualizados com sucesso!')
                return
        except ValueError:
            print('\nOcorreu um erro ao atualizar o estudante! Certifique-se de inserir um número válido para a matrícula.')
    
    @staticmethod
    def excluir(menu_operacoes):
        if not menu_operacoes.dados_estudantes:
            print('\nNenhum estudante matriculado até o momento!')
            return
        try:
            matricula = int(input('\nPara voltar ao menu, digite 0.\nQual estudante você deseja excluir do sistema?\nDigite o nº da matricula: '))
            if matricula == 0:
                print('\nVoltando para o menu de operações...')
                return
            else:
                for estudante in menu_operacoes.dados_estudantes:
                    if estudante.matricula == matricula:
                        print(f'\nVocê tem certeza que deseja excluir o aluno {estudante.nome.capitalize()} de matrícula: {estudante.matricula}?')
                        while True:
                            escolha = input('\n[Y/N]? ')
                            if escolha.upper() == 'Y':
                                menu_operacoes.dados_estudantes.remove(estudante)
                                print('\nAluno excluito com sucesso!')
                                return
                            elif escolha.upper() == 'N':
                                print('\nVoltando para o menu de operações...')
                                return
                            else:
                                print('\nOpção inválida, tente novamente!')
                    else:
                        print('\nNúmero de matrícula informado não existe no banco de dados!')
                        return
        except ValueError:
            print('\nOcorreu um erro ao excluir o aluno. Certifique-se de inserir um número válido para a matrícula.')
            
class Professor():
    def __init__(self, nome):
        self.nome = nome
