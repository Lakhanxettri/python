# here is a program for the management of products in a department store
def welcome():
    print("welcome to our department store sir")
welcome()
no_of_people = int(input("enter how many persons have entered to store"))
if (no_of_people>=5):
    print(f"you got the discount {no_of_people}*0.5")
else:
    print(f"you got the discount {no_of_people}*0.1")
class Item():
    def __init__(self,name_of_item):
        print(f"the total price of {name_of_item}")
    def total_price_of_product(self,x,y):
        return(x*y)
item1 = Item("iphone")
item1.no_of_items = 100
item1.price_of_item = 100000
print(item1.total_price_of_product(item1.no_of_items,item1.price_of_item))
item2 = Item("laptop")
item2.no_of_items = 10
item2.price_of_item = 500000
print(item2.total_price_of_product(item2.no_of_items,item2.price_of_item))
item3 = Item("airpods")
item3.no_of_items = 1000
item3.price_of_item = 5000
print(item3.total_price_of_product(item3.no_of_items,item3.price_of_item))
item4 = Item("airphones")
item4.no_of_items = 80
item4.price_of_item = 1500
print(item4.total_price_of_product(item4.no_of_items,item4.price_of_item))
#here if you want to add more products available in department store

def greeting():
    print("thank you so much sir for visiting our store sir")
greeting()
def what_you_buyed():
    a = int(input("enter the price of product  what you have buyed"))
    print(int(a)*int(f"{no_of_people}"))
what_you_buyed()

 