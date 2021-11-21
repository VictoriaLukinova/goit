from collections import UserDict
from datetime import datetime, timedelta

class Field:
    '''Super class for Name and Phone'''
    def __init__(self) -> None:
        self.__value = None

class Name(Field):
    def __init__(self, name:str) -> None:
        self.__value = name

class Phone(Field):
    def __init__(self, value = None) -> None:
        self.__value = None
        if value:
            self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if (type(value) != str or len(value) != 12):
            print('Input valid phone') 
        if value.isdigit():
            self.__value = value

    @value.getter
    def value(self):
        return f'Value is {self.__value}'

class Birthday(Field):
    def __init__(self, value = None) -> None:
        self.__value = None
        if value:
            self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        try:
            self.__value = datetime.strptime(self.birthday, '%d.%m.%Y')
        except ValueError:
            print('Input valid date')

    @value.getter
    def value(self):
        return f'Value is {self.__value}'


class Record:
    def __init__(self, name: Name, phone: Phone, birthday = '') -> None:
        self.name = name
        self.phones = [phone]
        self.data = {self.name: self.phones}
        self.birthday = birthday

    def add_phone(self, phone: str) -> None:
        '''Method for add phone to list'''

    def delete_phone(self):
        '''Method for delete phone from list'''

    def change_phone(self):
        '''Method for change phone in list'''

    def days_to_birthday(self) -> int:
        if self.birthday:
            today = datetime.now()
            birthday = datetime.strptime(self.birthday, '%d.%m.%Y')
            if today.month > birthday.month or (today.month == birthday.month and today.day > birthday.day):
                birthday_year = today.year + 1
            else:
                birthday_year = today.year
            next_birthday = datetime(year= birthday_year, month= birthday.month, day= birthday.day, hour= 0)
            difference = birthday - today
            return difference.days
        return None

class AddressBook(UserDict):
    def add_record(self, record: Record) -> dict[str, list]:
        self.data.update(record.data)

    def iterator(self, n: int):
        pass