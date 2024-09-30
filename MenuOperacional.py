from Classes import Estudante, Professor, Disciplina, Turma, Matricula

import json

ESTUDANTE = 1
DISCIPLINA = 2
PROFESSOR = 3
TURMA = 4
MATRICULA = 5

class MenuOperacional:
    """
    Classe responsável por exibir o menu de operações e realizar as operações CRUD (Criar, Ler, Atualizar, Deletar)
    para cada módulo do sistema (estudantes, professores, disciplinas, turmas e matrículas).
    """
    def __init__(self):
        """
        Inicializa o objeto MenuOperacional, carregando os dados de cada módulo a partir dos respectivos arquivos JSON.
        """
        self.dados_estudantes = self.carregar_dados('dados_estudantes.json')
        self.dados_professores = self.carregar_dados('dados_professores.json')
        self.dados_disciplinas = self.carregar_dados('dados_disciplinas.json')
        self.dados_turmas = self.carregar_dados('dados_turmas.json')
        self.dados_matriculas = self.carregar_dados('dados_matriculas.json')

    @staticmethod
    def exibir_menu_operacional(opcao_navegacao):
        """
        Exibe o menu de operações para o módulo selecionado.

        Args:
            opcao_navegacao: Um número inteiro representando o módulo selecionado no menu principal.
        """
        tipos_usuarios = ['ESTUDANTES', 'DISCIPLINAS', 'PROFESSORES', 'TURMAS', 'MATRICULAS']
        print(f'\n*** MENU DE OPERAÇÕES PARA {tipos_usuarios[opcao_navegacao - 1]}! ***\n ')
        print('1. Incluir \n2. Listar \n3. Atualizar \n4. Excluir \n5. Voltar para o menu principal')

    @staticmethod
    def obter_opcao_operacional():
        """
        Obtém a opção selecionada pelo usuário no menu de operações.

        Realiza validações para garantir que a entrada seja um número inteiro válido entre 1 e 5.
        Em caso de erro, exibe mensagens de erro apropriadas e solicita nova entrada.

        Returns:
            A opção operacional selecionada pelo usuário (um número inteiro entre 1 e 5).
        """
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
        """
        Realiza a operação de inclusão para o módulo selecionado.

        Args:
            opcao_navegacao: Um número inteiro representando o módulo selecionado no menu principal.
        """
        if opcao_navegacao == ESTUDANTE:
            novo_estudante = Estudante.incluir(self)
            if novo_estudante:
                self.dados_estudantes.append(novo_estudante)
                print(f'\nO estudante {novo_estudante.nome.capitalize()} de matrícula {novo_estudante.matricula} foi cadastrado com sucesso!')
                self.salvar_dados('dados_estudantes.json', self.dados_estudantes)
        elif opcao_navegacao == PROFESSOR:
            novo_professor = Professor.incluir()
            if novo_professor:
                self.dados_professores.append(novo_professor)
                print(f'O professor {novo_professor.nome.capitalize()} de código {novo_professor.codigo} foi cadastrado com sucesso!')
                self.salvar_dados('dados_professores.json', self.dados_professores)
        elif opcao_navegacao == DISCIPLINA:
            nova_disciplina = Disciplina.incluir()
            if nova_disciplina:
                self.dados_disciplinas.append(nova_disciplina)
                print(f'A disciplina {nova_disciplina.nome.capitalize()} de código {nova_disciplina.codigo} foi cadastrada com sucesso!')
                self.salvar_dados('dados_disciplinas.json', self.dados_disciplinas)
        elif opcao_navegacao == TURMA:
            nova_turma = Turma.incluir(self.dados_turmas ,self.dados_professores, self.dados_disciplinas)
            if nova_turma:
                self.dados_turmas.append(nova_turma)
                print(f'A turma de código {nova_turma.codigo} foi cadastrada com sucesso!')
                self.salvar_dados('dados_turmas.json', self.dados_turmas)
        elif opcao_navegacao == MATRICULA:
            nova_matricula = Matricula.incluir(self.dados_turmas, self.dados_estudantes, self.dados_matriculas)
            if nova_matricula:
                self.dados_matriculas.append(nova_matricula)
                print(f'A matrícula de código {nova_matricula.codigo} foi cadastrada com sucesso!')
                self.salvar_dados('dados_matriculas.json', self.dados_matriculas)

    def listar(self, opcao_navegacao):
        """
        Realiza a operação de listagem para o módulo selecionado.

        Args:
            opcao_navegacao: Um número inteiro representando o módulo selecionado no menu principal.
        """
        if opcao_navegacao == ESTUDANTE:
            Estudante.listar(self)
        elif opcao_navegacao == PROFESSOR:
            Professor.listar(self.dados_professores)
        elif opcao_navegacao == DISCIPLINA:
            Disciplina.listar(self.dados_disciplinas)
        elif opcao_navegacao == TURMA:
            Turma.listar(self.dados_turmas, self.dados_professores, self.dados_disciplinas)
        elif opcao_navegacao == MATRICULA:
            Matricula.listar(self.dados_matriculas, self.dados_turmas, self.dados_estudantes)

    def atualizar(self, opcao_navegacao):
        """
        Realiza a operação de atualização para o módulo selecionado.

        Args:
            opcao_navegacao: Um número inteiro representando o módulo selecionado no menu principal.
        """
        if opcao_navegacao == ESTUDANTE:
            Estudante.atualizar(self)
            self.salvar_dados('dados_estudantes.json', self.dados_estudantes)
        elif opcao_navegacao == PROFESSOR:
            Professor.atualizar(self.dados_professores)
            self.salvar_dados('dados_professores.json', self.dados_professores)
        elif opcao_navegacao == DISCIPLINA:
            Disciplina.atualizar(self.dados_disciplinas)
            self.salvar_dados('dados_disciplinas.json', self.dados_disciplinas)
        elif opcao_navegacao == TURMA:
            Turma.atualizar(self.dados_turmas, self.dados_professores, self.dados_disciplinas)
            self.salvar_dados('dados_turmas.json', self.dados_turmas)
        elif opcao_navegacao == MATRICULA:
            Matricula.atualizar(self.dados_matriculas, self.dados_turmas, self.dados_estudantes)
            self.salvar_dados('dados_matriculas.json', self.dados_matriculas)

    def excluir(self, opcao_navegacao):
        """
        Realiza a operação de exclusão para o módulo selecionado.

        Args:
            opcao_navegacao: Um número inteiro representando o módulo selecionado no menu principal.
        """
        if opcao_navegacao == ESTUDANTE:
            Estudante.excluir(self)
            self.salvar_dados('dados_estudantes.json', self.dados_estudantes)
        elif opcao_navegacao == PROFESSOR:
            Professor.excluir(self.dados_professores)
            self.salvar_dados('dados_professores.json', self.dados_professores)
        elif opcao_navegacao == DISCIPLINA:
            Disciplina.excluir(self.dados_disciplinas)
            self.salvar_dados('dados_disciplinas.json', self.dados_disciplinas)
        elif opcao_navegacao == TURMA:
            Turma.excluir(self.dados_turmas)
            self.salvar_dados('dados_turmas.json', self.dados_turmas)
        elif opcao_navegacao == MATRICULA:
            Matricula.excluir(self.dados_matriculas)
            self.salvar_dados('dados_matriculas.json', self.dados_matriculas)
                   
    @staticmethod                           
    def salvar_dados(nome_arquivo, dados):
        """
        Salva os dados em um arquivo JSON.

        Args:
            nome_arquivo: O nome do arquivo JSON onde os dados serão salvos.
            dados: A lista de objetos a serem salvos.
        """
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, default=lambda o: o.__dict__, indent=4)
    @staticmethod
    def carregar_dados(nome_arquivo):
        """
        Carrega os dados de um arquivo JSON.

        Args:
            nome_arquivo: O nome do arquivo JSON de onde os dados serão carregados.

        Returns:
            Uma lista de objetos criados a partir dos dados JSON, ou uma lista vazia se o arquivo não existir.
        """
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados_json = json.load(arquivo)
                if nome_arquivo == 'dados_estudantes.json':
                    return [Estudante(item['cpf'], item['nome']) for item in dados_json]
                elif nome_arquivo == 'dados_professores.json':
                    return [Professor(item['nome'], item['cpf']) for item in dados_json]
                elif nome_arquivo == 'dados_disciplinas.json':
                    return [Disciplina(item['nome']) for item in dados_json]
                elif nome_arquivo == 'dados_turmas.json':
                    return [Turma(item['codigo_professor'], item['codigo_disciplina']) for item in dados_json]
                elif nome_arquivo == 'dados_matriculas.json':
                    return [Matricula(item['codigo_turma'], item['codigo_estudante']) for item in dados_json]
        except FileNotFoundError:
            return []