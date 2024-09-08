from Classes import Estudante
import re

dados_Estudantes = []
class MenuOperacional:

    def __init__(self, opcao_navegacao):
        self.opcao_navegacao = opcao_navegacao
        
    def exibir_menu_operacional(self):
        tipos_usuarios = ['ESTUDANTES','DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']
        print(f'\n*** MENU DE OPERAÇÕES PARA {tipos_usuarios[self.opcao_navegacao - 1]}! ***\n ')
        print('1. Incluir \n2. Listar \n3. Atualizar \n4. Excluir \n5. Voltar para o menu principal')
    
    def obter_opcao_operacional(self):
        while True: 
            try:
                opcao_operacional = int(input('\nEscolha uma opção: '))
                if 1 <= opcao_operacional <= 5:
                    return opcao_operacional
                else:
                    print('\nOpção inválida, tente novamente! Escolha uma opção entre 1 e 5.')

            except TypeError:
                print('\nOpção inválida! Digite um NÚMERO entre 1 e 5.')
            except:
                print('\nOcorreu um erro, tente novamente!')
    
    def incluir(self):
        if self.opcao_navegacao == 1:
            print("\n**** INCLUSÃO ****")
            while True:
                cpf = input('\nPara voltar ao menu principal, digite 0.\n\nInsira o CPF do estudante: ')
                if cpf == '0':
                    return
                elif not self.validar_cpf(cpf):
                    print('\nCPF inválido, tente novamente!')    
                elif self.cpf_ja_existe(cpf):
                    print('\nJá existe um estudante cadastrado com este CPF! Tente novamente!')    
                else:
                    break
            
            while True:
                nome = input('\nPara voltar ao menu principal, digite 0.\n\nInsira o nome do estudante: ')
                if nome == '0':
                    return
                elif not re.match("^[A-Za-z ]+$", nome):
                    print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                else:  
                    break
                
            matricula = len(dados_Estudantes) + 1      
            novo_estudante = Estudante(cpf, nome, matricula)            
            dados_Estudantes.append(novo_estudante)
            
            print(f'\nO estudante {nome.capitalize()} de matrícula {matricula} foi cadastrado com sucesso!')
            
    def listar(self):
        if self.opcao_navegacao == 1:
            if len(dados_Estudantes) == 0:
                print('\nNão há nenhum estudante cadastrado.')
            else:
                print('\n**** LISTA DE ALUNOS ****')
                for estudante in dados_Estudantes:
                        print(f'\nMatricula: {estudante.matricula}\nAluno: {estudante.nome.upper()}\nCPF: {estudante.cpf}')
                        
    def atualizar(self):
        if len(dados_Estudantes) == 0:
            print('\nNenhum estudante matriculado até o momento!')
            return
        try:
            matricula = int(input('\nPara voltar ao menu principal, digite 0.\nQual aluno você deseja atualizar?\nDigite o nº da matricula: '))
            if matricula == 0:
                return
            else:
                for estudante in dados_Estudantes:
                    if estudante.matricula == matricula:
                        while True:
                            buffer = estudante.cpf
                            estudante.cpf = 0
                            cpf = input('\nPara voltar ao menu principal, digite 0.\n\nInsira o CPF do estudante: ')
                            if cpf == '0':
                                return
                            elif not self.validar_cpf(cpf):
                                print('\nCPF inválido, tente novamente!')
                                estudante.cpf = buffer
                            elif self.cpf_ja_existe(cpf):
                                print('\nJá existe um estudante cadastrado com este CPF! Tente novamente!')
                                estudante.cpf = buffer
                            else:
                                estudante.cpf = cpf
                                break
                        
                        while True:
                            nome = input('\nPara voltar ao menu principal, digite 0.\n\nInsira o nome do estudante: ')
                            if nome == '0':
                                return
                            elif not re.match("^[A-Za-z ]+$", nome):
                                print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                            else:  
                                estudante.nome = nome
                                break
                print('\nDados do aluno atualizados com sucesso!')
                return
        except:
            print('\nOcorreu um erro ao atualizar o estudante!')
        
        
    def excluir(self):
        if len(dados_Estudantes) == 0:
            print('\nNenhum estudante matriculado até o momento!')
            return
        try:
            matricula = int(input('\nPara voltar ao menu principal, digite 0.\nQual estudante você deseja excluir do sistema?\nDigite o nº da matricula: '))
            if matricula == 0:
                return
            else:
                for estudante in dados_Estudantes:
                    if estudante.matricula == matricula:
                        print(f'\nVocê tem certeza que deseja excluir o aluno {estudante.nome} de matrícula: {estudante.matricula}?')
                        while True:
                            escolha = input('\n[Y/N]? ')
                            if escolha.upper() == 'Y':
                                dados_Estudantes.remove(estudante)
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
            print('\nOcorreu um erro ao excluir o aluno, tente novamente!')            
                                
    def validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            return False
        if cpf == cpf[0] * 11:
            return False
        
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
            
        resto = soma % 11
        
        digito1 = 0 if resto < 2 else 11 - resto
        
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto        
        
        return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
    
    def cpf_ja_existe(self, cpf):
        for estudante in dados_Estudantes:
            if cpf == estudante.cpf:
                return True
        return False