class Model:

    def __init__(self, database):
        self.db = database
        try:
            self.data = self.db.read()
        except FileNotFoundError:
            self.data = {}

    def create(self, name, phone):
        if not self.data:
            self.data = {name: phone}
        self.data[name] = phone
        self.db.write(self.data)
        return self.data

    def retrieve(self, name=None):
        if name:
            return self.data[name]
        return self.data

    def update(self, name, new_phone):
        self.data[name] = new_phone
        self.db.write(self.data)
        return self.data[name]

    def delete(self, name):
        del self.data[name]
        self.db.write(self.data)
        return self.data
