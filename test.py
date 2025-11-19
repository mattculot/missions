##############################
# Tests pour la classe Duree #
##############################
# Kim Mens, 30-10-2021, à compléter par les étudiants
#matt culot et livio curati

# Pour le moment, pour tester votre programme orienté objet
# vous allez encore utiliser les instructions "assert" comme
# dans les missions 5 à 7. 
# (Dans une mission futur nous introduirons le nouveau mécanisme
#  des tests unitaires qui est encore mieux approprié pour tester
#  du code orienté objet.)

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree(0,0,0)
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
d3 = Duree(10,20,59)
#Duree(heure, minute, secondes)

# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS
    
# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    #delta(self, d), on soustrait d à self et on retorune la valeur (vérif que c'est bien - si d > self et inversement
    # Création d’objets Duree
    assert d1.delta(d0) > 0, "Test 1 duree delta"
    assert d0.delta(d1) < 0, "Test 2 duree delta"
    assert d1.delta(d3) == 0, "Test 3 duree delta"
    try:
        d1.delta("mot") == False, "Test 4 duree delta"
    except AttributeError:
        pass
    
# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2) == True, "Test 1 Duree apres"
    assert not d0.apres(d1) == True, "Test 2 Duree apres"
    assert not d1.apres(d3) == True, "Test 3 Duree apres"
    assert d1.apres(d0) == True, "Test 4 Duree apres"
    try:
        assert d1.apres("mot") == False, "Test 6 Duree apres"
    except AttributeError:
        pass
    
# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    dA = Duree(1, 10, 20)
    dB = Duree(2, 5, 15)
    dA.ajouter(dB)
    assert (dA.h, dA.m, dA.s) == (3, 15, 35), "Test 1 Duree ajouter"

    dC = Duree(0, 0, 50)
    dD = Duree(0, 0, 20)
    dC.ajouter(dD)
    assert (dC.m, dC.s) == (1, 10), "Test 2 Duree ajouter"

    dE = Duree(1, 50, 0)
    dF = Duree(0, 30, 0)
    dE.ajouter(dF)
    assert (dE.h, dE.m) == (2, 20), "Test 3 Duree ajouter"

    dG = Duree(1, 59, 50)
    dH = Duree(1, 59, 20)
    dG.ajouter(dH)
    assert not (dG.h, dG.m, dG.s) == (3, 0, 10), "Test 4 Duree ajouter"

    dI= Duree(5, 30, 10)
    dJ = Duree(0, 0, 0)
    dI.ajouter(dJ)
    assert (dI.h, dI.m, dI.s) == (5, 30, 10), "Test 5 Duree ajouter"

    try:
        dK = Duree(1,1,1)
        dK.ajouter("mot")
        assert False, "Test 6 Duree ajouter"
    except AttributeError:
        pass

    pass

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))
c1 = Chanson("bla", "blo", Duree(0,61,61))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    assert str(c) == "Let's Dance - David Bowie - 00:04:05", "Test 1 Chanson __str__"
    assert str(c1) == "bla - blo - 01:02:01", "Test 2 Chanson__str__"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)

##############################
# Tests pour la classe Album #
##############################

# CREATION D'UN OBJET DE LA CLASSE Album A TESTER
album = Album(1)

c1 = Chanson("bla", "blo", Duree(0,4,0))
c2 = Chanson("blabla", "bloblo", Duree(1,10,0))
c3 = Chanson("blablabla", "blobloblo", Duree(0,10,0))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Album
def test_Album_str():
    texte = str(album)
    assert "01: bla - blo - 00:04:00" in texte, "Test Album __str__"

# FONCTION POUR TESTER LA METHODE add DE LA CLASSE Album
def test_Album_add():
    assert album.add(c1) == True, "Test 1 Album add"
    album.add(c2)
    assert album.add(c3) == False, "Test 2 Album add"


# APPEL DES DIFFERENTES FONCTIONS TEST
test_Album_add()
test_Album_str()


#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# Test du comportement du programme
def test_comportement():
    album = Album(1)
    c1 = Chanson("Test1", "Moi", Duree(0,4,0))
    c2 = Chanson("Test2", "Toi", Duree(0,3,30))

    assert album.add(c1) == True, "Test comportement 1"
    assert album.add(c2) == True, "Test comportement 2"

    assert album.duree.to_secondes() == (4*60 + 3*60 + 30), "Test comportement 3"

test_comportement()
