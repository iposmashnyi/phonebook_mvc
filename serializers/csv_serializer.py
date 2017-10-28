import csv


class CsvSerializer:

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
