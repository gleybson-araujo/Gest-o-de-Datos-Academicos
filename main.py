'''
Projeto de Crud básico para a disciplina de raciocínio computacional.
O objetivo é fazer um sistema de gestão de dados acadêmicos, gerindo: estudantes,
disciplinas, professores, turmas e matrículas.
'''
from MenuOperacional import MenuOperacional
from MenuPrincipal import MenuPrincipal


#declarei essas listas com as categorias para cada menu com o intuito de deixar o codigo
#mais dinamico e enxuto
tipos_menu = ['ESTUDANTES','DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']
tipos_operacao = ['INCLUIR', 'LISTAR', 'ATUALIZAR', 'EXCLUIR']
menu_operacoes = MenuOperacional()
while True: #loop para navegacao entre os menus
    MenuPrincipal.exibir_menu_principal()
    opcao_navegacao = MenuPrincipal.obter_opcao_navegacao()
    
    if opcao_navegacao == 6:
        print('\nSaindo do sistema...')
        break
    else:
        while True:
            menu_operacoes.exibir_menu_operacional(opcao_navegacao)
            opcao_operacional = menu_operacoes.obter_opcao_operacional()

            if opcao_operacional == 5:
                print('\nVoltando para o menu principal...')
                break #isso faz voltar pra menu principal
            
            else:
                match opcao_operacional:
                    case 1: menu_operacoes.incluir(opcao_navegacao)
                    case 2: menu_operacoes.listar(opcao_navegacao)
                    case 3: menu_operacoes.atualizar(opcao_navegacao)
                    case 4: menu_operacoes.excluir(opcao_navegacao)
            # elif 1 < opcao_navegacao < 5:
            #     print('\nEM DESENVOLVIMENTO!\n')
            #     break
            # else:
            #     print (f'\nVocê escolheu o menu {tipos_menu[opcao_navegacao - 1]}, e a operação {tipos_operacao[opcao_operacional - 1]}.')
            #     #print('\nSaindo do sistema...')
            #     #break