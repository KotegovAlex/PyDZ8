import db.db_sql as dbs
import db.db_txt as dbt
import db.db_csv as dbc
import gui

# Выбор файла для работы:
def choose_type():
    return input('Введите тип файла для работы (.txt, .db, .csv или exit): ')

# Выбран тип .db
def type_sql():
    print('Для работы выбран тип .db')
    dbs.init()
    while True:
        match gui.get_func():
            case 'new':
                dbs.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_birth_date(),
                                    gui.get_phone_num())                
            case 'new_number':
                dbs.add_new_number(gui.get_phone_num(), gui.get_id())                
            case 'read':
                dbs.read_base()                
            case 'del':
                dbs.del_data(gui.get_id())                
            case 'find':
                dbs.find_data(gui.get_lname())                
            case 'edit':
                operation = gui.get_operation()
                match operation:
                    case 'fname':
                        attribute = gui.get_fname()
                    case 'lname':
                        attribute = gui.get_lname()
                    case 'birth_date':
                        attribute = gui.get_birth_date()
                    case 'number':
                        attribute = gui.get_phone_num()            
                dbs.edit_data(operation, gui.get_id(), attribute)
            case 'exit':
                dbs.close()
                return

# Выбран тип .txt
def type_txt():
    print('Для работы выбран тип .txt')
    while True:
        match gui.get_func():
            case 'new':
                dbt.add_new_data(gui.get_fname(), 
                                    gui.get_lname(),
                                    gui.get_birth_date(),
                                    gui.get_phone_num())                
            case 'new_number':
                dbt.add_new_number(gui.get_phone_num(), gui.get_id())                
            case 'read':
                dbt.read_base()                
            case 'del':
                dbt.del_data(gui.get_id())                
            case 'find':
                dbt.find_data(gui.get_lname())                
            case 'edit':
                operation = gui.get_operation()
                match operation:
                    case 'fname':
                        attribute = gui.get_fname()
                    case 'lname':
                        attribute = gui.get_lname()
                    case 'birth_date':
                        attribute = gui.get_birth_date()
                    case 'number':
                        attribute = gui.get_phone_num()            
                dbt.edit_data(operation, gui.get_id(), attribute)
            case 'exit':
                return

# Выбран тип .csv
def type_csv():
    print('Для работы выбран тип .csv')

