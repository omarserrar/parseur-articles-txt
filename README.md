# parseur-articles-txt

Pour pouvoir exécuter le programme, écrire sur la ligne de commande le nom du programme suivi du répertoire qui contient tout les fichiers PDF à convertir en txt:

→  python_parseur.py repertoire

Le programme convertit les fichiers du répertoire et les parse pour récupérer: 
- le nom du fichier d’origine
- Le titre du papier
- Le résumé ou abstract de l’auteur

il les met dans un nouveau répertoire qui s’appelle «out».

Quand le fichier comporte un titre de deux ou plusieurs lignes, seule la première ligne sera afficher.

