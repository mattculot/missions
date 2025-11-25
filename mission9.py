"""
Classes fournies pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 14 novembre 2025
"""
#Livio Curati et Matt Culot
class Duree :
    """
    Représente une durée dans le temps en format hh:mm:ss
    """    

    def __init__(self, h, m, s):
        """
        @pre:  h est un entier positif.
               m est un entier entre 0 (compris) et 60 (non compris)
               s est un entier entre 0 (compris) et 60 (non compris)
        @post: Une object de type 'Duree' est créé
        """
        self.h = h
        self.m = m
        self.s = s
        while self.s > 60:
            self.m += 1
            self.s -= 60
        while self.m >= 60:
            self.h += 1
            self.m -= 60

    def to_secondes(self):
        """
        @post: renvoie la durée convertie en secondes (un entier)
        """
        return self.h*3600 + self.m*60 + self.s

    def delta(self, d):
        """
        Renvoie la différence en secondes entre la durée 'self' et 'd'. 
        Peut être négative si la durée représentée par 'd' est plus
        grande que celle de 'self'.
        @pre:  d est une instance de 'Duree'
        @post: la différence en secondes entre 'self' et 'd'
               (la différence est négative si la durée 'd' est plus
                grande la durée 'self')
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self, d):
        """
        Renvoie l'ordre entre 2 durées.
        @pre:  d est une instance de 'Duree'
        @post: renvoie 'True' si la durée représentée par 'self' est
               strictement plus grande que celle représentée par 'd',
               renvoie 'False' sinon.
        """
        return self.delta(d) > 0

    def ajouter(self, d):
        """
        Ajoute la durée 'd' à 'self'.
        @pre:  d est une instance de 'Duree'
        @post: la durée représentée par 'self' est incrémentée par
               la durée représentée par 'd'
        """
        sum = self.to_secondes()+d.to_secondes()
        self.s = sum % 60
        self.m = sum // 60 % 60
        self.h = sum // 3600

    def __str__(self):
        """
        Revoie la représentation en string de la durée
        en format 'hh:mm:ss'
        """
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)

class Media:
    """
    Représente un média générique, comme une chanson, un livre audio ou une vidéo
    qui peut être 'joué' pour être écouté, lu ou regardé.
    """
    
    def __init__(self, titre, auteur, duree):
        """
        @pre:  titre est un string
               auteur est un string
               duree est une instance de 'Duree'
        @post: un média jouable générique
        """
        self.titre = titre
        self.auteur = auteur
        self.duree = duree

    def taille(self):
        """
        Renvoie la taille du média en méga-octets
        """
        return self.taille_par_seconde() * self.duree.to_secondes()

    def taille_par_seconde(self):
        """
        Renvoie la taille du média par seconde de durée en méga-octets
        """
        raise NotImplementedError("Method must be implemented by subclasses")
        # Cette méthode n'est pas implémentée ici mais devrait être implémentée
        # dans les classes filles, en fonction du type de média

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return str("Média")
        # Renvoit un string générique ici
        # qui sera spécialisé dans les classes filles

    def __str__(self):
        """
        Renvoie un string en format "(hh:mm:ss, Type) 'Titre' par Auteur"
        décrivant les détails de ce média.
        """
        s = "({}, {}) '{}' par {}".format(self.duree, self.type_media(), self.titre, self.auteur)
        return s

class ListeLecture:
    """
    Représente une compilation nommée de médias.
    """

    def __init__(self, name):
        """
        @pre:  name est un string
               id est un entier
        @post: Une instance de 'ListeLecture' ayant un identifiant unique. 
               Si 'id' est déjà utilisé par une autre instance, 
               alors une erreur 'ValueError' sera levée
        """
        self.id = 1
        self.name = name
        self.medias = []
        self.duree = Duree(0, 0, 0)

    def ajouter(self, media):
        """
        Ajoute 'media' à la liste de lecture
        @pre:  media est une instance de 'Media'
        @post: la liste de lecture comprend maintenant 'media'
        """
        self.medias.append(media)
        self.duree.ajouter(media.duree)

    def print_taille(self):
        """Imprime une liste des médias de cette liste avec leurs tailles en méga-octets"""
        total = 0
        for media in self.medias:
            try:
                taille = media.taille()
            except NotImplementedError:
                taille = None
            if taille is None:
                print("[Taille inconnue] " + media.titre)
            else:
                print("[{:.2f}MB] ".format(taille) + media.titre)
                total += taille
        print("TOTAL : {:.2f}MB\n".format(total))

    def __str__(self):
        s = "[#{}] {} ({} medias)\n".format(self.id, self.name, len(self.medias))
        i = 1
        for media in self.medias:
            s += "{:02}: ".format(i) + str(media) + "\n"
            i += 1
        return s

class LivreAudio(Media):
    """
    Représente un livre audio. En plus des attributs présents dans 'Media', 
    'LivreAudio' inclu aussi un attribut représentant l'éditeur du livre.
    """

    def __init__(self, titre, auteur, duree, editeur):
        """
        @pre:  titre est un string
               auteur est un string
               duree est une instance de 'Duree'
               editeur est un string
        @post: un livre audio ayant les propriétés demandées
        """
        super().__init__(titre, auteur, duree)
        self.editeur = editeur

    def taille_par_seconde(self):
        """
        Renvoie la taille de lecture par défaut d'un livre audio
        en méga-octets par seconde
        """
        return 0.01

    def type_media(self):
        """
        Renvoie un string indiquant le type de média
        """
        return "Livre Audio"

    def __str__(self):
        s = super().__str__() + ", édité par " + self.editeur
        return s
    
class Video(Media):

    def __init__(self, titre, auteur, duree, resolution):
        """pre: récupère les infos de média et une resolution
        post: crée un objet Video"""
        
        super().__init__(titre, auteur, duree)
        if resolution == '720p':
            self.resolution = '720p'
        elif resolution == '1080p':
            self.resolution = '1080p'
        elif resolution == '4k':
            self.resolution = '4k'
        else:
            raise ValueError
        
    def taille_par_seconde(self):
        """pre: la resolution de __init__
        post: retourne la taille par seconde en MO de la vidéo"""
        
        if self.resolution == '720p':
            return 0.1 * 2
        elif resolution == '1080p':
            return 0.1 * 5
        elif resolution == '4k':
            return 0.1 * 10
        
    def __str__(self):
        """Renvoie un string en format "(hh:mm:ss, Type) 'Titre' par Auteur (Resolution)"
        décrivant les détails de cette vidéo.
        """
        s = "({}, {}) '{}' par {} ({})".format(self.duree, self.type_media(), self.titre, self.auteur, self.resolution)
        return s
    
class chanson(Media):

    def __init__(self, titre, auteur, duree, album = None, feat = None):
        super().__init__(titre, auteur, duree)
        self.album = album
        if feat is not None:  #donc dans le cas où l'objet contient une liste 
            self.feat = feat  #feat =liste de string
        else:
            self.feat = []
    def type_media(self):
        return "Chanson"
        
    def taille_par_seconde(self):
        return 0.05

    def __str__(self):
        
        texte_feat = ""
        if self.feat:
            texte = ""
            for i in range(len(self.feat)):
                texte += self.feat[i]
                if i != len(self.feat):
                    texte += ", "
            texte_feat = " (feat. " + texte + ")"
            
        texte_album = ""
        if self.album:
            texte_album = "[Album : " + self.album + "]"
            
        
        s = "({}, {}) '{}' par {} {} {}".format(self.duree, self.type_media(), self.titre, self.auteur, texte_feat, texte_album)
        return s
        
        
        
