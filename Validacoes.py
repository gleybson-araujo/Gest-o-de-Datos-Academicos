class Validacoes:
    """
    Classe utilitária para realizar validações de dados no sistema.
    """

    @staticmethod
    def validar_cpf(cpf):
        """
        Valida um CPF.

        Args:
            cpf (str): O CPF a ser validado.

        Returns:
            True se o CPF for válido, False caso contrário.
        """
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

    @staticmethod
    def cpf_ja_existe(cpf, menu_operacoes):
        """
        Verifica se um CPF já está cadastrado para algum estudante.

        Args:
            cpf (str): O CPF a ser verificado.
            menu_operacoes (MenuOperacional): O objeto MenuOperacional para acessar os dados dos estudantes.

        Returns:
            True se o CPF já estiver cadastrado para algum estudante, False caso contrário.
        """
        for estudante in menu_operacoes.dados_estudantes:
            if cpf == estudante.cpf:
                return True
        return False