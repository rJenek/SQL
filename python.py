import pymysql
from flask import Flask, render_template

connection = pymysql.connect(db='lesson', user='root', passwd='root',
                             unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
cursor = connection.cursor()

app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')


@app.route("/CreateDB", methods=('GET', 'POST'))
def CreateDB():
    print("Придумайте название базы данных")
    name = str(input())

    create_db_query = "CREATE DATABASE " + name
    try:
        cursor.execute(create_db_query)
        print("База данных была успешно созданна")
    except Exception as e:
        print(e)

        connection.close()
    return render_template('index.html')


@app.route("/DeleteDB", methods=('GET', 'POST'))
def DeleteDB():
    print("Напишите название базы данных, которую хотите удалить")
    name = str(input())

    drop_db_query = "DROP DATABASE " + name
    try:
        cursor.execute(drop_db_query)
        print("База данных была успешно удаленна");
    except Exception as e:
        print(e)

        connection.close()
    return render_template('index.html')


@app.route("/CreateTB", methods=('GET', 'POST'))
def CreateTB():
    print("Напишите название таблицы")
    name = str(input())
    print("Напишите название нашей новой колонки")
    name_col = str(input())
    print("Напишите тип данных Например VARCHAR (20)")
    int_col = str(input())

    create_table_query = "CREATE TABLE " + name + "(" + name_col + " " + int_col + ")"
    try:
        cursor.execute(create_table_query)
        print("Таблица была успешно созданно")
    except Exception as e:
        print(e);

        connection.close()
    return render_template('index.html')


@app.route("/DeleteTB", methods=('GET', 'POST'))
def DeleteTB():
    print("Напишите название таблицы которую хотите удалить")
    name = str(input())

    drop_table_query = "DROP TABLE " + name
    try:
        cursor.execute(drop_table_query)
        print("Таблица была успешно удаленна")
    except Exception as e:
        print(e)

        connection.close()
    return render_template('index.html')


@app.route("/ChangeTB", methods=('GET', 'POST'))
def ChangeTB():
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())
    print("Напишите название колонки в которую вы хотите внести изменения")
    name_col = str(input())
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())


@app.route("/SelectTB", methods=('GET', 'POST'))
def SelectTB():
    print("Напишите название таблицы")
    name = str(input())
    print("Напишите название колонки которую вы хотите ипмортировать ")
    print("Если хотите импортировать все данные напишите all")
    name_col = str(input())
    if name_col == 'all':

        import_table_query = "SELECT * FROM " + name
        try:
            cursor.execute(import_table_query)
            print("Данные успешно импортированны")
        except Exception as e:
            print(e)

            connection.close()

        for row in cursor.fetchall():
            print(row)

    else:

        import_table_query = "SELECT  FROM " + name
        try:
            cursor.execute(import_table_query)
            print("Данные успешно импортированны")
        except Exception as e:
            print(e)

            connection.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
