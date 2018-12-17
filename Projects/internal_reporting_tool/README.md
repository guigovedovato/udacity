# Movie Trailer

**Internal Reporting** is an app designed for get reporting from database.

## Requisites

* Download and install [Python](https://www.python.org/downloads/) (v3.7.1)

## Instalation

* Clone/Download repository
* Run internal_reporting.py

## Creating User

```sql
CREATE USER app_user WITH ENCRYPTED PASSWORD '4pp_U$3R';
GRANT ALL PRIVILEGES ON DATABASE news TO app_user;
```

## Creating Views

```sql
-- Quais são os três artigos mais populares de todos os tempos?
-- * "Princess Shellfish Marries Prince Handsome" — 1201 views
CREATE VIEW topthreemostpopulararticles AS
SELECT ar.title, TO_CHAR(COUNT(ar.slug), '999G999') || ' views' AS num
  FROM articles ar
  INNER JOIN log lo on ar.slug = SUBSTRING(lo.path, 10)
  GROUP BY ar.title
  ORDER BY num DESC
  LIMIT 3;

ALTER TABLE topthreemostpopulararticles
  OWNER TO app_user;
```
```sql
-- Quem são os autores de artigos mais populares de todos os tempos?
-- * Ursula La Multa — 2304 views
CREATE VIEW mostpopularauthors AS
SELECT au.name, TO_CHAR(COUNT(ar.slug), '999G999') || ' views' AS num
  FROM articles ar
  INNER JOIN log lo on ar.slug = SUBSTRING(lo.path, 10)
  INNER JOIN authors au on ar.author = au.id
  GROUP BY au.name
  ORDER BY num DESC;

ALTER TABLE mostpopularauthors
  OWNER TO app_user;
```
```sql
-- Em quais dias mais de 1% das requisições resultaram em erros?
-- * July 29, 2016 — 2.5% errors
CREATE VIEW requestswithmorethanonepererror AS
SELECT TO_CHAR(dte :: DATE, 'Mon dd, yyyy') AS date, TO_CHAR(percent,'999D99%') || ' errors' AS percentage FROM (SELECT 
    time::timestamp::date AS dte,
    status,
    ROUND((COUNT(*) / SUM(COUNT(*)) OVER(PARTITION BY time::timestamp::date) ) * 100,2) AS percent 
FROM log
GROUP BY time::timestamp::date, status
ORDER BY percent DESC) AS p
WHERE p.percent > 1 AND status = '404 NOT FOUND'

ALTER TABLE requestswithmorethanonepererror
  OWNER TO app_user;
```