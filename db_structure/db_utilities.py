import sqlite3


class ConnectToDatabase(object):
    """ Connect to our store database.
        
    We work with one database and therein we have all our tables with our stock :)
    """
    
    def __init__(self, database):
        self.database = database
    
    def connect(self):
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
        return
    
    def commit(self):
        self.conn.commit()
        return
    
    def close(self):
        self.conn.close()
        return


class ConnectToCardsTable(ConnectToDatabase):
    """ Class to handle operations in the table that holds cards.
        
    We hardcode the table's name and we henceforth call it cards. Because of this
    the class instance is created without a "cards" variable.
    """
    
    def __init__(self, database):
        super(ConnectToCardsTable, self).__init__(database)
        self.tablename = 'cards'
    
    def create_table(self):
        self.t = (self.tablename,)
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", self.t)
        table_test = self.c.fetchall()
        if table_test is None:
            print("Creating table..")
            self.c.execute('''CREATE TABLE ?
                (date text, trans text, symbol text, qty real, price real)''', self.t)
            print("Table done.")
            return
        else:
            print("Working with existing table..")
            return

def insert_row(self):
    """Python's security precautions to hardcode the table name here. (We call it cards)"""
    self.c.execute("INSERT INTO cards VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    return
