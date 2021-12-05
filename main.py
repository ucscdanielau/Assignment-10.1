#demo program

#import BurgerKingOrder class
from Assignment10_1 import BurgerKingOrder

#Creating an instance of BurgerKingOrder
order = BurgerKingOrder()
#Instance adds 4 whoppers to order
order.add_item("whopper", 4)
#instance adds 2 milkshakes to order
order.add_item("milkshake",2)
#Instance removes 3 whoppers from order
order.remove_item("Whopper", 3)
#prints out menu and your order
print(order.get_menu())
print(order.get_order())
