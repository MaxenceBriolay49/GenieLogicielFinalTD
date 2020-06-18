# TD cours de genie logiciel 2020

## Exercice 1:

Développer un formulaire d’inscription pour un club de sport de votre voix. Le but étant de suivre le modèle MVC pour votre développement. Vous utiliserez une base de donnée SQLite.
L’application devra fournir les fonctionnalité suivante:
Inscription par un adhérent
Modification par l’administrateur
Suppression d’un adhérent par l’administrateur
List et recherche d’un adhérent par l’administrateur

Elle sera donc composé de deux interfaces différentes: une interface d’inscription et une interface administrateur. 
L’administrateur devra bien sur pour accéder à sa page se connecter.

Librairies Python:
Sqlalchemy pour la base de donée avec une base (https://docs.sqlalchemy.org/en/13/orm/tutorial.html) 
Interface graphique (TKinter)

## Exercice 2:

En reprenant l’exercice précédent: (création d’une architecture 3 tiers)
Le client de notre logiciel souhaite que les inscriptions puissent être faites en ligne:
En gardant votre modèle précédent, vous devrez créer à la place de votre Vue une API REST. Vous développerez ensuite un client permettant d'inscrire une personne en passant par cette Vue. 

2 APIs:
    API 1
Faire une demande d’inscription (POST) <- adhérent
    API2
modifier son profil (PUT) <- administrateur
voir un profil (GET) <- administrateur
suppression (DELETE) <- administrateur

Nous partirons du principe que l’administrateur à un client différent et n’a pas besoin de s’identifier. Cette partie sera vue plus tard. Faites quelques chose de simple !

Librairies Python:
Flask (https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/ )

## Exercice 3:


Ecrire le diagramme de classe complet de notre application
Ecrire le diagramme séquence de l’inscription d’un participant. 
Ajouter feature et compléter diagramme de classe avec les feature suivantes:
Choix d’un sport (l’application doit permettre l’inscription à un sport) 
Ajouter adhérents - entraîneur en fonction du niveau
(Créer un dictionnaire de langue et ajouter la langue dans vos URL. 
(Exemple requête: GET /adherents?lang=en) Vous utiliserez ensuite le design pattern “decorateur” pour injecter la bonne langue à chaque appelle.) ? 

## Exercice 4

mise en place du Git avec README, RELEASE Note, contributing guide)
Chaque dois ajouter une feature par une branche
 Ajout créneaux de prof associé à un sport et un niveau. L’utilisateur doit pouvoir récupérer ses créneaux de sports
Un utilisateur doit pouvoir modifier son profile (ajout d’un mot de passe et un identifiant pour qu’il puisse être identifier). L’identification pourra être faite par un décorateur au niveau de l’appelle sur l’API. 

Ecriture de tests unitaire

Ecrire des tests unitaires sur l’application d’inscription sportive développée en cours.
Test inscription
Test modification
Test identification
…

## Exercice 5

Mise en place des places des tests dans une intégration continue

