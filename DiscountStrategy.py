"""
DiscountStrategy class
    -Takes order total and returns discounted total
"""

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: int):
        self.percentage = percentage
        
    def apply(self, total: float) -> float:
        return total * (1 - self.percentage/100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: int, amount: int):
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.amount
        return total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95
