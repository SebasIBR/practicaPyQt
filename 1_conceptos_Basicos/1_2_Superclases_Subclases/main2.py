#las subclase sobreescribe los metodos para realizar sus propias acciones

class Madre:
    def __init__(self):
        print("Soy Madre")
        
class Hijo:
    def __init__(self):
        print("Soy Hijo")
        
hijo=Hijo()