--
-- Creating Database catalog_db
--

CREATE DATABASE catalog_db
  WITH OWNER = vagrant
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       CONNECTION LIMIT = -1;

GRANT ALL PRIVILEGES
    ON DATABASE catalog_db TO vagrant;
