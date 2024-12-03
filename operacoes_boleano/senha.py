usuario = input("digite o nome de usuario: ")
senha = input("digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login efetuado com sucesso!")
    print("Bem-vindo, administrador!")
else:
    print("Login ou senha incorretos!")
