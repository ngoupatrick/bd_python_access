from sqlite3 import sqlite_version
import psycopg2  # type:ignore

params = {
    "user": "xrlwwavp",
    "password": "QR8Lt78vwZU5ivofDlJ3Owvj-_OxMwJP",
    "host": "abul.db.elephantsql.com",
    "port": "5432",
    "database": "xrlwwavp"
}

SQL_VERSION = "SELECT version();"

SQL_CREATE_TABLE = '''CREATE TABLE person(
        ID SERIAL PRIMARY KEY,
        name TEXT NOT NULL
      ); '''

SQL_SELECT = 'SELECT * FROM person'

SQL_INSERT = 'INSERT INTO person (ID,name) VALUES (%s,%s)'
SQL_INSERT_VALUE = (2, 'SYLLA')

# FONCTION DE TEST DE CONNEXION À LA BASE DE DONNÉES


def test_connexion_bd():
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Afficher la version de PostgreSQL
        cur.execute(SQL_VERSION)
        version = cur.fetchone()
        print("Version : ", version, "\n")

        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à PostgreSQL", error)

# FONCTION DE CREATION DE LA BASE DE DONNÉES


def create_table(SQL):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(SQL)
        conn.commit()
        print("Table créée avec succès dans PostgreSQL")

        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création du table PostgreSQL", error)

# FONCTION DE SELECTION DES DONNÉES


def select_sql(SQL):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(SQL)
        print("Sélectionner des lignes dans la table person")
        res = cur.fetchall()

        for row in res:
            print("Id = ", row[0], )
            print("Name = ", row[1])

        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors du sélection à partir de la table person", error)

# FONCTION D'INSERTION DES DONNÉES


def insert_sql(SQL, VALUE):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(SQL, VALUE)
        conn.commit()
        count = cur.rowcount
        print(count, "enregistrement inséré avec succès dans la table person.")

        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de l'insertion dans la table person", error)


if __name__ == "__main__":
    # test de connexion
    test_connexion_bd()

    # creation de table, le faire qu'une fois
    # create_table(SQL=SQL_CREATE_TABLE)

    # insertion des données
    #insert_sql(SQL=SQL_INSERT, VALUE=SQL_INSERT_VALUE)

    # Sélection des données
    select_sql(SQL=SQL_SELECT)
