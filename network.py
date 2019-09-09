import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.connect((self.host, self.port))
        response = self.s.recv(1024).decode('ascii')
        with open('config.json', 'w') as outfile:
            outfile.write(response)

    def send_data(self, keys):
        self.s.connect((self.host, self.port))
        self.s.send(json.dump({'keys': keys, 'dead': False}))

    def get_data(self):
        response = str(self.s.recv(1024).decode('ascii')).replace('\'', '"')
        json_file = json.loads(response)
        return json_file['keys']
