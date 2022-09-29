from pickle import TRUE
import functions as f
import gui

def button_click():
    while TRUE:
        match f.choose_type():
            case '.db':
                f.type_sql()
            case '.txt':
                f.type_txt()
            case '.csv':
                f.type_csv()
            case 'exit':
                return