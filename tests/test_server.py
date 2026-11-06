


#importazione della libreria base socket
import socket as sck

#creazione del server
server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORT = 5000

server.bind((IP, PORT))

server.listen(5)    #quante richieste puo avere in coda.

