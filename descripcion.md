(**Nota:** esta es una version en md del pdf de las instrucciones del proyecto.)

# Reporte del Proyecto Final

#### Implementación de Almacenamiento y Consultas en MongoDB y

#### Propuesta de Esquema Relacional

## Introducción

En el presente proyecto final, se llevará a cabo la lectura de un archivo JSON que contiene
documentos con información de libros. Estos documentos se almacenarán en una colección
denominada books dentro de una base de datos de MongoDB llamada proyecto_final. A partir
de estos datos, se realizarán varias consultas a la colección y se propondrá un esquema
relacional, considerando que algunos campos no son atómicos.

## Estructura de los Documentos JSON

Los documentos JSON que se emplearán en este proyecto contienen los siguientes campos:

- _id: Identificador único del documento
- title: Título del libro
- isbn: Número Internacional Normalizado del Libro
- pageCount: Número de páginas del libro
- publishedDate: Fecha de publicación del libro
- thumbnailUrl: URL de la imagen en miniatura del libro
- shortDescription: Descripción corta del libro
- longDescription: Descripción larga del libro
- status: Estado del libro (arreglo)
- authors: Autores del libro (arreglo)
- categories: Categorías del libro (arreglo)

## Almacenamiento en MongoDB

Para el almacenamiento de los documentos JSON en MongoDB, se llevará a cabo la inserción
de cada documento en la colección books. La estructura de los documentos se ajustará
automáticamente a los tipos de datos compatibles con MongoDB.

## Proceso de Inserción

1. Lectura del archivo JSON: Se procederá a la lectura del archivo JSON que contiene los
documentos de libros.
2. Conexión a MongoDB: Se establecerá una conexión con la base de datos de MongoDB
proyecto_final.
3. Inserción de documentos: Cada documento leído del archivo JSON se insertará en la
colección books.


## Consultas a la Colección

Se realizarán diversas consultas a la colección books para extraer y analizar información
relevante. Algunas de las consultas que se podrían realizar son las siguientes:

### Consultas Típicas

- Consulta por título: Buscar libros por su título.
- Consulta por ISBN: Buscar un libro específico mediante su número ISBN.
- Consulta por autor: Obtener todos los libros escritos por un autor en particular.
- Consulta por categoría: Listar libros que pertenecen a una categoría específica.
- Consulta por estado: Filtrar libros según su estado.
- Número total de libros: Contar el total de libros almacenados en la colección.
- Añadir 5 consultas más

## Propuesta de Esquema Relacional

El esquema relacional propuesto considera que algunos campos de los documentos JSON
no son atómicos (es decir, contienen arreglos). La normalización del esquema relacional
ayudará a evitar redundancias y a mantener la integridad de los datos.

### Tablas Propuestas

Libros:

- id: Identificador único
- titulo: Título del libro
- isbn: Número Internacional Normalizado del Libro
- numero_paginas: Número de páginas del libro
- fecha_publicacion: Fecha de publicación del libro
- url_miniatura: URL de la imagen en miniatura del libro
- descripcion_corta: Descripción corta del libro
- descripcion_larga: Descripción larga del libro

Estados:

- id: Identificador único
- libro_id: Referencia al identificador del libro
- estado: Estado del libro

Autores:

- id: Identificador único
- libro_id: Referencia al identificador del libro
- autor: Nombre del autor


Categorías:

- id: Identificador único
- libro_id: Referencia al identificador del libro
- categoria: Nombre de la categoría

## Conclusiones

En conclusión, el presente proyecto final aborda la lectura y almacenamiento de documentos
JSON en una base de datos de MongoDB y la realización de consultas relevantes a la
colección de libros. Además, debe crearse un esquema relacional que normaliza los datos no
atómicos, asegurando la integridad y eficiencia del sistema de base de datos.

## Entrega

Reporte PDF con la descripción del trabajo realizado y cuaderno (notebook) de Jupyter con la
documentación en markdown de las celdas que lo requieran.



