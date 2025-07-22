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

    def __add__(self, outraFrac):
        novoNum = self._num * outraFrac.den + self._den * outraFrac.num
        novoDen = self._den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        return Fracao(novoNum // divComum, novoDen // divComum)        
    
class fracaoMista(Fracao):
    def __init__(self, inteiro, num, den):
        super().__init__(num, den)
        self._inteiro = inteiro

    def __str__(self):
        return str(self._inteiro) + " " + str(self._num) + "/" + str(self._den)

    @property
    def inteiro(self):
        return self._inteiro

    @inteiro.setter
    def inteiro(self, valor):
        self._inteiro = valor
        
    def __add__(self, outraFrac):
        novoNum = self._num * outraFrac.den + self._den * outraFrac.num
        novoDen = self._den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        return fracaoMista(self._inteiro + outraFrac.inteiro, novoNum // divComum, novoDen // divComum)
    
    def simplifica(self):
        divComum = mdc(self._num, self._den)
        self._num = self._num // divComum
        self._den = self._den // divComum
        if self._num >= self._den:
            inteiro = self._num // self._den
            self._inteiro += inteiro
            self._num = self._num % self._den

if __name__ == "__main__":
    frac1 = Fracao (7, 2) 
    frac2 = Fracao(14, 3)
    frac3 = frac1 + frac2
    print(frac3)
    print()
    # frac1 = Fracao (7, 2)
    # frac2 = Fracao(14, 3)
    # frac3 = frac1 + frac2
    # print(frac3)
