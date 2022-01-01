class Vecteur2d : #Classe principale Vecteur 2d
    x = 0
    y = 0

    def __init__(self,x,y) : #Methode pour define les variable
        self.x = x
        self.y = y
    
    def show(self): #Fonctin afficher les Objects
        return "Vecteur: x="+str(self.x)+" ,y= "+str(self.y)+" ."
    
#la surcharge de 2 vecteurs 
    def __add__(self,other):
        X = self.x + other.x
        Y = self.y + other.y
        p = Vecteur2d(X,Y)
        return p


V1 = Vecteur2d(2,2) #Object 1
print(V1.show())
V2 = Vecteur2d(4,3) #Object 2
print(V2.show())

V3 = V1 + V2
print(V3.show())


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

