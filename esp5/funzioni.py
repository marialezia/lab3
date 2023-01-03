import numpy as np
import sys

#definisco funzioni
'''
def trovaNumPicchi(spettroPot, soglia):
    
#funzione che conta il numero di picchi dello spettro di potenza, inserisco la soglia oltre la quale voglio che mi consideri il picco, #un ciclo for scorre l'array e vede se supera la foglia, se la supera aggiunge 1 a conta
   
    conta = 0
    for i in range(len(spettroPot)):
        if spettroPot[i] > soglia:
            conta = conta+1
    return conta
   ''' 
def massimi(spettroPot, soglia, nPicchi):
    #nPicchi = trovaNumPicchi(spettroPot, soglia)
    picchi = np.empty([0]) #creo un array di lunghezza pari al numero di picchi che vedo nella figura
    #faccio un ciclo for che scorre sull'array dello spettro di potenza per trovare i massimi
    copiaPot = spettroPot.copy()
    for i in range(nPicchi):
        inMax= np.argmax(copiaPot) #trovo l'indice in cui si trova l'elemento massimo
        if spettroPot[inMax] > soglia :
            picchi = np.append(picchi, int(inMax)) #salvo nell'array picchi l'indice del primo massimo
            for i in range(10):
                copiaPot[inMax+i] = 0
                copiaPot[inMax-i] = 0
 #faccio diventare 0 il massimo e gli elementi intorno, così la volta dopo il ciclo mi ritrova il massimo successivo 
    #resistuisce l'array che ha in se l'indice di tutti i massimi
    picchi=picchi.astype(int)
    return picchi

def mascheraCoeff(spettroPot, massimi, soglia, termini):
    #termini = 0 o 1 se voglio solo il termine centrale, se voglio anche i due vicini termini = 2 (uno dx e uno a sx), se voglio i 4 vicini(2 a dx, 2 a sx) termini = 3
    mask = np.full(len(spettroPot), False) #creo maschera vuota (cioè array lungo quante spettroPot pieno di False)
    
    for i in massimi:
        if spettroPot[i] > soglia: #faccio questo if per scegliere quali picchi mettere, scelgo la soglia in modo da avere solo i picchi che sono più alti di quel valore
            maskk = spettroPot == spettroPot[i]
            mask = mask + maskk
            #dopo aver creato la maschera scelgo se lasciare solo il termine principale o anche i termini vicini facendoli diventare True
            for j in range(termini):
                mask[i+j] = True
                mask[i-j] = True
    return mask

def printaFreq(frequenze, massimi):
    for i in range(len(massimi)) :
        print('Frequenza ', i, ' = ', frequenze[massimi[i]])


            
