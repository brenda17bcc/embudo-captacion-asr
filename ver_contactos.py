import sqlite3

conn = sqlite3.connect("contactos.db")
filas = conn.execute(
    "SELECT id, fecha, nombre, telefono, servicios, gasto_mensual, estado "
    "FROM contactos"
).fetchall()
conn.close()

print(f"Total de contactos: {len(filas)}\n")
for fila in filas:
    print(fila)