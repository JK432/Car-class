# Create a class Car with attributes Model, year, and price 
# and a method cost() for displaying price. 
# Create two instances of the class and call the method for each instance 
class car:
  def __init__(self,mod,yr,prz):
    self.Model=mod
    self.year=yr
    self.price=prz
  def cost(self):
    print("cost: ",self.price)


c1=car("jk4302",2022,10000000)
c2=car("san",2021,5000000)

c1.cost()
c2.cost()