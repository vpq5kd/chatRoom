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

"""handles the client's connection to the server"""
def handle_client(chat_member):
    client_connection = chat_member.socket
    welcome_message = "Welcome to my chat room, please enter your name:"
    client_connection.send(welcome_message.encode('utf-8'))
    client_name = client_connection.recv(1024).decode('utf-8')



#main:
def main():
    server_socket = create_server()
    while True:
        client_socket, client_address = server_socket.accept()
        temp = chat_member(client_socket,client_address)
        chat_member_array.append(temp)

        print(client_address)





main()



