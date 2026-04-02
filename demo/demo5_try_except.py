class Employe:
    def __init__(self, pSalaire) -> None:
        self._salaire = pSalaire

    @property
    def salaire(self):
        return self._salaire
    
    @salaire.setter
    def salaire(self, nvx_salaire) :
        try :
            if nvx_salaire > self._salaire :
                1 / 0
                self._salaire = nvx_salaire
                print("Imprimer uniquement si pas d'erreur")

        except TypeError as e:
            nvx_salaire = input("Veuillez rentrer un nombre")
            self.salaire = int(nvx_salaire)

        except Exception as e:
            print(f"Erreur : {e}" )
        
        else : 
            print("ce bloc est exécuté seulement s'il n'y a pas d'exceptions")

        finally :
            print("Ce bloc est toujours exécuté.") 


emp = Employe(500)
print(emp.salaire)
emp.salaire = "waopeirj"
emp.salaire = 2000
print(emp.salaire)
emp.salaire = 984654
print(emp.salaire)