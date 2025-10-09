# Examen DE BRAULIO jijija

preguntas = [
    ("1. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?",
     {"A": "Tarjeta Gráfica", "B": "Memoria principal", "C": "Sistema de entrada/Salida", "D": "CPU"},
     "A"),
    
    ("2. El lenguaje máquina está compuesto por:",
     {"A": "Símbolos lógicos y matemáticos", "B": "Pseudocódigo", "C": "Instrucciones en inglés abreviado", "D": "Código binario"},
     "D"),
    
    ("3. Un lenguaje de programación de alto nivel se caracteriza por:",
     {"A": "Ser el más rápido", "B": "Control directo del hardware", "C": "Ser independiente de la arquitectura", "D": "Muy difícil de aprender"},
     "C"),
    
    ("4. ¿Qué es un algoritmo?",
     {"A": "Pasos finitos y bien definidos", "B": "Un lenguaje de programación", "C": "El código fuente", "D": "Instrucciones en binario"},
     "A"),
    
    ("5. En pseudocódigo, ¿qué estructura se usa si se cumple una condición?",
     {"A": "Mientras", "B": "Para", "C": "Secuencial", "D": "Condicional"},
     "D"),
    
    ("6. El propósito principal del pseudocódigo es:",
     {"A": "Traducir a máquina", "B": "Planificar la lógica", "C": "Ejecutar más rápido", "D": "Controlar registros"},
     "B"),
    
    ("7. Un programa de computadora es:",
     {"A": "Una colección de algoritmos", "B": "El sistema operativo", "C": "Un hardware", "D": "Instrucciones que ejecuta la computadora"},
     "D"),
    
    ("8. Diferencia entre 'mientras' y 'repetir':",
     {"A": "No hay diferencia", "B": "'Repetir' solo usa números", "C": "'Mientras' es más rápido", "D": "'Mientras' puede no ejecutarse, 'Repetir' al menos una vez"},
     "D"),
    
    ("9. El lenguaje Ensamblador es de nivel:",
     {"A": "Medio", "B": "Alto", "C": "Bajo", "D": "Muy alto"},
     "C"),
    
    ("10. Estructura adecuada para repetir un número de veces conocido:",
     {"A": "Para", "B": "Si", "C": "Repetir", "D": "Mientras"},
     "A")
]

puntaje = 0

print("=== Examen primer parcial ===\n")

for texto, opciones, correcta in preguntas:
    print(texto)
    for letra, opcion in opciones.items():
        print(f"{letra}) {opcion}")
    resp = input("Tu respuesta (A/B/C/D): ").upper()
    
    if resp == correcta:
        print(" Correcto!\n")
        puntaje += 1
    else:
        print(f" Incorrecto. La correcta era {correcta}) {opciones[correcta]}\n")

print("=== Resultado final ===")
print(f"Tu calificacion: {puntaje} de {len(preguntas)}")

if puntaje == 10:
    print(" Excelente, lo hiciste perfecto!")
elif puntaje >= 7:
    print(" Muy bien, buen trabajo.")
elif puntaje >= 5:
    print(" Regular, necesitas practicar más.")
else:
    print(" Debes repasar los temas.")










