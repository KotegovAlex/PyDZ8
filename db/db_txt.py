# Добавление новой записи:
def add_new_data(fname, lname, birth_date, number):
    with open(r'db\handbook.txt', 'r', encoding="utf-8") as file:     
        data = file.readlines()
    read_data = [data[i][2:-3] for i in range(len(data))]
    read_data = [data[i].split('; ') for i in range(len(data))]
    id = int(read_data[len(data) - 1][0]) + 1

    data = id + '; ' + fname + '; ' + lname + '; ' + birth_date + '; ' + number
    with open(r'db\handbook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

# Новый номер:
def add_new_number(data, id):
    pass
    # print('Номер успешно добавлен!')

# Считывание базы данных:
def read_base():
    with open(r'db\handbook.txt', 'r', encoding="utf-8") as file:     
        data = file.readlines()
    data = [data[i][:-1].split('; ') for i in range(len(data))]
    data = [data[i][1:-1] for i in range(len(data))]
    print(data)
    print('Считывание завершено!')

# Удаление записи:
def delete_data(id, data):   
    pass 
    # data = ['**'.join(data[i]) for i in range(len(data)) if int(data[i][0]) != int(id)]
    # with open(r'db\handbook.txt', 'w', encoding="utf-8") as file:
    #     for i in range(len(data)):
    #         file.write(f'**{data[i]}**\n')
    # print('Запись успешно удалена!')

# Поиск записей:
def find_data(data):  
    pass  
    # try:
    #     result = cur.execute("SELECT * FROM people WHERE lname == ?;", (data,)).fetchall()
    #     print('Найдено:')
    #     print(result)
    #     print('Поиск завершен!')
    # except sql.Error as error:
    #     print("Ошибка при работе с SQLite", error)

# Редактирование записи:
def edit_data(operation, id, data):
    pass
    # try:
    #     match operation:
    #         case 'number':
    #             cur.execute("UPDATE phone_number SET number = ? WHERE people_id == ?", (data, id))    
    #         case 'lname':
    #             cur.execute("UPDATE people SET lname = ? WHERE people_id == ?", (data, id))
    #         case 'fname':
    #             cur.execute("UPDATE people SET fname = ? WHERE people_id == ?", (data, id))
    #         case 'birth_date':
    #             cur.execute("UPDATE people SET birth_date = ? WHERE people_id == ?", (data, id))           
    #     handbook.commit()
    #     print('Запись успешно отредактирована!')
    # except sql.Error as error:
    #     print("Ошибка при работе с SQLite", error)