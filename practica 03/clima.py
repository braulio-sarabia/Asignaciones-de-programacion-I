dia = input("Ingresa el día de la semana: ").lower()
clima = input("Ingresa el clima (soleado, lluvioso, nublado): ").lower()
match dia:
    case "lunes":
        if clima == "soleado":
            print("Es lunes y hace sol . ¡Perfecto para iniciar la semana con energía!")
        elif clima == "lluvioso":
            print("Es lunes y está lloviendo . Lleva paraguas y empieza con calma.")
        elif clima == "nublado":
            print("Es lunes y está nublado . Ideal para concentrarte en tus tareas.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")
match dia:
    case "martes":
        if clima == "soleado":
            print("Es martes y hace sol . ¡Perfecto para iniciar la semana con energía!")
        elif clima == "lluvioso":
            print("Es martes y está lloviendo . Lleva paraguas y empieza con calma.")
        elif clima == "nublado":
            print("Es martes y está nublado . Ideal para concentrarte en tus tareas.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")
match dia:
    case "miercoles":
        if clima == "soleado":
            print("Es miercoles y hace sol . ¡Perfecto para iniciar la semana con energía!")
        elif clima == "lluvioso":
            print("Es miercoles y está lloviendo . Lleva paraguas y empieza con calma.")
        elif clima == "nublado":
            print("Es miercoles y está nublado . Ideal para concentrarte en tus tareas.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")
match dia:
    case "jueves":
        if clima == "soleado":
            print("Es jueves y hace sol . ¡Perfecto para iniciar la semana con energía!")
        elif clima == "lluvioso":
            print("Es jueves y está lloviendo . Lleva paraguas y empieza con calma.")
        elif clima == "nublado":
            print("Es jueves y está nublado . Ideal para concentrarte en tus tareas.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")

    case "viernes":
        if clima == "soleado":
            print("Es viernes soleado . ¡Excelente día para planear algo divertido!")
        elif clima == "lluvioso":
            print("Es viernes lluvioso . Quizás una peli en casa sea buena idea.")
        elif clima == "nublado":
            print("Es viernes nublado . Perfecto para descansar antes del fin de semana.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")

    case "sábado" | "domingo":
        if clima == "soleado":
            print("Es fin de semana soleado . ¡Sal a disfrutar al aire libre!")
        elif clima == "lluvioso":
            print("Es fin de semana lluvioso . Disfruta un café y un buen libro.")
        elif clima == "nublado":
            print("Es fin de semana nublado . Relájate y recarga energías.")
        else:
            print("Clima no reconocido, intenta con 'soleado', 'lluvioso' o 'nublado'.")
