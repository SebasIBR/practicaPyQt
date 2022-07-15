import numpy as np
lista_departamentos=["ANTIOQUIA","BOGOTA","VALLE DEL CAUCA"]
Estandar_defecto=[]

def nuevo_departamento(departamento):
    global Estandar_defecto
    new=np.array(departamento)
    archivo=open("Pruebas/lista_dep.txt","w")
    contenido=str(new)
    archivo.write(contenido)
    archivo.close()

departamento=open("Pruebas/lista_dep.txt","r")
defecto_departamento=departamento.read()
defec_depar=str(defecto_departamento)
print("El departamento por defecto es",defec_depar)
