import pymysql

connection = pymysql.connect(db='lesson', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
cursor = connection.cursor()

print("""  Выберите действие
1.Создать базу данных
2.Удалить базу данных
3.Создать таблицу
4.Удалить таблицу
5.Внести данные в таблицу
6.Импортировать данные из таблицы
7.Вывести количество записий в таблице """)
a = int(input())

def create_db():
    print("Придумайте название базы данных")
    name = str(input())

    create_db_query = "CREATE DATABASE " + name
    try:
        cursor.execute(create_db_query)
        print("База данных была успешно созданна")
    except Exception as e:
        print(e)

        connection.close()
def drop_db():
    print("Напишите название базы данных, которую хотите удалить")
    name = str(input())

    drop_db_query = "DROP DATABASE " + name
    try:
        cursor.execute(drop_db_query)
        print("База данных была успешно удаленна");
    except Exception as e:
        print(e)

        connection.close()

def create_table():
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
def drop_table():
    print("Напишите название таблицы которую хотите удалить")
    name = str(input())


    drop_table_query = "DROP TABLE " + name
    try:
        cursor.execute(drop_table_query)
        print("Таблица была успешно удаленна")
    except Exception as e:
        print(e)

        connection.close()
def change_table():
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())
    print("Напишите название колонки в которую вы хотите внести изменения")
    name_col = str(input())
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())
def import_table():
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


def count():
    print("");
    name = str(input());

