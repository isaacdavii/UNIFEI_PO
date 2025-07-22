# importar module sys para pegar o tipo da exception
import sys

lista = ['a', 0, 2]

for elemento in lista:
    try:
        print("O elemento é ", elemento)
        r = 1/int(elemento)
        break
    except:
        print("Oops!", sys.exc_info()[0], "ocorreu")
        print("Próxima entrada")
        print()
print("O número recíproco de", elemento , "é", r)

# sys.exc_info()[0]  # Retorna o tipo da exceção
# sys.exc_info()[1]  # Retorna o valor da exceção
# sys.exc_info()[2]  # Retorna o traceback da exceção
# sys.exc_info()  # Retorna uma tupla com as informações da exceção
# sys.exc_info() é uma função que retorna uma tupla contendo informações sobre a exceção atualmente tratada.
# sys.exc_info() é útil para obter informações detalhadas sobre a exceção que ocorreu, como o tipo da exceção, o valor da exceção e o traceback.
