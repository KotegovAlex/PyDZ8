# Добавление записи:
def add_new_data(data):
    with open('handbook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

# Считывание базы данных из .txt
def read_base():
    with open('handbook.txt', 'r', encoding="utf-8") as file:     
        data = file.readlines()
    data = [data[i][:-1].split('**') for i in range(len(data))]
    data = [data[i][1:-1] for i in range(len(data))]
    return data

# Удаление записи из базы данных .txt 
def delete_data(id, data):    
    data = ['**'.join(data[i]) for i in range(len(data)) if int(data[i][0]) != int(id)]
    with open('handbook.txt', 'w', encoding="utf-8") as file:
        for i in range(len(data)):
            file.write(f'**{data[i]}**\n')