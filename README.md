# DataEngineering Projet étude des performances des équipes ayant participé à Fort Boyard de 2003 à 2023
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scrapy](https://img.shields.io/badge/Scrapy-%2314D08C.svg?style=for-the-badge&logo=scrapy&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/dash-008DE4?style=for-the-badge&logo=dash&logoColor=white)

## Description
L'objectif de ce projet est d'étudier les performances des équipes participant à la mythique émission TV Fort Boyard. 

Pour cela nous récupérons les informations par WebScraping avec les librairies Selenium et Scrapy sur le site [https://o.fortboyard.tv/gains.php#parsaison](https://o.fortboyard.tv/gains.php#parsaison), et nous les compilons dans un fichier json.  

Ensuite ce fichier json est importé dans une base MongoDB pour avoir un meilleur contrôle sur l'accès des données.

Enfin nous extrayons les données qui nous intéressent et les visualisons avec la librairie plot dans un dashboard implémentée grâce à la librairie dash.

Chaque étape du projet est isolée dans un container Docker.

Le projet est managé grâce à un docker-compose.yml.

Dans la branche principale de github nous trouvons le docker-compose permettant de lancer et de gérer l'ensemble projet, ainsi que les fichiers Dockerfile de chaque container.

Le dossier __programmes__ contient :

* Les programmes non conteneurisés (détaillés plus bas dans la rubrique **Programmes python**)

* Les fichiers contenant les librairies nécessaires (Pipfile et requirements.txt) au fonctionnement des programmes.

## Pré-requis
Ce projet nécessite l'utilisation de Docker. S'il n'est pas déjà téléchargé :

* [Pour Windows](https://docs.docker.com/desktop/install/windows-install/)

* [Pour Linux](https://docs.docker.com/desktop/install/linux-install/)

* [Pour Mac](https://docs.docker.com/desktop/install/mac-install/)


## Guide d'installation
Dans un terminal de commandes, commencez par vous déplacer vers le dossier où sera enregistré le projet avec la commande :

``
cd chemin_vers_le_dossier_de_votre_choix
``

Cloner le projet avec la commande:

``
git clone https://github.com/RyanKHOU/Project_DataEngineering_Khou_Le.git
``

Créer les containers et les images du projet avec la commande (à la racine du projet)

``
docker-compose build 
``

Lancer  l'exécution du projet avec la commande 

``
docker-compose up -d
``

Ensuite il faut attendre que le container dash_app soit actif. Quand c'est le cas il suffit de se rendre sur l'adresse IP https://127.0.0.1:8050.

## Guide d'utilisation

### Programmes python

* __data_collectinng.py__ : scrape les données depuis le site [https://o.fortboyard.tv/gains.php#parsaison](https://o.fortboyard.tv/gains.php#parsaison) et génère un fichier json contenant toutes les informations récupérées.

* __values.py__ : récupère l'ensemble des données depuis le container dont l'image est une base de données mongodb. Ce fichier de code contient également les fonctions essentiels pour faire un premier traitement des données comme la fonction *time_to_seconds()* ou pour déclarer des histogrammes avec la variable *fig_time*.

* __visualization.py__ : interface permettant d'implémenter le framework de l'application via des fonctions implémentant les graphiques, les boutons, les sliders, l'affichage des images et leurs interactions.

* __main.py__ : permet de démarrer le dashboard en appelant la variable *app* implémentées dans **visualization.py** contenant toute l'architecture du dashboard.

### Dockerfiles

### docker-compose

Le docker-compose créé 3 services : 

- **selenium-chrome** : il permet de lancer le container permettant de scraper les données sur le site d'étude. Il s'appuie sur une image *selenium-chrome* qui, par défaut utilise le port 4444.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pour plus d'informations :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GitHub de l'image](https://github.com/SeleniumHQ/docker-selenium)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dépôt docker de l'image](https://hub.docker.com/r/selenium/standalone-chrome)


- **mongodb** : il permet de stocker les données dans une base de données. Il s'appuie sur une image mongo qui utilise par défaut le port 27017.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pour plus d'informations :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dépôt docker de l'image](https://hub.docker.com/_/mongo)


- **dash_app** : il permet d'afficher à l'écran le dashboard. Etant donné qu'il utilise un framework dash, le dashboard est accessible via le port 8050.

## Diagramme de classe 

## Contributeurs

Ce projet a été développé par Van-Minh Christophe LE (étudiant 4e année filière DSIA) et Ryan KHOU (étudiant 4e année filière DSIA) dans le cadre de l'unité Data Engineering dispensé à l'ESIEE PARIS.
