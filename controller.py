from configparser import RawConfigParser


class Controller:

    def get_action(self, action, phonebook, view):

        if action == '1':
            name = view.input('Name ')
            phone = view.input('Phone ')
            view.response(phonebook.create(name, phone))

        elif action == '2':
            name = view.input('Name ')
            view.response(phonebook.retrieve(name))

        elif action == '3':
            name = view.input('Name ')
            new_phone = view.input('New Phone ')
            view.response(phonebook.update(name, new_phone))

        elif action == '4':
            name = view.input('Name ')
            view.response(phonebook.delete(name))

        elif action == '5':
            raise KeyboardInterrupt('Exit')

    def read_config(self):
        config = RawConfigParser()
        config.read('config.ini')

        file_name = config.get('File', 'filename')
        file_extension = config.get('File', 'extension')
        connection = config.get('File', 'connection')

        return file_name, file_extension, connection
