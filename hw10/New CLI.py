from collections import UserDict

class Field:
    '''Super class for Name and Phone'''

class Name(Field):
    def __init__(self, name:str) -> None:
        self.value = name

class Phone(Field):
    value = ''

class Record:
    def __init__(self, name: Name, phone: Phone) -> None:
        self.name = name
        self.phones = [phone]

    def add_phone():
        '''Method for add phone to list'''

    def delete_phone():
        '''Method for delete phone from list'''

    def change_phone():
        '''Method for change phone in list'''

class AddressBook(UserDict):
    def add_record(self, record: Record) -> dict[str, list]:
        self.data.update(record)