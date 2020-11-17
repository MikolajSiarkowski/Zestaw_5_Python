import math
def NWW(a,b):
    return int(abs(a*b / math.gcd(a,b)))

def simplify(frac):
    dziel = math.gcd(frac[0],frac[1])
    frac[0] = int(frac[0]/dziel)
    frac[1] = int(frac[1]/dziel)
    return frac

def add_frac(frac1, frac2):             # frac1 + frac2
    frac = [0 , 0]
    wiel = NWW(frac1[1],frac2[1])
    liczba1 = wiel / frac1[1]
    liczba2 = wiel / frac2[1]
    frac1[1] = wiel
    frac2[1] = wiel
    frac1[0] = frac1[0] * liczba1
    frac2[0] = frac2[0] * liczba2
    frac[0] = int(frac1[0]+frac2[0])
    frac[1] = int(frac1[1])
    simplify(frac)
    return frac
           

def sub_frac(frac1, frac2):             # frac1 - frac2
    frac = [0 , 0]
    wiel = NWW(frac1[1],frac2[1])
    liczba1 = wiel / frac1[1]
    liczba2 = wiel / frac2[1]
    frac1[1] = wiel
    frac2[1] = wiel
    frac1[0] = frac1[0] * liczba1
    frac2[0] = frac2[0] * liczba2
    frac[0] = int(frac1[0]-frac2[0])
    frac[1] = int(frac1[1])
    simplify(frac)
    return frac
    
    
def mul_frac(frac1, frac2):             # frac1 * frac2
    frac = [0 , 0]
    frac[0] = int(frac1[0]*frac2[0])
    frac[1] = int(frac1[1]*frac2[1])
    simplify(frac)
    return frac
    
    
def div_frac(frac1, frac2):             # frac1 / frac2
    frac = [0 , 0]
    frac[0] = int(frac1[0]*frac2[1])
    frac[1] = int(frac1[1]*frac2[0])
    simplify(frac)
    return frac
    
    
def is_positive(frac):                  # bool, czy dodatni
    if(frac[0] < 0 or frac[1] < 0):
        return False
    else:
        return True
    
    
def is_zero(frac):                      # bool, typu [0, x]
    if(frac[0] == 0):
        return True
    else:
        return False
    
    
def cmp_frac(frac1, frac2):             # -1 | 0 | +1
    wiel = NWW(frac1[1],frac2[1])
    liczba1 = wiel / frac1[1]
    liczba2 = wiel / frac2[1]
    frac1[1] = wiel
    frac2[1] = wiel
    frac1[0] = frac1[0] * liczba1
    frac2[0] = frac2[0] * liczba2
    if(frac1[0] > frac2[0]):
        return 1
    elif(frac1[0] == frac2[0]):
        return 0
    elif(frac1[0] < frac2[0]):
        return -1
    else:
        pass
    
def frac2float(frac):                   # konwersja do float
    liczba = float(frac[0]/frac[1])
    return liczba

