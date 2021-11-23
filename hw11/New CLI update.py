from collections import UserDict
from datetime import datetime, timedelta
from typing import Optional

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
    def value(self):
        return f'Value is {self.__value}'

class Name(Field):
    @property
    def value(self):
        return self.__value
        
    @value.getter
    def value(self):
        return f'Name is {self.__value}'

class Phone(Field):
    @property
    def value(self) -> None:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if (type(value) != str or len(value) != 12):
            print('Input valid phone in format 380123456789') 
        if value.isdigit():
            self.__value = value

    @value.getter
    def value(self) -> None:
        return f'Phone is {self.__value}'

class Birthday(Field):
    @property
    def value(self) -> None:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        try:
            self.__value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            print('Input valid date in format dd.mm.YYYY')

    @value.getter
    def value(self) -> None:
        return f'Birthday is {self.__value}'

class Record:
    def __init__(self, name: Name, phone: Phone, birthday: Optional[Birthday] = None) -> None:
        self.name = name
        self.phones = [phone]
        self.data = {self.name: self.phones}
        self.birthday = birthday

    def add_phone(self, phone: Phone) -> None:
        '''Method for add phone to list'''
        self.phones.append(phone)

    def delete_phone(self, phone: Phone) -> None:
        '''Method for delete phone from list'''
        try:
            self.phones.remove(phone)
        except ValueError:
            print('Phone not in list')

    def change_phone(self, olden_phone: Phone, new_phone: Phone) -> None:
        '''Method for change phone in list'''
        i = self.phones.index(olden_phone)
        olden_phone = self.phones.pop(i)
        self.phones.insert(i, new_phone)
        
    def days_to_birthday(self) -> int:
        if self.birthday:
            today = datetime.now()
            birthday = self.birthday
            if today.month > birthday.month or (today.month == birthday.month and today.day > birthday.day):
                birthday_year = today.year + 1
            else:
                birthday_year = today.year
            next_birthday = datetime(year= birthday_year, month= birthday.month, day= birthday.day, hour= 0)
            difference = next_birthday - today
            return difference.days
        return None

class AddressBook(UserDict):
    def add_record(self, record: Record) -> dict[str, list]:
        self.data.update(record.data)

    def get_iterator(self):
        for key in self.data:
            yield f'Name: {key}, phones: {self.data[key]}'

    def iterator(self, n: int):
        gen = self.get_iterator()
        for _ in range(n):
            print(next(gen))
