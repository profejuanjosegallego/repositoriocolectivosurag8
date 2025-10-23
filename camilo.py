 #nombre: Juan Camilo Valencia
 #nota=5.0

def ejecutar_cuestionario():
    preguntas = [
        {
            "pregunta": "¿Qué es GitHub?",
            "opciones": [
                "a) Un sistema operativo",
                "b) Una plataforma de control de versiones y colaboración",
                "c) Un lenguaje de programación",
                "d) Una red social común"
            ],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué comando se usa para clonar un repositorio?",
            "opciones": [
                "a) git push",
                "b) git commit",
                "c) git clone",
                "d) git pull"
            ],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué es un commit en Git?",
            "opciones": [
                "a) Una rama del repositorio",
                "b) Un error en el código",
                "c) Una instantánea de los cambios realizados",
                "d) Un archivo eliminado"
            ],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué comando se usa para subir cambios al repositorio remoto?",
            "opciones": [
                "a) git push",
                "b) git add",
                "c) git commit",
                "d) git status"
            ],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Qué es un Pull Request?",
            "opciones": [
                "a) Descargar cambios del repositorio",
                "b) Una solicitud para revisar y fusionar cambios",
                "c) Eliminar una rama",
                "d) Crear un nuevo repositorio"
            ],
            "respuesta_correcta": "b"
        }
    ]

    puntuacion = 0
    total_preguntas = len(preguntas)

    print("\n¡Bienvenido al Cuestionario de GitHub!\n")
    
    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        
        respuesta = input("\nSelecciona tu respuesta (a, b, c, d): ").lower()
        
        if respuesta == pregunta['respuesta_correcta']:
            print("¡Correcto! 🎉")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta_correcta']}")
        print("\n" + "-"*50 + "\n")

    porcentaje = (puntuacion / total_preguntas) * 100
    print(f"\nHas completado el cuestionario!")
    print(f"Tu puntuación: {puntuacion}/{total_preguntas} ({porcentaje:.1f}%)")
    
    if porcentaje == 100:
        print("¡Perfecto! ¡Eres un experto en GitHub! 🏆")
    elif porcentaje >= 80:
        print("¡Muy bien! Tienes un buen conocimiento de GitHub! 🌟")
    elif porcentaje >= 60:
        print("¡Bien! Pero aún hay espacio para mejorar 📚")
    else:
        print("Te recomiendo estudiar un poco más sobre GitHub 💪")

if __name__ == "__main__":
    ejecutar_cuestionario()