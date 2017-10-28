import socket


class View:
    def __init__(self):
        s = socket.socket()
        s.bind(('127.0.0.1', 5000))
        s.listen(1)
        print('Waiting for connections...')
        self.c, a = s.accept()
        print('Connected', a)

    def input(self, message):
        self.c.sendall(message.encode('utf8'))
        return self.c.recv(1024).decode('utf8')[:-2]

    def _response(self, message):
        self.c.sendall(message.encode('utf8'))

    def response(self, message):
        self._response(str(message) + '\n')
