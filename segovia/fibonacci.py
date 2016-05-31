fibonacci = []
b = 1 
a = 0
try :
	numero = input("cuantas cifras de la secuencia fibonacci deseas\n")
	i = 0
	while i< numero:
   		fibonacci.append(b)
  		c = a + b 
   		a = b
   		b = c
   		i = i+1
	print "La secuencia es %s " % (fibonacci)
except:
	print "Ingrese solamente numeros \n"


