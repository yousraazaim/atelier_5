class Rectangle():
    nom = ""
    x = 0
    y = 0
    def __init__(self, x, y,nom):
        self.nom = nom
        self.x = x
        self.y = y    

    def show(self):
        return "le "+self.nom+" est de longeur: "+str(self.x)+" et de largeur: "+str(self.y)+"."

    def surface(self):
        return "Sa surface est: "+(str(self.x * self.y))

class Carre(Rectangle):
    def __init__(self,x,nom):
        super().__init__(self,x)
        self.nom = nom

    def show(self):
        return "le "+self.nom+" est de cote: "+str(self.x)+"."
    
    def surface(self):
            return "La surface du carre est: "+(str(self.x * self.x))


R = Rectangle(5,8,"Rectangle")
print(R.show())
print(R.surface())

