#Ashley Wohlrab

class Product:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

    def countQuan(self, count):
        if count > self.quantity:
            return False
        else:
            return True

    def countPrice(self, count):
        return count * self.price

    def removeStock(self, count):
        self.quantity -= count

p1 = Product("Ultrasonic range finder", 2.50, 4)
p2 = Product("Servo motor", 14.99, 10)
p3 = Product("Servo controller", 44.95, 5)
p4 = Product("Microcontroller Board", 34.95, 7)
p5 = Product("Laser range finder", 149.99, 2)
p6 = Product("Lithium polymer battery", 8.99, 8)

products = [p1, p2, p3, p4, p5, p6]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].quantity > 0:
            print(str(i)+")",products[i].item, "$", products[i].price)
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].countQuan(count):
            if cash >= products[prodId].countPrice(count):
                products[prodId].removeStock(count)
                cash -= products[prodId].countPrice(count)
                print("You purchased", count, products[prodId].item +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].item)

main()
