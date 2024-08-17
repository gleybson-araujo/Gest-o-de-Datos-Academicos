class MenuOperacional:

    def __init__(self, opcao_navegacao):
        self.opcao_navegacao = opcao_navegacao

    def exibir_menu_operacional(self):
        tipos_usuarios = ['ESTUDANTES','DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']
        print(f'\n*** MENU DE OPERAÇÕES PARA {tipos_usuarios[self.opcao_navegacao - 1]}! ***\n ')
        print('1. Incluir \n2. Listar \n3. Atualizar \n4. Excluir \n5. Voltar para o menu principal')
    
    def obter_opcao_operacional(self):
        while True:
            opcao_operacional = int(input('\nEscolha uma opção: '))
            try:
                if 1 <= opcao_operacional <= 5:
                    return opcao_operacional
                else:
                    print('\nOpção inválida, tente novamente! Escolha uma opção entre 1 e 5.')

            except ValueError:
                print('\nOpção inválida! Digite um NÚMERO entre 1 e 5.')