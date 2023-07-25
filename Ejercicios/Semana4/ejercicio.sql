
USE DESASTRES
GO

CREATE PROCEDURE p_ETL_Desastres
AS
BEGIN

    TRUNCATE TABLE DESASTRES_BDE.dbo.DESASTRES_FINAL

    INSERT INTO DESASTRES_BDE.dbo.DESASTRES_FINAL
    SELECT  TBL.Cuatrenio,
            AVG(TBL.Temperatura)      AS Temp_AVG,
            AVG(TBL.NivelOxigeno)     AS Oxi_AVG,
            SUM(TBL.Tsunamis)         AS T_Tsunamis,
            SUM(TBL.OlasCalor)        AS T_OlasCalor,
            SUM(TBL.Terremotos)       AS T_Terremotos,
            SUM(TBL.Erupciones)       AS T_Erupciones,
            SUM(TBL.Incendios)        AS T_Incendios,
            AVG(TBL.Muertes_Jovenes)  AS M_Jovenes_AVG,
            AVG(TBL.Muertes_Adultos)  AS M_Adultos_AVG,
            AVG(TBL.Muertes_Ancianos) AS M_Ancianos_AVG
    FROM (
        SELECT  CASE WHEN c.año < 2026 THEN '2023-2026' ELSE '2027-2030' END AS Cuatrenio,
                c.temperatura               AS Temperatura,
                c.oxigeno                   AS NivelOxigeno,
                d.Tsunamis                  AS Tsunamis,
                d.Olas_calor                AS OlasCalor,
                d.Terremotos                AS Terremotos,
                d.Erupciones                AS Erupciones,
                d.Incendios                 AS Incendios, 
                (m.R_Menor15 + m.R_15_a_30) AS Muertes_Jovenes,
                (m.R_30_a_45 + m.R_45_a_60) AS Muertes_Adultos,
                m.R_M_a_60                  AS Muertes_Ancianos
        FROM DESASTRES.dbo.clima c
             JOIN DESASTRES.dbo.desastres d ON (c.año = d.año)
             JOIN DESASTRES.dbo.muertes m ON (c.año = m.año)
        ) TBL
    GROUP BY TBL.Cuatrenio

END
GO

