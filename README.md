# parseur-articles-txt

## Parseur
Parseur-articels-txt est un convertisseur PDF -> texte ou PDF -> xml.

## Comment l'utiliser ?

Pour pouvoir lancer le programme, il faut écrire sur la ligne de commande le nom du programme suivi du répertoire qui contient tous les fichiers PDF à convertir en txt ou en xml :

→  python_parseur.py -x|-t repertoire

Ce programme affiche un menu au début de l'exécution du système et demande à l'utilisateur de choisir un PDF à convertir et le parser pour récupérer: 

article>      
&lt;preamble> Le nom du fichier d’origine &lt;/preamble>
&lt;titre> Le titre du papier &lt;/titre>
&lt;auteur> La section auteurs et leur adresse&lt;/auteur>
&lt;abstract> Le résum  é de l’article&lt;/abstract>
&lt;introduction> La introduction&lt;/introduction>
&lt;corps> Le développement du papier&lt;/corps>
&lt;conclusion> La conclusion du papier&lt;/conclusion>
&lt;discussion> La discussion du papier&lt;/discussion>
&lt;biblio> Les références bibliographiques du papier&lt;/biblio>
&lt;/article>


il le met dans un nouveau répertoire qui s’appelle «out».

## Problèmes rencontrès

Le fonctionnement de ce programme dépend des fichiers PDF.

Quand le fichier comporte un titre de deux ou plusieurs lignes, seule la première ligne sera afficher.


