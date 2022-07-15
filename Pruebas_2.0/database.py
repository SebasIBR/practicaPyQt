import numpy as np

database= [(1, 'Leticia', 1, 'Amazonas'),(2,'Chacha',1,'Amazonas'),(3, 'Medellin', 2, 'Antioquia')]
departamentos=["Amazonas","Antioquia"]
#Primer indice id del municipio
#Segundo indice nombre del municipio
#Tercer indice id del departamento
#Cuarto indice nombre del departamento
def Guardar(departamento,municipio):
    new=np.array(departamento)
    new2=np.array(municipio)
    archivo=open("Pruebas_2.0/base.txt","w")
    contenido=str(new)
    contenido2=str(new2)
    archivo.write(contenido + '\n' )
    archivo.write(contenido2)
    archivo.close()
    
with open("Pruebas_2.0/base.txt") as archivo_defecto: 
    lineas= archivo_defecto.readlines()
    lineas= list(map(lambda l: l.rstrip('\n'),lineas))
    defecto_departamento=lineas[0]
    defecto_municipio=lineas[1]

print("departamento",defecto_departamento)
print("municipio",defecto_municipio)
    
# departamento=open("Pruebas_2.0/base.txt","r")
# defecto_departamento=departamento.readlines(0)
# defecto_municipio=departamento.readlines(1)
# defec_depar=str(defecto_departamento)
# defec_muni=str(defecto_municipio)
# print("El departamento por defecto es",defec_depar)
# print("El municipio por defeto es",defec_muni)