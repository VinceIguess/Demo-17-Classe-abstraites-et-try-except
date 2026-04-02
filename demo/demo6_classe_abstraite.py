from abc import ABC, abstractmethod
import json
# on ne peut pas créer d'instances d'une classe contenant une méthode abstraite
class Employe(ABC):
    liste_employe = []
    _next_ID = 1000
    def __init__(self,p_nom, p_prenom, p_salaire_de_base):
        self._nom = p_nom
        self._prenom = p_prenom
        self.salaire = p_salaire_de_base
        self.ID = self._next_ID
        self._next_ID += 1
        self.liste_employe.append(self)

    @property
    def nom_complet(self) :
        return f"{self._prenom} {self._nom}"
    
    @abstractmethod
    def calculer_paie(self):
        pass

    @classmethod
    def afficher_liste_employe(cls):
        print(json.dumps(cls.liste_employe, indent = 4))       

    @staticmethod
    def info_retraite():
        return "Il faut avoir 65 et plus ou avoir 35 ans d'ancienneté pour se qualifier."
      


class Programmeur(Employe):
    def __init__(self, p_nom, p_prenom, p_salaire_de_base,p_language_favori=""):
        super().__init__(p_nom, p_prenom, p_salaire_de_base)
        self.language_favori = p_language_favori

    def calculer_paie(self):
        return self.salaire
    
class Vendeur(Employe):
    def __init__(self, p_nom, p_prenom, p_salaire_de_base, p_commission):
        super().__init__(p_nom, p_prenom, p_salaire_de_base)
        self.commission = p_commission
    #Au bébut: pas de calculer_paie... donc Vendeur est une classe abstraite
    
    #On redéfinie la fonction calculer_paie -> Vendeur n'est plus ue classe abstraite
    def calculer_paie(self):
        return self.salaire + self.commission
    
if __name__ == "__main__" :
    # on ne peut pas créer d'instances d'une classe contenant une méthode abstraite
    emp1 = Employe("Desjardins","Yvon", 70000)
    emp2 = Programmeur("Tremblay", "Ana",80000, p_language_favori="Python")
    print(emp2.calculer_paie())
    emp3 = Vendeur("Marley", "Bob", 40000,20000)
    print(emp3.calculer_paie())










#employe1.test_abs()

#employe2 = Employe("Bartholemy","Duchamp")
#prog1 = Programmeur("Desjardins","Carole","Python")
#prog1.test_abs()

# for emp in Employe.liste_employe: 
#     print(f'{emp.prenom} {emp.nom} {emp.ID}')
#     emp.test_abs()


#print("\n")