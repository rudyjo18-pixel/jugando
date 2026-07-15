#simulador de vueltas de carreras
carros = int(input("Ingrese la cantidad de carros: "))
vueltas = int(input("Ingrese la cantidad de vueltas: "))
seleccion = str.lower(input("favor seleccione la marca de los carros: ferrari, mercedes, red bull: "))
ganador = "ferrari"
def carrera(carros, vueltas):
    for i in range(1, vueltas + 1):
        if i == 1:
            print(f"Inicia la carrera con {carros} carros")
        elif i == vueltas // 2:
            print(f"Se ha completado la vuelta {i} de {vueltas}")
            print(f"se a llegado a la mitad de la carrera, se han completado {i} vueltas de {vueltas}")
        elif i == vueltas:
            print(f"Se ha completado la vuelta {i} de {vueltas}")
            print(f"Se ha completado la carrera con {carros} carros")
        else:
            # Esto solo se ejecuta si NO es ni la 1, ni la mitad, ni la última
            print(f"Se ha completado la vuelta {i} de {vueltas}")

    if seleccion == ganador:
            print(f"El carro {ganador} ha ganado la carrera")
    else:
            print(f"El carro {seleccion} ha terminado la carrera pero no gano")

carrera(carros, vueltas)

    