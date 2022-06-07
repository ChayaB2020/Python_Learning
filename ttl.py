class Vehicle():
    def __init__(self,type_vehicle, trans_type='Manual'):
        self.type_vehicle=type_vehicle
        self.trans_type=trans_type
        print(f"Type of vehicle is {self.type_vehicle} having transmission type: {self.trans_type}")
    def speed(self,force,mass):
        self.force=force
        self.mass=mass
        return(self.force/self.mass)

veh1=Vehicle(type_vehicle='1')
veh2=Vehicle(type_vehicle='2')
veh3=Vehicle(type_vehicle='3')
my_list=[]
my_list.append(veh1.speed(100,10))
my_list.append(veh2.speed(150,16))
my_list.append(veh3.speed(200,19))
first=my_list[0]
index_temp=0
for index,i in enumerate(my_list):
    if first<i:
        first=i
        index_temp=index+1
print(str(first)+","+str(index_temp))