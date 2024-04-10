import socket
import time
import threading

# Create a socket object

class SockerServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket()
        self.conection_status = False
        self.client_status = False
        self.client_info = {}
        self.thread = None
        self.client_socket = None
        self.client_address = None

    def start(self):
        self.s.bind((self.ip, self.port))
        self.s.listen(5)
        self.conection_status = True
        print("Server started")
    
    def accept(self):
        self.client_socket, self.client_address = self.s.accept()
        self.client_status = True
        print(f"Connection from {self.client_address}")
        print("Connected to client")
        print(f"client_socket: {self.client_socket}")

    def send(self, data):
        if self.conection_status:
            self.client_socket.send(data.encode())
        else:
            print("No connection")
    
    def receive(self):
        if self.conection_status:
            return self.client_socket.recv(1024).decode()
        else:
            print("No connection")
            return None
    
    def close(self):
        self.s.close()
        self.conection_status = False
        print("Server closed")

    def run(self):
        self.start()
        while self.conection_status:
            if not self.client_status:
                self.accept()
            try:
                data = self.receive()
                if data == "exit":
                    # close the connection with the client
                    self.client_socket.close()
                    print("client disconnected")
                    self.client_socket = None
                    self.client_address = None
                    self.client_status = False
                else:
                    print(f"Received: {data}")
                    self.send("Received")
            except:
                self.client_socket.close()
                print("client disconnected")
                self.client_socket = None
                self.client_address = None
                self.client_status = False
        self.close()
    
    def __del__(self):
        self.s.close()
        print("Server closed")

# Create a server object
server = SockerServer("0.0.0.0", 12345)
server.run()
    
