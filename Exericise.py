"""
    Fecha:20/09/2023
    Autor: Juan Esteban Florez
    Objetivo: Se requiere un software que calcule si un aprendiz tiene el estilo de aprendizaje Asimilador.
    Para ello deben realizarse 7 preguntas de respuesta SI o NO. 
    Si el aprendiz obtuvo 4 o más respuestas en SI entonces el sistema deberá indicarle que es Asimilador, 
    de lo contrario le dirá que su estilo de aprendizaje es otro.
"""

print("Bienvenido Aprendiz.")

def calcular_estilo_aprendizaje(respuestas):
    contador_si = respuestas.count("Y")
    if contador_si >= 4:
        return "Asimilador"
    else:
        return "Otro estilo de aprendizaje"

def realizar_encuesta():
    respuestas = []
    preguntas = [
        "1.Cuando aprendes algo nuevo, ¿prefieres que te presenten teorías o conceptos antes que ejemplos prácticos?",
        "2.¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos?",
        "3.¿Encuentras útil hacer esquemas, resúmenes o diagramas para organizar la información que estás aprendiendo?",
        "4.¿Te gusta analizar y reflexionar sobre las ideas y conceptos antes de ponerlos en práctica?",
        "5.¿Tienes tendencia a destacar en asignaturas que requieren comprensión de teorías y conceptos, como las matemáticas o la física?",
        "6.¿Te sientes más cómodo en entornos de aprendizaje estructurados, como conferencias o clases magistrales?",
        "7.¿Prefieres aprender de manera independiente en lugar de trabajar en grupos o equipos?"
    ]

    for pregunta in preguntas:
        respuesta = input(pregunta + " (Y/N): ")
        while respuesta.upper() not in ["Y", "N"]:
            respuesta = input("Por favor, responde con Y o N: ")
        respuestas.append(respuesta.upper())

    estilo_aprendizaje = calcular_estilo_aprendizaje(respuestas)
    print("Tu estilo de aprendizaje es:", estilo_aprendizaje)

realizar_encuesta()
