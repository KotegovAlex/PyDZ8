import functions as f
import db
import gui

def button_click():
    handbook_temp = db.read_base()
    while True:
        match gui.get_operation():
            case 'new':
                db.add_new_data(f.new_data(f.new_id(handbook_temp), 
                                            gui.get_lname(), 
                                            gui.get_fname(), 
                                            gui.get_phone_num()))
                print('Запись успешно добавлена!')
            case 'del':
                db.delete_data(gui.get_id(), handbook_temp)
                print('Запись успешно удалена!')
            case 'find':
                print(f.find(gui.get_lname(), handbook_temp))
            case 'exit':
                break