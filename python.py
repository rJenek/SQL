import pymysql

print("    Выберите действие");
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
    connection = pymysql.connect(db='mydb', user='root', passwd='root', unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    cursor = connection.cursor();

    delete_existing_table = "drop table if exists name ";
    create_table_query = """create table name()""";


    try:
        cursor.execute( delete_existing_table );
        print("Существующая таблица была удаленна")
        cursor.execute(create_table_query);
        print("Таблица была успешно созданна");
    except Exception as e:
        print(e);

        connection.close()
elif a==2:
    print("Напишите название базы данных, которую хотите удалить");
    name = input(chr());
elif a==3:
    print("сколько");
    print("Напишите название таблицы");
    print("Напишите название таблицы");


elif a==4:
    print("");
elif a==5:
    print("Через пробел напишете название таблицы ");
    name = input(chr());
elif a==6:
    print("");
elif a==7:
    print("");
else:
    print("Вы ввели неверное число");
