#!/usr/bin/python2

import psycopg2
import getpass

def configure():
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        return 3

    cur = conn.cursor()

    with open("schema.psql") as schema:
        schema_specification = schema.read()
    
    try:
        cur.execute(schema_specification)
    except:
        return 2

    return 1

