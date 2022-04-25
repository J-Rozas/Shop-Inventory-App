from db.run_sql import run_sql

from models.publisher import Publisher

def select_all():
    list_of_publishers = []

    sql = "SELECT * FROM publishers"

    all_publishers = run_sql(sql)

    for element in all_publishers:
        publisher = Publisher(element["name"], element["country"], element["address"], element["id"])
        list_of_publishers.append(publisher)

    return list_of_publishers