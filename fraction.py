def mcm(m,n):
    while m%n != 0:
        m_o = m
        n_o = n

        m = n_o
        n = m_o%n_o
    return n	
class Fraction:
  
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)
        if den ==0:
             raise Exception("No usar 0 en el denominador") 
    def __str__(self):
     return str(self.num)+ "/" + str(self.den)
 
    def addition (self,frac):
        num= self.num*frac.den+ self.den*frac.num
        den= self.den* frac.den
        minimocomun= mcm(num,den)
        return Fraction(num//minimocomun, den//minimocomun)

    def rest (self,frac):
        num= self.num*frac.den - self.den*frac.num
        den= self.den* frac.den
        minimocomun = mcm(num,den)
        return Fraction(num/minimocomun, den/minimocomun)
	
    def multiplication (self,frac):
        num= self.num * frac.num
        den= self.den * frac.den
        return Fraction(num,den)
    
    def division (self,frac):
        num=self.num*frac.den
        den=self.den*frac.num
        return Fraction(num,den)
		
while True:
   num1= int(input("El Numerador 1: "))
   den1= int(input("El Denominador 1: "))

   fract1=Fraction(num1,den1)
   print("Fraccion 1: ",str(fract1),"\n")

   num2=int(input("El Numerador 2: "))
   den2=int(input("El Denominador 2: "))

   fract2=Fraction(num2,den2)
   print("Fraccion 2: ",str(fract2),"\n")


   operacion=input("Indique operacion con los simbolos (+, -, *, /): ")

   if operacion == '+':
       result= fract1.addition(fract2) 
       print("Fraccion 1 + Fraccion 2 = ",str(result))

   elif operacion == '-':
       result= fract1.rest(fract2) 
       print(" Fraccion 1 - Fraccion 2 = ",str(result))
    
   elif operacion == '-':
       result= fract1.multiplication(fract2) 
       print(" Fraccion 1 * Fraccion 2 = ",str(result))    
       
   elif operacion == '/':
       result= fract1.division(fract2)
       print("Fraccion 1  / Fraccion 2 = ",str(result))    
   else:
	   print("Indique una operacion valida...")
   if (input("\n ¿Desea continuar las operaciones (Seleccione 'tecla enter ' para continuar y 'n' para no continuar) \n") == "n"):
       break
