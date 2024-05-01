class Item:
    def calculate_total_pirce(self,x,y):
        return x*y
        
        
item1 = Item()
# creating attribute
item1.name ="phone"
item1.price=100
item1.quantity=5
# print(type(item1))
# print(type(item1.name))
print(item1.calculate_total_pirce(item1.price,item1.quantity))

item2=Item()
# creating attribute
item2.name ="laptop"
item2.price=1000
item2.quantity=3
print(item2.calculate_total_pirce(item2.price,item2.quantity))