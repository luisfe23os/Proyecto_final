from data.refrigerios import refrijerios
from helpers.crearCSV import crearCSVRefrigerios
from helpers.crearHTML import crearTabla
from helpers.crearPDF import crear_pdf

import pandas as pd

#Usamos la función crear CSVRefrigerios
crearCSVRefrigerios(refrijerios,'BDRefrigerios.csv')

# creando un dataframe desde una CSV
dataFrameRefrigerios = pd.read_csv('data/BDRefrigerios.csv')

#buscar refrigerios costo unitario > 20000
filtroCostoUnitario = dataFrameRefrigerios.query('(Precio>20000)')     
print(filtroCostoUnitario)

#Buscar refrigerios costo total <1000000
filtroCostoTotal = dataFrameRefrigerios.query('(CostoTotal<1000000)')     
print(filtroCostoTotal)
#Buscar refrigerio cantidad<1000
filtroCantidad = dataFrameRefrigerios.query('(Cantidad<100)')     
print(filtroCantidad)

# convertir el DF en Tabla html
crearTabla(dataFrameRefrigerios,'refrigerios')
crearTabla(filtroCostoUnitario,'CostoUnitarioRefrigerios')
crearTabla(filtroCostoTotal,'CostoTotal')
crearTabla(filtroCantidad,'CantidadRefrigerio')

#convertir HTML en PDF
crear_pdf('tables/CostoTotal.html',output_path="pdf/CostoTotalRefrigerios.pdf")
crear_pdf('tables/refrigerios.html',output_path="pdf/Refrigerios.pdf")