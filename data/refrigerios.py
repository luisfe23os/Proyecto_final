import pandas as pd
import random

refrijerios =[]

for i in range(3000):
    nombre = random.choice(['chicharron','papas','longaniza','huevos revueltos'])
    precio = random.randint(15000,40000)
    cantidad = random.randint(1,100)
    costoTotal = (cantidad*precio)
    refrijerio=[nombre,precio,cantidad,costoTotal]
    refrijerios.append(refrijerio)
    
# print(refrijerios)

tabla = pd.DataFrame(refrijerios),

# print (tabla)