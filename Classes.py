import re
from Validacoes import Validacoes

class Estudante():
    """
    Representa um estudante no sistema de gestão acadêmica.

    Attributes:
        proxima_matricula (int): Variável de classe para controlar a próxima matrícula disponível.
        cpf (str): CPF do estudante.
        nome (str): Nome do estudante.
        matricula (int): Matrícula do estudante, gerada automaticamente.
    """

    proxima_matricula = 1

    def __init__(self, cpf, nome):
        """
        Inicializa um novo objeto Estudante.

        Args:
            cpf (str): CPF do estudante.
            nome (str): Nome do estudante.
        """
        self.cpf = cpf
        self.nome = nome
        self.matricula = Estudante.proxima_matricula
        Estudante.proxima_matricula += 1

    @staticmethod
    def incluir(menu_operacoes):
        """
        Inclui um novo estudante no sistema.

        Solicita ao usuário o CPF e o nome do estudante, e cria um novo objeto Estudante.
        Realiza validações para garantir que:
        - O CPF seja válido.
        - Não exista outro estudante com o mesmo CPF.
        - O nome seja válido (apenas letras e espaços).
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            menu_operacoes (MenuOperacional): Objeto MenuOperacional para acesso aos dados dos estudantes.

        Returns:
            Um novo objeto Estudante se a inclusão for bem-sucedida, ou None se o usuário cancelar.
        """

        while True:
            cpf = input('\nPara voltar ao menu, digite 0.\n\nInsira o CPF do estudante: ')
            if cpf == '0':
                print('\nVoltando para o menu de operações...')
                return None
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
                return None 
            elif not re.match("^[A-Za-z ]+$", nome):
                print('\nNome inválido, o nome só pode conter letras sem acentuação.')
            else:
                break

        return Estudante(cpf, nome)

    @staticmethod
    def listar(menu_operacoes):
        """
        Lista todos os estudantes cadastrados no sistema.

        Exibe uma mensagem informativa se não houver estudantes cadastrados.
        Caso contrário, imprime uma lista formatada com a matrícula, o nome e o CPF de cada estudante.

        Args:
            menu_operacoes (MenuOperacional): Objeto MenuOperacional para acesso aos dados dos estudantes.
        """

        if not menu_operacoes.dados_estudantes:
            print('\nNenhum estudante matriculado até o momento!')
        else:
            print('\n**** LISTA DE ALUNOS ****')
            for estudante in menu_operacoes.dados_estudantes:
                print(f'\nMatricula: {estudante.matricula}\nAluno: {estudante.nome.upper()}\nCPF: {estudante.cpf}')

    @staticmethod
    def atualizar(menu_operacoes):
        """
        Atualiza os dados de um estudante existente.

        Solicita ao usuário a matrícula do estudante a ser atualizado e os novos dados (CPF e nome).
        Realiza validações para garantir que:
        - A matrícula seja válida (existente na lista).
        - O novo CPF seja válido e não esteja sendo usado por outro estudante.
        - O novo nome seja válido (apenas letras e espaços).
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            menu_operacoes (MenuOperacional): Objeto MenuOperacional para acesso aos dados dos estudantes.
        """

        if not menu_operacoes.dados_estudantes:
            print('\nNenhum estudante matriculado até o momento!')
            return

        try:
            matricula = int(input('\nPara voltar ao menu, digite 0.\nQual aluno você deseja atualizar?\nDigite o nº da matricula: '))
            if matricula == 0:
                print('\nVoltando para o menu de operações...')
                return

            for estudante in menu_operacoes.dados_estudantes:
                if estudante.matricula == matricula:
                    while True:
                        buffer = estudante.cpf
                        estudante.cpf = 0  
                        novo_cpf = input('\nPara voltar ao menu, digite 0.\n\nInsira o CPF do estudante: ')
                        if novo_cpf == '0':
                            estudante.cpf = buffer
                            print('\nVoltando para o menu de operações...')
                            return
                        elif not Validacoes.validar_cpf(novo_cpf):
                            print('\nCPF inválido, tente novamente!')
                            estudante.cpf = buffer
                        elif Validacoes.cpf_ja_existe(novo_cpf, menu_operacoes):
                            estudante.cpf = buffer
                            print('\nJá existe um estudante cadastrado com este CPF! Tente novamente!')
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

            print('\nNúmero de matrícula informado não existe no banco de dados!')

        except ValueError:
            print('\nOcorreu um erro ao atualizar o estudante! Certifique-se de inserir um número válido para a matrícula.')

    @staticmethod
    def excluir(menu_operacoes):
        """
        Exclui um estudante do sistema.

        Solicita ao usuário a matrícula do estudante a ser excluído.
        Realiza validações para garantir que a matrícula seja válida (existente na lista)
        e pede confirmação antes de excluir.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            menu_operacoes (MenuOperacional): Objeto MenuOperacional para acesso aos dados dos estudantes.
        """

        if not menu_operacoes.dados_estudantes:
            print('\nNenhum estudante matriculado até o momento!')
            return

        try:
            matricula = int(input('\nPara voltar ao menu, digite 0.\nQual estudante você deseja excluir do sistema?\nDigite o nº da matricula: '))
            if matricula == 0:
                print('\nVoltando para o menu de operações...')
                return

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
    """
    Representa um professor no sistema de gestão acadêmica.

    Attributes:
        proximo_codigo (int): Variável de classe para controlar o próximo código disponível.
        codigo (int): Código único do professor, gerado automaticamente.
        nome (str): Nome do professor.
        cpf (str): CPF do professor.
    """

    proximo_codigo = 1

    def __init__(self, nome, cpf):
        """
        Inicializa um novo objeto Professor.

        Args:
            nome (str): Nome do professor.
            cpf (str): CPF do professor.
        """
        self.codigo = Professor.proximo_codigo
        Professor.proximo_codigo += 1
        self.nome = nome
        self.cpf = cpf

    @staticmethod
    def incluir():
        """
        Inclui um novo professor no sistema.

        Solicita ao usuário o nome e o CPF do professor, e cria um novo objeto Professor.
        Realiza validações para garantir que:
        - O nome seja válido (apenas letras e espaços).
        - O CPF seja válido.
        Permite que o usuário volte ao menu digitando '0'.

        Returns:
            Um novo objeto Professor se a inclusão for bem-sucedida, ou None se o usuário cancelar.
        """

        while True:
            nome = input("\nPara voltar ao menu, digite 0.\n\nInsira o nome do professor: ")
            if nome == '0':
                print("\nVoltando para o menu de operações...")
                return None 
            elif not re.match("^[A-Za-z ]+$", nome):
                print("\nNome inválido, o nome só pode conter letras sem acentuação.")
            else:
                break

        while True:
            cpf = input("\nPara voltar ao menu, digite 0.\n\nInsira o CPF do professor: ")
            if cpf == '0':
                print("\nVoltando para o menu de operações...")
                return None 
            elif not Validacoes.validar_cpf(cpf):
                print("\nCPF inválido, tente novamente!")
            else:
                break

        return Professor(nome, cpf)

    @staticmethod
    def listar(dados_professores):
        """
        Lista todos os professores cadastrados no sistema.

        Exibe uma mensagem informativa se não houver professores cadastrados.
        Caso contrário, imprime uma lista formatada com o código, o nome e o CPF de cada professor.

        Args:
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
        """

        if not dados_professores:
            print("\nNenhum professor cadastrado até o momento!")
        else:
            print("\n**** LISTA DE PROFESSORES ****")
            for professor in dados_professores:
                print(f"\nCódigo: {professor.codigo}\nNome: {professor.nome.upper()}\nCPF: {professor.cpf}")

    @staticmethod
    def atualizar(dados_professores):
        """
        Atualiza os dados de um professor existente.

        Solicita ao usuário o código do professor a ser atualizado e os novos dados (nome e CPF).
        Realiza validações para garantir que:
        - O código seja válido (existente na lista).
        - O novo nome seja válido (apenas letras e espaços).
        - O novo CPF seja válido e não esteja sendo usado por outro professor.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
        """

        if not dados_professores:
            print("\nNenhum professor cadastrado até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual professor você deseja atualizar?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for professor in dados_professores:
                if professor.codigo == codigo:
                    while True:
                        novo_nome = input("\nPara voltar ao menu, digite 0.\n\nInsira o novo nome do professor: ")
                        if novo_nome == '0':
                            print("\nVoltando para o menu de operações...")
                            return
                        elif not re.match("^[A-Za-z ]+$", novo_nome):
                            print("\nNome inválido, o nome só pode conter letras sem acentuação.")
                        else:
                            professor.nome = novo_nome
                            break

                    while True:
                        buffer = professor.cpf  
                        professor.cpf = 0  
                        novo_cpf = input("\nPara voltar ao menu, digite 0.\n\nInsira o novo CPF do professor: ")
                        if novo_cpf == '0':
                            professor.cpf = buffer 
                            print("\nVoltando para o menu de operações...")
                            return
                        elif not Validacoes.validar_cpf(novo_cpf):
                            print("\nCPF inválido, tente novamente!")
                            professor.cpf = buffer  
                       
                        elif any(p.cpf == novo_cpf for p in dados_professores if p.codigo != codigo):
                            print("\nCPF já cadastrado para outro professor. Tente novamente!")
                            professor.cpf = buffer  
                        else:
                            professor.cpf = novo_cpf
                            break

                    print("\nDados do professor atualizados com sucesso!")
                    return

            print("\nCódigo de professor informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao atualizar o professor! Certifique-se de inserir um número válido para o código.")

    @staticmethod
    def excluir(dados_professores):
        """
        Exclui um professor do sistema.

        Solicita ao usuário o código do professor a ser excluído.
        Realiza validações para garantir que o código seja válido (existente na lista)
        e pede confirmação antes de excluir.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
        """

        if not dados_professores:
            print("\nNenhum professor cadastrado até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual professor você deseja excluir?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for professor in dados_professores:
                if professor.codigo == codigo:
                    print(f"\nVocê tem certeza que deseja excluir o professor {professor.nome.capitalize()} de código: {professor.codigo}?")
                    while True:
                        escolha = input("\n[Y/N]? ")
                        if escolha.upper() == 'Y':
                            dados_professores.remove(professor)
                            print("\nProfessor excluído com sucesso!")
                            return
                        elif escolha.upper() == 'N':
                            print("\nVoltando para o menu de operações...")
                            return
                        else:
                            print("\nOpção inválida, tente novamente!")

            print("\nCódigo de professor informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao excluir o professor. Certifique-se de inserir um número válido para o código.")

class Disciplina:
    """
    Representa uma disciplina no sistema de gestão acadêmica.

    Attributes:
        proximo_codigo (int): Variável de classe para controlar o próximo código disponível.
        codigo (int): Código único da disciplina, gerado automaticamente.
        nome (str): Nome da disciplina.
    """

    proximo_codigo = 1

    def __init__(self, nome):
        """
        Inicializa um novo objeto Disciplina.

        Args:
            nome (str): Nome da disciplina.
        """
        self.codigo = Disciplina.proximo_codigo
        Disciplina.proximo_codigo += 1
        self.nome = nome

    @staticmethod
    def incluir():
        """
        Inclui uma nova disciplina no sistema.

        Solicita ao usuário o nome da disciplina e cria um novo objeto Disciplina.
        Realiza validações para garantir que o nome seja válido (apenas letras e espaços)
        e permite que o usuário volte ao menu digitando '0'.

        Returns:
            Um novo objeto Disciplina se a inclusão for bem-sucedida, ou None se o usuário cancelar.
        """

        while True:
            nome = input("\nPara voltar ao menu, digite 0.\n\nInsira o nome da disciplina: ")
            if nome == '0':
                print("\nVoltando para o menu de operações...")
                return None  
            elif not re.match("^[A-Za-z ]+$", nome):
                print("\nNome inválido, o nome só pode conter letras sem acentuação.")
            else:
                break  

        return Disciplina(nome)  

    @staticmethod
    def listar(dados_disciplinas):
        """
        Lista todas as disciplinas cadastradas no sistema.

        Exibe uma mensagem informativa se não houver disciplinas cadastradas.
        Caso contrário, imprime uma lista formatada com o código e o nome de cada disciplina.

        Args:
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.
        """

        if not dados_disciplinas:
            print("\nNenhuma disciplina cadastrada até o momento!")
        else:
            print("\n**** LISTA DE DISCIPLINAS ****")
            for disciplina in dados_disciplinas:
                print(f"\nCódigo: {disciplina.codigo}\nNome: {disciplina.nome.upper()}")

    @staticmethod
    def atualizar(dados_disciplinas):
        """
        Atualiza o nome de uma disciplina existente.

        Solicita ao usuário o código da disciplina a ser atualizada e o novo nome.
        Realiza validações para garantir que o código seja válido (existente na lista)
        e que o novo nome seja válido (apenas letras e espaços).
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.
        """

        if not dados_disciplinas:
            print("\nNenhuma disciplina cadastrada até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual disciplina você deseja atualizar?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for disciplina in dados_disciplinas:
                if disciplina.codigo == codigo:
                    while True:
                        novo_nome = input("\nPara voltar ao menu, digite 0.\n\nInsira o novo nome da disciplina: ")
                        if novo_nome == '0':
                            print("\nVoltando para o menu de operações...")
                            return
                        elif not re.match("^[A-Za-z ]+$", novo_nome):
                            print("\nNome inválido, o nome só pode conter letras sem acentuação.")
                        else:
                            disciplina.nome = novo_nome
                            break

                    print("\nDados da disciplina atualizados com sucesso!")
                    return

            print("\nCódigo de disciplina informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao atualizar a disciplina! Certifique-se de inserir um número válido para o código.")

    @staticmethod
    def excluir(dados_disciplinas):
        """
        Exclui uma disciplina do sistema.

        Solicita ao usuário o código da disciplina a ser excluída.
        Realiza validações para garantir que o código seja válido (existente na lista)
        e pede confirmação antes de excluir.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.
        """

        if not dados_disciplinas:
            print("\nNenhuma disciplina cadastrada até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual disciplina você deseja excluir?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for disciplina in dados_disciplinas:
                if disciplina.codigo == codigo:
                    print(f"\nVocê tem certeza que deseja excluir a disciplina {disciplina.nome.capitalize()} de código: {disciplina.codigo}?")
                    while True:
                        escolha = input("\n[Y/N]? ")
                        if escolha.upper() == 'Y':
                            dados_disciplinas.remove(disciplina)
                            print("\nDisciplina excluída com sucesso!")
                            return
                        elif escolha.upper() == 'N':
                            print("\nVoltando para o menu de operações...")
                            return
                        else:
                            print("\nOpção inválida, tente novamente!")

            print("\nCódigo de disciplina informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao excluir a disciplina. Certifique-se de inserir um número válido para o código.")

class Turma:
    """
    Representa uma turma no sistema de gestão acadêmica.

    Attributes:
        proximo_codigo (int): Variável de classe para controlar o próximo código disponível.
        codigo (int): Código único da turma, gerado automaticamente.
        codigo_professor (int): Código do professor responsável pela turma.
        codigo_disciplina (int): Código da disciplina ministrada na turma.
    """

    proximo_codigo = 1

    def __init__(self, codigo_professor, codigo_disciplina):
        """
        Inicializa um novo objeto Turma.

        Args:
            codigo_professor (int): Código do professor responsável pela turma.
            codigo_disciplina (int): Código da disciplina ministrada na turma.
        """
        self.codigo = Turma.proximo_codigo
        Turma.proximo_codigo += 1
        self.codigo_professor = codigo_professor
        self.codigo_disciplina = codigo_disciplina

    @staticmethod
    def incluir(dados_turmas, dados_professores, dados_disciplinas):
        """
        Inclui uma nova turma no sistema.

        Solicita ao usuário os códigos do professor e da disciplina, e cria um novo objeto Turma.
        Realiza validações para garantir que:
        - Exista pelo menos um professor e uma disciplina cadastrados.
        - Os códigos de professor e disciplina sejam válidos (existam nas respectivas listas).
        - Não exista outra turma com o mesmo professor e disciplina.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.

        Returns:
            Um novo objeto Turma se a inclusão for bem-sucedida, ou None se o usuário cancelar.
        """

        if not dados_professores or not dados_disciplinas:
            print("\nÉ necessário cadastrar pelo menos um professor e uma disciplina antes de cadastrar uma turma!")
            return None

        while True:
            try:
                codigo_professor = int(input("\nPara voltar ao menu, digite 0.\n\nDigite o código do professor: "))
                if codigo_professor == 0:
                    print("\nVoltando para o menu de operações...")
                    return None

                professor_encontrado = False
                for professor in dados_professores:
                    if professor.codigo == codigo_professor:
                        professor_encontrado = True
                        break

                if not professor_encontrado:
                    print("\nCódigo de professor inválido. Tente novamente!")
                    continue

                codigo_disciplina = int(input("Digite o código da disciplina: "))
                if codigo_disciplina == 0:
                    print("\nVoltando para o menu de operações...")
                    return None

                disciplina_encontrada = False
                for disciplina in dados_disciplinas:
                    if disciplina.codigo == codigo_disciplina:
                        disciplina_encontrada = True
                        break

                if not disciplina_encontrada:
                    print("\nCódigo de disciplina inválido. Tente novamente!")
                    continue

                if any(t.codigo_professor == codigo_professor and t.codigo_disciplina == codigo_disciplina for t in dados_turmas):
                    print("\nEssa turma já existe (mesmo professor e disciplina). Tente novamente!")
                    continue

                return Turma(codigo_professor, codigo_disciplina)

            except ValueError:
                print("\nEntrada inválida. Digite um número inteiro para o código do professor e da disciplina.")

    @staticmethod
    def listar(dados_turmas, dados_professores, dados_disciplinas):
        """
        Lista todas as turmas cadastradas no sistema.

        Exibe uma mensagem informativa se não houver turmas cadastradas.
        Caso contrário, imprime uma lista formatada com o código da turma, o nome do professor e o nome da disciplina.

        Args:
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.
        """

        if not dados_turmas:
            print("\nNenhuma turma cadastrada até o momento!")
        else:
            print("\n**** LISTA DE TURMAS ****")
            for turma in dados_turmas:
                nome_professor = next((p.nome for p in dados_professores if p.codigo == turma.codigo_professor), "Professor não encontrado")
                nome_disciplina = next((d.nome for d in dados_disciplinas if d.codigo == turma.codigo_disciplina), "Disciplina não encontrada")
                print(f"\nCódigo da turma: {turma.codigo}")
                print(f"Professor: {nome_professor}")
                print(f"Disciplina: {nome_disciplina}")

    @staticmethod
    def atualizar(dados_turmas, dados_professores, dados_disciplinas):
        """
        Atualiza os dados de uma turma existente.

        Solicita ao usuário o código da turma a ser atualizada e os novos códigos do professor e da disciplina.
        Realiza validações para garantir que:
        - O código da turma seja válido (existente na lista).
        - Os novos códigos de professor e disciplina sejam válidos (existam nas respectivas listas).
        - A combinação professor-disciplina não gere uma turma duplicada (excluindo a turma atual).
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_professores (list): Lista contendo os objetos Professor cadastrados.
            dados_disciplinas (list): Lista contendo os objetos Disciplina cadastrados.
        """

        if not dados_turmas:
            print("\nNenhuma turma cadastrada até o momento!")
            return

        try:
            codigo_turma = int(input("\nPara voltar ao menu, digite 0.\n\nQual turma você deseja atualizar?\nDigite o código da turma: "))
            if codigo_turma == 0:
                print("\nVoltando para o menu de operações...")
                return

            for turma in dados_turmas:
                if turma.codigo == codigo_turma:
                    while True:
                        try:
                            novo_codigo_professor = int(input("\nPara voltar ao menu, digite 0.\n\nDigite o novo código do professor: "))
                            if novo_codigo_professor == 0:
                                print("\nVoltando para o menu de operações...")
                                return
                            elif novo_codigo_professor == turma.codigo_professor:
                                print("\nO código do professor é o mesmo. Insira um código diferente ou 0 para voltar.")
                                continue

                            professor_encontrado = any(p for p in dados_professores if p.codigo == novo_codigo_professor)
                            if not professor_encontrado:
                                print("\nCódigo de professor inválido. Tente novamente!")
                                continue

                            novo_codigo_disciplina = int(input("Digite o novo código da disciplina: "))
                            if novo_codigo_disciplina == 0:
                                print("\nVoltando para o menu de operações...")
                                return
                            elif novo_codigo_disciplina == turma.codigo_disciplina:
                                print("\nO código da disciplina é o mesmo! Insira um código diferente ou 0 para voltar.")
                                continue

                            disciplina_encontrada = any(d for d in dados_disciplinas if d.codigo == novo_codigo_disciplina)
                            if not disciplina_encontrada:
                                print("\nCódigo de disciplina inválido. Tente novamente!")
                                continue

                            turma_existente = any(t for t in dados_turmas if t.codigo_professor == novo_codigo_professor and t.codigo_disciplina == novo_codigo_disciplina and t.codigo != codigo_turma)
                            if turma_existente:
                                print("\nEssa turma já existe (mesmo professor e disciplina). Tente novamente!")
                                continue

                            turma.codigo_professor = novo_codigo_professor
                            turma.codigo_disciplina = novo_codigo_disciplina
                            print("\nDados da turma atualizados com sucesso!")
                            return
                        except ValueError:
                            print("\nEntrada inválida! Digite números inteiros para os códigos.")

            print("\nCódigo de turma informado não existe no banco de dados!")
        except ValueError:
            print("\nOcorreu um erro ao atualizar a turma! Certifique-se de inserir um número válido para o código da turma.")
            
    @staticmethod
    def excluir(dados_turmas):
        """
        Exclui uma turma do sistema.

        Solicita ao usuário o código da turma a ser excluída.
        Realiza validações para garantir que o código seja válido (existente na lista)
        e pede confirmação antes de excluir.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
        """

        if not dados_turmas:
            print("\nNenhuma turma cadastrada até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual turma você deseja excluir?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for turma in dados_turmas:
                if turma.codigo == codigo:
                    print(f"\nVocê tem certeza que deseja excluir a turma de código: {turma.codigo}?")
                    while True:
                        escolha = input("\n[Y/N]? ")
                        if escolha.upper() == 'Y':
                            dados_turmas.remove(turma)
                            print("\nTurma excluída com sucesso!")
                            return
                        elif escolha.upper() == 'N':
                            print("\nVoltando para o menu de operações...")
                            return
                        else:
                            print("\nOpção inválida, tente novamente!")

            print("\nCódigo de turma informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao excluir a turma. Certifique-se de inserir um número válido para o código.")
class Matricula:
    """
    Representa uma matrícula de um estudante em uma turma no sistema de gestão acadêmica.

    Attributes:
        proximo_codigo (int): Variável de classe para controlar o próximo código de matrícula disponível.
        codigo (int): Código único da matrícula, gerado automaticamente.
        codigo_turma (int): Código da turma na qual o estudante está matriculado.
        codigo_estudante (int): Matrícula do estudante.
    """

    proximo_codigo = 1

    def __init__(self, codigo_turma, codigo_estudante):
        """
        Inicializa um novo objeto Matricula.

        Args:
            codigo_turma (int): Código da turma na qual o estudante está matriculado.
            codigo_estudante (int): Matrícula do estudante.
        """
        self.codigo = Matricula.proximo_codigo
        Matricula.proximo_codigo += 1
        self.codigo_turma = codigo_turma
        self.codigo_estudante = codigo_estudante

    @staticmethod
    def incluir(dados_turmas, dados_estudantes, dados_matriculas):
        """
        Inclui uma nova matrícula no sistema.

        Solicita ao usuário os códigos da turma e do estudante, e cria um novo objeto Matricula.
        Realiza validações para garantir que:
        - Exista pelo menos uma turma e um estudante cadastrados.
        - Os códigos de turma e estudante sejam válidos (existam nas respectivas listas).
        - Não exista outra matrícula com o mesmo código de turma e estudante.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_estudantes (list): Lista contendo os objetos Estudante cadastrados.
            dados_matriculas (list): Lista contendo os objetos Matricula cadastrados

        Returns:
            Um novo objeto Matricula se a inclusão for bem-sucedida, ou None se o usuário cancelar.
        """

        if not dados_turmas or not dados_estudantes:
            print("\nÉ necessário cadastrar pelo menos uma turma e um estudante antes de cadastrar uma matrícula!")
            return None

        while True:
            try:
                codigo_turma = int(input("\nPara voltar ao menu, digite 0.\n\nDigite o código da turma: "))
                if codigo_turma == 0:
                    print("\nVoltando para o menu de operações...")
                    return None

                if not any(t.codigo == codigo_turma for t in dados_turmas):
                    print("\nCódigo de turma inválido. Tente novamente!")
                    continue

                codigo_estudante = int(input("Digite a matrícula do estudante: "))
                if codigo_estudante == 0:
                    print("\nVoltando para o menu de operações...")
                    return None

                if not any(e.matricula == codigo_estudante for e in dados_estudantes):
                    print("\nMatrícula de estudante inválida. Tente novamente!")
                    continue

                if any(m.codigo_turma == codigo_turma and m.codigo_estudante == codigo_estudante for m in dados_matriculas):
                    print("\nEssa matrícula já existe. Tente novamente!")
                    continue

                return Matricula(codigo_turma, codigo_estudante)

            except ValueError:
                print("\nEntrada inválida. Digite um número inteiro para o código da turma e a matrícula do estudante.")

    @staticmethod
    def listar(dados_matriculas, dados_turmas, dados_estudantes):
        """
        Lista todas as matrículas cadastradas no sistema.

        Exibe uma mensagem informativa se não houver matrículas cadastradas.
        Caso contrário, imprime uma lista formatada com:
        - Código da matrícula
        - Código da turma
        - Nome do estudante e sua matrícula

        Args:
            dados_matriculas (list): Lista contendo os objetos Matricula cadastrados
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_estudantes (list): Lista contendo os objetos Estudante cadastrados.
        """

        if not dados_matriculas:
            print("\nNenhuma matrícula cadastrada até o momento!")
        else:
            print("\n**** LISTA DE MATRÍCULAS ****")
            for matricula in dados_matriculas:
                turma = next((t for t in dados_turmas if t.codigo == matricula.codigo_turma), None)
                estudante = next((e for e in dados_estudantes if e.matricula == matricula.codigo_estudante), None)

                if turma and estudante:
                    print(f"\nCódigo da matrícula: {matricula.codigo}")
                    print(f"Turma: {turma.codigo}")
                    print(f"Estudante: {estudante.nome} (Matrícula: {estudante.matricula})")
                else:
                    print(f"\nMatrícula {matricula.codigo} com informações inválidas (turma ou estudante não encontrado)")

    @staticmethod
    def atualizar(dados_matriculas, dados_turmas, dados_estudantes):
        """
        Atualiza os códigos de turma e estudante de uma matrícula existente.

        Solicita ao usuário o código da matrícula a ser atualizada e os novos códigos de turma e estudante.
        Realiza validações para garantir que:
        - O código da matrícula seja válido (existente na lista).
        - Os novos códigos de turma e estudante sejam válidos (existam nas respectivas listas).
        - A combinação turma-estudante não gere uma matrícula duplicada (excluindo a matrícula atual).
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_matriculas (list): Lista contendo os objetos Matricula cadastrados
            dados_turmas (list): Lista contendo os objetos Turma cadastrados.
            dados_estudantes (list): Lista contendo os objetos Estudante cadastrados.
        """

        if not dados_matriculas:
            print("\nNenhuma matrícula cadastrada até o momento!")
            return

        try:
            codigo_matricula = int(input("\nPara voltar ao menu, digite 0.\n\nQual matrícula você deseja atualizar?\nDigite o código da matrícula: "))
            if codigo_matricula == 0:
                print("\nVoltando para o menu de operações...")
                return

            for matricula in dados_matriculas:
                if matricula.codigo == codigo_matricula:
                    while True:
                        try:
                            novo_codigo_turma = int(input("\nPara voltar ao menu, digite 0.\n\nDigite o novo código da turma: "))
                            if novo_codigo_turma == 0:
                                print("\nVoltando para o menu de operações...")
                                return
                            elif novo_codigo_turma == matricula.codigo_turma:
                                print("\nO código da turma é o mesmo. Insira um código diferente ou 0 para voltar.")
                                continue

                            if not any(t.codigo == novo_codigo_turma for t in dados_turmas):
                                print("\nCódigo de turma inválido. Tente novamente!")
                                continue

                            novo_codigo_estudante = int(input("Digite a nova matrícula do estudante: "))
                            if novo_codigo_estudante == 0:
                                print("\nVoltando para o menu de operações...")
                                return
                            elif novo_codigo_estudante == matricula.codigo_estudante:
                                print("\nA matrícula do estudante é a mesma. Insira uma matrícula diferente ou 0 para voltar.")
                                continue

                            if not any(e.matricula == novo_codigo_estudante for e in dados_estudantes):
                                print("\nMatrícula de estudante inválida. Tente novamente!")
                                continue

                            matricula_existente = any(m for m in dados_matriculas if m.codigo_turma == novo_codigo_turma and m.codigo_estudante == novo_codigo_estudante and m.codigo != codigo_matricula)
                            if matricula_existente:
                                print("\nEssa matrícula já existe. Tente novamente!")
                                continue

                            matricula.codigo_turma = novo_codigo_turma
                            matricula.codigo_estudante = novo_codigo_estudante
                            print("\nDados da matrícula atualizados com sucesso!")
                            return

                        except ValueError:
                            print("\nEntrada inválida. Digite um número inteiro para o código da turma e a matrícula do estudante.")

            print("\nCódigo de matrícula informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao atualizar a matrícula! Certifique-se de inserir um número válido para o código da matrícula.")
    
    @staticmethod
    def excluir(dados_matriculas):
        """
        Exclui uma matrícula do sistema.

        Solicita ao usuário o código da matrícula a ser excluída.
        Realiza validações para garantir que o código seja válido (existente na lista)
        e pede confirmação antes de excluir.
        Permite que o usuário volte ao menu digitando '0'.

        Args:
            dados_matriculas (list): Lista contendo os objetos Matricula cadastrados.
        """

        if not dados_matriculas:
            print("\nNenhuma matrícula cadastrada até o momento!")
            return

        try:
            codigo = int(input("\nPara voltar ao menu, digite 0.\n\nQual matrícula você deseja excluir?\nDigite o código: "))
            if codigo == 0:
                print("\nVoltando para o menu de operações...")
                return

            for matricula in dados_matriculas:
                if matricula.codigo == codigo:
                    print(f"\nVocê tem certeza que deseja excluir a matrícula de código: {matricula.codigo}?")
                    while True:
                        escolha = input("\n[Y/N]? ")
                        if escolha.upper() == 'Y':
                            dados_matriculas.remove(matricula)
                            print("\nMatrícula excluída com sucesso!")
                            return
                        elif escolha.upper() == 'N':
                            print("\nVoltando para o menu de operações...")
                            return
                        else:
                            print("\nOpção inválida, tente novamente!")

            print("\nCódigo de matrícula informado não existe no banco de dados!")

        except ValueError:
            print("\nOcorreu um erro ao excluir a matrícula. Certifique-se de inserir um número válido para o código.")