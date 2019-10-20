# Introduction à Power BI

### Notes de cours
##### Préparées par Samuel Tremblay, VP-Éducation 2019-2020
#### Sommaire
1. L'interface de Power BI
  * Les rubans
  * Les panneaux
2. Introduction au modèle relationnel
  * Clé primaire & étrangère
  * Cardinalité des relations
  * Intégrité référencielle
3. Traitement des données
  * Imputation et remplacement
  * Colonnes calculées
  * Mesures
4. Principes de visualisation
  * Comparer des données
  * Montrer la composition
  * Montrer la distribution
  * Montrer une relation
5. Projet dans Power BI
  * Importation
  * Traitement
  * Visualisation
  
![](images/sep_1.png)
### Les rubans
Les rubans sont situés dans le haut de l'interface utilisateur de Power BI. Ils sont au nombre de 4 : l'accueil, l'affichage, la modélisation et l'aide. Voyons un peu à quoi servent les trois premiers, le quatrième étant triviale.

#### Ruban d'accueil
![](images/ruban_accueil.PNG)

Le ruban d'accueil rassemble les actions permettant d'amorcer un projet de tableau de bord dans Power BI, d'ajouter des éléments visuels à une page ou encore d'ajouter une nouvelle page. 

La section « Données externes » permet d'importer des données dans le logiciel. Le bouton « Obtenir les données » sera ici le principal outil d'importation. Si la connexion était en temps réel avec une base de données, le bouton « Actualiser » permettrait de rafraîchir les données et visuels.

La section « Insérer » permet d'ajouter une multitude d'éléments visuels au rapport : des visualisations, formes, images, zones de texte, boutons, etc.

#### Ruban d'affichage
![](images/ruban_affichage.PNG)

Le ruban d'affichage contient les options utiles afin d'adapter l'interface de Power BI à son style de travail. Il permet d'afficher un grillage, d'afficher des panneaux normalement cachés ou encore d'aligner les visualisations sur le grillage.

#### Ruban de modélisation
![](images/ruban_modélisation.PNG)

Le ruban de modélisation est le principal ruban lorsqu'il est question d'interagir avec les données. La section « Calculs » contient les outils nécéssaires à la création d'indicateurs de performance dérivés des données ou encore de colonnes utilisant la syntaxe DAX, de l'anglais *data analysis expressions*. DAX est la grande soeur des formules Excel, adaptée pour PowerPivot avec une logique de modèle relationnel à sa base.

La section « Mise en forme » permet de spécifier le format de données d'une colonne en particulier. C'est ici qu'il faut indiquer au logiciel si un nombre en un pourcentage, un montant d'argent, etc.

La section « Propriétés » permet aussi de spécifier le format de données mais pour des données spatiales. Différentes options incluent la ville, la région, le pays, etc. Si une colonne contient des liens vers des sites web, c'est aussi ici qu'il faut l'indiquer.

### Les panneaux
Les panneaux sont situés à droite de l'interface utilisateur de Power BI. Ils sont au nombre de 3 : filtres, visualisations et champs. Ils sont le principal outil afin d'interagir avec les visulisations du tableau de bord.

#### Panneau de filtres

---

#### Panneau de visualisations

<img align="left" src="images/panneau_visualisations.PNG">

Le panneau de visualisation est le panneau le plus complexe et celui dont vous vous servirez le plus souvent afin de personnaliser les paramètres des visuels par défaut de Power BI. L'image à gauche montre le haut du panneau, qui sert à sélectionner le type de visuel. Les visuels par défaut de Power BI s'arrête à l'image de « Py », pour Python. 

En effet, le logiciel supporte les visuels personnalisés codés en R ou Python. Ceux-ci ne sont cependant pas interactifs. C'est après ce symbol que commencent les visuels provenant de la Place de marché. Plus bas, vous retrouverez 3 onglets.

---

<img align="right" src="images/panneau_visualisations_1.PNG">

Le premier onglet est celui permettant de sélectionner les données à utiliser en glissant des attributs dans différents champs, lesquels varient selon le type visuel choisi. 

Fait important : lorsqu'un attribut est glissé dans le champ « valeurs », Power BI utilise par défaut la somme de ce champ. Il faut donc être prudent afin de sélectionner la bonne méthode d'aggrégation des données.

Les visuels supportent aussi la coloration en fonction d'une variable catégorielle, par exemple. Ceci est possible via le champ « Légende ». Ainsi, si un nuage de points représente un groupe aux catégories d'âge variées, y glisser l'attribut colorera les points automatiquement.

---

<img align="left" src="images/panneau_visualisations_2.PNG">

Le second onglet est celui contenant l'ensemble des options de personnalisation graphique du visuel. S'il y a un détail à l'oeil qui vous dérange, il y a 100% de chances qu'il soit possible de le changer grâce à cet onglet. Il est donc important de bien fouiller dans cette section afin de trouver le paramètre que vous voulez personnaliser.

Titre du graphique, couleur des points, grosseur du trait, titres des axes... Tout s'y trouve. En fonction du visuel, des paramètres supplémentaires peuvent aussi être disponibles.

Les noms des sections sont assez explicites mais parfois un paramètre peut parfois être bien caché : Seule l'expérience vous permettra de trouver rapidement où aller.

---

<img align="right" src="images/panneau_visualisations_3.PNG">

Le troisième et dernier onglet contient les fonctions analytiques proposées par Microsoft pour chacune des visusalisations. C'est ici, par exemple, que se retrouve l'option d'ajouter une ligne de tendance (régression linéaire) pour une visulisation de type « nuage de points ».

Cet onglet n'est pas toujours disponible puisque certaines visualisations ne supportent tout simplement pas de méthodes analytiques avancées : pensons aux tableaux, par exemple. Les séries temporelles permettent de faire de l'auto-régression en spécifiant quelques paramètres. La documentation de Power BI explique quelle méthode est utilisée.

---

#### Panneau de champs

<img align="left" src="images/panneau_champs.PNG">

Le panneau champs est l'endroit où sont rassemblées toutes les données que vous avez importées jusqu'à présent. Celles-ci sont affichées par table, qui montre les différentes colonnes lorsque vous la cliquez. Le symbole de sommation indique une donnée numérique qui supportera différents modes d'agrégation (sommation, moyenne, maximum, etc.).

Dans l'exemple à gauche, quatre tables ont été importées ; la table « immeuble_id » contient deux colonnes, dont une qui est numérique, «  TYPE_TRANSACTION ».

Le carré à gauche de chaque colonne permet de cocher un attribut afin qu'il soit utilisé dans le visuel présentement sélectionné. C'est une option alternative à glisser l'attribut vers le premier onglet du panneau de visualisation.

</br>

![](images/sep_2.png)

Le modèle relationnel est une philosophie de gestion des bases de données basée sur l'existence d'uplets, reliés entre eux par des relations. On dit alors qu'une base de donnée organisée selon ce modèle est une base de données relationnelle.

### Clé primaire & étrangère

Chaque entrée d'une table doit posséder un identifiant unique, qu'on qualifie de « clé primaire ». Le matricule HEC est un bon exemple de clé primaire. Ainsi, les caractéristiques communes d'un enregistrement doivent être regroupées dans une même table (âge, sexe, nom, etc), c'est-à-dire liées à la clé primaire

Une clé étrangère permet d'effectuer la liaison avec une autre table, laquelle n'a pas la même clé primaire. Les cours suivis sont un bon exemple de ce concept. Ici, la clé primaire serait l'identifiant du cours, tel que MATH101 par exemple, et le matricule étudiant serait, de ce point de vue, une clé étrangère.

Power BI détecte automatiquement les relations entre les tables lorsqu'elles sont ajoutées. Il va donc assigner une cardinalité en plus de déterminer quelles sont les clés à retenir. Il faut cependant vérifier qu'il ne s'est pas trompé.

### Cardinalité des relations

La cardinalité est un concept très important du modèle relationnel. Si la cardinalité est mal spécifiée, Power BI peut aggréger de façon incorrecte les données. Il existe trois types de cardinalité :

* 1 à 1 : Pour chaque entrée dans la table A, la table B a une entrée.
* 1 à N : Pour chaque entrée dans la table A, il y a N entrées dans la table B.
* M à N : Pour M entrées dans la table A, il y a N entrées dans la table B.

Le concept de cardinalité M à N peut être difficile à saisir. Un exemple concret de ce type de relation est le suivant : un étudiant peut être inscrit à plusieurs classes et une classe peut avoir plusieurs étudiants. Ainsi, plusieurs étudiants ont plusieurs classes et vice-versa.

![](images/sep_3.png)
### Imputation et remplacement

### Colonnes calculées

### Mesures

![](images/sep_4.png)
### Comparer des données

### Montrer la composition

### Montrer la distribution

### Montrer une relation

![](images/sep_5.png)
### Importation

### Traitement

### Visualisation
