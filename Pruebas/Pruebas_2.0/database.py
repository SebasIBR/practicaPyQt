import numpy as np
# import shutil
# fuente= "Pruebas_2.0/base.txt"
# destino= "Pruebas_2.0/base2.txt"
database= [(1, 'Leticia', 1, 'Amazonas'),(2,'Chacha',1,'Amazonas'),(3, 'Medellin', 2, 'Antioquia')]
departamentos=["Amazonas","Antioquia"]
colores=["Rojo","Verde","Azul","Amarillo"]
#Primer indice id del municipio
#Segundo indice nombre del municipio
#Tercer indice id del departamento
#Cuarto indice nombre del departamento
def Guardar(departamento,municipio,color,estado):
    if estado == True:
        new=np.array(departamento)
        new2=np.array(municipio)
        new3=np.array(color)
        archivo=open("Pruebas_2.0/base.txt","w")
        contenido=str(new)
        contenido2=str(new2)
        contenido3=str(new3)
        archivo.write(contenido + '\n' )
        archivo.write(contenido2 + '\n')
        archivo.write(contenido3)
        archivo.close()
    else:
        print("Los datos no fueron cambiados")
# shutil.copyfile(fuente, destino)
    
with open("Pruebas_2.0/base.txt") as archivo_defecto: 
    lineas= archivo_defecto.readlines()
    lineas= list(map(lambda l: l.rstrip('\n'),lineas))
    defecto_departamento=lineas[0]
    defecto_municipio=lineas[1]
    defecto_color=lineas[2]