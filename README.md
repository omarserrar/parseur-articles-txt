# parseur-articles-txt

## Parseur
Parseur-articels-txt est un convertisseur PDF -> texte ou PDF -> xml.

## Comment l'utiliser ?

Pour pouvoir lancer le programme, écrire sur la ligne de commande le nom du programme suivi du répertoire qui contient tous les fichiers PDF à convertir en txt ou en xml :

→  python_parseur.py -x|-t repertoire

Pour convertir le fichier pdf en xml, il faut ajouter -x.
Pour convertir le fichier pdf en txt, il faut ajouter -t.

Ce programme convertit les fichiers du répertoire et les parse pour récupérer: 

<article>
<preamble> Le nom du fichier d’origine </preamble>
<titre> Le titre du papier </titre>
<auteur> La section auteurs et leur adresse </auteur>
<abstract> Le résumé de l’article </abstract>
<biblio> Les références bibliographiques du papier</biblio>
</article>

il les met dans un nouveau répertoire qui s’appelle «out».

## Problèmes rencontrès

Le fonctionnement de ce programme dépend des fichiers PDF.

Quand le fichier comporte un titre de deux ou plusieurs lignes, seule la première ligne sera afficher.


