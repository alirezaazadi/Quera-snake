from threading import Thread
import socket
from datetime import datetime
import random, json, time


class Server:

    def __init__(self, number_of_clients, port):

        self.port = port
        self.conf = ('', self.port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(self.conf)
        self.number_of_clients = number_of_clients
        self.clients = []

    def wait_for_clients(self):

        self.s.listen(10)

        for i in range(self.number_of_clients):
            c, addr = self.s.accept()
            self.clients.append((c, addr))

        self.s.close()

    def start(self):

        self.wait_for_clients()

        config = {
            "cell_size": 30,
            "back_color": [255, 255, 255],
            "fruit_color": [255, 0, 0],
            "block_color": [139, 69, 19],
            "block_cells": [
                [14, 14],
                [13, 14],
                [12, 14],
                [15, 14],
            ],
            "sx": 30,
            "sy": 50,
            "table_size": 20,
            "height": 800,
            "width": 800,
            "id": -1,
            "snakes": []
        }

        for i in range(len(self.clients)):
            config['snakes'].append({
                "id": i,
                "keys": {
                    'snake_' + str(i) + '_w': "UP",
                    'snake_' + str(i) + '_s': "DOWN",
                    'snake_' + str(i) + '_a': "LEFT",
                    'snake_' + str(i) + '_d': "RIGHT",
                },
                "sx": random.randint(1, config['table_size']),
                "sy": random.randint(1, config['table_size']),
                "color": [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)],
                "direction": "LEFT",
            })

        for ind, it in enumerate(self.clients):
            config['id'] = ind
            it[0].sendall(str(json.dumps(config)).encode('ascii'))

    def pass_cycle(self):

        ls = []
        ret = False

        for client in self.clients:
            c = client[0]

            data = json.loads(c.recv(1024).decode('ascii'))
            ret |= not data['dead']
            ls += data['keys']

        for client in self.clients:
            client[0].sendall(str(ls).encode('ascii'))

        return ret

    def finish(self):

        for client in self.clients:
            c = client[0]
            c.close()

    def main(self):

        self.start()

        while self.pass_cycle():
            time.sleep(0.1)

        self.finish()


if __name__ == '__main__':
    server = Server(1)
    server.main()
