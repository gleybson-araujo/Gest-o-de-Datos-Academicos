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

            except ValueError:
                print('\nOpção inválida! Digite um NÚMERO entre 1 e 5.')
            except:
                print('\nOcorreu um erro, tente novamente!')
    
    def incluir(self):
        if self.opcao_navegacao == 1:
            while True:
                print("\n**** INCLUSÃO ****")
                nome = input('\nPara voltar ao menu principal, digite 0.\nInsira o nome do estudante:')
                if nome == '0':
                    break
                elif not re.match("^[A-Za-z ]+$", nome):
                    print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                else:  
                    dados_Estudantes.append(Estudante(nome.upper()))
                    print('\nEstudante incluido com sucesso!')
                    break
            
    def listar(self):
        if self.opcao_navegacao == 1:
            if len(dados_Estudantes) == 0:
                print('\nNão há nenhum estudante cadastrado.')
            else:
                print('\n**** LISTA DE ALUNOS ****')
                count = 1
                for estudante in dados_Estudantes:
                        print(f'{count}. {estudante.nome}')
                        count += 1
                        
    def atualizar(self):
        print('\nEM DESENVOLVIMENTO!\n')
        
    def excluir(self):
        print('\nEM DESENVOLVIMENTO!\n')