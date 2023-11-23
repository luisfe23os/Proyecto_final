import pandas as pd
import random

usuarios=[]

for i in range(10):
    nombre = random.choice(['juan','andrea','sara','jorge'])
    contrasena = random.choice(['admin123','arboles000'])
    edad = random.randint(18,62)
    salario = random.randint(1160000,3000000)
    genero = random.choice(['m','f'])
    usuario=[nombre,contrasena,edad,salario,genero]
    usuarios.append(usuario)
    
# print(usuarios)

tabla = pd.DataFrame(usuarios),

# print (tabla)