import sqlite3

conn = sqlite3.connect("data_base.db")
cursor = conn.cursor()


def examination(user_id, nickname):
    sql = "SELECT user_id FROM main"
    q = cursor.execute(sql).fetchall()
    users_ids = []
    for i in q:
        users_ids.append(i[0])

    if user_id not in users_ids:
        sql = 'SELECT id FROM main'
        try:
            id = cursor.execute(sql).fetchall()[-1]
            cursor.execute(f"""INSERT INTO main(id, nickname, user_id, score)
                            VALUES ({id[0] + 1}, '{nickname}', {user_id}, 0)""")
            conn.commit()
        except IndexError:
            cursor.execute(f"""INSERT INTO main(id, nickname, user_id, score)
                VALUES ({1}, '{nickname}', {user_id}), 0""")
            conn.commit()


def take_all_users_id():
    sql = "SELECT user_id FROM main"
    q = cursor.execute(sql).fetchall()
    users_ids = []
    for i in q:
        users_ids.append(i[0])

    return users_ids


def new_note(user_id, note):
    sql = 'SELECT id FROM notebook'
    note = note
    try:
        id = cursor.execute(sql).fetchall()[-1]
        cursor.execute(f"""INSERT INTO notebook(id, user, note)
                        VALUES({id[0] + 1}, {user_id}, '{note}')""")
        conn.commit()
    except IndexError:
        cursor.execute(f"""INSERT INTO notebook(id, user, note)
                                VALUES(1, {user_id}, '{note}')""")
        conn.commit()


def note():
    return None