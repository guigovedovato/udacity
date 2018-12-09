from db import DB
from file import File


questions_queries = {
    "Quais são os três artigos mais populares de todos os tempos?":
        "SELECT * FROM authors",
    "Quem são os autores de artigos mais populares de todos os tempos?":
        "SELECT * FROM authors",
    "Em quais dias mais de 1% das requisições resultaram em erros?":
        "SELECT * FROM authors"
}

def main():
    for item in questions_queries:
        file = File()
        file.write(item)
        print(item)
        db = DB("news")
        result = db.execute_query(questions_queries[item])
        file.write(result)
        print(result)

main()