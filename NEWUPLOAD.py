import pandas as pd
from sqlalchemy import create_engine, text
import numpy as np


sql_commands = [
    # 1. Transformación de Categorías
    "ALTER TABLE Categorias RENAME TO Categories_old",
    """CREATE TABLE IF NOT EXISTS Categorias (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        nombre TEXT
    )""",
    "INSERT INTO Categorias (nombre) SELECT DISTINCT categoria FROM Categories_old",

    # 2. Creación de LibroCategoria
    """CREATE TABLE IF NOT EXISTS LibroCategoria (
        libro_id VARCHAR(24) NOT NULL,
        categoria_id INTEGER NOT NULL,
        PRIMARY KEY (libro_id, categoria_id),
        FOREIGN KEY (libro_id) REFERENCES Libros(id),
        FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
    )""",
    """INSERT INTO LibroCategoria (libro_id, categoria_id)
    SELECT co.libro_id, c.id
    FROM Categories_old co
    JOIN Categorias c ON co.categoria = c.nombre""",

    # 3. Normalización de Autores
    """CREATE TABLE IF NOT EXISTS AutoresNormalizados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL UNIQUE
    )""",
    "INSERT IGNORE INTO AutoresNormalizados (nombre) SELECT DISTINCT autor FROM Autores",

    # 4. Creación de LibroAutor
    """CREATE TABLE IF NOT EXISTS LibroAutor (
        libro_id VARCHAR(24) NOT NULL,
        autor_id INT NOT NULL,
        PRIMARY KEY (libro_id, autor_id),
        FOREIGN KEY (libro_id) REFERENCES Libros(id),
        FOREIGN KEY (autor_id) REFERENCES Autores(id)
    )""",
    """INSERT INTO LibroAutor (libro_id, autor_id)
    SELECT a.libro_id, an.id
    FROM Autores a
    JOIN AutoresNormalizados an ON a.autor = an.nombre""",

    # 5. Renombrar tablas (ejecutar solo si todo lo anterior funciona)
    "RENAME TABLE Autores TO Autores_Backup",
    "ALTER TABLE AutoresNormalizados RENAME TO Autores",

    # 6. Eliminar tabla backup 
    "ALTER TABLE LibroAutor DROP FOREIGN KEY LibroAutor_ibfk_2",
    "DROP TABLE Autores_Backup"
]

# Ejecutar cada comando por separado
with engine.connect() as conn:
    for cmd in sql_commands:
        try:
            conn.execute(text(cmd))
            conn.commit()
        except Exception as e:
            print(f"Error al ejecutar: {cmd[:50]}...")
            print(f"Error detallado: {str(e)}")
            conn.rollback()  # Revertir en caso de error
            break  # Detener la ejecución si hay un error
