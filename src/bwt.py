#Author: Barro Fabio 5BT-i


#funzione codifica della stringa con bwt
def encode_bwt(testo):
    
    rotazioni = []
    lunghezza = len(testo)

    #range(lunghezza) anziché range(testo)
    for i in range(lunghezza):
        
        # rotazione a sinistra
        rotazione = testo[i:] + testo[:i]
        rotazioni.append(rotazione)

    # ordinamento tramite exchange sort delle rotazioni
    n = len(rotazioni)

    for i in range(n):
        for j in range(i + 1, n):
            # Se l'elemento corrente è alfabeticamente maggiore di quello successivo, effettua lo scambio
            if rotazioni[i] > rotazioni[j]:

                # scambia i valori in maniera decresciente
                temp = rotazioni[i]
                rotazioni[i] = rotazioni[j]
                rotazioni[j] = temp
    


    # Costruzione della stringa BWT estraendo l'ultimo carattere di ogni rotazione ordinata
    bwt = ""
    for r in rotazioni:
        bwt += r[-1]

    return bwt


#main
if __name__ == "__main__":
    stringa_banana = "banana$"

    print(encode_bwt(stringa_banana))
