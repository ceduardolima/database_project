from janelas import *

def admMostrarTabelas(admClasse):
    tabelaRequisitada = admClasse.informandoTabelas()
    if tabelaRequisitada == 'c': admClasse.informacoesClientes()
    if tabelaRequisitada == 'e': admClasse.informacoesEstoque()
    if tabelaRequisitada == 'f': admClasse.informacoesFuncionarios()

adm = PaginaAdm()
while True:
    comandoRecebido = adm.informandoComando()
    if comandoRecebido == 'c': adm.informacoesParaCadastro()
    if comandoRecebido == 't': admMostrarTabelas(adm)
    if comandoRecebido == 's': break
