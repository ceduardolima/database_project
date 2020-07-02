from sqldados import *

class MenuInicial():
    def __init__(self):
        self.usuario = None
        self.senha = None
        self.rootId = 2
        self.banco = SqLite()

    def Login(self):
        self.usuario = int(input("ID: "))
        self.senha = input("Senha: ")
        tabelaFuncionarios = self.banco.obterDadosDatabela('funcionarios')
        identificacao, senha = tabelaFuncionarios[0], tabelaFuncionarios[3]

        if self.usuario == self.rooId and self.senha == senha:
            pass
        
        elif self.usuario is not self.rootId and self.usuario == identificacao and self.senha == senha:
            pass




