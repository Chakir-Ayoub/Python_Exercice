def palindrome():
    nom=input("Donner une chaine de caractére :")
    nom1="".join(reversed(nom))
    print(nom1)
    if(nom==nom1):
        return True
    else:
        return False
        
resultat=palindrome()
print(resultat)