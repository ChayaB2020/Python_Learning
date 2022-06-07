#This is to practice class example from Udemy training.
class Circle():
    pi=3.142
    def __init__(self, radius=1):
        self.radius=radius
        self.area= Circle.pi* radius*radius
    def changed_area(self,new_radius):
        self.radius=new_radius
        self.area=Circle.pi * new_radius*new_radius
class Child(Circle):
    def __init_(self,radius):
        #Circle.__init__()
        self.radius=radius
    def whatever(self):
        print("Inside whatever function")

a=Circle()
print(f" radius is {a.radius} and area is {a.area}")
#a.changed_area(10)
#print(f" radius is {a.radius} and area is {a.area} ad pi value is {a.pi}")

c=Child(3)
c.whatever()
c.changed_area(2)
print(f"this is child class having {c.radius} and changed_area is having {c.radius}and {c.area}")

