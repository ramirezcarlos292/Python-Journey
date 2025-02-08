class Product:
    def __init__(self, product_name, price, location, code):
        self.product_name = product_name
        self.price = price
        self.location = location
        self.code = code
        self.available = True
    
    def __str__(self):
        return f"{self.product_name}"
    
class Customer:
    def __init__(self, ):
        pass