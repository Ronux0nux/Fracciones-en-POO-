class Fraction:
    ##Make a class in python that creates fraction objects (using a constructor).##
    ##atributos##
    num = 0
    den = 0

    def __init__(self, num, den):  ##constructor#
        self.num = num
        self.den = den
        

    def __add__(self, other):

        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        r = Fraction(num, den)
        return r

    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        r = Fraction(num, den)
        return r

    def __truediv__(self, other):
        num = self.num / other.den
        den = self.den / other.num
        r = Fraction(num, den)
        return r

    def __mul__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        r = Fraction(num, den)
        return r



	
while True:
        
        num1 = int(input("Enter Numerador 1:   \n "))
        den1 = int(input("Enter Denominador 1: \n "))  
       
        num = Fraction(num1,den1) 
        print("Fraccion 1" + str(1)+ "\n")

        num2 = int(input("Enter Numerador 2:   \n "))
        den2 = int(input("Enter Denominador 2: \n "))   
        num = Fraction(num,den2)
        print("Fraccion 2" + str(2)+ "\n")         
               
	##opcines al usuario
        opcionMenu = input("ingresa una opcion  -->  ")
        if opcionMenu=="1":
            input("Has pulsado la Addicion  \npulsa una tecla para continuar")
            r = 1 + 2 
            print("1 + 2 = " + str(r) + "")
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la Sustracion  \npulsa una tecla para continuar")
            r = 1 + 2 
            print("1 - 2 = " + str(r) + "")
        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la multiplicacion \npulsa una tecla para continuar")
            r = 1 * 2 
            print("1 * 2 = " + str(r) + "")
        elif opcionMenu=="4":
            print ("")
            input("Has pulsado la Division  \npulsa una tecla para continuar")
            r = 1 / 2 
            print("1 / 2 = " + str(r) + "")
        elif opcionMenu=="p":
                break
        else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
