# --- MAIN EXECUTION BLOCK (Testing) ---
if __name__ == "__main__":
    
    id_usuario = input("Ingresa tu ID: ")
    cuenta = SavingsAccount(id_usuario)

if cuenta.encontrado:
    while True:
        print(f"\n--- Hola {cuenta.name} | Saldo: ${cuenta.amount} ---")
        print("1. Depositar | 2. Retirar | 3. Transferir | 4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            m = float(input("amount a depositar: "))
            cuenta.Deposit(m)
        elif opcion == "2":
            m = float(input("amount a retirar: "))
            cuenta.Withdraw(m)
        elif opcion == "3":
            dest = input("ID del usuario destino: ")
            m = float(input("amount a transferir: "))
            cuenta.Transfer(dest, m)
        elif opcion == "4":
            print("¡Adiós!")
            break
else:
    print("ID no encontrado.")