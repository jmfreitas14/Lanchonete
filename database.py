import sqlite3

conn = sqlite3.connect("lanchonete.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo NUMBER NOT NULL,
    quant NUMBER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cardapio (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    codigo NUMBER NOT NULL,
    preco NUMBER NOT NULL
);
""")

print("Conectado ao banco de dados!!!")
