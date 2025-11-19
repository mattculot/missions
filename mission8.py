class Duree :

    def __init__(self,h,m,s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
            m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.h = h
        self.m = m
        self.s = s
        if self.s > 60:
            self.m += 1
        if self.m > 60:
            self.h += 1
        pass

    def to_secondes(self):
        
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        compte_sec_tot = self.s + (self.m*60) + (self.h*3600)
        return compte_sec_tot
    
    def  afficher_secondes(self):
        compte_sec_tot = self.to_secondes()
        print("une durée de " + str(self.h) + "h " + str(self.m) + "m " + str(self.s) + "s compte " + str(compte_sec_tot) + " secondes")

    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
               et la durée d passée en paramètre.
               Cette valeur renovoyée est positif si cette durée (self)
               est plus grand que la durée d, négatif sinon.
        
        """
        nbr_sec_d = d.to_secondes()
        compte_sec_tot = self.s + (self.m*60) + (self.h*3600)
        diff = compte_sec_tot - nbr_sec_d
        return diff
    
    def afficher_delta(self, d):
        diff = self.delta(d)
        print(str(diff) + " secondes")
        
    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
               d passée en paramètre; retourne False sinon.
        """
        diff = self.delta(d)
        if diff <= 0:
            return False
        else:
            return True
        
    def ajouter(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
               corrigée de manière à ce que les minutes et les secondes soient
               dans l'intervalle [0..60[, en reportant au besoin les valeurs
               hors limites sur les unités supérieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
               Ne retourne pas une nouvelle durée mais modifié la durée self.
        """

        self.h = self.h + d.h
        self.m = self.m + d.m
        self.s = self.s + d.s
        
        while self.s >= 60:
            self.m += 1
            self.s -= 60
            
        while self.m >= 60:
            self.h += 1
            self.m -= 60

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        temps = "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)
        return temps
 

class Chanson :
    
    def __init__(self,t,a,d):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
        un auteur a et une durée d.
        """
        self.t = t
        self.a = a
        self.duree = d
        
    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
        "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        descrip = self.t + " - " + self.a + " - " + str(self.duree)
        return descrip
    pass

class Album :
    
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
        et avec une liste de chansons vide.
        """
        chanson = []
        self.numero = numero
        # album = self.numero + chanson + descrip
        # return album
    pass

if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    pass
    # A COMPLETER PAR LES ETUDIANTS
    # (mettez ici votre code pour créer les albums à partir de la lecture du fichier
