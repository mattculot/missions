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
    
    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
               et la durée d passée en paramètre.
               Cette valeur renovoyée est positif si cette durée (self)
               est plus grand que la durée d, négatif sinon.
        
        """
        self.d = d
        nbr_sec_d = d.to_secondes()
        compte_sec_tot = self.s + (self.m*60) + (self.h*3600)
        diff = compte_sec_tot - nbr_sec_d
        print(diff)
        return diff
    
    def afficher_seconde(self):
        compte_sec_tot = to_secondes(self)
        print("une durée de " + str(self.h) + "h " + str(self.m) + "m " + str(self.s) + "s compte " + str(compte_sec_tot) + " secondes")

    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
               d passée en paramètre; retourne False sinon.
        """
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

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
 

class Chanson :
    
    # A COMPLETER PAR LES ETUDIANTS    
    pass

class Album :
    
    # A COMPLETER PAR LES ETUDIANTS
    pass

if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    pass
    # A COMPLETER PAR LES ETUDIANTS
    # (mettez ici votre code pour créer les albums à partir de la lecture du fichier