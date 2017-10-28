import json


class JsonSerializer:

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
