import sqlite3


class Database:
    def __init__(self, db_file='records.db'):
    #Intializes the database connection and cursor.
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row #Allows to access column by name
            self.cursor = self.conn.cursor()
            self._create_tables()
        except sqlite3.Error as e:
            print("There was a failure to intialize database.\n")
            print(e)
            raise
            
        
    def _create_tables(self):
        #creates the tables if they don't exist
        listing_table_creation = '''CREATE TABLE IF NOT EXISTS listings (
                                        id INTEGER PRIMARY KEY,
                                        address TEXT NOT NULL,
                                        price REAL NOT NULL);'''
        self.cursor.execute(listing_table_creation)
        self.conn.commit()

    def add_listing(self, address, price):
    #Adding listing to records database
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
            return False # Signal 
        
    def get_all_listings(self):
        self.cursor.execute("SELECT * FROM listings") #highlights what I need
        return self.cursor.fetchall() #Actually gets that stuff for me
    
    def close_connection(self):
        if self.conn: #Checks if database is open
            self.conn.close() #End db connection
    
    #test code
db = Database()
print("Add listing...\n")
db.add_listing("2106 Gaylin Hills Ct.", 32000)
all_listings = db.get_all_listings()

for  listing in all_listings:
    print(f" ID: {listing['id']}, Address: {listing['address']} Price: {listing['price']}")

db.close_connection()