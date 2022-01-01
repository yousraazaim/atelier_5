class Personne : #Classe principale Personne
    _nom = ""
    _prenom = ""
    _age = 0
    _cne = 0
    _moyenne = 0

    def __init__(self,nom,prenom,age,cne,moyenne) : #Methode pour define les variable
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._cne = cne
        self._moyenne = moyenne

    def toString(self): #Fonctin afficher les Objects
        return "[Nom: "+self._nom+" ,prenom: "+self._prenom+" ,age: "+str(self._age)+" ,CNE: "+str(self._cne)+" ,moyenne "+str(self._moyenne)+" ]"

P1= Personne("azemat","zainab",20,96969,15) #Object 1
P2= Personne("el rhaiti","khaoula",34,952,17)         #Object 2
P3= Personne("zanzan","hanhan",22,57343,92)       #Object 3


mylist = []  #Declaration de la liste

mylist.append(P1) #Remplier la liste
mylist.append(P2)
mylist.append(P3)



for obj in mylist :
    print(obj.toString())

print("\nresultat de tri: \n")

mylist.sort(key=lambda x: x._age)

for obj in mylist :
    print(obj.toString())







