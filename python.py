import pymysql


print("  Выберите действие")
print("1.Создать базу данных")
print("2.Удалить базу данных")
print("3.Создать таблицу")
print("4.Удалить таблицу")
print("5.Внести данные в таблицу")
print("6.Импортировать данные из таблицы")
print("7.Вывести количество записий в таблице")
a = int(input())

if a == 1:
    print("Придумайте название базы данных")
    name = str(input())


    connection = pymysql.connect(db='lesson', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor()

    create_db_query = "CREATE DATABASE " + name
    try:
        cursor.execute(create_db_query)
        print("База данных была успешно созданна")
    except Exception as e:
        print(e)

        connection.close()
elif a==2:
    print("Напишите название базы данных, которую хотите удалить")
    name = str(input())
    connection = pymysql.connect(db='lesson', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor()

    drop_db_query = "DROP DATABASE " + name
    try:
        cursor.execute(drop_db_query)
        print("База данных была успешно удаленна");
    except Exception as e:
        print(e)

        connection.close()

elif a==3:
    print("Напишите название таблицы")
    name = str(input())
    print("Напишите название нашей новой колонки")
    name_col = str(input())
    print("Напишите тип данных Например VARCHAR (20)")
    int_col = str(input())



    connection = pymysql.connect(db='lesson', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor()

    create_table_query = "CREATE TABLE " + name + "(" + name_col + " " + int_col + ")"
    try:
        cursor.execute(create_table_query)
        print("Таблица была успешно удаленна")
    except Exception as e:
        print(e);

        connection.close()
elif a==4:
    print("Напишите название таблицы которую хотите удалить")
    name = str(input())

    connection = pymysql.connect(db='lesson', user='root', passwd='root',  unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor()

    drop_table_query = "DROP TABLE " + name
    try:
        cursor.execute(drop_table_query)
        print("Таблица была успешно удаленна")
    except Exception as e:
        print(e)

        connection.close()
elif a==5:
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())
    print("Напишите название колонки в которую вы хотите внести изменения")
    name_col = str(input())
    print("Напишите название таблицы в которую вы хотите внести изменения")
    name = str(input())
elif a==6:
    print("Напишите название таблицы")
    name = str(input())
    print("Напишите название колонки которую вы хотите ипмортировать ")
    print("Если хотите импортировать все данные напишите all")
    name_col = str(input())
    if name_col == 'all':
        connection = pymysql.connect(db='lesson', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
        cursor = connection.cursor()

        import_table_query = "SELECT * FROM " + name
        try:
            cursor.execute(import_table_query)
            print("Данные успешно импортированны")
        except Exception as e:
            print(e)

            connection.close()

        rows = cursor.execute(import_table_query)
        for row in rows:
            print
            row

        else:
            connection = pymysql.connect(db='lesson', user='root', passwd='root',
                                         unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
            cursor = connection.cursor()

            import_table_query = "SELECT * FROM " + name
            try:
                cursor.execute(import_table_query)
                print("Данные успешно импортированны")
            except Exception as e:
                print(e)

                connection.close()


elif a==7:
    print("");
    name = str(input());
else:
    print("Вы ввели неверное число");
