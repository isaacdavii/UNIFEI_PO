# Definir as exceptions

class UsernameDuplicado(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class EmailInvalido(Exception):
    pass

class User:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    def getUsername(self):
        return self.__username

    def getEmail(self):
        return self.__email

if __name__ == "__main__":

    listaExemplo = [
        ("paulo", "paulo@gmail.com", 21),
        ("maria", "maria@gmail.com", 19),
        ("antonio", "antonio@gmail.com", 25),
        ("pedro", "pedro@gmail.com", 15),
        ("marisa", "marisa@", 23),
        ("ana", "ana@gmail.com", -22),
        ("maria", "maria2@gmail.com", 27)
    ]

    cadastro = {}

    for username, email, idade in listaExemplo:
        try:
            if username in cadastro:
                raise UsernameDuplicado("Username já cadastrado: " + username)
            if idade < 18 and idade >= 0:
                raise IdadeMenorQuePermitida("Idade menor que 18: " + str(idade))
            if idade < 0:
                raise IdadeInvalida("Idade inválida: " + str(idade))
            if '@' not in email or '.' not in email.split('@')[-1]:
                raise EmailInvalido("Email inválido: " + email)

            user = User(username, email)
            cadastro[username] = user 
            print(f"Usuário {username} cadastrado com sucesso.")
            
        except (UsernameDuplicado, IdadeMenorQuePermitida, IdadeInvalida, EmailInvalido) as e:
            print(f"Erro ao cadastrar usuário {username}: {e}")