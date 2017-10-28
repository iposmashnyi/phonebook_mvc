import json
import csv
import configparser


def read_json(user=None):
    with open('{}.{}'.format(filename, extension), 'rt') as f:
        obj = f.read()
        if user:
            return json.loads(obj)[user]
        else:
            return json.loads(obj)


def write_json(user=None, users=None):

    if user:
        try:
            users = read_func()
        except FileNotFoundError:
            users = user
        else:
            user_name, user_phone = list(user.items())[0]
            users[user_name] = user_phone

    with open('{}.{}'.format(filename, extension), 'wt') as f:
        f.write(json.dumps(
            users
        ))


def read_csv(users):
    with open('{}.{}'.format(filename, extension), 'wt') as f:
        pass


def write_csv(users):
    with open('{}.{}'.format(filename, extension), 'wt') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(users)


config = configparser.RawConfigParser()
config.read('config.ini')

filename = config.get('File', 'filename')
extension = config.get('File', 'extension')

if extension == 'csv':
    write_func = write_csv
    read_func = read_csv
else:
    write_func = write_json
    read_func = read_json


def create_user(name, phone):
    users = {name: phone}
    write_func(users)


def get_user(name):
    try:
        phone = read_func(name)
    except KeyError:
        print('No such user')
    else:
        print(phone)


def update_user(name, new_phone):
    delete_user(name)
    create_user(name, new_phone)


def delete_user(name):
    users = read_func()

    if users and name in users:
        del users[name]
    else:
        raise ValueError('No such user or users are empty')

    write_func(users=users)


def set_config(ext, name):
    config.set('File', 'extension', ext)
    config.set('File', 'filename', name)

    with open('config.ini', 'wt') as configfile:
        config.write(configfile)

    config.read('config.ini')

    global filename, extension
    filename = config.get('File', 'filename')
    extension = config.get('File', 'extension')


def get_action(choose):

    if choose == '1':
        name = input('Name ')
        phone = input('Phone ')
        create_user(name, phone)
    elif choose == '2':
        name = input('Name ')
        get_user(name)
    elif choose == '3':
        name = input('Name ')
        new_phone = input('New Phone ')
        update_user(name, new_phone)
    elif choose == '4':
        name = input('Name ')
        delete_user(name)
    elif choose == '5':
        extension = input('Choose file format (csv|json) ')
        filename = input('Enter file name ')
        set_config(extension, filename)
    elif choose == '6':
        raise KeyboardInterrupt('Exit')


if __name__ == '__main__':

    while True:
        choose = input(
            """Choose what you want to do:
                1: create
                2: get
                3: update
                4: delete
                5: settings
                6: exit
            """
        )
        try:
            get_action(choose)
        except KeyboardInterrupt as e:
            print(e)
            break
