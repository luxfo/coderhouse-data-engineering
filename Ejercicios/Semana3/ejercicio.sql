-- Create Databases
CREATE DATABASE BDE;
GO
CREATE DATABASE BDE_DW;
GO

-- Use BDE
USE BDE  
GO
-- Create schema
CREATE SCHEMA articulos AUTHORIZATION dbo;
GO
-- Create table titulos
CREATE TABLE articulos.titulos (
    id          int NOT NULL,
    nombre      varchar(50) NOT NULL,
    tipo        varchar(20) NOT NULL,
    autor_id    int NOT NULL
);
GO
-- Insert values
INSERT INTO articulos.titulos
VALUES (1, 'Oracle', 'bbdd', 3);
INSERT INTO articulos.titulos
VALUES (2, 'Sql Server', 'bbdd', 5);
INSERT INTO articulos.titulos
VALUES (3, 'NodeJs', 'framework', 2);
INSERT INTO articulos.titulos
VALUES (4, 'Python', 'dev', 4);
INSERT INTO articulos.titulos
VALUES (5, 'BigQuery', 'BI', 6);
INSERT INTO articulos.titulos
VALUES (6, 'Javascript', 'dev', 1);

-- Create table autores
CREATE TABLE articulos.autores (
    id          int NOT NULL,
    nombre      varchar(100) NOT NULL,
    apellido    varchar(100) NOT NULL,
    telefono    varChar(16)
);
-- Insert values
INSERT INTO articulos.autores
VALUES (1, 'Luciano', 'Perez', '1122334455');
INSERT INTO articulos.autores
VALUES (2, 'Cesar', 'Rodriguez', '1155443322');
INSERT INTO articulos.autores
VALUES (3, 'Pedro', 'Fernandez', '1166778899');
INSERT INTO articulos.autores
VALUES (4, 'Cristina', 'Garcia', '1199887766');
INSERT INTO articulos.autores
VALUES (5, 'Gabriela', 'Gonzalez', '1156789722');
INSERT INTO articulos.autores
VALUES (6, 'Monica', 'Martinez', '1198761234');

-- Create Table DimTitulo
USE BDE_DW 
GO

CREATE TABLE dbo.DimTitulos(
    titulo_id       int NOT NULL,
    titulo_nombre   varchar(50) NOT NULL,
    titulo_tipo     varchar(20) NOT NULL,
    autor_nombre    varchar(200),
    autor_telefono  varchar(16)
);
GO

-- Create SP
USE BDE
GO

CREATE PROCEDURE p_ETL_Insertar_DimTitulo
AS
BEGIN

    TRUNCATE TABLE BDE_DW.dbo.DimTitulos;
    
    INSERT INTO BDE_DW.dbo.DimTitulos
    SELECT  t.titulo_id,
            t.titulo,
            CASE t.tipo
                 WHEN 'bbdd' THEN 'Base de datos'
                 WHEN 'BI' THEN 'BI Analitica'
                 WHEN 'frameworks' THEN 'Frameworks'
                 WHEN 'dev' THEN 'Desarrollo'
                 ELSE t.tipo
            END,
            a.nombre + ' ' + a.apellido,
            a.telefono
    FROM BDE.articulos.titulos as t
    JOIN BDE.articulos.autores as a ON t.autor_id = a.id

END

GO

-- Execute SP
EXECUTE p_ETL_Insertar_DimTitulo;
GO

