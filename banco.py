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

# --- MAIN EXECUTION BLOCK (Testing) ---
if __name__ == "__main__":
    # 1. Create instance
    MyAccount = SavingsAccount()
    
    # 2. Test Deposit 
    print(MyAccount.Deposit(1000))
    
    # 3. Test Withdraw
    print(MyAccount.Withdraw(200)) 
    
    # 4. Test Error
    print(MyAccount.Withdraw(5000))