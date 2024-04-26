#imports:
import socket

#global variables:
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 1000

#functions:
def create_socket():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return client_socket

#main:
def main():
    try:
        #create the client_socket
        client_socket = create_socket()

        #connect to server
        client_socket.connect((SERVER_ADDRESS,SERVER_PORT))
        welcome_message = client_socket.recv(1024).decode('utf-8')
        print(welcome_message)

        #get client's name:
        client_name = input().encode('utf-8')
        client_socket.send(client_name)

        #get available members:
        members_list = client_socket.recv(4096).decode('utf-8')
        print(members_list)


    except Exception as e:
        print(e)
main()