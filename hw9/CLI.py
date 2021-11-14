import collections

CONTACTS_DICT = {
    'Anna' : '0931111111'
}
Command_list = collections.namedtuple('Command_list',['command', 'name', 'phone',])

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
def add(command_list: Command_list) -> str:
    global CONTACTS_DICT
    if command_list.name not in CONTACTS_DICT:
        CONTACTS_DICT.update({command_list.name: command_list.phone})
        return 'New contact has been added'
    else:
        return f"Contact {command_list.name} in list!"

@input_error
def change(command_list: Command_list) -> str: 
    global CONTACTS_DICT
    CONTACTS_DICT[command_list.name] = command_list.phone
    return f'Contact {command_list.name} has been changed'

@input_error
def phone(command_list: Command_list) -> str :
    return CONTACTS_DICT[command_list.name]

def show_all(*arg) -> str:
    global CONTACTS_DICT
    for key, value in CONTACTS_DICT.items():
        print(key, ' : ', value)
    return 'End of contacts'

def exit(*arg) -> str:
    return "Good bye!"

def command_error(*arg) -> str:
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

def get_handler(command: str):
    try:
        return COMMAND_DICT[command]
    except KeyError:
        return command_error

def change_command(command:str) -> Command_list: #Обработка команды
    commands = command.split()
    if len(commands) == 0:
        command_list = Command_list('', '', '')
        return command_list    
    if commands[0].lower() == 'show' and commands[1].lower() == 'all':
        delete = commands.pop(1)
        commands[0] = commands[0] + ' ' + delete
    if commands[0].lower() == 'good' and commands[1].lower() == 'bye':
        delete = commands.pop(1)
        commands[0] = commands[0] + ' ' + delete
    commands[0] = commands[0].lower()
    if len(commands) == 1:
        command_list = Command_list(commands[0], '', '')
    elif len(commands) == 2:
        command_list = Command_list(commands[0], commands[1], '')
    elif len(commands) >= 3:
        command_list = Command_list(commands[0], commands[1], commands[2])
    return command_list

def main():
    while True:
        command = input()
        command_list = change_command(command)
        func = get_handler(command_list.command)
        print(func(command_list))
        if command_list.command in ('exit', 'close', 'good bye'):
            return

if __name__ == '__main__':
    main()
