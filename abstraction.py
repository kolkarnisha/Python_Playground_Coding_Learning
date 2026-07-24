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
