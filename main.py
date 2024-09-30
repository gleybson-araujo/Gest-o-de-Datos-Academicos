'''
Sistema de Gestão Acadêmica - CRUD Básico

Este projeto implementa um sistema de gerenciamento de dados acadêmicos, 
permitindo realizar operações CRUD (Criar, Ler, Atualizar, Deletar) para as 
seguintes entidades:

* Estudantes: Cadastro de estudantes com CPF e nome.
* Professores: Cadastro de professores com código, nome e CPF.
* Disciplinas: Cadastro de disciplinas com código e nome.
* Turmas: Cadastro de turmas, associando um professor e uma disciplina.
* Matrículas: Cadastro de matrículas, associando um estudante a uma turma.

O sistema utiliza estruturas de dados em memória (listas) para armazenar as 
informações e arquivos JSON para garantir a persistência dos dados.

Funcionalidades:

* Incluir: Permite adicionar novos registros de estudantes, professores, disciplinas, turmas e matrículas.
* Listar: Exibe todos os registros cadastrados para cada entidade.
* Atualizar: Permite modificar os dados de um registro existente.
* Excluir: Remove um registro do sistema.

O projeto inclui validações de dados para garantir a integridade das informações 
e tratamento de exceções para lidar com possíveis erros durante a execução.
'''

from MenuOperacional import MenuOperacional
from MenuPrincipal import MenuPrincipal

menu_operacoes = MenuOperacional()

while True: 
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
                break
            
            else:
                match opcao_operacional:
                    case 1: menu_operacoes.incluir(opcao_navegacao)
                    case 2: menu_operacoes.listar(opcao_navegacao)
                    case 3: menu_operacoes.atualizar(opcao_navegacao)
                    case 4: menu_operacoes.excluir(opcao_navegacao)