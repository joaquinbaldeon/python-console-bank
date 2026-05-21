print("¡Hola! Soy tu asistente de cuentas de ahorro.")

account_in_general = []

def ask(prompt):
    return input(prompt).lower()

def Validation(authenticator):
    if authenticator not in ["registrarse", "iniciar sesión", "iniciar","registrar","sesión"]:
        print("Ingrese una opción válida.\n")
        return False
    else:
        print("Muchas gracias.")
        print("Cargando...\n")
        return True

def question():
    while True:
        authenticator = ask("¿Desea REGISTRARSE o INICIAR SESIÓN?\n *  ")
        if Validation(authenticator):
            return authenticator

def add_account(username, password):
    for account in account_in_general:
        if account["username"] == username:
            print(f"Error: el nombre de usuario '{username}' ya está ocupado.")
            return 
 
    account_in_general.append({"username": username, "password": password})
    print(f"Cuenta de {username} agregada correctamente.")

def login(username, password):
    for account in account_in_general:
        if account["username"] == username:
            if account["password"] == password:
                print(f"¡Bienvenido {username}!\n")
                return True
            else:
                print("Contraseña incorrecta.\n")
                return False
    print("Usuario no encontrado.\n")
    return False

def run_auth():
    while True:
        eleccion = question()
        if eleccion in ["registrarse","registrar"]:
            username = input("Ingrese su nombre de usuario: \n *  ")
            password = input("Ahora ingrese su contraseña: \n *  ")
            add_account(username, password)
        else:
            username = input("Ingrese su nombre de usuario: \n *  ")
            password = input("Ahora ingrese su contraseña: \n *  ")
            user_logged_in = login(username, password)
            if user_logged_in:
                return username, password
            else:
                print("Intente de nuevo o regístrese si no tiene cuenta.\n")

if __name__ == "__main__":
    run_auth()
