class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest / 100  

    def value_after(self, years):
        return self.principal * (1 + self.interest) ** years

    def __str__(self):
        return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest * 100:.2f}%"

investment = Investment(1000.00, 5.12)
print(investment)  
