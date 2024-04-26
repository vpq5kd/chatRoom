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
    def set_name(self,name):
        self.name = name
    def get_name_and_ip(self):
        return f'{self.name} @ {self.address}'
    def get_ip(self):
        return self.address
    def get_socket(self):
        return self.socket

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
    chat_member.set_name(client_name)
    chat_member_info = [member.get_name_and_ip() for member in chat_member_array]
    chat_member_as_string = "\n".join(chat_member_info)
    chat_members = f"Here is the list of people available to chat with:\n{chat_member_as_string}".encode('utf-8')
    client_connection.send(chat_members)
    enter_ip = "please enter the IP Address of the person you'd like to chat with: ".encode('utf-8')
    client_connection.send(enter_ip)
    connected = False
    while(not connected):
        test_requested_ip = client_connection.recv(1024).decode('utf-8')
        for chat_member in chat_member_array:







#main:
def main():
    server_socket = create_server()
    while True:
        client_socket, client_address = server_socket.accept()
        temp = chat_member(client_socket,client_address)
        chat_member_array.append(temp)
        threading.Thread(target=handle_client, args=(temp,)).start()





main()



