import socket
import time
import threading

# Create a socket client class

class SockerClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket()
        self.conection_status = False

    def connect(self):
        self.s.connect((self.ip, self.port))
        self.conection_status = True
        print("Connected to server")
    
    def send(self, data):
        if self.conection_status:
            self.s.send(data.encode())
        else:
            print("No connection")
    
    def receive(self):
        if self.conection_status:
            return self.s.recv(1024).decode()
        else:
            print("No connection")
            return None
    
    def close(self):
        self.s.close()
        self.conection_status = False
        print("Connection closed")
    
    def run(self):
        self.connect()
        while True:
            data = input("Enter data: ")
            self.send(data)
            if data == "exit":
                break
            print(f"Received: {self.receive()}")
        self.close()
    
    def __del__(self):
        self.s.close()
        print("Connection closed")

# Create a client object
client = SockerClient("192.168.0.104", 12345)

# Run the client
client.run()