# Internal Reporting

**Internal Reporting** is an app designed for get reporting from PostgreSQL database. 


## Requisites

* Download and install [Python](https://www.python.org/downloads/) (v3.7.1)
* Download and unpack [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Instalation

* Clone/Download repository
* Import *news* database
```sql
psql -d news -f newsdata.sql
```

## Execution

* Run 
```
python internal_reporting.py
```

## Creating Views

* Execute the script create_views.sql
```sql
psql -d news -f create_views.sql
```
