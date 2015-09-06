import os
import sqlite3


class ConnectToDatabase:
    """ Connect to our store database.
        
    We work with one database and therein we have all our tables with our stock :)
    """
    
    def __init__(self, root, database):
        self.db = database
        self.root = root
    
    def connect(self):
        db = os.path.join(self.root, self.db)
        self.conn = sqlite3.connect(self.db)
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
    the class instance is created without a "cards" variable. We also predefine here
    the table headers.
    """
    
    def __init__(self, root, database):
        super(ConnectToCardsTable, self).__init__(root, database)
        self.tablename = 'cards'
        self.root = root
        self.db = database
    
    def drop_table(self):
        self.c.execute('drop table if exists cards')
        self.commit()
    
    def create_table(self):
        self.t = (self.tablename,)

        # see all tables. fetch later to get the list of tuples
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        
        if self.t not in self.c.fetchall():
            print("Creating table..")
            
            self.c.execute('''CREATE TABLE cards
                (code, bought_date)''' ) #, bought_from, bought_price, source_code, occassion,
            #photo_id, m_f, family_member, features, sale_price, size)''')
            print("Table done.")
            return
        else:
            print("Working with existing table..")
        return

    def insert_row(self, row):
        """Python's security precautions to hardcode the table name here. (We call it cards)"""
        self.create_table()
        self.c.execute("INSERT INTO cards VALUES (?, ?)", row)
        return