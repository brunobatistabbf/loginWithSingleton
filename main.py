from login import Login
from singleton import SingletonMetaClass

if __name__ == '__main__':
    #Usuario 1
    login_instance1 = SingletonMetaClass.get_instance(Login)
    login_instance1.login("user1", "password1")

    #Usuario 2
    login_instance2 = SingletonMetaClass.get_instance(Login)
    login_instance2.login("user2", "password2")

    #Verificando se os dois usuarios estão usando a mesma instancia
    print()
    print("Verficando se está utilizando a mesma instancia:")
    print(id(login_instance1) == id(login_instance2))
