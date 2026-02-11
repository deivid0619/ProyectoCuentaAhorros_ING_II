class SavingsAccount:
    def __init__(self): 
        self.Balance = 0
        print("--- Account created with Balance $0 ---")
    def Deposit(self, Amount):
        try:
            # 1. Validate that input is a number
            if not isinstance(Amount, (int, float)):
                return "Error: The Amount must be a number."

            # 2. Validate that Amount is positive
            if Amount <= 0:
                return "Error: The Amount must be greater than zero."

            # 3. Perform deposit
            self.Balance += Amount
            return f"Success: Deposited ${Amount}. New Balance: ${self.Balance}"

        except Exception as e:
            return f"System Error: {str(e)}"

    def Withdraw(self, Amount):
        try:
            # 1. Validate that input is a number
            if not isinstance(Amount, (int, float)):
                return "Error: The Amount must be a number."

            # 2. Validate that Amount is positive
            if Amount <= 0:
                return "Error: The Amount must be greater than zero."

            # 3. Validate sufficient funds (Critical Rule)
            if Amount > self.Balance:
                return "Error: Insufficient funds."

            # 4. Perform withdrawal
            self.Balance -= Amount
            return f"Success: Withdrew ${Amount}. New Balance: ${self.Balance}"

        except Exception as e:
            return f"System Error: {str(e)}"
        
    def PrintStatement(self):
        return f"--- Current Balance: ${self.Balance} ---"

# --- MAIN EXECUTION BLOCK (Testing) ---
if __name__ == "__main__":
    MyAccount = SavingsAccount()
    
    # 1. Depositar dinero
    print("--- Test 1: Deposit ---")
    print(MyAccount.Deposit(2000))
    
    # 2. Retirar dinero
    print("\n--- Test 2: Valid Withdraw ---")
    print(MyAccount.Withdraw(500))
    
    # 3. Validar saldo insuficiente
    print("\n--- Test 3: Insufficient Funds ---")
    print(MyAccount.Withdraw(10000)) 
    
    # 4. Consultar el saldo
    print("\n--- Test 4: Report ---")
    print(MyAccount.PrintStatement())