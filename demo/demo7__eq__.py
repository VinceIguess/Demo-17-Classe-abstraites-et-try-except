
class adresse_IP:
    def __init__(self, p_adresse_IP:str):
        self.adresse = p_adresse_IP

    @property
    def adresse(self) : return self._adresse

    @adresse.setter
    def adresse(self, new_ip:str) : 
        ip_split = new_ip.split('.')
        if len(ip_split) != 4 : raise ValueError
        for i in ip_split :
            if int(i) < 0 or int(i) > 255 : raise ValueError
        self._adresse = new_ip

    def __eq__(self, autre) -> bool:
        est_egal = self.adresse == autre.adresse
        return est_egal

    def __str__(self) :
        return self.adresse


# Pour pouvoir comparer deux objets, il faut définir les méthodes magiques utilisées lors de comparaisons.

if __name__ == '__main__' :
    ip1 = adresse_IP("255.210.210.0")
    ip2 = adresse_IP("255.210.210.0")
    print( ip1 == ip2 )
    ip2 = adresse_IP("8.8.8.8")
    print( ip1 == ip2 )
