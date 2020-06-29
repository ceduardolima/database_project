from sqlite3 import *

banco = 'dados.db'
class SqLite:
    def __init__(self, master=banco):
        self.con = connect(master)
        self.cur = self.con.cursor()

    def _print(self):
        print(">> Ação realizada com sucesso <<", end='\n\n')
    
    def print_error(self, local, err):
        print(f">> Error ({local}): {err}")

    def fechar(self):
        self.con.close()
    
    def adicionar(self, tabela, valores):
        try:
            self.cur.execute(f"INSERT INTO {tabela} VALUES {valores}")
            _print()
        except Error as err: print_error('adicionar, err')
        self.con.commit()

    def remover(self, tabela, condicao):
        try:
            self.cur.execute(f"DELETE FROM {tabela} WHERE {condicao}")
            _print()
        except Error as err: print_error('remover', err)
        self.con.commit()
    
    def atualizar(self, tabela, valores, condicao):
        print(valores, condicao)
        for n in range(len(valores)):
            try:
                self.cur.execute(f"UPDATE {tabela} SET {valores[n][0]}='{valores[n][1]}' WHERE {condicao[0]}='{condicao[1]}'")
                _print()
            except Error as err: print_error('atualizar', err)
            self.con.commit()

    def printar_tabelas(self):
        self.cur.execute("SELECT tbl_name FROM sqlite_master WHERE type = 'table'")
        tabelas = self.cur.fetchall() 
        [print(nome, end=' ') for nome in tabelas]
    
    def printar_valores(self, tabela):
        self.cur.execute(f"SELECT * FROM {tabela}")
        valores = self.cur.fetchall()
        [print(valores[n]) for n in range(len(valores))]
