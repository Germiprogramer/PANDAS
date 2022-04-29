import pandas as pd

class Alojamientos():
    def __init__(self, archivo):
        self.archivo = archivo

    def creardiccionario(self):
        datos = pd.read_csv(self.archivo, header=0)

        notas= []

        alojamiento = list(datos[])


        Id_alojamiento = list(datos["IDalojamiento"])
        ID_anfitrion = list(datos["IDanfitrión"])
        distrito = list(datos["distrito"])
        precio = list(datos["precio"])
        plazas = list(datos["plazas"])

        for i in range(1,17):
            diccionario = {"Nota primer parcial {}".format(Id_alojamiento[i]) : Id_alojamiento[i] , "Nota segundo parcial {}".format(nombre[i]) : parcial_2[i] , "Asistencia" : asistencia[i]}
            notas.append(diccionario)
        print(notas)


csv = Alojamientos("calificaciones.csv")
csv.creardiccionario()