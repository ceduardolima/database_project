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

    @staticmethod
    def _defaultadd(values, firstdefault=True):
        """Create a String without '' on the default
                firstdefault == True -> use for table that have the primary key
                firstdefault == False -> use for table that dont have the primary key"""
        new_string = ""
        if firstdefault: new_string = "(DEFAULT"
        for value in values:
            print(values)
            if value == '': 
                new_string += ", DEFAULT"
            else:
                new_string += f", '{value}'"

        return new_string + ")"

    def addvalues(self, table, values):
        """Add a new value on the select table"""
        sql_string = self._defaultadd(values)
        print(sql_string)
        self.cursor.execute(f"INSERT INTO {table} VALUES {sql_string}")
        self.conn.commit()
