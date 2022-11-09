class Fraction():
    ##Make a class in python that creates fraction objects (using a constructor).##
                         ##atributos##
    num=0
    den=0 

def __init__ (self ,num,den):  ##constructor#
    self.num = num 
    self.den = den
def addition (self,other):
     if(self.den != other.den):
            den = self.den * other.den
            nume = (self.num*other.den)+(other.num*self.den)
            print("Addition:",num,"/",den)
     else:
def sustraction (self,other):
     if(self.den != other.den):
            den = self.den * other.den
            nume = (self.num*other.den)-(other.num*self.den)
            print("Sustraction:",num,"/",den)
     else:
def div (self,other):
      num = self.num / other.den
      den= self.den / other.num
      print("Division:",num,"/",den)
    
def multiply (self, other):
    num = self.num * other.den
    den= self.den * other.num
    print("Multiply:",num,"*",den)
    ##variables that can be used by the user##
num1 = 0
num2 = 0
den1 = 0
den2 = 0
cas1 = 0
cas2 = 0
option = 0 
 ##lets start to make the menu## 
num1 = int(input("Enter Numerator 1: "))
while(den1 == 0):
    den1 = int(input("Enter Denominator 1: "))
    if(den1!=0):
        break
    print("Enter a Denominator, cant be zero")
num2 = int(input("Enter Numerator 2: "))
while(den2 == 0):
    den2 = int(input("Enter Denominator 2: "))
    if(den2!=0):
        break
    print("Again Enter a Denominator, cant be zero")

cas1= Fraction(num1, den1)
print("Fraction 1 =",cas1.nu,"/",cas1.den)
cas2 = Fraction(num2, den2)
print("Fraction 2 =",cas2.num,"/",cas2.den)


print("\n ----------------Menu of mathematics operations in fractions with POO---------------- \n ")  
print(" 1)\n Addition")

print(" 2)\n Subtraction")

print(" 3)\n Multiplication")

print(" 4)\n Division\n")


options  = input("\nEnter an option:")

match(opcion):
    case '1':
        cas1.addition(cas2)
    case '2':
        cas1.subtraction(cas2)
    case '3':
        cas1.multiplication(cas2)
    case '4':
        cas1.division(cas2)

print("RM")