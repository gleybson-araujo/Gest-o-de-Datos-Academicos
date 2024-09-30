# Gest-o-de-Datos-Academicos
## Sistema de Gestão Acadêmica - CRUD Básico

Este projeto implementa um sistema de gerenciamento de dados acadêmicos, permitindo realizar operações CRUD (Criar, Ler, Atualizar, Deletar) para as seguintes entidades:

* **Estudantes:**
    * CPF
    * Nome

* **Professores:**
    * Código (Número inteiro)
    * Nome
    * CPF

* **Disciplinas:**
    * Código (Número inteiro)
    * Nome

* **Turmas:**
    * Código (Número inteiro)
    * Código do professor (Número inteiro)
    * Código da disciplina (Número inteiro)

* **Matrículas:**
    * Código (Número inteiro)
    * Código da turma (Número inteiro)
    * Código do estudante (Número inteiro)

O sistema utiliza estruturas de dados em memória (listas) para armazenar as informações e arquivos JSON para garantir a persistência dos dados.

**Funcionalidades:**

* **Incluir:** Permite adicionar novos registros de estudantes, professores, disciplinas, turmas e matrículas.
* **Listar:** Exibe todos os registros cadastrados para cada entidade.
* **Atualizar:** Permite modificar os dados de um registro existente.
* **Excluir:** Remove um registro do sistema.

O projeto inclui validações de dados para garantir a integridade das informações e tratamento de exceções para lidar com possíveis erros durante a execução.