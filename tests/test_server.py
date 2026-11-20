import socket as sck

IP = "127.0.0.1"
PORT = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    # Opzione per riutilizzare l'indirizzo ed evitare errori di porta occupata al riavvio
    server.setsockopt(sck.SOL_SOCKET, sck.SO_REUSEADDR, 1)
    
    server.bind((IP, PORT))
    server.listen(5)
    print(f"Server in ascolto su {IP}:{PORT}...")

    # Ciclo infinito per mantenere il server sempre attivo
    try:
        while True:
            conn, addr = server.accept()
            print(f"\nConnessione accettata da {addr}")

            with conn:
                dati = conn.recv(1024)
                if dati:
                    print("Dati ricevuti dal client:", dati.decode())
                    conn.sendall(dati)
    except KeyboardInterrupt:
        print("\nServer arrestato manualmente.")


