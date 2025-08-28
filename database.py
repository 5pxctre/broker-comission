import sqlite3


class Database:
    def __init__(self, db_file='records.db'):
    #Intializes the database connection and cursor.
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    def _create_tables(self):
        #creates the tables if they don't exist
        listing_table_creation = '''CREATE TABLE IF NOT EXISTS listings (
                                        id INTEGER PRIMARY KEY,
                                        address TEXT NOT NULL,
                                        price REAL NOT NULL);'''
        self.cursor.execute(listing_table_creation)
        self.conn.commit()

    def add_transaction(self, address, price):
    #Adding transaction to records database
        try:
        #try block tries something to insert data, but if it fails it will go to except.
            self.cursor.execute("INSERT INTO listings (address, price) VALUES (?,?)", (address, price))
            self.conn.commit()
            print("Listing added successfully into database as id #", self.cursor.lastrowid)
            #Will tell you in terminal that it was successful and the last row id number for that record
            return True # Signal success
        except sqlite3.Error as e:
            #Run only if an error occurs
            print(e)
            #Below undos any changes to database 
            self.conn.rollback()
            return False # Signal Fail
        
        #still need to implement this class in captracker.py