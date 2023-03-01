class Rectangle:
    
    def __init__(self,largeur,hauteur) :
          self.Largeur = largeur
          self.Hauteur  = hauteur
          
    def Afficher(selef):
            print(selef.Hauteur)
            print(selef.Largeur)
    def aire(self):
        return self.Largeur*self.Hauteur
    def perimetre(self):
        return self.Hauteur+self.Largeur*3.14
    

ma_Rectangle=Rectangle(5,2)
ma_Rectangle.Afficher()
s1=ma_Rectangle.aire()
s2=ma_Rectangle.perimetre()
print(s1)
print(s2)   
    
    
            