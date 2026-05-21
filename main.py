from bankaccount import BankAccount
from auth import run_auth

username, pin = run_auth() 
acc = BankAccount(username, pin)

def Display():
    print()
    print("Eliga su acción:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Historial")
    print("4. Saldo")
    print("5. Salir")
    print()

while True:
    Display()
    option = str(input("Ingrese acción (1-5): "))

    if option == "1":
        value = float(input("Ingrese monto: "))
        try:
            print()
            acc.deposit(value)
            print(f"Depositado {value} con éxito.")
            print()
        except(ValueError):
            print()
    elif option == "2":
        value = float(input("Ingrese monto: "))
        try:
            print()
            acc.withdraw(value)
            print(f"Retirado {value} con éxito.")
            print()
        except(ValueError):
            print()
    elif option == "3":
        print()
        for t in acc.get_transactions():
            print(t)
    elif option == "4":
        print()
        print("Saldo actual:", acc.balance)
        print()
    elif option == "5":
        print()
        print("Saliendo...")
        print()
        break
    else:
        print()
        print("Eliga una acción válida.")
        print()