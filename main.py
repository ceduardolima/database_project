from janelas import *

def admMostrarTabelas(admClasse):
    tabelaRequisitada = admClasse.informandoTabelas()
    if tabelaRequisitada == 'c': admClasse.informacoesClientes()
    if tabelaRequisitada == 'e': admClasse.informacoesEstoque()
    if tabelaRequisitada == 'f': admClasse.informacoesFuncionarios()

def manipularDados(admClasse):
    print("a -> Atualizar algum dado da tabela")
    print("d -> Deletar algum dado da tabela")
    comando = input(">> Comando: ")
    tabela = input("Tanela a ser modificada: ")
    idObj = input("Informe o ID: ")

    if comando == 'a':
        quantidadeAdd = int(input("Quantos dados voce quer adicionar? "))
        colunas, novosValores = [], []
        for _ in range(quantidadeAdd):
            colunas.append(input("Nome da coluna: "))
            novosValores.append(input("Novo valor: "))
        valoresZipados = zip(colunas, novosValores)
        admClasse.atualizarTabela(tabela, valoresZipados, ('id', idObj))
    
    if comando == 'd': admClasse.apagarDadosDaTabela(tabela, ('id', idObj))


adm = PaginaAdm()
while True:
    comandoRecebido = adm.informandoComando()
    if comandoRecebido == 'c': adm.informacoesParaCadastro()
    if comandoRecebido == 'm': manipularDados(adm)
    if comandoRecebido == 't': admMostrarTabelas(adm)
    if comandoRecebido == 's': break
