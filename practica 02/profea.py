#if else elif
edad=  int(input("dime tu edad:"))

if edad >= 10 and edad <18:
    print("eres un adolecente")
elif edad >=18:
    print("eres un adulto")
else:
    print ("todavia eres un niño")


#match



opcion=int(input"""
1. Agregar
2. Editar
3.eliminar
4.Leer
5.Finalizar
""")


match opcion:
    case 1:
    print("se ha agregado correctamente")
    case 2:
    print("se ha agregado correctamente")
    case 3:
    print("se ha agregado correctamente")
    case 4:
    print("se ha agregado correctamente")
    case 5:
    print("se ha agregado correctamente")
