# Barro Fabio - 5BT-i

## Implementazione della Trasformata di Burrows-Wheeler (BWT) con comunicazione Client-Server TCP in Python

La trasformata di Burrows-Wheeler è una tecnica di riordinamento dei caratteri di una stringa che raggruppa simboli simili, aumentando la fattorizzazione dei dati per successive fasi di compressione.

# Funzionamento

Data una stringa di lunghezza N, vengono svolte tramite ciclo `for` tutte le sue permutazioni spostando l'ultimo carattere all'inizio (o il primo alla fine) per ottenere N stringhe diverse. Per evitare eventuali ambiguità dell'algoritmo si usa un carattere terminatore (`$`).

Ottenute le permutazioni, salviamo le stringhe all'interno di una matrice in ordine alfabetico tramite un algoritmo di riordinamento classico (**Exchange Sort**).

La trasformata finale consiste nel leggere l'ultima colonna della matrice ordinata dall'alto verso il basso: la stringa ottenuta sarà la nostra trasformata BWT finale.

L'obiettivo del progetto, oltre a scrivere la trasformata di Burrows-Wheeler, è quello di utilizzare i **socket** in Python per la comunicazione client-server tramite i rispettivi script `client.py` e `server.py`, Il link della repository è allinterno del file requierments.txt.
