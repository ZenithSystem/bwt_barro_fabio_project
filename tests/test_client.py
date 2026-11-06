

import socket as sck

IP = "127.0.0.1"
PORT = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect((IP, PORT))

    client.sendall(messaggio.encode())

    dati = client.recv(1024)

    print("Messaggio ricevuto dal server", dati.decode())