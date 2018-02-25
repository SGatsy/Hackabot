import sqlite3
from sqlite3 import Error

class salva():

    def __init__(self, dbname="database.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        
    def prima(self):        
        stmt = "CREATE TABLE IF NOT EXISTS items (description text)"
        stmtt = "CREATE TABLE IF NOT EXISTS foto (description text)"
        self.conn.execute(stmt)
        self.conn.execute(stmtt)
        self.conn.commit()
    
    def aggiungi_testo(self, item_text):          
        stmt = "INSERT INTO items (description) VALUES (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def aggiungi_foto(self,items):
        stmt = "INSERT INTO foto (description) VALUES (?)"
        ars = (items, )
        self.conn.execute(stmt,ars)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):          
        stmt = "SELECT description FROM items"
        return [x[0] for x in self.conn.execute(stmt)]
    
    def prendi_foto(self):
        stmt = "SELECT description FROM foto"
        for x in self.conn.execute(stmt):          
            return x[0]