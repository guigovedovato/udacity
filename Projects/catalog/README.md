# Catalog App

**Catalog App** is an application designed to manage a list of items in a variety of categories. This project consists of:
* The home page displays all current categories next to recently added items.
* Selecting a specific category shows all available items for that category.
* Selecting a specific item shows specific information about that item.
* After logging in, a user has the ability to add, update, or remove information about their own items.
* To run the program successfully, it is requested:
    * Please, see [Requirements](#requirements) for requirements of this project;
    * How to install in [Instalation](#Instalation) section;
    * Setup database [Setup Database](#setup-database) section;
    * How to execute the app in [Execution](#execution) section;
    * See the Application in [Application](#application) section;

## Requirements

* Download and install [Python](https://www.python.org/downloads/) (v3.7.1)
* Download and install [PostgreSQL](https://www.postgresql.org/download/)
* Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
* Download and install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* Create your own OAuth 2.0 client IDs [Google Developers](https://console.developers.google.com)

## Instalation

* Clone/Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
* Clone/Download this repository and *copy and paste* all content of **catalog** to the same in *fullstack-nanodegree-vm*
* Create the file **client_secrets.json** and insert your own *Google API Credentials*

## Setup Database

* Create *catalog_db* database
```sql
psql -d catalog_db -f create_database.sql
```

* Create Tables
```
python database_setup.py
```

* Load initial data
```
python load_data.py
```

## Execution

* Start the Vagrant VM
* Run the *python script* application.py
```
python application.py
```

## Application

* Open the *browser* and go to http://localhost:8000 or [click here](http://localhost:8000)
