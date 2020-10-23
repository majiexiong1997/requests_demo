import socket

class SocketClient:
    def __init__(self):
        self.ip_addr = socket.gethostname()
        self.client = socket.socket()
        self.client.connect((self.ip_addr,9999))
    def send_msg(self):
        global msg
        while True:

            msg = str(msg)
            if len(msg) == 0: continue
            self.client.send(msg.encode())
            data_sure = self.client.recv(1024)
            print(data_sure.decode())
            if data_sure == 'bye':
                self.client.send(b'bye')
                break

        self.client.close()


if __name__ == '__main__':
    SocketClient().send_msg()