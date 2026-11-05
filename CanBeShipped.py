"""
CanBeShipped interface
    -Interface for any object that can be shipped
    -abstract calculate_shipping_cost(weight) method
"""

from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass