fileName = "inventoryInfo.txt"
delimeter = '='

file = open(fileName, 'r') ##reads file

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = [] ##empty list for books

class Books:
    def __init__(self, title, id, quantity, price ):
        self.title = title
        self.id = id
        self.quantity = quantity
        self.price = price

def findValue(fullstring):
    fullString = fullstring.rstrip('\n') ##ommits r variable
    value = fullstring[fullString.index(delimeter)+1:] ##locate index to start at
    return value

def Purchase():
    itemsPurchased = input("What book would you like to purchase?")
    if itemsPurchased == "The Great Gatsby":
        print("totaled: $7.99")
    if itemsPurchased == "The Color Purple":
        print("$14.99")
    if itemsPurchased == "War and Peace":
        print("totaled: $8.99")
    if itemsPurchased == "To Kill a Mocking Bird":
        print("totaled: $13.99")
    if itemsPurchased == "Pride and Prejudice":
        print("totaled: $7.99")
    if itemsPurchased == "Jane Eyre":
        print("totaled: $12.99")
    if itemsPurchased == "Ulysses":
        print("totaled: $5.99")

for line in file:
    if line.startswith('title'):
        title = findValue(line)
    if line.startswith('id'):
        id = findValue(line)
    if line.startswith('quantity'):
        quantity = findValue(line)
    if line.startswith('price'):
        price = findValue(line)

option = input("Would you like to view the inventory? y/n\n")
if option == "y":
    print(title)
    print(id)
    print(quantity)
    print(price)

else: print("Navigating to homepage...")