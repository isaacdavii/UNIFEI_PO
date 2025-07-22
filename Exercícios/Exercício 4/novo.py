from classes.comissionado import Comissionado
from classes.contratado import Contratado

def main():
    funcContratado = Contratado(1001, "João da Silva", 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200_000)
    funcContratado.adicionaVenda(101, 3, 2022, 300_000)
    funcContratado.adicionaVenda(102, 4, 2022, 600_000)
    funcComissionado = Comissionado(1002, "José Santos", 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200_000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400_000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500_000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print(func.getDados())
        print("Renda no mês 3 de 2022: ")
        print(func.calculaRenda(3, 2022))
        
if __name__ == "__main__":
    main()