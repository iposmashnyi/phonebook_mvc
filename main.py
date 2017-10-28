from phonebook.model import Model
from phonebook.controller import Controller
from phonebook.serializers import csv_serializer, json_serializer
from phonebook import network_view
from phonebook import console_view


def main():
    controller = Controller()
    filename, extension, connection = controller.read_config()

    if extension == 'json':
        db = json_serializer.JsonSerializer(filename)
    else:
        db = csv_serializer.CsvSerializer(filename)

    if connection == 'network':
        view = network_view.View()
    else:
        view = console_view.View()

    phonebook = Model(db)

    while True:
        help_message = \
            """
            Choose action:
            1: create
            2: get
            3: update
            4: delete
            5: exit
            """
        view.response(help_message)
        action = view.input('Action = ')
        try:
            controller.get_action(action, phonebook, view)
        except KeyboardInterrupt as e:
            print(e)
            break


if __name__ == '__main__':
    main()
