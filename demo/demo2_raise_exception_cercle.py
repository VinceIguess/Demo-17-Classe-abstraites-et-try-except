class cercle:
    # Le constructeur soulève une erreur si la valeur passée en paramètre est négative.
    def __init__(self,p_rayon) -> None:
        if p_rayon <= 0 : 
            raise ValueError("Le rayon doit être sup à 0")
        
        self._rayon = p_rayon



try :    
    c1 = cercle(-35)
    print(c1._rayon)
except ValueError:
    print("Oops! Le rayon n'est pas valide")
except TypeError as e:
    print(f"Erreur de type : {e}")
else: #exécuté si il n'y a pas d'exceptions
    print("Yay, le rayon est valide!")
    print(c1._rayon)
finally:
    print("bloc toujours exécuté")