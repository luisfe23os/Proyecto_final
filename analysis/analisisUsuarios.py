from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla

import pandas as pd

#Usamos la función crear CSVUsuarios
crearCSVUsuarios(usuarios,'BDUsuarios.csv')
# creando un dataframe desde una CSV
dataFrameUsuarios = pd.read_csv('data/BDUsuarios.csv')
# convertir el DF en Tabla html
crearTabla(dataFrameUsuarios,'usuarios')
#Se filtran los datos
#Buscar los sembradores mujeres>40 años y ganen entre minimo y 2 minimos
filtroUno = dataFrameUsuarios.query('(Edad>40) and (Genero=="f") and (Salario>=1160000 and Salario<=2320000)')     
print(filtroUno)
#Buscar los sembradores menores<20 años
filtroDos = dataFrameUsuarios.query('(Edad<=20)')     
print(filtroDos)
#Buscar los sembradores hombres>50 años
filtroTres = dataFrameUsuarios.query('(Edad>50)and(Genero=="m")')     
print(filtroTres)
# convertir el DF en Tabla html
crearTabla(filtroUno,'mujeresMayores')
crearTabla(filtroDos,'sembradoresMenores')
crearTabla(filtroTres,'sembradoresHombres')
