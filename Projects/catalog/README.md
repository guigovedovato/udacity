# Catalog App

**Catalog App** is an application designed to manage a list of items in a variety of categories. This project consists of:
* The home page displays all current categories next to recently added items.
* Selecting a specific category shows all available items for that category.
* Selecting a specific item shows specific information about that item.
* After logging in, a user has the ability to add, update, or remove information about their own items.
* To run the program successfully, it is requested:
    * Please, see [Requirements](#requirements) for requirements of this project;
    * How to install in [Instalation](#Instalation) section;
    * Creating database [Creating Database](#creating-database) section;
    * How to execute the app in [Execution](#execution) section;
    * See the Application in [Application](#application) section;

## Requirements

* Download and install [Python](https://www.python.org/downloads/) (v3.7.1)
* Download and install [PostgreSQL](https://www.postgresql.org/download/)
* Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
* Download and install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

## Instalation

* Clone/Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
* Clone/Download this repository and *copy and paste* all content of **catalog** to the same in *fullstack-nanodegree-vm*

## Creating Database

* Create *catalog_db* database and tables
```sql
psql -d catalog_db -f create_database.sql
```

* Create views
```sql
psql -d catalog_db -f create_views.sql
```

* Load initial data
```sql
psql -d catalog_db -f load_data.sql
```

## Execution

* Start the Vagrant VM
* Run the *python script* application.py
```
python application.py
```

## Application

* Open the *browser* and go to http://localhost:8000 or [click here](http://localhost:8000)
