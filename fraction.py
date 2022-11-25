def mcm(m,n):
    while m%n != 0:
        m_o = m
        n_o = n

        m = n_o
        n = m_o%n_o
    return n
	    
class Fraction:
	
	num=0 
	den=1

	def __init__(self, num, den):
		self.num = int(num)
		if den ==0:
			raise Exception("No usar 0 en el denominador")
		self.den = int(den)

	def __str__(self):
		return str(self.num)+ "/" + str(self.den)
		
	
	def addition (self,otherfrac):
		num= self.num*otherfrac.den+ self.den*otherfrac.num
		den= self.den* otherfrac.den
		mc= mcm(num,den)
		return Fraction(num//mc, den//mc)

	def rest (self,otherfrac):
		num= self.num*otherfrac.den - self.den*otherfrac.num
		den= self.den* otherfrac.den
		comun = mcm(num,den)
		return Fraction(num//mc, den//mc)
	
	    
	def multiplication (self,otherfrac):
		num= self.num * otherfrac.num
		den= self.deno * otherfrac.den
		return Fraction(num,den)

	def division (self,otherfrac):
		num=self.num*otherfrac.den
		den=self.den*otherfrac.num
		return Fraction(num,den)	
		

num=int(input("numerador 1: "))
den=int(input("denominador 1: "))

fract1=Fraction(num,den)
print("Fraccion 1: ",str(fract1),"\n")

num=int(input("numerador 2: "))
den=int(input("denominador 2: "))

fract2=Fraction(num,den)
print("Fraccion 2: ",str(fract2),"\n")


operacion=input("Indique operacion con los simbolos (+, -, *, /): ")

if operacion == '+':
		result= fract1.addition(fract2)
		print("Fraccion 1 + Fraccion 2 = ",str(result))

elif operacion == '-':
		result= fract1.rest(fract2)
		print(" Fraccion 1 - Fraccion 2 = ",str(result))

elif operacion == '*':
	result= fract1.multiplication(fract2)
	print("Fraccion 1 * Fraccion 2 = ",str(result))

elif operacion == '/':
		result= fract1.division(fract2)
		print("Fraccion 1  / Fraccion 2 = ",str(result))

else:
	print("Indique una operacion valida...")