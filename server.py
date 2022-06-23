
import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
       # print(addr)

        # --------- Student code here
        playerName = player_socket.recv(1024).decode().strip()
        if(len(CLIENTS.keys()) == 0) :
            CLIENTS[playerName] = {'player_type' : 'player1'}
        
        else : 
            CLIENTS[playerName] = {'player_type' : 'player1'}
        
        CLIENTS[playerName]['player_socket'] = player_socket
        CLIENTS[playerName]['addr'] = addr
        CLIENTS[playerName]['playerName'] = playerName

        CLIENTS[playerName]['turn'] = False
        print(CLIENTS)
        print(f'Connection established with {playerName} : {addr}')

       

        # --------- Student code here






def setup():
    print("\n")
    print("\t\t\t\t\t\t*** Welcome to tambola ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()
