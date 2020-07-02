from sqldados import *

class MenuInicial():
    def __init__(self):
        self.usuario = None
        self.senha = None
        self.cpf = None
    
    def introMenu(self):
        print("l -> Login")
        print("c -> Cadastro")
    
    def cadastro(self):
        self.usuario = input("Insira o nome de usuario: ")
        self.senha = input("Insira uma senha: ")
        self.cpf = input("Insira seu cpf: ")
        dadosCadastro = (self.usuario, self.senha, self.cpf)
        banco = SqLite()
        dadosCadastroFormatado = banco.formatandoDados(dadosCadastro)
        banco.AdicionandoCadatro(dadosCadastroFormatado)
        banco.fecharConexao()

menu = MenuInicial()
menu.cadastro()

