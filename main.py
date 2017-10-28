from phonebook.model import PhoneBookModel
from phonebook.controller import PhonebookController
from phonebook.serializers import csv_serializer, json_serializer
from phonebook.view import View


def main():
    controller = PhonebookController()
    view = View()
    filename, extension = controller.read_config()

    if extension == 'json':
        db = json_serializer.JsonSerializer(filename)
    else:
        db = csv_serializer.CsvSerializer(filename)

    phone_book = PhoneBookModel(db)

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
            controller.get_action(action, phone_book, view)
        except KeyboardInterrupt as e:
            print(e)
            break


if __name__ == '__main__':
    main()
