#imports:
import socket

#global variables:
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8888

REAL_PERSON = 0
NOT_REAL_PERSON = 1
MESSAGE_RECEIVED = '2'.encode('utf-8')

#functions:

"""creates socket"""
def create_socket():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    return client_socket

"""handles a chat between the other client. (empty placeholder"""
def start_chatting():
    return

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

        #server hello
        server_hello = client_socket.recv(1024).decode('utf-8')
        print(server_hello)

        #get available members:
        members_list = client_socket.recv(4096).decode('utf-8')
        print(members_list)
        list_received = MESSAGE_RECEIVED
        client_socket.send(list_received)
        enter_name = client_socket.recv(1024).decode('utf-8')
        print(enter_name)

        #'connect' with a client

        connected = False
        while(not connected):
            person_to_chat = input().encode('utf-8')
            client_socket.send(person_to_chat)
            is_person_real = int(client_socket.recv(1024).decode('utf-8'))
            if is_person_real == REAL_PERSON:
                start_session = client_socket.recv(1024).decode('utf-8')
                print(start_session)
                start_chatting()
                break
            elif is_person_real == NOT_REAL_PERSON:
                not_real = client_socket.recv(1024).decode('utf-8')
                print(not_real)




    except Exception as e:
        client_socket.close()
        print(e)
main()