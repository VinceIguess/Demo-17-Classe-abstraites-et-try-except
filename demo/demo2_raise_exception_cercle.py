class cercle:
    # Le constructeur soulève une erreur si la valeur passée en paramètre est négative.
    def __init__(self,p_rayon) -> None:
        if p_rayon <= 0 : 
            raise ValueError("Le rayon doit être sup à 0")
        
        self._rayon = p_rayon




c1 = cercle(-35)
print(c1._rayon)