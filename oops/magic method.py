class Item:
    def __init__(self,name,price,quantity=0):
        assert price>=0,f"price {price} is not greater than zero!"
        assert quantity>=0,f"quantity"
        
        self.name = name
        self.price= price
        self.quantity= quantity

    def calculate_total_price(self):
        return self.price*self.quantity
        
        
item1 = Item("phone",100,5)
item2=Item("laptop",100,3)
item2.has_numpad=False
print(item1.calculate_total_price())
print(item2.calculate_total_price())
