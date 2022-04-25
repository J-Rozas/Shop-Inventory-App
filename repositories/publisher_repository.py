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


def add(publisher):
    sql = "INSERT INTO publishers (name, country, address) VALUES (%s, %s, %s) RETURNING id"
    values = [publisher.name, publisher.country, publisher.address]

    result = run_sql(sql, values)

    id = result[0]["id"]

    publisher.id = id


def delete(id):
    sql = "DELETE FROM publishers WHERE id = %s"
    values = [id]

    run_sql(sql, values)


def select(id):
    sql = "SELECT * FROM publishers WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]

    return result


def update(publisher):
    sql = "UPDATE publishers SET name = %s, country = %s, address = %s WHERE id = %s"
    values = [publisher.name, publisher.country, publisher.address, publisher.id]

    run_sql(sql, values)