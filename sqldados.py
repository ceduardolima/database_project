from pymysql import *

banco = 'dados'
class SqLite:
    def __init__(self, master=banco):
        self.master = master
        self.con = connect(host='localhost', user='root', passwd='')
        self.cur = self.con.cursor()
        self.cur.execute(f"USE {self.master}") 

    def confirmarAcaoRealizada(self):
        """Printa mensagem quando alguma ação foi realizada sem Erro"""
        print(">> Ação realizada com sucesso <<", end='\n\n')
    
    def printError(self, local, err):
        """Printa o Erro ocorrido"""
        print(f">> Error ({local}): {err}")

    def fecharConexao(self):
        """Fecha a conexao com o banco de dados"""
        self.con.close()

    def formatandoDados(self, dadosRecebidos):
        """Ajusta a entrada de dados para tabelas q possuem id auto_increment"""
        dadosFormatados = "(DEFAULT"
        for dado in dadosRecebidos:
            formatacao = f",'{dado}'"
            dadosFormatados = dadosFormatados + formatacao
        return dadosFormatados + ")"

    def DadosRecebidosDoUsuario(self, dadosInseridos, condicaoDeSaida=True):
        """Retorna os dados organizados para a função que irá ser executada\
            condicaoDeSaida == True -> Usado para adicionar dados na tabela\
            condicaoDeSaida == False -> Usado para fazer o update de uma tabela"""
        if condicaoDeSaida: return dadosInseridos
        elif condicaoDeSaida==False:
            coluna, valorColuna = dadosInseridos[0], dadosInseridos[1]
            return zip(coluna, valorColuna)
    
    def adicionarDadosNasTabelas(self, tabelaInserida, valoresParaAdicionar):
        """Adiciona os dados inseridos nas tabela indicada pelo usuario"""
        self.cur.execute(f"INSERT INTO {tabelaInserida} VALUES {valoresParaAdicionar}")
        self.con.commit()
        self.confirmarAcaoRealizada()

    def atualizarTabela(self, tabela, colunasEvaloresAtualizados, especificando):
        colunaEspecificada, valorColuna = especificando
        try:
            for atualizacoes in colunasEvaloresAtualizados:
                coluna, valor = atualizacoes
                print(coluna, valor)
                self.cur.execute(f"UPDATE {tabela} SET {coluna}='{valor}' WHERE {colunaEspecificada}={valorColuna}")
            self.con.commit()
            self.confirmarAcaoRealizada()
        except Error as err: self.printError('atualizar', Error)
    
    def obterDadosDatabela(self, tabela):
        self.cur.execute(f"SELECT * FROM {tabela}")
        return self.cur.fetchall()

    def printarDadosDaTabela(self, dadosTabela):
        for dado in dadosTabela:
            print("\n", "------------------------------------------")
            [print(f"--{dado[quantidade]}", end="") for quantidade in range(len(dado))]
        
    def apagarDadosDaTabela(self, tabela, dadosRecebidos):
        coluna, valorColuna = dadosRecebidos
        try:
            self.cur.execute(f"DELETE FROM {tabela} WHERE {coluna}={valorColuna}")
            self.con.commit()
            self.confirmarAcaoRealizada()
        except: self.printError('apagarDadosDaTabela', Error)


