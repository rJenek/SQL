import pymysql

print("  Выберите действие");
print("1.Создать базу данных");
print("2.Удалить базу данных");
print("3.Создать таблицу");
print("4.Удалить таблицу");
print("5.Внести данные в таблицу");
print("6.Импортировать данные из таблицы");
print("7.Вывести количество записий в таблице");
a = int(input());

if a == 1:
    print("Придумайте название базы данных");
    name = str(input());


    connection = pymysql.connect(db='mysql', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor();

    create_db_query = "CREATE DATABASE (`name`) VALUES (%s)"
    try:
        cursor.execute(create_db_query, (('name')));
        print("База данных была успешно созданна");
    except Exception as e:
        print(e);

        connection.close()
elif a==2:
    print("Напишите название базы данных, которую хотите удалить");
    name = str(input());
    connection = pymysql.connect(db='mydb', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor();

    create_table_query = "DROP DATABASE {name}";
    try:
        cursor.execute(create_table_query);
        print("База данных была успешно удаленна");
    except Exception as e:
        print(e);

        connection.close()

elif a==3:
    print("Напишите название таблицы");
    name = str(input());

    connection = pymysql.connect(db='mydb', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor();

    create_table_query = "CREATE TABLE {name}";
    try:
        cursor.execute(create_table_query);
        print("База данных была успешно удаленна");
    except Exception as e:
        print(e);

        connection.close()
elif a==4:
    print("Напишите название таблицы которую хотите удалить");
    name = str(input());

    connection = pymysql.connect(db='mydb', user='root', passwd='root',
                                 unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor();

    delete_table_query = "DROP TABLE VALUES ('name')"
    try:
        cursor.execute(delete_table_query);
        print("Таблица была успешно удаленна");
    except Exception as e:
        print(e);

        connection.close()
elif a==5:
    print("");
    name = str(input());
elif a==6:
    print("");
    name = str(input());
elif a==7:
    print("");
    name = str(input());
else:
    print("Вы ввели неверное число");
