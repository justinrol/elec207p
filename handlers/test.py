import socket


class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg)  :
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < 1024:
            chunk = self.sock.recv(min(2 - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)

socket = mysocket()

# socket.connect('34.252.66.133', 8888)
socket.connect('localhost', 8000)
socket.mysend('default, c0:5:c2:d0:17:70, e4:3e:d7:3c:c5:92, c0:05:c2:bc:94:59')
print(socket.myreceive())
socket.mysend('terminate')

