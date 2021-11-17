CONTACTS_DICT = {
    'Anna' : '0931111111'
}

def input_error(func):
    def inner(command_list):
        global CONTACTS_DICT
        try:
            return func(command_list)
        except KeyError:
            return 'Give me a valid name'
        except ValueError:
            return 'Give me a name and phone please!'
        except IndexError:
            return 'Give me a name and phone please'
    return inner

def hello(*arg) -> str:
    return 'How can I help you?'

@input_error
def add(name: str, phone: str) -> str:
    global CONTACTS_DICT
    if name not in CONTACTS_DICT:
        CONTACTS_DICT.update({name: phone})
        return 'New contact has been added'
    else:
        return f"Contact {name} in list!"

@input_error
def change(name: str, phone: str) -> str: 
    global CONTACTS_DICT
    CONTACTS_DICT[name] = phone
    return f'Contact {name} has been changed'

@input_error
def phone(name: str, phone: str) -> str :
    return CONTACTS_DICT[name]

def show_all(*arg) -> str:
    global CONTACTS_DICT
    for key, value in CONTACTS_DICT.items():
        print(key, ' : ', value)
    return 'End of contacts'

def exit(*arg) -> str:
    return "Good bye!"

COMMAND_DICT ={
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'exit': exit,
    'close': exit,
    'good bye': exit
}

def get_command_set(string:str) -> set: #Обработка команды
    command_list = string.split() 
    if len(command_list) == 0:
        return('', '', '')   
    if command_list[0].lower() == 'show' and command_list[1].lower() == 'all':
        delete = command_list.pop(1)
        command_list[0] = command_list[0] + ' ' + delete
    if command_list[0].lower() == 'good' and command_list[1].lower() == 'bye':
        delete = command_list.pop(1)
        command_list[0] = command_list[0] + ' ' + delete
    command = command_list[0].lower()
    try:
        name = command_list[1]
    except IndexError:
        name = ''
    try:
        phone = command_list[2]
    except IndexError:
        phone = ''
    return (command, name, phone)

def main():
    command = ''
    while command not in ('exit', 'close', 'good bye'):
        string = input()
        command, name, phone = get_command_set(string)
        try:
            func = COMMAND_DICT[command]
        except KeyError:
            func = None
            print("Command is not found. Please, try again")
        if func:
            print(func(name, phone))

if __name__ == '__main__':
    main()
