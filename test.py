#matt culot et livio curati

from mission10 import *

################################################################################################################"
# melange de type de medias

l1 = LivreAudio("Sweden", "livreaudio1", Duree(0, 3, 36), "Minecraft OST")

v1 = Video("Sweden", "video1", Duree(0, 3, 36), '1080p')
        
m1 = Media("Revenge", "med1", Duree(0, 4, 24))

    
playliste5 = ListeLecture("Melange")

elements = [
        LivreAudio("Sweden", "livreaudio1", Duree(0, 3, 36), "Minecraft OST"),

        LivreAudio("Revenge", "livreaudio2", Duree(0, 4, 24), "Fallen Kingdoms"),
        
        Video("Sweden", "video1", Duree(0, 3, 36), '1080p'),
        
        Video("Revenge", "video2", Duree(0, 4, 24), '4k'),
        
        Media("Revenge", "med1", Duree(0, 4, 24)),
        
        Media("Journal d'un noob (tome 1)", "med2", Duree(2, 36, 21))
        ]

for element in elements:
    playliste5.ajouter(element)

    
    
    
###############################################################################################################"
# partie main
    
if __name__ == "__main__":

    m1.save()
    v1.save()
    l1.save()
    
    playliste5.save()
    