from controllers.db_controller import Db
from sqlalchemy import text

db = Db("mysql","pymysql", "root", "root", "localhost", 3306, "lista")

def get_item():
    with db.connect() as conn:
        return conn.execute(text(f"SELECT * FROM ListaDeCompras"))
    
def insert_item(name, quantity):
    with db.connect() as conn:
        conn.execute(text(f"INSERT INTO listadecompras(nomeDoItem, quantidade) VALUES ('{name}', '{quantity}')"))
        conn.commit()

def delete_item(name):
    with db.connect() as conn:
        conn.execute(text(f"DELETE FROM listadecompras WHERE nomeDoItem = '{name}'"))
        conn.commit()

def edit_item_with_name(name, quantity, new_name):
    with db.connect() as conn:
            conn.execute(text(f"UPDATE listadecompras SET quantidade = '{quantity}', nomeDoItem = '{new_name}' WHERE nomeDoItem = '{name}'"))
            conn.commit()

def edit_item(name, quantity):
    with db.connect() as conn:
            conn.execute(text(f"UPDATE listadecompras SET quantidade = '{quantity}' WHERE nomeDoItem = '{name}'"))
            conn.commit()