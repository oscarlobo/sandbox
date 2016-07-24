var1 = True
while var1 is True:
   try:
	opcion = input("Ingrese una opcion   \n 1) Elegir numero \n 2) Ver lista del 1 al 100 \n 3) Salir \n")
   except:
   	print "Ingrese solo numeros... \n"
   if opcion == 1:
	try:
	    numero = input("Ingrese un numero : \n")
	    if (numero%3) == 0 and (numero%5) == 0:
		print " Fizzbuzz \n"
            elif numero % 3 == 0:
		print " Fizz \n"
	    elif numero % 5 ==0:
		print "Buzz \n"
	    				
	except:
	    print "Ingrese solo numeros \n" 
   elif opcion == 2: 
	for n in range(1 , 101): # en la funcion range que significa rango tenemos un for que recorre los numeros de 1 al 100
	    if n % 3 == 0 and n % 5 == 0:
		print "FizzBuzz con %s \n" % (n)
	    elif n % 3 == 0:
		print "Fizz con %s \n" %(n)
	    elif n % 5 == 0:
		print "Buzz %s \n" % (n)
	
   elif opcion == 3:
	var1 = False	

   
