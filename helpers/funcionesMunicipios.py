import random
from data.municipios import municipiosAntioquia,arboles

def randomMunicipios():
    combinaciones = []
    
    for i in range(2000):
        
        municipio=random.choice(municipiosAntioquia)
        arbol=random.choice(arboles)
        cantidad=random.randint(100,1000)
        siembra= [municipio,arbol,cantidad]       
        combinaciones.append(siembra)
    return combinaciones