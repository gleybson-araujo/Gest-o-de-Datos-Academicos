class MenuPrincipal:

    @staticmethod
    def exibir_menu_principal(): #exibe o primeiro menu de opcoes
        print('*********************************')
        print('**     BEM-VINDO AO PORTAL     **')
        print('*********************************\n')

        print('1. Estudantes \n2. Disciplinas\n3. Professores\n4. Turmas \n5. Matrículas \n6. Sair')
    
    @staticmethod
    def obter_opcao_navegacao(): #metodo p/ ler o input e tratar possiveis erros
        while True:
            try:
                opcao_navegacao = int(input('\nQual seu destino hoje? '))
                if opcao_navegacao == 1 or opcao_navegacao == 6:
                    return opcao_navegacao
                elif 1 < opcao_navegacao < 6:
                    print('\nEM DESENVOLVIMENTO!')
                else:
                    print('\nOpção inválida, tente novamente! Escolha uma opção entre 1 e 6.')  
            except ValueError:
                print('\nOpção inválida! Digite um NÚMERO entre 1 e 6.')

            