from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            ph = Phone(phone)
            self.phones.append(ph)
        except ValueError:
            return ph

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def remove_phone(self, phone):
        try:
            self.phones.remove(self.find_phone(phone))
        except ValueError:
            return None

    def edit_phone(self, old_phone: str, new_phone: str):
        ph = self.find_phone(old_phone)
        if ph:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            return "Phone not found."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record  # self[record.name.value]
        return record

    def find(self, name: str):
        return self.data.get(name)  # return self.get(name) error не будет:UserDict

    def delete(self, name: str):
        if self.find(name):
            del self.data[name]

    # Створення нової адресної книги

#
# book = AddressBook()
#
# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# # Додавання запису John до адресної книги
# book.add_record(john_record)
#
# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
#
# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)
#     # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
#
# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
#
# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
#
# # Видалення запису Jane
# book.delete("Jane")
