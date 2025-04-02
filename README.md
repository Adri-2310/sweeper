# project sweeper

## analyse du project
* générer un tableau en 2D contenant des valeurs numérique
  * un 9 représente une mine
  * un chiffre représente le nombre de mine adjacentes
  * taille minimale 5 et maximale 20
  * tableau rectangulaire
* nb mines: 5 minimum, 1/3 du tableau max
* placement aléatoire des bombes
* choix de la taille et du nb de mines par l'utilisateur
* ne pas tomber sur une bombe en validant la première cellule
  * génération paresseuse de la solution
* remplacer le Tui par un Gui (tkinter ou toga)
* étendre la recheche sur un "0"
* détecter la fin du jeu
  * Boom
  * clean field
* poser un drapeau
* afficher le terrain de jeu 
* garder en mémoire le nombre de bombes restantes
* coordonnées des cases ("B1")
* possibilité de mettre et retirer le drapeau
* création d'un lanceur -> choix entre Tui et Gui

## Amélioration
* ajout d'un timer
* ajout high scores
* persistence des données
* ajout musique 
* publication (exe)
* animations
* multijoueur (?)
* Easter Egg