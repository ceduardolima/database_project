from pymysql import (connect, cursors, Error)

class SQL:
    num_connection = 0

    def __init__(self, data_name, host, user, password):
        self.data_name = data_name
        self.host = host
        self.__user = user
        self.__password = password
        self.conn = connect(
                             host=self.host,
                             user=self.__user,
                             passwd=self.__password)
        self.cursor = self.conn.cursor()
        self._createconnection()
        SQL.num_connection += 1

    def __repr__(self):
        return "SQL('{}', '{}', '{}')".format(self.data_name, self.host, self.__user)

    def __str__(self):
        return "Data Name: {}, Number of connection: {}".format(self.data_name, self.num_connection)

    def _createconnection(self):
        """Create a connection with the database"""
        try: 
            self.cursor.execute(f"USE {self.data_name}")
        except:  print(">> Error: ConnectionError")
    
    def closeconnectio(self):
        """Close the connection"""
        self.conn.close()
        SQL.num_connection -= 1

    def _fetchdada(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cur.fetchall()
    
    @staticmethod
    def _strcreation(str_list):
        new_str = "("
        for value in str_list[:-1]:
            if value == 'DEFAULT':
                new_str += "{}, ".format(value)
            else:
                new_str += "'{}', ".format(value)
        return "{} {}{}".format(new_str, str_list[-1], ")")

    @staticmethod
    def _defaultadd(values, firstdefault=True):
        """Create a String without '' on the default
                firstdefault == True -> use for table that have the primary key
                firstdefault == False -> use for table that dont have the primary key"""
        if firstdefault: values.insert(0 ,"DEFAULT") 
        new_list = []
        for value in values:
            if value == '': new_list.append("DEFAULT")
            else: new_list.append(value)
        return new_list

    def addvalues(self, table, values):
        """Add a new value on the select table"""
        sql_string = self._strcreation(self._defaultadd(values))    
        print(sql_string)    
        self.cursor.execute(f"INSERT INTO {table} VALUES {sql_string}")
        self.conn.commit()

    def updatevalues(self, table, columns, values, conditions):
        """Updatethe values in the table"""
        sql_lista = self._defaultadd(values, firstdefault=False)
        for n in range(len(columns)):
            self.cursor.execute(f"UPDATE {table} SET {columns[n]}='{sql_lista[n]}' WHERE {conditions[0]}='{conditions[1]}'")
        self.conn.commit()
    
    def prt_alltable(self, table):
        alldata = self._fetchdada(table)
        for data in alldata:
            [print(element) for element in data]
            print('------------------')

        





sql = SQL('dados', 'localhost', 'root', '')
sql.updatevalues('estoque', ['nome', 'estoque'], ['pq1', 'p0p6'], ['id', '6'])