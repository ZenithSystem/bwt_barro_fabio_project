import socket as sck

IP = "127.0.0.1"
PORT = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    server.bind((IP, PORT))

    server.listen(5)    #quante richieste puo avere in coda.

    conn, addr = server.accept()     #restituisce una tupla da due elementi

    with conn:
        print("Socket di ascolto: ", server.getsockname())
        print("Socket di connessione: ", conn.getsockname())

        dati = server.recv(1024)
        print("Dati ricevuti dal client", dati.decode())
        conn.sendall(dati)
