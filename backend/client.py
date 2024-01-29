import socket
import select
import errno
import sys

HEADER_LENGTH = 10
#je définis mon localhost
IP = "127.0.0.1"
PORT = 3030
#Se connecter via l'input (choisir son username)
my_username = input("Username: ")
#Je set mon client serverside
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

#je m'assure que le nom d'utilisateur ai le bon encodage
username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
#envoi du nom de l'utilisateur au serveur.
client_socket.send(username_header + username)

while True: 
    #On va ensuite envoyer le message.
    #vu que j'ai pu définir mon nom d'utilisateur, on va l'afficher et grace a l'input on peut mettre un message à sa suite.
    message = input(f"{my_username} > ")
    
    
    #On veut s'assurer d'envoyer un message juste en appuiyant sur entrée
    if message : 
        message = message.encode("utf-8")
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
    
    try:
        while True:
        #Réception des messages:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Déconnexion du serveur")
                sys.exit()
            #On récupère le nom d'utilisateur qu'on a envoyé précédemment    
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")
            #On récupère le message qu'on a envoyé précédemment
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")
            #On affiche les deux.
            print(f"{username} > {message}")
            
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Erreur de lecture", str(e))
            sys.exit()
        continue
       
    except Exception as e:
        print("General error".str(e))
        sys.exit()
        