class Employe :
    def __init__(self, p_nom:str, p_prenom:str, p_salaire:int):
        self.nom = p_nom
        self.prenom = p_prenom
        self._salaire = p_salaire
    
    @property
    def salaire(self) :  return self._salaire

    @salaire.setter
    def salaire(self, p_nvx_salaire) :
        if p_nvx_salaire < self._salaire :
            raise ValueError("Le nouveau salaire doit être plus grand.")
        else :
            self._salaire = p_nvx_salaire

chimiste = Employe("Bela", "Tapputi", 45000)
chimiste.salaire = 3000


