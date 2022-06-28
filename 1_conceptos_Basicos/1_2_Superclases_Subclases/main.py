# Conceptos basicos de clases y objetos
# una subclase hereda todo de una superclase

class Madre:
    def __init__(self):
        print(f"Soy madre")
        
class Hijo(Madre):
    pass

hijo=Hijo()