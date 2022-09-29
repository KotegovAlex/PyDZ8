import hb_functions as f
import gui as g
import handbook_base as hb


   

csv_click()

def csv_index_plus(data) -> int:
    'Find missed index.'
    for i in range(1, len(data)):
        old_index = int(data[i].split(";")[0])
        if old_index != i: break
    return i


def csv_find_to_id(id, data) -> str:
    "In process. Find element to column by column's name."
    for i in range(1, len(data)):
            print(data[i])

def create_csv(data, path_file = 'handbook.csv'):
    'Create a new empty handbook.'
    with open(path_file, 'w', encoding="utf-8") as file:
        file.write(data.replace(' ', ';'))


def csv_header(data) -> str:
    return data[0].split(';')


def csv_read(path_file = 'handbook.csv') -> str:
    with open(path_file, 'r', encoding="utf-8") as csvfile:     
        data = csvfile.readlines()
    return data

def csv_add(data, path_file = 'handbook.csv') -> str:
    'In process. Add record by id.'
    #id = f.csv_index_plus(data)
    #print(id)
    with open(path_file, 'w', encoding="utf-8") as file:
        file.write(f'{csv_header(data)}')
        file.write(f'{data}')
    return data

def csv_del_to_id(id, data) -> str:
    'In process. Delete record by id.'
    for i in range(1, len(data)):
        old_index = int(data[i].split(";")[0])
        if old_index != i: break
    return i