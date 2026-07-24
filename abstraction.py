class TV:
  def turn_on(self):
    sel.__power_supply()
    self.__motherboard()
    self.__display()
 def __power_supply(self):
   print("power on")
 def __motherboard(self):
   print("motherboard started")
def __display(self):
  print("display activated")
tv=TV()
tv.turn_on()
'''output: 
power on
motherboard started
display activated'''
#abstract classes
#ABSTRACT METHODS
""" these are available in the abc module (ABSTRACT BASE CLASS)"""
"""import abc module"""
from abc import ABC, abstractmethod
class vehicle(abc):
     pass
class vehicle(abc):
     @abstractmethod
       def start(self):
          pass
''' here abstract method means every child class must implement the start method '''
from abc import ABC,abstractmethod
class vehicle(ABC):
      @abstractmethod
         def start(self):
            pass
class car(vehicle):
        def start(self):
          print("car strted")
car=car()
car.start()
# implementation of ecommerce gateway

from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

payments = [CreditCard(),UPI(),PayPal()]
for payment in payments:
    payment.pay(500)
