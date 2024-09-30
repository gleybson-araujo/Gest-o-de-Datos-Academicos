class MenuPrincipal:
    """
    Classe responsável por exibir o menu principal do sistema e obter a opção de navegação escolhida pelo usuário.
    """
    @staticmethod
    def exibir_menu_principal(): 
        """
        Exibe o menu principal do sistema, com as opções disponíveis para o usuário.
        """
        print('*********************************')
        print('**     BEM-VINDO AO PORTAL     **')
        print('*********************************\n')

        print('1. Estudantes \n2. Disciplinas\n3. Professores\n4. Turmas \n5. Matrículas \n6. Sair')
    
    @staticmethod
    def obter_opcao_navegacao(): 
        """
        Obtém a opção de navegação escolhida pelo usuário no menu principal.

        Realiza validações para garantir que a entrada seja um número inteiro válido entre 1 e 6.
        Em caso de erro, exibe mensagens de erro apropriadas e solicita nova entrada.

        Returns:
            A opção de navegação selecionada pelo usuário (um número inteiro entre 1 e 6).
        """
        while True:
            try:
                opcao_navegacao = int(input('\nQual seu destino hoje? '))
                if 1 <= opcao_navegacao <= 6:
                    return opcao_navegacao
                else:
                    print('\nOpção inválida, tente novamente! Escolha uma opção entre 1 e 6.')  
            except ValueError:
                print('\nOpção inválida! Digite um NÚMERO entre 1 e 6.')

            