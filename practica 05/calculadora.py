while True:
    print("in ---calculadora basica---")
    print("1.sumar dos numeros")
    print("2. restar dos numeros")
    print("3. multiplicar dos numeros")
    print("4. dividir dos numeros")
    print("5. salir")

    opcion=input("elige un opcion(1,2,3,4,5):")
    if opcion == '1':
        print ("has elegido sumar")
        A=int(input("elige el primer numero"))
        B=int(input("elige el segundo numero"))
        print("el resultado de la suma es:",A+B)

    
    elif opcion == '2':
        print ("has elegido restar")
        A=int(input("elige el primer numero"))
        B=int(input("elige el segundo numero"))
        print("el resultado de la resta es:",A-B)

    elif opcion == '3':
        print ("has elegido multiplicar")
        A=int(input("elige el primer numero"))
        B=int(input("elige el segundo numero"))
        print("el resultado de la multiplicacion es:",A*B)

    elif opcion == '4':
        print ("has elegido dividir")
        A=int(input("elige el primer numero"))
        B=int(input("elige el segundo numero"))
        print("el resultado de la division es:",A/B)

    elif opcion == '5':
        print ("has elegido salir. BYE")
        break
    else:
        print("opcion no valida. intenta de nuevo")



