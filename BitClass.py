import math

class BitClass:

    #costruttore
    def __init__(self,segno,esponente,mantissa):
        self._segno = segno
        self._esponente = esponente
        self._mantissa = mantissa
    
    def __str__(self):
        return f"{self.segno},{self.esponente},{self.mantissa}"
    def getSegno(self):
        return self.segno
    def getEsponente(self):
        return self.esponente
    def getMantissa(self):
        return self.mantissa
    def setSegno(self,value):
        self.segno = value
    
        
        
        
    

    
    def fromFloatToBin(self, floating_data):
        pass


