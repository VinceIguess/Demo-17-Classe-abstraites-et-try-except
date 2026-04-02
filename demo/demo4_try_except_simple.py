employes:list[dict] = [ {"id" :1 , "nom":"Yves Beauchamps" , "salaire": 50000  },
                        {"id" :2 , "nom":"Ana Tremblay" , "salaire": 55000 },
                        {"id" :3 , "nom":"Éric Mathieu" , "salaire": 35000 },
                        {"id" :4 , "nom":"Vincent Carrier" , "salaire": "N\\A" },
                        {"id" :5 , "nom":"Pierre Gallant" , "salaire": 132000  }]


# On veut calculer la moyenne des salaires :

def calcul_moyenne_simple(p_data:list[dict]) :
    moy_simple:int = 0
    for e in p_data :
        moy_simple += e['salaire']
    moy_simple /= len(p_data)
    return moy_simple

def calcul_moyenne_gestion_exception(p_data:list[dict]) :
    # même fonction, mais en gèrant les exceptions.
    moy_simple:int = 0
    cpt:int = 0
    for e in p_data :
        try: #doit être dans la boucle 
            moy_simple += e['salaire']
            cpt += 1
        except Exception as er:
            print(f"Erreur dans ligne {e}")
            print(er)
    moy_simple /= cpt
    return moy_simple

if __name__ == "__main__" : 
    moyenne = calcul_moyenne_simple(employes)
    print(f"La moyenne est de {moyenne}")