
CREATE DATABASE escuela;

CREATE TABLE cursos(
    codigo CHAR(6) NOT NULL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    clase TINYINT(1) NOT NULL
);


