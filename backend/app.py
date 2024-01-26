#Initialisation de notre projet d'application Python.
#Ce premier projet va consister à creer une application de chat et la création d'un serveur backend.
#Je me base sur une vidéo datant de 4 ans ce qui est assez vieux mais va me permettre de travailler avec les sockets.
import socket
import select


HEADER_LENGTH = 10
#je définit mon localhost
IP = "127.0.0.1"
PORT = 3030

#je créé mon socket (connecteur). c'est lui qui va me servir de serveur. 
#AF_INET ET SOCK_STREAM sont nos IPC. Ils servent à faciliter la communication entre les plateformes
#AF_INET (IPv4)rend le dialogue avec n'importe quelle machine dans le monde facile. En gros notre localhost
#SOCK_STREAM en gros notre port (pour symplifier)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Je comprends pas trop a quoi ça sert
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

#Je stock notre serveur dans une liste pour le réutiliser avec select.
sockets_list = [server_socket]

clients = {}
#Si je veux placer des variables dans mes string je dois placer un f avant ma string.
print(f"Serveur en écoute sur le port {IP}:{PORT}...")
#Rappel: pour créer une fonction on la définit avec def
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_lenght = int(message_header.decode("utf-8").strip())
    except:
        pass
    
    
    
    
#https://www.youtube.com/watch?v=CV7_stUWvBQ&t=148s
#https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
#https://code.visualstudio.com/docs/python/python-tutorial