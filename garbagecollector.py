import gc
from unicodedata import name
print("garbagecollecter enabled:",gc.isenabled())
class employee:
    def __init__(self,name):
        self.name=name
        print(f"{self.name}object created")
    def __del__(self):
        print(f"{self.name}object destroyed")
emp=employee("nisha")
print("working with object")
del emp
print("programming finished")


d={}
student={"name":"nisha","age":22}
#using dict()
d=dict()
dict(name="taj",age=56)
#using list of tuples
student=dict([('name','nisha','age',23)])




          
    
