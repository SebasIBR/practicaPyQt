class Madre:
    def __init__(self):
        print("Lina")

class Padre:
    def __init__(self):
        print("Harry")
        
class Hermano:
    def __init__(self):
        super().__init__()
        print("Cristian")

class Yo(Madre,Padre,Hermano):
    def __init__(self):
        Madre.__init__(self)
        Padre.__init__(self)
        Hermano.__init__(self)
        print("sebastian")
        
yo=Yo()