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
        print("База данных была успешно удаленна")
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
        print(e)

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
    return render_template("index.html")


@app.route("/ChangeTB", methods=('GET', 'POST'))
def ChangeTB():
    print("""Выберите действие:
    1.Добавить колонку
    2.Внести данные в колонку""")
    num = int(input())
    if num == 2:
        print("Напишите название таблицы в которую вы хотите внести изменения")
        name = str(input())
        print("Напишите название колонки куда вы хотите сделать запись")
        name_col = str(input())
        print("Сделайте запись в колонку")
        int_col = str(input())
        change_col_query = "INSERT INTO " + name + " (`" + name_col + "`) VALUES('" + int_col + "');"
        try:
            cursor.execute(change_col_query)
            print("Таблица была успешно изменена")
            print(change_col_query)
        except Exception as e:
            print(e)

            connection.close()

    else:
        print("Напишите название таблицы")
        name = str(input())
        print("Напишите название нашей новой колонки")
        name_col = str(input())
        print("Напишите тип данных. Например VARCHAR(20)")
        int_col = str(input())
        add_col_query = "ALTER TABLE " + name + " ADD COLUMN " + name_col + " " + int_col
        try:
            cursor.execute(add_col_query)
            print("Колонка успешно добавлена")
        except Exception as e:
            print(e)

            connection.close()

    return render_template('index.html')


@app.route("/SelectTB", methods=('GET', 'POST'))
def SelectTB():
    print("""Выберите действие:
        1.Импорт всех данных из тиблицы
        2.Количество записей в таблице""")
    num = int(input())
    if num == 1:
        print("Напишите название таблицы")
        name = str(input())
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
        print("Напишите название таблицы")
        name = str(input())
        import_table_query = "SELECT COUNT(*) FROM " + name
        try:
            cursor.execute(import_table_query)
            print("Данные успешно импортированны")
        except Exception as e:
            print(e)

            connection.close()

        for row in cursor.fetchall():
            print(row)
    return render_template('index.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
