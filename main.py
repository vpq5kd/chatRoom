#imports:
import socket
import threading
import os

#general issues/imporvements:
# *currently need a way to handle connections between clients better,
# i.e, "x wants to connect with you, would you like to chat?"

#global variables:
chat_member_array = []

#classes:
"""defines a chat_member and holds their data for chat room use"""
class chat_member:
    def __init__(self,client_socket,client_address):
        self.is_available = None
        self.name = None
        self.socket = client_socket
        self.address = client_address
    def set_name(self,name):
        self.name = name
    def set_is_available(self, is_available):
        self.is_available = True
    def get_name_and_ip(self):
        if self.is_available:
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
    #initializes connection variable
    client_connection = chat_member.socket

    #gets the name of the client
    welcome_message = "Welcome to my chat room, please enter your name:"
    client_connection.send(welcome_message.encode('utf-8'))
    client_name = client_connection.recv(1024).decode('utf-8')
    chat_member.set_name(client_name)

    #sends the available member info to the client
    chat_member_info = [member.get_name_and_ip() for member in chat_member_array]
    chat_member_as_string = "\n".join(chat_member_info)
    chat_members = f"Here is the list of people available to chat with:\n{chat_member_as_string}".encode('utf-8')
    client_connection.send(chat_members)

    #allows the client to choose who they want to chat with
    enter_ip = "please enter the IP Address of the person you'd like to chat with: ".encode('utf-8')
    client_connection.send(enter_ip)
    connected = False
    while(not connected):
        test_requested_member = None
        test_requested_ip = client_connection.recv(1024).decode('utf-8')
        is_member = False
        for member in chat_member_array:
            if test_requested_ip == member.get_ip():
                test_requested_member = member
                is_member = True
                break
        if(not is_member):
            not_member = f"{test_requested_ip} is not a valid ip address, please try again.".encode('utf-8')
            client_connection.send(not_member)
            continue

    #once the client is chosen, begin sending messages
    requested_member_name_ip = test_requested_member.get_name_and_ip()
    starting_session = f'starting session with{requested_member_name_ip}...'
    client_connection.send(starting_session)
    test_requested_member.set_is_available(False)
    chat_member.set_is_available(False)
    start_session(test_requested_member,chat_member)

"""starts a chat session between two clients."""

def start_session(requested_member, current_member):
    return













#main:
def main():
    server_socket = create_server()
    while True:
        client_socket, client_address = server_socket.accept()
        temp = chat_member(client_socket,client_address)
        chat_member_array.append(temp)
        threading.Thread(target=handle_client, args=(temp,)).start()

main()



