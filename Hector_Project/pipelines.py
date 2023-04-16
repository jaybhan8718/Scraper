import sqlite3
from itemadapter import ItemAdapter


class HectorProjectPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('hector_project.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS Scraped_Data""")
        self.curr.execute("""CREATE TABLE Scraped_Data (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Title TEXT UNIQUE,
                                Percentage REAL
                            )""")
    def process_item(self, item, spider):
        self.store_data(item)
        return item

    def store_data(self, item):
        adapter = ItemAdapter(item)
        title = adapter.get('Title')
        percentage = adapter.get('Percentage')
        # Check if the title already exists in the table
        self.curr.execute("""SELECT id FROM Scraped_Data WHERE Title = ?""", (title,))
        row = self.curr.fetchone()
        if row:
            # If the title already exists, update the percentage for that row
            self.curr.execute("""UPDATE Scraped_Data SET Percentage = ? WHERE id = ?""", (percentage, row[0]))
        else:
            # If the title doesn't exist, insert a new row
            self.curr.execute("""INSERT INTO Scraped_Data (Title, Percentage) VALUES (?, ?)""", (title, percentage))
        self.conn.commit()
