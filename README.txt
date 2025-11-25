# Livio Curati et Matt Culot
Le programme présenté met en place trois classes principales permettant de gérer des informations musicales : Duree, Chanson et Album. 

La classe Duree permet de représenter une durée en heures, minutes et secondes. 
 
-- to_secondes() calcule le nombre total de secondes de d,

-- afficher_secondes() l’affiche.

-- delta(d) calcule la différence en secondes avec une autre durée.

-- apres(d) renvoie true ou false indiquant si la durée actuelle est plus longue qu’une autre.
 
-- ajouter(d) additionne une autre durée à la durée actuelle. 

-- La méthode spéciale __str__() affiche la duree au format "hh:mm:ss" avec toujours deux chiffres.


La classe Chanson représente une chanson, caractérisée par un titre, un auteur et une durée.


La classe Album permet de regrouper plusieurs chansons. 

-- La méthode add(chanson) ajoute une chanson à un album si le nombre de chansons dépasse 100 ou si la durée > 75 minutes, retourne False. Sinon, la chanson est ajoutée et retourne True. 

-- La méthode __str__() donne une représentation complète de l’album (numéro, chansons,...)


Dans la partie __main__, on lit le fichier music-db.txt et on créer les albums et on les affiches.


Notre fichier test effectue des tests pour toutes les méthodes des classes et vérifie que toutes les classes fonctionnent ensemble.