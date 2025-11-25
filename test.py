"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 14 novembre 2025
matt culot et livio curati
"""

from mission9 import *

############################################################################################################################################"
#media

playliste1 = ListeLecture("Minecraft")

medias = [
        Media("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1)),
        Media("Sweden", "C418", Duree(0, 3, 36)),
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

for media in medias:
    playliste1.ajouter(media)

########################################################################################################################
# Livres audio

playliste2 = ListeLecture("Livres audio Minecraft")

livres_audio = [
        LivreAudio("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21), editeur="404 Éditions"),
        ]

for livre_audio in livres_audio:
    playliste2.ajouter(livre_audio)

############################################################################################
# videos

playliste3 = ListeLecture("Videos")

videos = [
        Video("Tuto installation Minecraft (100% gratuit!!)", "LeCrafteur", Duree(0, 10, 1), '720p'),
        Video("Sweden", "C418", Duree(0, 3, 36), '1080p'),
        Video("Revenge", "CaptainSparklez", Duree(0, 4, 24), '4k')
        ]
for video in videos:
    playliste3.ajouter(video)

############################################################################################
#objets pour la classe chanson

playliste4 = ListeLecture("Chansons")

chansons = [
        Chanson("Sweden", "C418", Duree(0, 3, 36), "Minecraft OST", None),

        Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), "Fallen Kingdoms", ["Villageois", "Herobrine"]),

        Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), None, ["Villageois", "Herobrine"])
        ]

for chanson in chansons:
    playliste4.ajouter(chanson)

################################################################################################################"
# melange de type de medias
    
playliste5 = ListeLecture("Melange")

elements = [
        Chanson("Sweden", "C418", Duree(0, 3, 36), "Minecraft OST", None),

        Chanson("Revenge", "CaptainSparklez", Duree(0, 4, 24), "Fallen Kingdoms", ["Villageois", "Herobrine"]),
        
        Video("Sweden", "C418", Duree(0, 3, 36), '1080p'),
        
        Video("Revenge", "CaptainSparklez", Duree(0, 4, 24), '4k'),
        
        Media("Revenge", "CaptainSparklez", Duree(0, 4, 24)),
        
        Media("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21))
        ]

for element in elements:
    playliste5.ajouter(element)
    
###############################################################################################################"
# partie main

def afficher_playliste(playliste):
    print(playliste)
    
if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Media ***\n")
    afficher_playliste(playliste1)
    playliste1.print_taille()
    
    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE LivreAudio ***\n")
    afficher_playliste(playliste2)
    playliste2.print_taille()
    
    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE Video ***\n")
    afficher_playliste(playliste3)
    playliste3.print_taille()
    
    print("\n*** TEST DE LA CLASSE ListeLecture ET DE LA CLASSE chanson ***\n")
    afficher_playliste(playliste4)
    playliste4.print_taille()
    
    print("\n*** TEST DE LA CLASSE ListeLecture ET DES 3 AUTRES CLASSES ***\n")
    afficher_playliste(playliste5)
    playliste5.print_taille()
    
    try:
        V1 = Video("Journal d'un noob (tome 1)", "Cube Kid", Duree(2, 36, 21), '180000p') #tester le raise de la classe video
    except ValueError:
        print("test du raise de la resolution de Video ok")
        
    
    

