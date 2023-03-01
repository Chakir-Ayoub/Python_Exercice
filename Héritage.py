class Personne:
    def __init__(self,nom,age,sexe,adresse):
        self.Nom=nom
        self.Age=age
        self.Sexe=sexe
        self.Adresse=adresse
    def presentation(self):
        print("Nom : ",self.Nom," Age : ",self.Age," Sexe : ",self.Sexe," Adresse : ",self.Adresse)

class Employe(Personne):
    def __init__(self, nom, age, sexe, adresse,num_employe,salaire):
        super().__init__(nom, age, sexe, adresse)
        self.Num_employe=num_employe
        self.Salaire=salaire
    def presentation(self):
        print(super().presentation(),' Num_Employee : ',self.Num_employe," Slaire : ",self.Salaire)
        

Personne=Personne('Mohamed',26,'F','Saada')
Personne.presentation()
Employe=Employe('Ayoub',22,'Mr','AFAQ1',1,80000)
Employe.presentation()
        