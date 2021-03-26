import psycopg2

try:
    conn = psycopg2.connect(database="mydb", user="haart",
    password="keen", host="localhost", port=5432)

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO managers (id, name, surname, job_name, department, birthday) VALUES (%s, %s, %s, %s, %s, %s)",
        ("2", "Ольга", "Антонова", "бухгалтер", "бухгалтерия", "02.02.2002"))
    conn.commit()

    cur.execute("SELECT id, name, surname FROM managers")
    for row in cur:
        print(row)
    cur.fetchone()
    cur.close()
except:
    print('ошибка работы с базой')
finally:
    conn.close()





