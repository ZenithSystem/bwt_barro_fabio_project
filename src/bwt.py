
#Author: Barro Fabio 5BT-i

#funzione codifica della stringa con bwt
def encode_bwt(testo):
    
    rotazioni = []
    lunghezza = len(testo)

    #for per lo scorrimento delle rotazioni 
    for i in range(testo):
        
        #rotazione a sinistra
        rotazione = testo[i:] + testo[:i]
        rotazioni.append(rotazione)

    #ordinamento tramite exchange sort delle rotazioni
    n = len(rotazioni)

    for i in range(n):
        for j in range(i + 1, n):
            if rotazioni[i] > rotazioni[j]:

                #scambia i valori in maniera decresciente
                temp = rotazioni[i]
                rotazioni[i] = rotazioni[j]
                rotazioni[j] = temp





#main
if __name__ == "__main__":
    stringa_banana = "banana$"