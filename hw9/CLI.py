CONTACTS_DICT = {
    'Anna' : '0931111111'
}
IN_CYCLE = True

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

def hello(*arg):
    return 'How can I help you?'

@input_error
def add(command_list):
    global CONTACTS_DICT
    if command_list[1] not in CONTACTS_DICT:
        CONTACTS_DICT.update({command_list[1]: command_list[2]})
        return 'New contact has been added'
    else:
        return f"Contact {command_list[1]} in list!"

@input_error
def change(command_list):
    global CONTACTS_DICT
    CONTACTS_DICT[command_list[1]] = command_list[2]
    return f'Contact {command_list[1]} has been changed'

@input_error
def phone(command_list):
    return CONTACTS_DICT[command_list[1]]

def show_all(*arg):
    global CONTACTS_DICT
    for key, value in CONTACTS_DICT.items():
        print(key, ' : ', value)
    return 'End of contacts'

def exit(*arg):
    global IN_CYCLE
    IN_CYCLE = False
    return "Good bye!"

def command_error(*arg):
    return "Command is not found. Please, try again"

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

def get_handler(command):
    try:
        return COMMAND_DICT[command]
    except KeyError:
        return command_error

def change_command(command): #Обработка команды
    command_list = command.split()
    if command_list[0].lower() == 'show' and command_list[1].lower() == 'all':
        delit = command_list.pop(1)
        command_list[0] = command_list[0] + ' ' + delit
    if command_list[0].lower() == 'good' and command_list[1].lower() == 'bye':
        delit = command_list.pop(1)
        command_list[0] = command_list[0] + ' ' + delit
    command_list[0] = command_list[0].lower()
    # if command_list[0] in ('hello', 'show all', 'exit', 'close', 'good bye'):
    #     if len(command_list) < 3:
    #         command_list.append('')
    #         command_list.append('')
    # if command_list[0] == 'phone' and len(command_list) == 2:
    #     command_list.append('')
    return command_list

def main():
    global IN_CYCLE
    while IN_CYCLE:
        command = input()
        command_list = change_command(command)
        func = get_handler(command_list[0])
        print(func(command_list))

if __name__ == '__main__':
    main()