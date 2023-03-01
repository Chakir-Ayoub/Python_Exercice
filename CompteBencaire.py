class CompteBancaire:
    def __init__(self,Nom_Titulaire,solde):
        self.nom_Titulaire = Nom_Titulaire
        self.Solde = solde
    def afficher(self):
        print("nom :", self.nom_Titulaire , "solde :" , self.Solde)
    def depot(self,montant) :
         self.Solde+=montant
    def  retrait(self,montant) :
        self.Solde-=montant
    def AfficherSold(self):
        print('Le Solde du Compte de ',self.nom_Titulaire,' est de : ',self.Solde)

Compte=CompteBancaire('Chakir',500)
Compte.depot(500)
Compte.retrait(10050)
Compte.afficher()
Compte.AfficherSold()
