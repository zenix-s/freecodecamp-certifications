# Budget app

class Category:
    Category = ""
    ledger = []
    balance = 0.0
    def __init__(self, Category):
        self.Category = Category
    def deposit(self, cant, desc = ""):
        self.saldo = self.saldo + float(cant)
        self.ledger.append({"amount":cant,"description":desc})
    def withdraw(self, cant, desc = ""):
        if self.saldo > float(cant):
            self.saldo = self.saldo - float(cant)
            self.ledger.append({"amount":-cant,"description":desc})
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def __str__(self):
        x = "*************Food*************\n"
        for i in self.ledger:
            x1 = str(i ["description"])[0:23]
            x2 = str(format(float(i["amount"]),'.2f'))[-7:]
            x = x +  x1 + (" " * (30 - (len(x1)+len(x2)))) + x2 + "\n"
        return x
        
comida = Category("Comida")
comida.deposit(20,"Dinero para comida")
comida.withdraw(13,"hola pepe")
comida.deposit(10.87, "deposito algo")


print(str(comida))
print(comida.saldo)


