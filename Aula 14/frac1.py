def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.num == f2.num) and (f1.den == f2.den)    

class Fracao():    
    def __init__(self, num, den):

        self._num = num        
        self._den = den     

    def __str__(self):
        return str(self._num) + "/" + str(self._den)

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den

    def simplifica(self):
        divComum = mdc(self._num, self._den)
        self._num = self._num // divComum
        self._den = self._den // divComum            

if __name__ == "__main__":
    frac1 = Fracao(3,4)
    frac2 = Fracao(3,4)
    print(mesmaFracao(frac1, frac1))
    print(frac1 is frac2)
    frac1 = frac2
    print(frac1 is frac2)