import json

class SavingsAccount:
    def __init__(self, id_ingresado):
        # 1. Cargar el archivo JSON
        with open("users.json", "r") as f:
            datos = json.load(f)
        
        # 2. Guardar el indice para saber con que usuario se trabajara
        self.encontrado = False
        # Se busca en la lista de usuarios
        for i in range(len(datos["Usuarios"])):
            if datos["Usuarios"][i]["id"] == id_ingresado:
                self.indice = i
                self.user = datos["Usuarios"][i]
                self.name = self.user["name"]
                self.amount = float(self.user["amount"])
                self.encontrado = True
                break   
        
    def save_data(self):
        # Leer para no borrar a los otros usuarios
        with open("users.json", "r") as f:
            full_data = json.load(f)
        
        # Actualizar y save_data como string para mantener tu formato
        full_data["Usuarios"][self.indice]["amount"] = str(self.amount)
        
        with open("users.json", "w") as f:
            json.dump(full_data, f, indent=4)
    
    def Deposit(self, amount):
        if amount > 0:
            self.amount += amount
            self.save_data()
            print(f"Nuevo saldo: {self.amount}")
        else:
            print("Error: El amount debe ser mayor a 0")

    #Se verifica si el numero si es positivo, luego verifica si tienes cantidad suficiente en la cuenta.
    def Withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
            self.save_data()
            print(f"Nuevo saldo: {self.amount}")
        else:
            print("Error: Fondos insuficientes o amount inválido")
            
    def Transfer(self, id_destino, amount):
        if 0 < amount <= self.amount:
            # Abrimos el archivo para buscar al destinatario
            with open("users.json", "r") as f:
                full_data = json.load(f)
            
            destino_encontrado = False
            nombre_destino = "" # Variable para guardar el nombre del que recibe
            
            for u in full_data["Usuarios"]:
                if u["id"] == id_destino:
                    # 1. Restamos de nuestro saldo local
                    self.amount -= amount
                    # 2. Sumamos al destinatario en los datos del archivo
                    u["amount"] = str(float(u["amount"]) + amount)
                    nombre_destino = u["name"] # <--- Guardamos el nombre aquí
                    destino_encontrado = True
                    break
            
            if destino_encontrado:
                # 3. Actualizamos nuestro saldo en los datos del archivo y guardamos
                full_data["Usuarios"][self.indice]["amount"] = str(self.amount)
                with open("users.json", "w") as f:
                    json.dump(full_data, f, indent=4)
                
                # Aqui mostramos en nombre e id
                print(f"Transferencia exitosa a {nombre_destino} (ID: {id_destino})")
            else:
                print("Error: El usuario destino no existe.")
        else:
            print("Error: Fondos insuficientes.")
        
    def PrintStatement(self):
        return f"--- Titular: {self.name} | Saldo Actual: ${self.amount} ---"