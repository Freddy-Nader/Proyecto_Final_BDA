import pandas as pd
from sqlalchemy import create_engine, text
import numpy as np

# Connect to MySQL server "Bases"
engine = create_engine('mysql+pymysql://root:warmachinerox2005@127.0.0.1:3306/proyecto_final')

# Recreate tables
with engine.connect() as conn:
    conn.execute(text("""
    ALTER TABLE Categorias RENAME TO Categories_old;

CREATE TABLE IF NOT EXISTS Categorias (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre TEXT
);


INSERT INTO Categorias (nombre)
SELECT DISTINCT categoria FROM Categories_old;

CREATE TABLE IF NOT EXISTS LibroCategoria (
    libro_id VARCHAR(24) NOT NULL,
    categoria_id INTEGER NOT NULL,
    PRIMARY KEY (libro_id, categoria_id),
    FOREIGN KEY (libro_id) REFERENCES Libros(id),
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);

INSERT INTO LibroCategoria (libro_id, categoria_id)
SELECT co.libro_id, c.id
FROM Categories_old co
JOIN Categorias c ON co.categoria = c.nombre;

SELECT * FROM Categorias;
SELECT * FROM LibroCategoria;


CREATE TABLE IF NOT EXISTS LibroAutor (
    libro_id VARCHAR(24) NOT NULL,
    autor_id INT NOT NULL,
    PRIMARY KEY (libro_id, autor_id),
    FOREIGN KEY (libro_id) REFERENCES Libros(id),
    FOREIGN KEY (autor_id) REFERENCES Autores(id)
);

CREATE TABLE IF NOT EXISTS AutoresNormalizados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

INSERT IGNORE INTO AutoresNormalizados (nombre)
SELECT DISTINCT autor FROM Autores;

INSERT INTO LibroAutor (libro_id, autor_id)
SELECT a.libro_id, an.id
FROM Autores a
JOIN AutoresNormalizados an ON a.autor = an.nombre;

SELECT 
    l.id AS libro_id,
    l.titulo,
    an.id AS autor_id,
    an.nombre AS autor
FROM Libros l
JOIN LibroAutor la ON l.id = la.libro_id
JOIN AutoresNormalizados an ON la.autor_id = an.id
ORDER BY l.titulo;

RENAME TABLE Autores TO Autores_Backup;
ALTER TABLE AutoresNormalizados RENAME TO Autores;

RENAME TABLE Autores TO Autores_Backup;
ALTER TABLE AutoresNormalizados RENAME TO Autores;

ALTER TABLE LibroAutor DROP FOREIGN KEY LibroAutor_ibfk_2; 

DROP TABLE Autores_Backup;
    
    """))


# Verify the data was inserted
with engine.connect() as conn:
    print("\nCounts in each table:")
    for tabla in ['Libros','Autores','Categorias','Estados','LibroAutor','LibroCategoria']:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {tabla}")).fetchone()[0]
        print(f"{tabla}: {count} registros")

    print("\nFirst 5 books:")
    result = conn.execute(text("SELECT id, titulo, isbn FROM Libros LIMIT 5;"))
    for row in result:
        print(row)