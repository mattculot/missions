class Duree :
    
    def __init__(self,h,m,s):
    """
    @pre: h, m et s sont des entiers positifs (ou zéro)
          m et s sont < 60
    @post: Crée une nouvelle durée en heures, minutes et secondes.
    """
    self.h = heure
    self.m = minute
    self.s = seconde
    if self.s < 60:
        self.m += 1
    if self.m < 60:
        self.h +=
    pass

    def to_secondes(self):
    """
    @pre:  -
    @post: Retourne le nombre total de secondes de cette instance de Duree (self).
    Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
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