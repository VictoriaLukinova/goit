from collections import UserDict
from dateutil.parser import parse
from datetime import datetime, timedelta
from typing import Optional
import pickle

class Field:
    '''Super class for Name, Phone and Birthday'''
    def __init__(self, value = None) -> None:
        self.__value = None
        if value:
            self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value

    @value.getter
    def value(self) -> str:
        return str(self.__value)

class Name(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str) -> None:
        self.__value = value

    @value.getter
    def value(self) -> str:
        return str(self.__value)

class Phone(Field):
    @property
    def value(self) -> None:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if not isinstance(value, str):
           raise TypeError('Input string')
        elif (value[0] != '+' or len(value) != 13):
            print('Input valid phone in format +380123456789') 
        elif value[1:].isdigit():
            self.__value = value

    @value.getter
    def value(self) -> str:
        return str(self.__value)

class Birthday(Field):
    @property
    def value(self) -> datetime:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = parse(value)

    @value.getter
    def value(self) -> str:
        if self.__value:
            return self.__value

class Record:
    def __init__(self, name: str, phone: Optional[str] = None, birthday: Optional[str] = None) -> None:
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.data = {self.name: self.phones}
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone: str) -> None:
        '''Method for add phone to list'''
        self.phones.append(Phone(phone))

    def delete_phone(self, phone: str) -> None:
        '''Method for delete phone from list'''
        for user_phone in self.phones:
            if user_phone.value == phone:
                self.phones.remove(user_phone)

    def change_phone(self, olden_phone: str, new_phone: str) -> None:
        '''Method for change phone in list'''
        i = 0
        for user_phone in self.phones:
            if user_phone.value == olden_phone:
                self.phones.remove(user_phone)
                self.phones.insert(i, Phone(new_phone))
            i += 1
        
    def days_to_birthday(self) -> int:
        if self.birthday and self.birthday.value:
            today = datetime.now()
            birthday = self.birthday.value
            date_1 = datetime(year= today.year, month= birthday.month, day= birthday.day)
            date_2 = datetime(year= today.year+1, month= birthday.month, day= birthday.day)
            next_birthday = date_1 if date_1 > today else date_2
            difference = next_birthday - today
            return difference.days
        return None

class AddressBook(UserDict):
    def add_record(self, record: Record) -> dict[Name, list[Phone]]:
        self.data.update(record.data)

    def iterator(self, number: int):
        items_list = list(self.data.items())
        yield from (
            items_list[index:index + number]
            for index in range(0, len(items_list), number)
        )
    
    def print_records(self, number: int):
        for records in self.iterator(int(number)):
            for key, value in records:
                name = key.value
                phones_list = [phone.value for phone in value]
                phones = ', '.join(phones_list)
                print(f'{name} {phones}')

    def save_data_to_file(self, filename:str = None) -> None:
        self.filename = filename if filename else 'data.txt'
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    def read_from_file(self, filename:str = None):
        self.filename = filename if filename else 'data.txt'
        with open(self.filename, 'rb') as file:
            decode_obj = pickle.load(file)
        return decode_obj

    def find_in_data(self, string:str):
        for key, value in self.data.items():
            phones = ', '.join([phone.value for phone in value])
            if string in key.value or string in phones:
                print(f'{key.value} {phones}')
