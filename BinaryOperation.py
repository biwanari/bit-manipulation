"""
4 principal operation for binary digit
"""
from BitClass import *

def binary_string_adder(bina,binb):
    #calcoliamo la lista maggiore
    risultato = []
    if len(bina) > len(binb):
        diff = len(bina) - len(binb)
        binb = [0] * diff + binb
    else:
        diff = len(binb) - len(bina)
        bina = [0] * diff + bina

    #----------------------------
    carry = 0
    i = len(bina) - 1
    while i >= 0:
        #caso 1  -> 0 + 0
        if (bina[i] + binb[i] + carry) == 0:
            risultato.append(0)
            i -= 1

        #caso 2 -> 1+0 or 0 + 1
        elif (bina[i] + binb[i] + carry) == 1:
            risultato.append(1)
            carry = 0
            i -= 1 

        #caso 3 -> 1 + 1 = 0 with carry 1
        elif (bina[i] + binb[i] + carry) == 2:
            if i == 0:
                risultato.append(0)
                carry = 1
                risultato.append(carry)
                break
            else:
                risultato.append(0)
                carry = 1
                i -= 1

        #caso  -> 1 + 1  + 1 = 1 with carry 1
        elif (bina[i] + binb[i] + carry) == 3:
            if i == 0:
                risultato.append(1)
                carry = 1
                risultato.append(carry)
                break
            else:
                risultato.append(1)
                carry = 1
                i -= 1


    risultato.reverse()
    return(risultato)
    


def complements(binary_number):
    complemento = []
    i = 0
    if type(binary_number) is list :
        if 0 not in binary_number:
            complemento = [0] * len(binary_number)
            print (complemento)
        elif 1 not in binary_number:
            complemento = [1] * len(binary_number)
            print (complemento)
        else:
            for i in binary_number:
                if i == 0:
                    complemento.append(1)
                else:
                    complemento.append(0)
         
    else:
        l = list(binary_number)
        print (l)
        if "0" not in l:
            complemento = [0] * len(l)
            print (complemento)
        elif "1" not in l:
            complemento = [1] * len(l)
            print (complemento)
        else:
            for i in l:
                if i == "0":
                    complemento.append(1)
                else:
                    complemento.append(0)
    print (complemento)


        
        
            
        
        


def binary_string_sub(binay_number):
    pass

def binary_string_multiplier(binary_number):
    pass

def binary_string_div(binary_number):
    pass


    
