import csv

def crearCSVUsuarios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='', encoding='utf-8') as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Nombre','Contraseña','Edad','Salario','Genero'])
        writer.writerows(lista)
        
def crearCSVRefrigerios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w', newline='',encoding='utf-8') as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Nombre','Precio','Cantidad','CostoTotal'])
        writer.writerows(lista)
        
def crearCSVMunicipiosArboles(lista,nombreArchivo):
    print(lista)
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8',) as archivoCSV:
        write =csv.writer(archivoCSV)
        write.writerow(['Nombre','Arboles','Cantidad'])
        write.writerows(lista)