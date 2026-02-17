# --- MAIN EXECUTION BLOCK (Testing) ---
from banco import SavingsAccount

if __name__ == "__main__":
    
    id_usuario = input("Enter you ID: ")
    cuenta = SavingsAccount(id_usuario)

if cuenta.encontrado:
    while True:
        print(f"\n--- Hello {cuenta.name} | Balance: ${cuenta.amount} ---")
        print("1. Deposit | 2. Withdraw | 3. Transfer | 4. Exit")
        opcion = input("Choose a option: ")

        if opcion == "1":
            m = float(input("Amount to deposit: "))
            cuenta.Deposit(m)
        elif opcion == "2":
            m = float(input("Amount to withdraw: "))
            cuenta.Withdraw(m)
        elif opcion == "3":
            dest = input("ID destiny user: ")
            m = float(input("Amount to transfer: "))
            cuenta.Transfer(dest, m)
        elif opcion == "4":
            print("¡Good Bye!")
            break
else:
    print("ID not found")
