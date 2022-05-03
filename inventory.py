fileName = "inventoryInfo.txt"
delimeter = '='

file = open(fileName, 'r') ##reads file

def findValue(fullstring):
    fullString = fullstring.rstrip('\n') ##ommits r variable
    value = fullstring[fullString.index(delimeter)+1:] ##locate index to start at
    value = value.replace(" ", "") ##ommit spaces
    return value


for line in file:
    if line.startswith('name'):
        name = findValue(line)
    if line.startswith('id'):
        id = findValue(line)
    if line.startswith('quantity'):
        quantity = findValue(line)
    if line.startswith('price'):
        price = findValue(line)

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = [] ##empty list for books

class Books:
    def __init__(self, name, id, quantity, price ):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price

print(name)
print(id)
print(quantity)
print(price)