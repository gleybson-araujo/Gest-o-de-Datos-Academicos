from Classes import Estudante

ESTUDANTE = 1
DISCIPLINA = 2
PROFESSOR = 3
TURMA = 4
MATRICULA = 5

class MenuOperacional:

    def __init__(self):
        self.dados_estudantes = []

    @staticmethod
    def exibir_menu_operacional(opcao_navegacao):
        tipos_usuarios = ['ESTUDANTES','DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']
        print(f'\n*** MENU DE OPERAÇÕES PARA {tipos_usuarios[opcao_navegacao - 1]}! ***\n ')
        print('1. Incluir \n2. Listar \n3. Atualizar \n4. Excluir \n5. Voltar para o menu principal')

    @staticmethod
    def obter_opcao_operacional():
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

    def incluir(self, opcao_navegacao):
        if opcao_navegacao == ESTUDANTE:
            novo_estudante = Estudante.incluir(self)
            if novo_estudante:
                self.dados_estudantes.append(novo_estudante)
                print(f'\nO estudante {novo_estudante.nome.capitalize()} de matrícula {novo_estudante.matricula} foi cadastrado com sucesso!')
        
    def listar(self, opcao_navegacao):
        if opcao_navegacao == ESTUDANTE:
            Estudante.listar(self)
                    
    def atualizar(self, opcao_navegacao):
        if opcao_navegacao == ESTUDANTE:
            Estudante.atualizar(self)

    def excluir(self, opcao_navegacao):
        if opcao_navegacao == ESTUDANTE:
            Estudante.excluir(self)            
                                
    
        return False