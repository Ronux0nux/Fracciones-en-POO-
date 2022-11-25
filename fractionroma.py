class Fraction:
    ##Make a class in python that creates fraction objects (using a constructor).##
    ##atributos##
    num = 0
    den = 0

    def __init__(self, num, den):  ##constructor#
        self.num = num
        self.den = den

    def addition(self, other):

        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        r = Fraction(num, den)
        return r

    def sustraction(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        r = Fraction(num, den)
        return r

    def div(self, other):
        num = self.num / other.den
        den = self.den / other.num
        r = Fraction(num, den)
        return r

    def multiply(self, other):
        num = self.num * other.den
        den = self.den * other.num
        r = Fraction(num, den)
        return r


def casos(options):

    match options:
        case (1):
            r = cas1.addition(cas2)
            print(f"{r.num} / {r.den}")
        case (2):
            r = cas1.subtraction(cas2)
            print(f"{r.num} / {r.den}")
        case (3):
            r = cas1.multiply(cas2)
            print(f"{r.num} / {r.den}")
        case (4):
            r = cas1.div(cas2)
            print(f"{r.num} / {r.den}")
        case _:
            print("Invalid operation")


##lets start to make the menu##
   
    num1 = int(input("Enter Numerator 1: "))
    den1 = 0
    while den1 != 0:
        den1 = int(input("Enter Denominator 1: "))
    if den1 == 0:
        break
        
    print("Enter a Denominator, cant be zero")
num2 = int(input("Enter Numerator 2: "))
den2 = 0
while den2 != 0:
    den2 = int(input("Enter Denominator 2: "))
    if den2 == 0:
        break
    print("Again Enter a Denominator, cant be zero")

cas1 = Fraction(num1, den1)
print(f"Fraction 1 = {cas1.num}/{cas1.den}")
cas2 = Fraction(num2, den2)
print(f"Fraction 2 = {cas2.num}/{cas2.den}")


print(
    "\n ----------------Menu of mathematics operations in fractions with POO---------------- \n "
)
print(" 1)\n Addition")

print(" 2)\n Subtraction")

print(" 3)\n Multiplication")

print(" 4)\n Division\n")


options = int(input("\nEnter an option:"))
casos(options)
