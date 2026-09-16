import sqlite3
import json
from datetime import datetime

# Nombre del archivo de la base de datos
DB_PATH = "contactos.db"


def crear_tabla():
    """Crea la tabla 'contactos' si todavía no existe."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT,
            ciudad TEXT,
            horario TEXT,
            servicios TEXT NOT NULL,
            gasto_mensual REAL,
            consentimiento INTEGER NOT NULL,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)
    conn.commit()
    conn.close()


def guardar_contacto(nombre, telefono, email, ciudad, horario, pagos, consentimiento):
    """Guarda un nuevo contacto en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO contactos
        (fecha, nombre, telefono, email, ciudad, horario,
         servicios, gasto_mensual, consentimiento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            nombre,
            telefono,
            email,
            ciudad,
            horario,
            json.dumps(pagos, ensure_ascii=False),
            sum(pagos.values()),
            int(consentimiento),
        ),
    )
    conn.commit()
    conn.close()