Barro Fabio 5BT-i 

Implementazione della Trasformata di Burrows-Wheeler (BWT) con comunicazione Client-Server TCP in Python

La trasformata di Burrows-Wheeler è una tecnica di riordinamento dei caratteri di una stringa che raggruppa simboli simili aumentando la fattorizzazione dei dati per successive fasi di compressione.

Funzionamento:

Data una stringa di lunghezza N, vengono svolte tramite ciclo for tutte le sue permutazioni spostando lultimo carattere all'inizio o il primo alla fine per ottenere N stringhe diverse, per evitare delle eventuali ambiguita del algoritmo si usa un carattere terminatore ($).
Ottenute le permutazioni salviamo le stringhe all'interno di una matrice in ordine alfabetico tramite un algoritmo di riordinamento classico (exchange Sort).

La trasformata finale consiste nel leggere l'ultina colonna della matrice ordinata dall'alto verso il basso 
e la stringa ottenuta sarà la nostra finale trasformata BWT.

L'obbiettivo del progietto oltre a scrivere la trasformata di Burrows-Wheeler è quello utilizzare il socket in python per lacomunicazione client - server con i loro relaitvi script client.py e server.py

