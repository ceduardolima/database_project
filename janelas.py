from sqldados import *

ROOT = 2
FUNCIONARIO = 3

class MenuInicial(SqLite):
    def __init__(self):
        super.__init__()
        self.usuario = None
        self.senha = None
        self.rootId = 2
        self.banco = banco

    def login(self):
        self.usuario = 2
        self.senha = '86231'
        tabelaFuncionarios = self.banco.obterDadosDatabela('funcionarios')
        admSenha = tabelaFuncionarios[0][3]

        if self.usuario == self.rootId and self.senha == admSenha:
            self.banco.fecharConexao()
            return ROOT
            
        else:
            return [FUNCIONARIO for funcionario in tabelaFuncionarios if self.usuario == funcionario[0] and self.senha == funcionario[3]]
            
class PaginaAdm(SqLite):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def informandoComando():
        print(">> Pagina do Administrador <<")
        print("c -> Cadastrar algum funcionario")
        print("m -> Manipular dos dados de alguma tabela")
        print("t -> visualizar informações das tabelas")
        inputComando = input("> Comando: ")
        return inputComando
    
    @staticmethod
    def informandoTabelas():
        print(">> Tabelas <<")
        print("c -> Clientes")
        print("e -> Estoque")
        print("f -> funcionarios")
        return input("> comando: ")
    
    def informacoesFuncionarios(self):
        informacoesTabela = self.obterDadosDatabela('funcionarios')
        print("-------- FUNCIONARIOS --------")
        print("ID | NOME | CPF | SENHA | COMISSAO POR PEÇA | COMISSAO POR SERVIÇO | DATA DE CADASTRO")
        self.printarDadosDaTabela(informacoesTabela)
    
    def informacoesClientes(self):
        informacoesTabela = self.obterDadosDatabela('clientes')
        print("-------- CLIENTES --------")
        print("ID | NOME | CPF | SENHA | CELULAR1 | CELULAR2 | CEP | CIDADE | BAIRRO ")
        self.printarDadosDaTabela(informacoesTabela)

    def informacoesEstoque(self):
        informacoesTabela = self.obterDadosDatabela('estoque')
        print("-------- ESTOQUE --------")
        print("ID | NOME | FORNECEDOR | QUANTIDADE | LOCALIZAÇÃO | PREÇO")
        self.printarDadosDaTabela(informacoesTabela)

    def informacoesParaCadastro(self):
        nomeFuncionario = input("Nome: ")
        cpf_Funcionario = input("Cpf: ")
        senhaFuncionario = input("Senha: ")
        dadosFormatados = self.formatandoDados((nomeFuncionario, cpf_Funcionario, senhaFuncionario))
        self.AdicionandoCadatro(dadosFormatados)

class Funcionario(SqLite):
    def __init__(self):
        super().__init__()

    def cadastroCliente(self):
        coluna = ('nome', 'cpf', 'celular1', 'celular2', 'cep', 'cidade', 'bairro')
        valores = []
        for n in range(len(coluna)):
            print(coluna[n])
            entrada = input()
            if entrada == '': valores.append('DEFAULT')
            else: valores.append(entrada)
        valorFomatado = self.formatandoDados(valores)
        self.adicionarDadosNasTabelas('clientes', valorFomatado)
    
    def pesquisarPorPeca(self, nomePeca, valor):
        valor = self.formatandoEntradaUnica(valor)
        print(valor)
        pecas = self.procurarPor('estoque', nomePeca, valor)
        for peca in pecas:
            print(f"---------- Peça ----------")
            print(f"id = {peca[0]}")
            print(f"Nome = {peca[1]}")
            print(f"Fornecedor = {peca[2]}")
            print(f"Qunatidade = {peca[3]}")
            print(f"Estoque = {peca[4]}")
            print(f"Valor = {peca[5]}")

