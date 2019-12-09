# parseur-articles-txt

## Parseur
Parseur-articels-txt est un convertisseur PDF -> texte ou PDF -> xml.

## Comment l'utiliser ?

Pour pouvoir lancer le programme, il faut écrire sur la ligne de commande le nom du programme suivi du répertoire qui contient tous les fichiers PDF à convertir en txt ou en xml :

→  python_parseur.py -x|-t repertoire

Ce programme affiche un menu au début de l'exécution du système et demande à l'utilisateur de choisir un PDF à convertir et le parser pour récupérer: 

article>      
<preamble> Le nom du fichier d’origine </preamble>
<titre> Le titre du papier </titre>
<auteur> La section auteurs et leur adresse</auteur>
<abstract> Le résum  é de l’article</abstract>
<introduction> La introduction</introduction>
<corps> Le développement du papier</corps>
<conclusion> La conclusion du papier</conclusion>
<discussion> La discussion du papier</discussion>
<biblio> Les références bibliographiques du papier</biblio>
</article>


il le met dans un nouveau répertoire qui s’appelle «out».

## Problèmes rencontrès

Le fonctionnement de ce programme dépend des fichiers PDF.

Quand le fichier comporte un titre de deux ou plusieurs lignes, seule la première ligne sera afficher.


