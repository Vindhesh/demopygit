import time
class Forex():
    def buy(self, product, currency, amount):
        self.product = str.upper(product)             
        self.currency = str.upper(currency)
        self.amount = float(amount)
        self.rate = float(71.74)
        self.INR_value = float(self.amount * self.rate)
        self.charges = float(250)
        self.payable = float(self.INR_value + self.charges)

    def sale(self):
        print(f"Your quotation for Forex is as follows:\n\nProduct \t\t:\t\t {self.product} \nCurrency \t\t:\t\t {self.currency} \nAmount \t\t\t:\t\t {self.amount}\nRate \t\t\t:\t\t {self.rate}\nINR value \t\t:\t\t {self.INR_value}\nCharges \t\t:\t\t {self.charges}\nTotal \t\t\t:\t\t {self.payable}")
    
order1 = Forex()
order1.buy(input("Enter product of your choice:\n"), input("Enter your choice of currency:\n"), input("Enter your amount: \n") )
order1.sale()
time.sleep(30)