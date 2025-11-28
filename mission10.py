class Duree:
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

    def to_secondes(self):
        """
        @post: renvoie la durée convertie en secondes (un entier)
        """
        return self.h * 3600 + self.m * 60 + self.s

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
        sum = self.to_secondes() + d.to_secondes()
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
        Méthode pour renvoyer la taille du média par seconde de durée en méga-octets.
        """
        raise NotImplementedError("Method must be implemented by subclasses")
        # Cette méthode n'est pas implémentée ici mais devrait être implémentée
        # dans les sous-classes, en fonction du type de média.

    def type_media(self):
        """
        Renvoie un string indiquant le type de média.
        """
        return str("Média")
        # Renvoit un string générique ici
        # qui sera spécialisé dans les sous-classes

    def __str__(self):
        """
        Renvoie un string en format "(hh:mm:ss, Type) 'Titre' par Auteur"
        décrivant les détails de ce média.
        """
        s = "({}, {}) '{}' par {}".format(self.duree, self.type_media(), self.titre, self.auteur)
        return s
    
    def save(self):
        """
        Sauvegarde les informations du livre audio dans un fichier texte.
        Le nom du fichier est composé comme suit : 'auteur_titre_LivreAudio.txt'.
        Le fichier contient chaque attribut sur une ligne séparée.
        """
        nom_fichier = self.auteur + "_" + self.titre + "_" + self.type_media()

        contenu = "Titre : " + self.titre + "\n" \
                  + "Auteur : " + self.auteur + "\n" \
                  + "Durée : " + str(self.duree) + "\n" \

        try:
            with open(nom_fichier, "w") as file:
                file.write(contenu)
        except Exception as e:
            print("Erreur lors de l'écriture du fichier :", e)

        return nom_fichier, contenu

class ListeLecture:
    """
    Représente une compilation nommée de médias.
    """

    def __init__(self, name):
        """
        @pre:  name est un string
        @post: Une instance de 'ListeLecture' est créée avec le nom 'name'
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

    def save(self):
        """
        Sauvegarde les informations du livre audio dans un fichier texte.
        Le nom du fichier est composé comme suit : 'auteur_titre_LivreAudio.txt'.
        Le fichier contient chaque attribut sur une ligne séparée.
        """
        i = 1
        for media in self.medias:
            try:
                media, contenu = media.save()
                with open(self.name, "a") as file:
                    file.write("[{}] {}\n{}\n".format(i ,str(media), contenu))
                    
            except Exception as e:
                print("une erreur est survenue", e)
                
            i += 1
        return self.name
    
    

class LivreAudio(Media):
    """
    Représente un livre audio. En plus des attributs présents dans 'Media',
    'LivreAudio' inclut aussi un attribut représentant l'éditeur du livre.
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

    def save(self):
        """
        Sauvegarde les informations du livre audio dans un fichier texte.
        Le nom du fichier est composé comme suit : 'auteur_titre_LivreAudio.txt'.
        Le fichier contient chaque attribut sur une ligne séparée.
        """
        nom_fichier, contenu = super().save()
        contenu += "Editeur: " + self.editeur + "\n"
        
        with open(nom_fichier, "a") as file:
            file.write("Editeur: " + self.editeur + "\n")

        return nom_fichier, contenu

class Video(Media):
    """
    Représente une vidéo que l'on pourrait visionner sur notre logiciel
    de lecture multimédia.
    """

    def __init__(self, titre, auteur, duree, resolution):
        if resolution not in ("720p", "1080p", "4K", "4k"):
            raise ValueError("Resolution not correct")
        super().__init__(titre, auteur, duree)
        self.resolution = resolution

    def taille_par_seconde(self):
        taille = 0.1
        facteur = 1
        if self.resolution == "720p":
            facteur = 2
        elif self.resolution == "1080p":
            facteur = 5
        elif self.resolution == "4K":
            facteur = 10
        return taille * facteur

    def type_media(self):
        return str("Vidéo")

    def __str__(self):
        s = super().__str__() + " (" + self.resolution + ")"
        return s
    
    def save(self):
        """
        Sauvegarde les informations du livre audio dans un fichier texte.
        Le nom du fichier est composé comme suit : 'auteur_titre_LivreAudio.txt'.
        Le fichier contient chaque attribut sur une ligne séparée.
        """
        nom_fichier, contenu = super().save()
        contenu += "Resolution: " + self.resolution + "\n"
        
        with open(nom_fichier, "a") as file:
            file.write("Resolution: " + self.resolution + "\n")
            

        return nom_fichier, contenu