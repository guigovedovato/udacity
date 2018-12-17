# Internal Reporting

**Internal Reporting** is an app designed for get reporting from database. This project consists of:
* Connecting to the *news* database via **vagrant** user
* Running views to view reports and answer these questions:
    * "Quais são os três artigos mais populares de todos os tempos?"
    * "Quem são os autores de artigos mais populares de todos os tempos?"
    * "Em quais dias mais de 1% das requisições resultaram em erros?"
* To run the program successfully, it is requested:
    * Please, see [Requirements](#requirements) for requirements of this project;
    * How to install in [Instalation](#Instalation) section;
    * The views used for questions in [Creating Views](#creating-views) section;
    * How to execute the app in [Execution](#execution) section;
    * The result of queries in [Result](#result) section;

## Requirements

* Download and install [Python](https://www.python.org/downloads/) (v3.7.1)
* Download and install [PostgreSQL](https://www.postgresql.org/download/)
* Download and unpack [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Instalation

* Clone/Download repository
* Import *news* database
```sql
psql -d news -f newsdata.sql
```

## Creating Views

* Run the *SQL script* create_views.sql
```sql
psql -d news -f create_views.sql
```

## Execution

* Run the *python script* internal_reporting.py
```
python internal_reporting.py
```

## Result

* The result of the report is written on result.txt file
