"""
PhysicalProduct class
    -Subclass of Product 'parent' class
    -Stores additional 'download_size' attribute
"""
from Product import Product

class DigitalProduct(Product):
    def __init__(self, Id, name, price, stock, download_size, ):
        super().__init__(Id, name, price, stock)
        self.__download_size = download_size

    def display_information(self): #return product info as dict
            product_info = super().display_information() #receive parent product info, which is a dict
            product_info["Download_Size"] = self.__download_size #adds download_size detail to dict
            return product_info

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

"""""
Testing
DP1 = DigitalProduct("PD001", "Software1", 100.50, 50, 50)

print(DP1.display_information())
print(DP1.get_fulfilment_info())

P1 = Product("PD003", "lappy", 100.50, 50)

print(P1.display_information())
"""""