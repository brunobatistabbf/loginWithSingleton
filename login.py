import random
import string
from singleton import SingletonMetaClass

class Login(metaclass=SingletonMetaClass):
    def __init__(self):
        self.user = None
        self.password = None

    def verify_bot(self):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print(f"Código de Captcha: {code}")
        user_input = input("Entre com o código acima: ")
        return user_input == code

    def login(self, user, password):
        if self.verify_bot(): #no login se chama o captcha
            self.user = user
            self.password = password
            print("Logado com Sucesso!")
        else:
            print("Erro na Verificação")
