
all_items = []
class Quantity:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
def getPrice(self):
    return self.qty
def getName(self):
    return self.name

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
class Cart:
    def __init__(self):
        self.list = []
    def addItem(self, quant):
        self.list.append(quant)
    def getTotal(self):
        total = 0
        price = 0
        for item in self.list:
            name = item.name
            for it in all_items:
                if name == it.name:
                    price = it.price
                    qty = item.qty
                    total = total + (price*qty)
        return total
    def getNumItems(self):
        count = 0
        for c in self.list:
            count = count + 1
        return count
#removes the item from list
    def removeItem(self, name):
        for it in self.list:
            if name == it.name:
                self.list.remove(it)
    def list_cart_items(self):
        print("Books available in your shopping cart:")
        for it in self.list:
         print("%s %i"%(it.name,it.qty))
    def list_all_items():
        print("Books  available for shopping along with their prices:")
        for it in all_items:
            print("%s %.2f$"%(it.name,it.price))
def main():
    c = Cart()
    with open("C:\Users\Makayla\OneDrive - Mississippi State University\Documents\methods\Cartclass\inventoryInfo.txt") as fd:
        for line in fd:
            name, price = line.split(" ")
            it = Item(name, float(price.strip()))
            all_items.append(it)
    print(all_items)
    choice = 1
    while choice!=6:
        print ("1. List all items and their prices")
        print ("2. List cart items")
        print ("3. Add an item to the cart")
        print ("4. Remove a item from the cart")
        print ("5. Checkout")
        print ("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice==6:
            return
        elif choice == 1:
            c.list_all_items()
        elif choice == 2:
            c.list_cart_items()
        elif choice == 3:
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            q = Quantity(name, quantity)
            c.addItem(q)
        elif choice == 4:
            name = input("Enter the name of the item to remove from cart: ")
            c.removeItem(name)
        elif choice == 5:
            total = c.getTotal()
            tax = total*0.07
            grand_total = total+tax
            print("Your subtotal: %.2f$" %(total))
            print("Your tax: %.2f$" %(tax))
            print("Your total: %.2f$" %(grand_total))
main()  