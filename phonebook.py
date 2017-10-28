import csv
import json
from configparser import RawConfigParser


class PhoneBook:

    def __init__(self, database):
        try:
            self.data = database.read()
        except FileNotFoundError:
            self.data = {}

    def create(self, name, phone):
        if not self.data:
            self.data = {name: phone}
        self.data[name] = phone
        db.write(self.data)
        return self.data

    def retrieve(self, name=None):
        if name:
            return self.data[name]
        return self.data

    def update(self, name, new_phone):
        self.data[name] = new_phone
        db.write(self.data)
        return self.data[name]

    def delete(self, name):
        del self.data[name]
        db.write(self.data)
        return self.data


class Controller:

    def get_action(self, action, phonebook):

        if action == '1':
            name = input('Name ')
            phone = input('Phone ')
            print(phonebook.create(name, phone))

        elif action == '2':
            name = input('Name ')
            print(phonebook.retrieve(name))

        elif action == '3':
            name = input('Name ')
            new_phone = input('New Phone ')
            print(phonebook.update(name, new_phone))

        elif action == '4':
            name = input('Name ')
            print(phonebook.delete(name))

        elif action == '5':
            raise KeyboardInterrupt('Exit')

    def read_config(self):
        config = RawConfigParser()
        config.read('config.ini')

        file_name = config.get('File', 'filename')
        file_extension = config.get('File', 'extension')

        return file_name, file_extension


class JsonHandler:

    def __init__(self, fname):
        self.filename = "{}.json".format(fname)

    def read(self):
        with open(self.filename, 'rt') as f:
            obj = f.read()
            return json.loads(obj)

    def write(self, data):
        with open(self.filename, 'wt') as f:
            obj = json.dumps(data)
            f.write(obj)


class CsvHandler:

    def __init__(self, fname):
        self.fieldnames = ['Name', 'Phone']
        self.filename = "{}.csv".format(fname)

    def read(self):
        with open(self.filename, 'rt') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            return dict(reader)

    def write(self, data):
        with open(self.filename, 'wt') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.fieldnames)
            writer.writerows([k, v] for k, v in data.items())


if __name__ == '__main__':

    controller = Controller()
    filename, extension = controller.read_config()

    if extension == 'json':
        db = JsonHandler(filename)
    else:
        db = CsvHandler(filename)

    phone_book = PhoneBook(db)

    while True:
        choose = input(
            """Choose what you want to do:
                1: create
                2: get
                3: update
                4: delete
                5: exit
            """
        )
        try:
            controller.get_action(choose, phone_book)
        except KeyboardInterrupt as e:
            print(e)
            break
