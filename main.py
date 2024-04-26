#imports:
import socket
import threading
import os

#global variables:
chat_member_array = []

#classes:
"""defines a chat_member and holds their data for chat room use"""
class chat_member:
    def __init__(self,client_socket,client_address):
        self.socket = client_socket
        self.address = client_address

#functions:
"""creates the server"""
def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 1000))
    server_socket.listen(5)
    return server_socket
#main:
def main():
    server_socket = create_server()
    while True:
        client_socket, client_address = server_socket.accept()
        temp = chat_member(client_socket,client_address)
        chat_member_array.append(temp)
        print(client_address)





main()



