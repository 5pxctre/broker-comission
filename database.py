import sqlite3

class Database:
    def __init__(self, db_file='records.db'):
        # Removed 'os' path verification. 
        # The database will be created in your current working directory.
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row 
            self.cursor = self.conn.cursor()
            self._create_tables()
        except sqlite3.Error as e:
            print("Failure to initialize database:", e)
            raise
            
    def _create_tables(self):
        listing_table_creation = '''CREATE TABLE IF NOT EXISTS listings (
                                        id INTEGER PRIMARY KEY,
                                        address TEXT NOT NULL,
                                        price REAL NOT NULL,
                                        split REAL,
                                        commission REAL,
                                        other_party REAL);'''
        self.cursor.execute(listing_table_creation)
        self.conn.commit()

    def add_listing(self, address, price, split, commission, other_party):
        try:
            query = """INSERT INTO listings 
                       (address, price, split, commission, other_party) 
                       VALUES (?, ?, ?, ?, ?)"""
            
            self.cursor.execute(query, (address, price, split, commission, other_party))
            self.conn.commit()
            print(f"Saved successfully! ID: {self.cursor.lastrowid}")
            return True 
        except sqlite3.Error as e:
            print("Error adding listing:", e)
            self.conn.rollback()
            return False 
        
    def get_all_listings(self):
        self.cursor.execute("SELECT * FROM listings") 
        return self.cursor.fetchall()
    
    def close_connection(self):
        if self.conn: 
            self.conn.close()