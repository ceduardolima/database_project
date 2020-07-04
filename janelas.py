from sqldados import *

ROOT = 2
FUNCIONARIO = 3

class MenuInicial():
    def __init__(self, banco=SqLite()):
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
    
    def informandoComando(self):
        print(">> Pagina do Administrador <<")
        print("c -> Cadastrar algum funcionario")
        print("m -> Manipular dos dados de alguma tabela")
        print("t -> visualizar informações das tabelas")
        inputComando = input("> Comando: ")
        return inputComando
    
    def informandoTabelas(self):
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
