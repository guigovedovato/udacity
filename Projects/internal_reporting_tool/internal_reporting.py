#!/usr/bin/env python3
from db import DB
from file import File


# Example:
# Quais são os três artigos mais populares de todos os tempos?
#  * "Princess Shellfish Marries Prince Handsome" — 1201 views
#  * "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
#  * "Political Scandal Ends In Political Scandal" — 553 views
# 
# Quem são os autores de artigos mais populares de todos os tempos?
#  * Ursula La Multa — 2304 views
#  * Rudolf von Treppenwitz — 1985 views
#  * Markoff Chaney — 1723 views
#  * Contribuidor anônimo — 1023 views
# 
# Em quais dias mais de 1% das requisições resultaram em erros?
#  * July 29, 2016 — 2.5% errors

def job_execute_query(execute_query):

    # Creating instances of File and DB
    file = File()
    db = DB()

    print("Starting log")

    for question in execute_query:
        print("Running query")
        file.write(question, db.execute_query(execute_query[question]))
    
    print("Ending log")

# List of questions and queries
job_execute_query(execute_query = {
    "Quais são os três artigos mais populares de todos os tempos?":
        "SELECT * FROM topthreemostpopulararticles",
    "Quem são os autores de artigos mais populares de todos os tempos?":
        "SELECT * FROM mostpopularauthors",
    "Em quais dias mais de 1% das requisições resultaram em erros?":
        "SELECT * FROM requestswithmorethanonepererror"
})
