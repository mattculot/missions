class Media:
    def __init__(self, titre, auteur, duree):
        """
        @pre:
            - titre est un string
            - auteur est un string
            - duree est une instance de 'Duree'
        @post: un média lisible générique
        """
        self.titre = titre
        self.auteur = auteur
        self.duree = duree

    def taille(self):
        """Renvoie la taille du média en méga-octets"""
        return self.duree.to_secondes()*0.05

    def __eq__(self, other):
        if not isinstance(other, Media): return False
        return self.titre == other.titre and self.auteur == other.auteur

    def __str__(self):
        s = "({}, {}MB) '{}' par {}".format(self.duree,self.taille(),self.titre,self.auteur)
        return s
    
    def __lt__(self, other):
        
        if not isinstance(other, Media):
            return False
    
        return self.auteur < other.auteur

#teste media +- ca je pense 
med = Media("matt", "livio", 23)
meda = Media("livio", "matt", 25)
print(med<meda)
print(meda<med)