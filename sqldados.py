from pymysql import (connect, cursors, Error)

banco = 'dados'
class SqLite:
    def __init__(self, master=banco):
        self.master = master
        self.con = connect(host='localhost', user='root', passwd='')
        self.cur = self.con.cursor()
        self.cur.execute(f"USE {self.master}") 
    
    @staticmethod
    def printError(local, err):
        """Printa o Erro ocorrido"""
        print(f">> Error ({local}): {err}")

    @staticmethod
    def formatandoEntradaUnica(dado):
        try: 
            if int(dado): return dado
        except ValueError: return "'" + dado + "'"

    @staticmethod
    def formatandoDados(dadosRecebidos):
        """Ajusta a entrada de dados para tabelas q possuem id auto_increment"""
        dadosFormatados = "(DEFAULT"
        for dado in dadosRecebidos:
            if dado == 'DEFAULT': formatacao = ", DEFAULT"
            else: formatacao = f",'{dado}'"
            dadosFormatados = dadosFormatados + formatacao
        return dadosFormatados + ")"
    
    @staticmethod
    def printarDadosDaTabela(dadosTabela):
        for dado in dadosTabela:
            [print(f"--{dado[quantidade]}", end="") for quantidade in range(len(dado))]
            print("\n", "------------------------------------------")

    def fecharConexao(self):
        """Fecha a conexao com o banco de dados"""
        self.con.close()
    
    def AdicionandoCadatro(self, infoCadastro):
        """Faz o cadastro dos funcionarios"""
        try:
            self.cur.execute(f"INSERT INTO funcionarios (id, nome, cpf, senha) VALUES {infoCadastro}")
            self.con.commit()
            return True
        except: self.printError('cadastro', Error)

    def adicionarDadosNasTabelas(self, tabelaInserida, valoresParaAdicionar):
        """Adiciona os dados inseridos nas tabela indicada pelo usuario"""
        self.cur.execute(f"INSERT INTO {tabelaInserida} VALUES {valoresParaAdicionar}")
        self.con.commit()
        return True
     
    def atualizarTabela(self, tabela, colunasEvaloresAtualizados, especificando):
        """Faz o update da tabela escolhida"""
        colunaEspecificada, valorColuna = especificando
        try:
            for atualizacoes in colunasEvaloresAtualizados:
                coluna, valor = atualizacoes
                self.cur.execute(f"UPDATE {tabela} SET {coluna}='{valor}' WHERE {colunaEspecificada}={valorColuna}")
            self.con.commit()
            return True
        except Error as err: self.printError('atualizar', Error)
    
    def obterDadosDatabela(self, tabela):
        """Pega os dados de uma tabela escolhida"""
        self.cur.execute(f"SELECT * FROM {tabela}")
        return self.cur.fetchall()

    def procurarPor(self, tabela, nomeColuna, valorColuna):
        self.cur.execute(f"SELECT * FROM {tabela} WHERE {nomeColuna}={valorColuna}")
        return self.cur.fetchall()
        
    def apagarDadosDaTabela(self, tabela, dadosRecebidos):
        """Apaga os dados de uma tabela"""
        coluna, valorColuna = dadosRecebidos
        try:
            self.cur.execute(f"DELETE FROM {tabela} WHERE {coluna}={valorColuna}")
            self.con.commit()
            return True
        except: self.printError('apagarDadosDaTabela', Error)


