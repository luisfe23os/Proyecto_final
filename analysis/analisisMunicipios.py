from data.ListaMunicipios import combinaciones
from helpers.crearCSV import crearCSVMunicipiosArboles
from helpers.crearHTML import crearTabla
from helpers.crearPDF import crear_pdf
import pandas as pd

#crear CSV
crearCSVMunicipiosArboles(combinaciones,'BDMunicipiosArboles.csv')

#crear dataframe
dataframeMunicipios=pd.read_csv('data/BDMunicipiosArboles.csv')

#Crear filtro municipios con mas de 90 arboles
filtroMa90=dataframeMunicipios.query('(Cantidad>90) ')

#municipios con tipo de arbol ceibas 
filtroCeibas=dataframeMunicipios.query('(Arboles=="ceibas")')

#municipios con menor siembra menor  10
filtroMenor=dataframeMunicipios.query('(Cantidad<10) ')

#convertir a html

crearTabla(dataframeMunicipios,'Municipios')
crearTabla(filtroMa90,'Smayor')
crearTabla(filtroCeibas,'Ceibas')
crearTabla(filtroMenor,'Smenor')

#Convertir a pdf
crear_pdf('tables/Municipios.html',output_path="pdf/ListaMunicipios.pdf")
crear_pdf('tables/Smayor.html',output_path="pdf/Municipiosdemayorsiembra.pdf")
crear_pdf('tables/Ceibas.html',output_path="pdf/SiembredeCeibas.pdf")
crear_pdf('tables/Smenor.html',output_path="pdf/Municipiosdemenorsiembra.pdf")
          