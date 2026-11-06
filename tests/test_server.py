


#importazione della libreria base socket
import socket as sck

#creazione del server
server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORT = 5000

server.bind((IP, PORT))

server.listen(5)    #quante richieste puo avere in coda.


conn, addr = server.accept()     #restituisce una tubla da due elementi

print("Socket di ascolto: ", server.getsockname())
print("Socket di connesione: ", conn.getsockname())

dati = server.recv(1024) #numero massimo di byte per chiamata per evetare che si sovraccarichi
print("Dati ricevuti dal client", dati.decode())
conn.sendall(dati)
