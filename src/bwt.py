
#Author: Barro Fabio 5BT-i

#funzione codifica della stringa con bwt
def encode_bwt(testo):
    
    rotazioni = []
    lunghezza = len(testo)

    #for per lo scorrimento delle permutazioni 
    for i in range(testo):
        #rotazione a sinistra
        rotazione = testo[i:] + testo[:i]
        rotazioni.append(rotazione)





#main
if __name__ == "__main__":
    stringa_banana = "banana$"