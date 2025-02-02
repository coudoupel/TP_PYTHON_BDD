# TP_PYTHON_BDD

## Introduction

Ce projet est une application web qui permet de gérer les différents aspects d'un restaurant. À l'aide de Flask (un framework Python), l'utilisateur peut ajouter et consulter des informations telles que les clients, menus, plats, boissons, commandes et avis.

## Prérequis

- Création d'une VM Debian 12
- Installation de poetry et python
- Base de données SQLite

Les différents scripts seront :

- Un script pour le fonctionnement global du projet
- Des scripts html/css pour l'interface web
- Une BDD MySQL pour stocker les différents informations du client

Pour créer la BDD :

Installation de mysql :

```
sudo apt install mysql-server
```

Ajout de la database:

```mysql
CREATE DATABASE resto;
CREATE USER 'vegeta'@'localhost' IDENTIFIED BY '***';
GRANT ALL PRIVILEGES ON resto.* TO 'vegeta'@'localhost';
FLUSH PRIVILEGES;
```

### Schéma simplifié

[![Image](https://i.goopics.net/wbghqu.png)](https://goopics.net/i/wbghqu)

## Arborescence du Projet

```
│── app.py                          # Application Flask (backend)
│── delete.py                       # Suppression de toute les données dans les tables
│── templates/                      # Dossier des fichiers HTML
│   │── index.html                  # Page d'accueil, liste des éléments du restaurant
│   │── add_client.html             # Formulaire d'ajout d'un client
│   │── add_menu.html               # Formulaire d'ajout d'un menu
│   │── add_plat.html               # Formulaire d'ajout d'un plat
│   │── add_boisson.html            # Formulaire d'ajout d'une boisson
│   │── add_commande.html           # Formulaire d'ajout d'une commande
│   │── add_avis.html               # Formulaire d'ajout d'un avis
│── static/                         # Dossier des fichiers statiques (CSS, images)
│   │── css/style.css               # Feuille de style CSS` 
```

## Fonctionnalités

L'application permet de :

-   **Gérer les clients** : Ajouter, consulter les informations des clients du restaurant (nom, adresse, email, réservation).
-   **Gérer les menus** : Ajouter de nouveaux menus avec un prix et une description.
-   **Gérer les plats** : Ajouter des plats au menu avec un nom, un prix, un type (viande, poisson, végétarien, etc.) et des calories.
-   **Gérer les boissons** : Ajouter des boissons avec un nom, un prix, un type et des calories.
-   **Gérer les avis** : Ajouter des avis clients sur les services du restaurant.
-   **Gérer les commandes** : Créer des commandes avec des informations sur le client, la date, le prix total et le mode de paiement.

## Description des scripts

### `app.py` (Flask - Python)

Ce script contient la logique backend de l'application. Il gère les différentes routes de l'application, les interactions avec la base de données et les rendus des templates HTML.

### `delete.py` (Python)
Ce fichier contient le script responsable de la suppression de toutes les données dans la base de données. Il efface les enregistrements des tables principales et des tables avec des clés étrangères, garantissant une suppression complète des données du restaurant.

### `index.html` (HTML)

La page principale qui affiche des tableaux pour chaque élément du restaurant (clients, menus, plats, boissons, avis et commandes). Chaque tableau présente les données et offre des liens pour ajouter de nouveaux éléments.

### `add_client.html`, `add_menu.html`, etc. (HTML)

Chacune de ces pages contient un formulaire permettant à l'utilisateur d'ajouter un client, un menu, un plat, etc. Ces formulaires envoient les données au backend via des requêtes POST.

### `style.css` (CSS)

La feuille de style utilisée pour styliser les pages HTML. Elle permet de rendre l'interface utilisateur agréable et cohérente.

## Fonctionnement

### Page d'Accueil

Lorsqu'un utilisateur arrive sur la page d'accueil de l'application, il voit plusieurs tableaux avec les informations des clients, menus, plats, boissons, avis et commandes.

-   Chaque tableau contient des données qui sont extraites de la base de données.
-   Des liens permettent à l'utilisateur d'ajouter de nouveaux éléments dans chaque catégorie.

### Ajout d'un élément

Lorsque l'utilisateur clique sur un lien pour ajouter un nouvel élément, il est redirigé vers un formulaire où il peut entrer les informations nécessaires :

-   **Client** : Nom, adresse, email, réservation.
-   **Menu** : Nom, prix, description.
-   **Plat** : Nom, prix, type, calories.
-   **Boisson** : Nom, prix, type, calories.
-   **Avis** : Client, note, commentaire.
-   **Commande** : Client, date, prix total, mode de paiement.

Les données sont ensuite envoyées via un formulaire POST et enregistrées dans la base de données.

### Traitement des Formulaires

Chaque formulaire utilise la méthode POST pour envoyer les données à l'application Flask, qui les insère dans la base de données correspondante.

### Visualisation des Données

Après l'ajout des données, l'utilisateur est redirigé vers la page d'accueil où les informations sont affichées dans les tableaux respectifs.

## Conclusion

Ce projet est une gestion simple mais complète d'un restaurant, permettant d'ajouter et de visualiser les clients, menus, plats, boissons, avis et commandes. Utilisant Flask pour la gestion des routes et des templates HTML, ce projet offre une interface intuitive pour gérer efficacement un restaurant.

Le projet peut encore être étendu en ajoutant des fonctionnalités comme la modification ou la suppression d'éléments, la gestion des réservations ou un système d'authentification pour les utilisateurs.
