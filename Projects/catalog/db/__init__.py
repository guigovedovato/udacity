#!/usr/bin/env python3
from db.config import open_file
import json


# 'postgresql://vagrant@localhost/catalog_db'
def create_connection(config_type):
    file = open_file(config_type)
    configuration = json.loads(
        open(file, 'r').read())
    return '{}://{}@{}/{}'.format(
        configuration["connection"]["database"],
        configuration["connection"]["user"],
        configuration["connection"]["host"],
        configuration["connection"]["schema"]
    )


DB_CONNECT = create_connection("db_connect")
