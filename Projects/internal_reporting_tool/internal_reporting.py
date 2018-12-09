#!/usr/bin/env python3
from db import DB
from file import File


# List of questions and queries
questions_queries = {
    "Quais são os três artigos mais populares de todos os tempos?":
        "SELECT * FROM authors",
    "Quem são os autores de artigos mais populares de todos os tempos?":
        "SELECT * FROM authors",
    "Em quais dias mais de 1% das requisições resultaram em erros?":
        "SELECT * FROM authors"
}

def main():

    # Creating instances of File and DB
    file = File()
    db = DB("news")

    for question in questions_queries:
        file.write(question, db.execute_query(questions_queries[question]))

main()