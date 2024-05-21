import sqlite3

class DataBase:
    def __init__(self, db_name='app.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self): #Criação da tabela cliente
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cliente (
                nome TEXT PRIMARY KEY,
                password TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def insert_cliente(self, nome, password): #Inserir um novo cliente na  tabela
        try:
            self.cursor.execute('INSERT INTO Cliente (nome, password) VALUES (?, ?)', (nome, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_cliente(self, nome):  #Eliminar um cliente
        self.cursor.execute('DELETE FROM Cliente WHERE nome = ?', (nome, ))
        self.conn.commit()

    def fetch_clientes(self): #Aceder à base de dados para recolher todos os clientes
        self.cursor.execute('SELECT nome, password FROM Cliente')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
