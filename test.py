"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 14 novembre 2025
"""

from mission9 import *

#
# FOURNI DE BASE
#

playliste1 = ListeLecture("Minecraft")

medias = [
        Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)),
        Media("Sweden", "C418", Duree(0, 3, 36)),
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

for media in medias:
    playliste1.ajouter(media)

medias = [
        Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)),
        Media("Sweden", "C418", Duree(0, 3, 36)),
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

playliste2 = ListeLecture("Livres audio Minecraft")

livres_audio = [
        LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21), editeur="404 Éditions"),
        ]

for livre_audio in livres_audio:
    playliste2.ajouter(livre_audio)

def afficher_playliste(playliste):
    print(playliste)
    
    
############################################################################################
liste_videos = [
        Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '720p'),
        Video("Sweden", "C418", Duree(0, 3, 36), '1080p'),
        Video("Revenge", "CaptainSparklez", Duree(0, 4, 24), '4k'),
        ]
#V1 = Video("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21), '180000p')

############################################################################################
C1 = chanson("Sweden", "C418", Duree(0, 3, 36), "Minecraft OST", None)

C2 = chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), "Fallen Kingdoms", ["Villageois", "Herobrine"])

C3 = chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), None, ["Villageois", "Herobrine"])



if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Media ***\n")
    afficher_playliste(playliste1)
    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE LivreAudio ***\n")
    afficher_playliste(playliste2)
    
    print("test pour la classe video")
    print(liste_videos)
    #print(V1) #l'erreur c'est normal ca veut dire que ca fonctionne bien
    print(C1)
    print(C2)
    print(C3)
    
    
    

