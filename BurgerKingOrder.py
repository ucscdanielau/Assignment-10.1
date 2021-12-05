#Daniel Au
#Prof. Kuttivelil
#CSE 20
#12/3/2021

#Assignment 10.1 Your Own class method

#This class named "BurgerKingOrder" prints out a formatted menu list of different items in different catagories such as burgers, sides, drinks, and sweets.  The user can then select what itemm they want and the amount they want.

#Create class BurgerKingOrder
class BurgerKingOrder:
  def __init__(self, menulist_dict = None):
    #Prints menu out for user to choose items from.
    self.__menu = f"MENU\nBurgers: Whopper, Impossible Whopper, Cheeseburger\nSides: Fries, Onion Rings, Mozzarella Sticks\nSweets: Ice Cream, Milkshake, Cake\nDrinks: Soda, Tea, Coffee"
    print(self.__menu)
    #Creates empty dictionary menulist
    if menulist_dict is None:
      self.__order = {}
    else:
      self.__order = {}
      for menu, count in menulist_dict.items():
        self.__order[menu.lower()] = count
    self.__menu_list = ["whopper", "impossible whopper", "cheeseburger", "fries", "onion rings", "mozzeralla sticks", "ice Cream", "milkshake", "soda","tea", "coffee"]
  #function to add items to order
  def add_item(self, item_name, count):
    item_name = item_name.lower()
    if item_name in self.__menu_list:
      self.__order[item_name] = self.__order.get(item_name,0) + count
    else:
      print("Item is not on menu")
  #function to remove items from order
  def remove_item(self, item_name, count):
    item_name = item_name.lower()
    if item_name in self.__order:
      self.__order[item_name] -= count
      if self.__order[item_name] <= 0:
        self.__order.pop(item_name)
    else:
      print(f"{item_name} was not found in the order")
  
  #returns order
  def get_order(self):
    return self.__order
  #returns menu
  def get_menu(self):
    return self.__menu