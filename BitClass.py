import math

class BitClass:

    #costruttore
    def __init__(self, segno, esponente, mantissa):
        #extrabit per il segno
        self.segno     =  ""
        self.esponente =  ""
        self.mantissa  =  ""
        if segno == "-":
            self.segno = 1
        elif segno == "+":
            self.segno = 0
         
        self.segno = "?"

        if all(c in '01' for c in esponente):
            self.esponente = int(esponente)
        
        
        self.esponente = "?"
        if all(c in '01' for c in mantissa):    
            self.mantissa  = int(mantissa)
        self.mantissa = "?"
        

    
    def __str__(self):
        return f"   S    E   M \n < {self.segno} , {self.esponente} , {self.mantissa} > "
    def getSegno(self):
        return self.segno
    def getEsponente(self):
        return self.esponente
    def getMantissa(self):
        return self.mantissa
    def setSegno(self,value):
        self.segno = value

    def setEsponente(self,nuovo_esponente):
        self.esponente = nuovo_esponente
    
    def setMantissa(self,nuova_mantissa):
        self.mantissa = nuova_mantissa
