"""
Product class
    -Stores product information
    -Manages its own state
"""

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, Id, name, price, stock):
        self.__product_id = Id
        self.__name = name
        self.__price = price
        self.__stock = stock
       
    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self): #return product info as dict
        return {
            "ID": self.__product_id, 
            "Name": self.__name, 
            "Price": self.__price, 
            "Stock": self.__stock,
        }
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass
