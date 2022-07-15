numero=[]
nnumero_2=["Mundo"]
def vv(num):
    global numero
    return numero.append(num)

vv("hola")

total = nnumero_2+numero
nuevo="".join([str(_) for _ in numero])
print(total)

