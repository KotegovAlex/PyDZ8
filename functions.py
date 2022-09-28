def new_data(id, lname, fname, phone_number):
    return '**'.join([id, lname, fname, phone_number])

def new_id(handbook):
    id_temp = [handbook[i][0] for i in range(len(handbook))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)

def find(lname, handbook):
    lname_list = [handbook[i] for i in range(len(handbook)) if handbook[i][1] == lname]
    return lname_list