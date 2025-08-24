from abc import ABC, abstractmethod


class Checker(ABC):
    @abstractmethod
    def check(self):
        pass


class QuantityChecker(Checker):
    def check(self, quantity):
        result = True
        if quantity is None or quantity <= 0:
            result = False
        return result
    

class VolumeChecker(Checker):
    def check(self, volume):
        result = True
        if volume is None or volume <= 0:
            result = False
        return result


class WeightChecker(Checker):
    def check(self, weight):
        result = True
        if weight is None or weight <= 0:
            result = False
        return result


class PriceChecker(Checker):
    def check(self, price):
        result = True
        if price is None or price <= 0:
            result = False
        return result
    

class StatusChecker(Checker):
    def check(self, status, key):
        result = False
        if status == key:
            result = True
        return result