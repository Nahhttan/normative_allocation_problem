# "Normative matching problem"

_Nathan LANGLOIS, pensées personnelles, inspirées par les mécanismes d'allocation des cours dans les Grandes Écoles françaises._


# Introduction: framework

## Individuals, courses and preferences

Soient 4 étudiants Alice, Bob, Carl et David. On les notera $A,B,C,D$. On suppose qu'ils doivent classer 4 cours $X,Y,Z,T$ proposés par ordre de préférence.

Une fois que les étudiants ont donné leurs préférences (sous la forme d'un préordre complet, i.e. une relation binaire réflexive, transitive et totale), un mécanisme d'allocation intervient pour attribuer chaque cours à un étudiant, de sorte qu'à la fin, chaque étudiant reçoive exactement un cours et chaque cours soit attribué à exactement un étudiant.

ATTENTION : le cadre ressemble à un cadre arrovien classique, mais ce n'est pas le cas. Les étudiants sont en concurrence pour obtenir le cours qu'ils préfèrent, et ils sont les seuls à obtenir leur cours. Dans le cadre arrovien, une seule alternative est socialement choisie.

Pour le dire de manière plus intuitive,

- dans le cadre arrovien, tout le monde est heureux et la tache est simple si tout le monde a les mêmes préférences (on choisit l'alternative unanimement préférée) ;
- dans le présent cadre, tout le monde est plus heureux et la tache est simple si personne n'a les mêmes préférences (de sorte que chaque étudiant peut se voir attribuer le cours qu'il préfère).

## Représentation des préférences : le profil de préférences

Prenons un exemple: supposons que les préférences des étudiants sont comme suit:

- A, B et C : $X\succ Y\succ Z\succ T$;
- D : $Z\succ X\succ T\succ Y$.

On peut alors résumer les préférences dans une matrice, chaque ligne représentant un étudiant, chaque colonne représentant le rang du choix. On obtient alors la matrice suivante :

$$
\begin{array}{rcccc}
& \text{1er} & \text{2e} & \text{3e} & \text{4e} \\
& \downarrow & \downarrow & \downarrow & \downarrow\\
A \to & X & Y & Z & T \\
B \to & X & Y & Z & T \\
C \to & X & Y & Z & T \\
D \to & Z & X & T & Y \\
\end{array}
$$

$$
\begin{bmatrix}
X & Y & Z & T \\
X & Y & Z & T \\
X & Y & Z & T \\
Z & X & T & Y \\
\end{bmatrix}
$$

Dans ce qui suit, nous ferons référence à l'ensemble des préférences en tant que _profil de préférences_, pour reprendre l'expression d'Arrow.


### Mécanisme d'allocation, hypothèse de bien-être linéaire

Nous supposons maintenant que le mécanisme d'allocation vise à maximiser le bien-être social (le bien-être global des étudiants). Pour atteindre cet objectif, le mécanisme d'allocation fait l'hypothèse que le bien-être d'un étudiant est linéairement corrélé négativement au rang du cours qu'il reçoit. Cela signifie que pour 4 cours, un premier choix donne 4 unités de bien-être, un deuxième choix donne 3 unités, un troisième choix 2 unités et un quatrième choix 1 unité.

(Il s'agit d'une hypothèse forte. Le bien-être non linéaire devrait être pris en compte à l'avenir ; voir la section Extensions).

Nous pouvons maintenant représenter le profil des préférences, c'est-à-dire les préférences de $A,B,C,D$, d'une manière plus simple : la matrice suivante est telle que chaque ligne correspond maintenant à un étudiant, et chaque colonne à un cours.

$$
\begin{array}{rcccc}
& X & Y & Z & T \\
& \downarrow & \downarrow & \downarrow & \downarrow\\
A\to & 4 & 3 & 2 & 1 \\
B\to & 4 & 3 & 2 & 1 \\
C\to & 4 & 3 & 2 & 1 \\
D\to & 3 & 1 & 4 & 2 \\
\end{array}
$$

$$
\begin{bmatrix}
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$

Le mécanisme d'allocation doit choisir 4 nombres dans la matrice précédente : 1 par ligne et par colonne, de sorte qu'il y ait une bijection entre l'ensemble des étudiants et l'ensemble des cours.

Par exemple, la matrice suivante correspond à l'attribution de $X$ à $A$ (produisant 4 unités de bien-être), $Z$ à $B$ (2 unités), $Y$ à $C$ (3) et $T$ à $D$ (2) :

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & 1 \\
4 & \color{orange} 3 & 2 & 1 \\
4 & 3 & \color{orange} 2 & 1 \\
3 & 1 & 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$

Le vecteur de bien-être associé à la première allocation est $(4,3,2,2)$.

Une autre répartition pourrait être :

$$
\begin{bmatrix}
4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & 3 & 2 & 1 \\
4 & \color{red} 3 & 2 & 1 \\
3 & 1 & \color{red} 4 & 2 \\ 
\end{bmatrix}
$$

Celle-ci produirait le vecteur $(4,4,3,1)$.

Notons que nous pouvons aussi, lorsque c'est possible, représenter 2 allocations sur une même matrice pour mieux les comparer. Voir :

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$


### Le coeur du problème

Mais dans le premier exemple, qu'est-ce qui est préférable ? $(4,3,2,2)$ ou $(4,4,3,1)$ ?

- La vision utilitariste affirmerait que $(4,4,3,1)$ est meilleur, parce que la somme de ses composantes s'élève à $12$, et que la somme de $(4,3,2,2)$ n'est que de $11$.
- La vision égalitaire, basée sur le critère du leximin, affirmerait que $(4,3,2,2)$ est meilleur, car sa composante minimale est de $2$, et le minimum de $(4,4,3,1)$ n'est que de $1$.

De plus, il apparaît (et peut être facilement prouvé) qu'il est impossible de trouver une allocation qui réconcilierait les deux points de vue en étant meilleure que les deux allocations selon les deux points de vue. Nous sommes donc confrontés à un conflit moral.

Il n'y a pas de meilleure réponse à la question de savoir quelle allocation est préférable : tout dépend de la théorie de la justice à laquelle nous croyons, de la _conception normative_ que nous adoptons.

Nous venons de montrer quelque chose d'important : pour allouer 4 cours à 4 étudiants avec un cours par étudiant, un mécanisme d'allocation doit nécessairement choisir une certaine conception normative, puisque (au moins) deux conceptions normatives entrent en conflit.

Est-ce toujours le cas, quel que soit le nombre de cours et le nombre d'étudiants ?

## Problématiques et conséquences

La raison d'être de ce projet est la question suivante : _un mécanisme d'allocation des vœux est-il condamné à prendre une position morale s'il doit fonctionner (c'est-à-dire renvoyer une allocation) quelles que soient les préférences des individus [domaine non restreint] ?_

En d'autres termes : _existe-t-il (au moins) un profil de préférences qui pose un conflit moral au mécanisme d'allocation, quel que soit le nombre de cours et d'étudiants ?_

Si c'est le cas, le lourd corollaire est que tout algorithme d'allocation conçu pour fonctionner pour n'importe quel profil de préférences comporte un biais moral.


# Formellement

On considère le cas simple avec $n$ étudiants, $n$ cours à choisir et un cours alloué à chaque étudiant (et donc un seul étudiant par cours).

## Definitions

- **Préférences** : on nomme _préférences_ une liste ordonnée de cours qui traduit les préférences d'un étudiant.

- **Profil de préférences** : l'ensemble des préférences de chaque étudiant forme un _profil de préférences_ que l'on peut résumer dans une matrice où chaque ligne représente les préférences d'un étudiant.

- **Allocation** : on nomme _allocation_ tout $n$-uplet de cours, traduisant le fait que le $i$<sup>e</sup> cours du $n$-uplet est affecté au $i$<sup>e</sup> étudiant (pour un profil de préférences donné).

- **Satisfaction** : on nomme _satisfaction_ pour une allocation le "vecteur de bien-être", i.e., le vecteur dont la $i$<sup>e</sup> composante est le bien-être de l'étudiant $i$. 

   Note : puisque toute conception normative respectable respecte la condition d'anonymat (symétrie des individus), on pourra se permettre d'utiliser le terme _satisfaction_ pour désigner ce même vecteur rangé par ordre décroissant.

- **Préférabilité selon une conception normative** : une allocation $a$ est dite _préférable à $b$ selon la conception normative_ $u$ si la satisfaction de $a$ est préférée à celle de $b$ selon $u$ (pour un profil de préférences donné).

   On note $a\succ_u b$ si la préférence est stricte, $a\succeq_u b$ si elle est large, et $a\sim_u b$ s'il ya indifférence.

- **Dominance normative** : une allocation $a$ _domine normativement_ $b$ si $a\succeq_u b$ pour toute conception normative $u$ (pour un profil de préférences et un ensemble de conceptions normatives donnés, non précisés s'il n'y a pas d'ambiguïté).

- **Efficacité normative** : une allocation $a$ est dite _normativement efficace_ si elle n'est normativement dominée par aucune autre allocation (pour un profil de préférences et un ensemble de conceptions normatives donnés, non précisés s'il n'y a pas d'ambiguïté).

- **Extensions aux satisfactions** : on étendra sans problème les définitions de _préférabilité selon une conception normative_, de _dominance normative_ et d'_efficacité normative_ aux satisfactions (vecteurs de bien-être).


# Partie computationnelle


## Fonctionnement

Le notebook présent dans ce repo permet de prouver computationnellement l'existence de profils de préférences qui suscitent un conflit normatif, pour $n\in\{4,5\}$, et son inexistence pour $n=3$.

Plus largement, il permet d'exhiber chaque conflit normatif possible entre deux conceptions normatives données, pour $n$ donné, en donnant un profil de préférences donnant lieu à ce conflit.

Note : la fonction n'affiche pas les doublons. Par exemple, si plusieurs profils de préférences _différents_ conduisent au _même_ conflit normatif (i.e., au _même_ ensemble d'allocations normativement efficace), alors un seul représentant sera affiché.

Par exemple, `print_dilemmes(4, score_utilitarisme, score_leximin)` affiche tous les dilemmes possibles entre utilitarisme et égalitarisme pour $n=4$.


## Un exemple de bout en bout

Cet exemple reprend celui de l'introduction, pas à pas.

~~~
Profil de préférences

[['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['C' 'A' 'D' 'B']]
~~~

Considérons le profil de préférences ci-dessus. Chaque ligne de la matrice représente un étudiant, plus précisément les préférences d'un étudiant : l'étudiant 1 préfère A, puis B, C, D.

Intuitivement, comment allouer optimalement les cours ? Puisque les étudiants 1, 2, 3 préfèrent tous les trois A, on peut allouer A à l'un des trois seulement. Disons à 1. Et allouons C à 4, clairement (c'est son préféré et les autres ne l'aiment pas). Ensuite, peu de latitude : on alloue B à 2 et D à 4 (c'est pareil que de faire l'inverse). On obtient l'allocation (A, B, D, C), et la satisfaction associée $(4,3,1,4)$, ou $(4,4,3,1)$ par ordre décroissant.

Mais dans l'option précédente, l'un des étudiants est profondément insatisfait, avec 1 point. Peut-être pourrait-on faire en sorte que personne ne soit si malheureux. On pourrait allouer D à 4 : il aurait une satisfaction de $2>1$, et on s'assurerait que les étudiants 1, 2, 3 n'aient pas leur dernier choix. On leur assignerait ensuite A, B et C indifféremment (puisqu'ils ont les mêmes préférences), par exemple A à 1, B à 2, C à 3. On obtient l'allocation (A, B, C, D), et la satisfaction associée $(4,3,2,2)$.

Quelle option est la meilleure ? Si l'on considère les conceptions normatives utilitaristes et égalitaristes (en se basant pour cette dernière sur le critère du leximin), alors
- $(4,4,3,1)\succ(4,3,2,2)$ pour un utilitariste puisque $4+4+3+1=12>11=4+3+3+2+2$ ;
- $(4,3,2,2)\succ(4,4,3,1)$ pour un égalitariste, puisque le moins bien-loti est à $2$ dans le 1er cas, et seulement à $1$ dans le second cas.

C'est ce brainstorming, qui consiste à chercher les meilleures allocations - les allocations _normativement efficaces_ - que réalise ce code. Voici l'output pour le profil de préférences considérée, et qui correspond à notre dilemme.

Note : on a codé une fonction de score pour le leximin, qui fonctionne tant que les niveaux de satisfaction sont inférieurs à 9. Elle est facilement adaptable.

~~~
   Satisfaction  Score_1  Score_2    Allocation
0  (4, 4, 3, 1)       12     1344  (A, B, D, C)
1  (4, 3, 2, 2)       11     2234  (A, B, C, D)
~~~


## [À venir / incomplet] Annexe : comment l'algorithme détermine-t-il les allocations normativement efficaces ?

On construit cet ensemble par récurrence. On note $\mathcal A_{NE}^P$ l'ensemble "provisoire" des allocations normativement efficaces. Soient un profil de préférences et $u,v$ deux conceptions normatives.

Il y a autant d'étapes que d'allocations possibles (i.e., $n!$).

À l'étape 1, $\mathcal A_{NE}^P=\emptyset$. On considère l'allocation $a_1$. On ajoute $a_1$ à $\mathcal A_{NE}^P$, puisque $a_1$ est normativement efficace au sein de l'ensemble des allocations $\mathcal A_{NE}^P \cup \{a_1\}$.

À l'étape $n$, supposons qu'on a $\mathcal A_{NE}^P=\{a_{(1)},\dots,a_{(n)}\}$ avec

$$
\begin{cases}
   a_{(1)}\succeq_u\dots\succeq_u a_{(n)} \\
   a_{(1)}\preceq_v\dots\preceq_v a_{(n)}
\end{cases}
$$

On considère l'allocation $a_{n+1}$. Alors il existe $i,j$ tels que


$$
\begin{cases}
   a_{(1)}\succeq_u\dots\succeq_u a_{(i)}\succeq_u a_{n+1}\succeq_u a_{(i+1)}\succeq_u\dots\succeq_u a_{(n)} \\
   a_{(1)}\preceq_u\dots\preceq_u a_{(j)}\preceq_u a_{n+1}\preceq_u a_{(j+1)}\preceq_u\dots\preceq_u a_{(n)} \\
\end{cases}
$$

Prenons un exemple pour intuiter la suite. Traduisons ces relations de préférences par des inégalités sur des scores. On va considérer qu'on peut quantifier la recommandabilité des allocations selon les normes $u$ et $v$ via des fonctions de score $s_u$ et $s_v$. Par exemple, si $u$ désigne l'utilitarisme, $s_u(\hat a)=7$ si la satisfaction de $\hat a$ est $(3,3,1)$.

$$
\begin{cases}
   10 &>& 8 &>& 6 &>& 4 &>& 2 \\
   12 &<& 14 &<& 16 &<& 18 &<& 20 
\end{cases}
$$

- Si $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 15)$, alors $a_{n+1}$ est normativement efficace, et s'intègre parfaitement dans la chaîne, entre $a_{(2)}$ et $a_{(3)}$.
- Si $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 13)$, alors $a_{n+1}$ ne sera pas normativement efficace, puisque normativement dominée par $a_{(2)}$ car $7<8$ d'une part et $13<14$ d'autre part.
- Si $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 19)$, alors non seulement $a_{n+1}$ est normativement efficace, mais elle élimine $a_{(3)}$ et $a_{(4)}$.


# Axes d'amélioration


## Prise en compte de la symétrie des alternatives

Pour l'instant, le code passe en revue tous les profils de préférences possibles en prenant en compte la symétrie des individus : $(ABC, ABC, CBA)$ et $(CBA, ABC, ABC)$ sont identiques à cet égard, donc le code ne regardera que le premier des deux.

Mais on peut encore diminuer le nombre de profils de préférences à étudier.

Ex : $(ABC, ACB, ACB) \sim (ABC, ABC, ACB)$ (il suffit de remplacer $B$ par $C$ et $C$ par $B$, ce qu'on peut faire par symétrie) $\sim (XYZ, XYZ, XZY)$ plus généralement.


## Fonction de satisfaction non linéaire

À ce stade, la satisfaction est linéaire :
- un 1er choix donne $n$ points de satisfaction,
- un 2e choix donne $n-1$,
- ...
- un dernier choix donne $1$.

On devrait pouvoir utiliser des fonctions de satisfaction non linéaires, par exemple
- convexes (un étudiant aime plus son 1er choix par rapport à son 2e, que son 2e par rapport à son 3e ; i.e., il veut autant que possible son choix 1, et à la rigueur peu lui importe 2 ou 3),
- concaves (un étudiant aime plus son 2e choix par rapport à son 3e, que son 1er par rapport à son 2e ; i.e., il veut autant que possible ne pas avoir son choix 3, et à la rigueur peu lui importe 1 ou 2).


## Comparer plus de 2 conceptions normatives

Pour l'instant, on regarde les dilemmes entre 2 conceptions normatives uniquement.

On devrait pouvoir en comparer davantage, déjà 3 dans un premier temps. On donne quelques exemples de ce que cela donnerait pour 3 conceptions normatives, notées $u,v,w$.

### Exemple pertinent 1


$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\
b &\succ_v& a &\succ_v& c \\
c &\succ_w& a &\succ_w& b 
\end{cases}
$$

### Exemple pertinent 2

Dans l'exemple suivant, on pourrait croire que $c$ n'est pas une allocation efficace, car on peut faire mieux selon toutes les conceptions normatives. En réalité, $c$ est bien une allocation efficace, car aucune allocation ne la domine normativement, i.e. lui est préférable selon toutes les conceptions normatives ; il faut bien garder en tête que c'est cela, le critère d'efficacité pour une allocation.

$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\
a &\succ_v& c &\succ_v& b \\
b &\succ_w& c &\succ_w& a 
\end{cases}
$$


### Exemple non pertinent

Ici, $c$ est dominée normativement par $b$, donc n'est pas normativement efficace.

$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\
b &\succ_v& c &\succ_v& a \\
b &\succ_w& a &\succ_w& c 
\end{cases}
$$


## Augmenter le nombre de cours par étudiant, d'étudiants par cours

On est pour l'instant dans le cas simple où $n$ = nombre d'étudiants = nombre de cours.

À voir ce qu'il est numériquement possible de faire (en termes de capacité informatique), mais il serait intéressant de checker l'existence de dilemmes dans des cas plus complexes.

Par exemple (relativement simple) : 8 cours, 4 étudiants, 2 cours à choisir par étudiant.


## Usage réel pour un profil de préférences donné

L'usage premier de ce code était de prouver l'existence de profils de préférences qui suscitent un dilemme.

Mais il serait intéressant de rendre ce code opérationnel pour, étant donné un profil de préférences (un input réel, par exemple les voeux de cours réels des étudiants d'une école/université), donner toutes les allocations efficaces (en fonction de fonctions de score, i.e. de conceptions de la justice distributive, données).


# Partie théorique

Ici, je tente de répondre à la problématique posée dans l'introduction : _existe-t-il (au moins) un profil de préférences qui pose un conflit moral au mécanisme d'allocation, quel que soit le nombre de cours et d'étudiants ?_

Pour ce faire, je considérerai le conflit "utilitarisme vs égalitarisme" (l'égalitarisme est représenté par le critère leximin).

J'utilise la façon dont les profils de préférences sont représentés dans l'introduction pour sauter les noms explicites des cours et considérer directement la matrice des préférences, ce qui est suffisant pour montrer les résultats.


## $n$ étudiants, $n$ cours

### $n=3$

Il n'y a pas de profil de préférences qui suscite un dilemme. Il existe bien pourtant deux vecteurs qui suscitent un dilemme : $(3,3,1)$ et $(2,2,2)$, mais on peut montrer que le vecteur $(3,3,2)$, qui domine normativement ces deux vecteurs, peut toujours être atteint si $(3,3,1)$ et $(2,2,2)$.

### $n=4$

La matrice de préférences donnée en exemple plus tôt fonctionne :

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$

Je n'en donnerai pas une preuve ici, mais on peut aisément intuité qu'avec une telle matrice, $(4,4,3,1)$ et $(4,3,2,2)$ sont tous deux normativement efficaces.

### $n\geq5$

Nous pouvons utiliser la même matrice de préférences et l'étendre.

Voir ci-après :

$$
\begin{bmatrix}
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$

Le raisonnement est le suivant :

- soit on attribue le premier cours à l'un des étudiants $A,B,C,D$, et alors la matrice représentant les préférences des 4 étudiants restants sur les 4 cours restants est la même que pour $n=4$, et donc on peut produire au mieux les vecteurs $(5,4,4,3,1)$ et $(5,4,3,2,2)$ ;

$$
\begin{bmatrix}
\color{orange} 5 & 4 & 3 & 2 & \color{red} 1 \\
\color{red} 5 & \color{orange} 4 & 3 & 2 & 1 \\
5 & \color{red} 4 & \color{orange} 3 & 2 & 1 \\
5 & 4 & \color{red} 3 & \color{orange} 2 & 1 \\
5 & 3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$
    
- soit on atttribue le premier cours à l'étudiant $E$, et alors toutes les allocations des 4 cours restants aux étudiants $A,B,C,D$ donneront le même vecteur de bien-être puisqu'ils ont les mêmes préférences ; on obtient donc le vecteur $(5,4,3,2,1)$ de toute façon.

$$
\begin{bmatrix}
5 & \color{green} 4 & 3 & 2 & 1 \\
5 & 4 & \color{green} 3 & 2 & 1 \\
5 & 4 & 3 & \color{green} 2 & 1 \\
5 & 4 & 3 & 2 & \color{green} 1 \\
\color{green} 5 & 3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$
    

Mais $(5,4,3,2,1)$ est clairement normativement inefficace, on doit donc choisir entre $(5,4,4,3,1)$ et $(5,4,3,2,2)$

Et l'on peut passer à un $n$ plus grand de la même manière. Le dilemme est que $(n,n-1,\dots,5,4,3,2,2)$ vs $(n,n-1,\dots,5,4,4,3,1)$, et apparaît en couleur.

$$
\begin{bmatrix}
\color{orange} n & n-1 & n-2 & \dots & 5 & 4 & 3 & 2 & \color{red} 1 \\
\color{red} n & \color{orange} {n-1} & n-2 & \dots & 5 & 4 & 3 & 2 & 1 \\
n & \color{red} {n-1} & \color{orange} {n-2} & \dots & 5 & 4 & 3 & 2 & 1 \\
\vdots & \vdots & \vdots & \vdots  & \vdots & \vdots & \vdots & \vdots & \vdots \\
n & n-1 & n-2 & \dots & \color{orange} 5 & 4 & 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & \color{red} 5 & \color{orange} 4 & 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & \color{red} 4 & \color{orange} 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & 4 & \color{red} 3 & \color{orange} 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & \bf 3 & \bf 1 & \color{red} {\bf 4} & \color{orange} {\bf 2} \\ 
\end{bmatrix}
$$

## $n\geq2$ étudiants, $p\geq 4$ cours, $n/p$ places par cours

Remarque : il faut que $n/p\in\mathbb N^\star$, donc $p|n$ ($p$ divise $n$).

### Exemple : 8 étudiants, 4 cours, 2 étudiants par cours

Nous devons choisir 2 nombres par colonne (puisqu'il y a 2 places par cours), mais toujours 1 nombre par ligne (chaque étudiant n'a toujours qu'un seul cours).

$$
\begin{bmatrix}
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
4 & 3 & 2 & 1 \\
3 & 1 & 4 & 2 \\ 
3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$

Ce profil de préférences suscite le dilemme $(4,4,3,3,2,2,2)$ vs $(4,4,4,4,4,3,3,1,1)$ :

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$

- Preuve
    
    $(4,4,4,4,3,3,1,1)$ : si nous voulons 4 fois $4$, nous devons donner $4$ aux deux derniers étudiants, et donner $4$ à 2 autres étudiants (peu importe lesquels : les 6 restants ont les mêmes préférences). Nous ne pouvons donc donner que deux fois $3$ et deux fois $1$. C'est clairement le mieux que nous puissions faire d'un point de vue utilitariste.
    
    Avec le même type de raisonnement, nous pouvons facilement vérifier que $(4,4,3,3,2,2,2,2)$ est le mieux que nous puissions faire d'un point de vue égalitariste.
    

On peut également trouver d'autres allocations normativement efficaces, comme $(4,4,4,3,3,2,2,1)$, et on peut également créer des dilemmes avec elles.

$$
\begin{bmatrix}
\color{green} 4 & 3 & 2 & 1 \\
\color{green} 4 & 3 & 2 & 1 \\
4 & \color{green} 3 & 2 & 1 \\
4 & \color{green} 3 & 2 & 1 \\
4 & 3 & \color{green} 2 & 1 \\
4 & 3 & 2 & \color{green} 1 \\
3 & 1 & \color{green} 4 & 2 \\ 
3 & 1 & 4 & \color{green} 2 \\ 
\end{bmatrix}
$$

## $n$ étudiants, $p$ cours, $p/n$ places par étudiant

### Exemple : 4 étudiants, 2 cours, 2 places par étudiant

Nous devons choisir 2 nombres par ligne (puisqu'il y a 2 places par étudiant), mais 1 nombre par colonne (il y a 1 place par cours).
 

$$
\begin{bmatrix}
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
6 & 5 & 2 & 1 & 8 & 7 & 4 & 3 \\ 
\end{bmatrix}
$$

Ce profil de préférences suscite le dilemme suivant : $(8,7,6,5,4,4,3,3)$ vs $(8,8,7,7,6,5,2,1)$ :

$$
\begin{bmatrix}
\color{orange} 8 & \color{orange} 7 & 6 & 5 & 4 & 3 & \color{red} 2 & \color{red} 1 \\
\color{red} 8 & \color{red} 7 & \color{orange} 6 & \color{orange} 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \color{red} 6 & \color{red} 5 & \color{orange} 4 & \color{orange} 3 & 2 & 1 \\
6 & 5 & 2 & 1 & \color{red} 8 & \color{red} 7 & \color{orange} 4 & \color{orange} 3 \\ 
\end{bmatrix}
$$

Une fois encore, on peut facilement trouver d'autres allocations normativement efficaces, comme $(8,8,7,6,5,3,3,2)$, et on peut aussi créer des dilemmes avec elles.

$$
\begin{bmatrix}
\color{green} 8 & \color{green} 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \color{green} 6 & \color{green} 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & \color{green} 3 & \color{green} 2 & 1 \\
6 & 5 & 2 & 1 & \color{green} 8 & 7 & 4 & \color{green} 3 \\ 
\end{bmatrix}
$$

## $n$ étudiants, $p$ cours, $k$ créneaux par étudiant, $nk/p$ créneaux par cours

### Exemple : 12 étudiants, 8 cours, 2 places par étudiant, 3 places par cours

$$
\begin{bmatrix}
\color{orange} 8 & \color{orange} 7 & 6 & 5 & 4 & 3 & \color{red} 2 & \color{red} 1 \\
\color{orange} 8 & \color{orange} 7 & 6 & 5 & 4 & 3 & \color{red} 2 & \color{red} 1 \\
\color{orange} 8 & \color{orange} 7 & 6 & 5 & 4 & 3 & \color{red} 2 & \color{red} 1 \\
\color{red} 8 & \color{red} 7 & \color{orange} 6 & \color{orange} 5 & 4 & 3 & 2 & 1 \\
\color{red} 8 & \color{red} 7 & \color{orange} 6 & \color{orange} 5 & 4 & 3 & 2 & 1 \\
\color{red} 8 & \color{red} 7 & \color{orange} 6 & \color{orange} 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \color{red} 6 & \color{red} 5 & \color{orange} 4 & \color{orange} 3 & 2 & 1 \\
8 & 7 & \color{red} 6 & \color{red} 5 & \color{orange} 4 & \color{orange} 3 & 2 & 1 \\
8 & 7 & \color{red} 6 & \color{red} 5 & \color{orange} 4 & \color{orange} 3 & 2 & 1 \\
6 & 5 & 2 & 1 & \color{red} 8 & \color{red} 7 & \color{orange} 4 & \color{orange} 3 \\
6 & 5 & 2 & 1 & \color{red} 8 & \color{red} 7 & \color{orange} 4 & \color{orange} 3 \\
6 & 5 & 2 & 1 & \color{red} 8 & \color{red} 7 & \color{orange} 4 & \color{orange} 3 \\
\end{bmatrix}
$$

## Extensions

### Bien-être non linéaire
   
Si la matrice est

$$
\begin{bmatrix}
a & b & c & d \\
a & b & c & d \\
a & b & c & d \\
b & d & a & c \\ 
\end{bmatrix}
$$

$$
\begin{bmatrix}
\color{orange} a & b & c & \color{red} d \\
\color{red} a & \color{orange} b & c & d \\
a & \color{red} b & \color{orange} c & d \\
b & d & \color{red} a & \color{orange} c \\ 
\end{bmatrix}
$$

Pour un égalitariste, $(a,b,c,c)$ est toujours mieux que $(a,a,b,d)$, mais pour que le dilemme émerge, il faut que le point de vue utilitariste diverge, i.e., il faut que $2c < a+d$. C'est toujours vrai pour une fonction d'utilité convexe (où $a-b>b-c>c-d$), puisque nous avons alors :

$$
\begin{align}
a+d &>b+c \\
&\geq c+c \\
&=2c
\end{align}
$$

Exemple

$$
\begin{bmatrix}
\color{orange} {10} & 6 & 3 & \color{red} 1 \\
\color{red} {10} & \color{orange} 6 & 3 & 1 \\
10 & \color{red} 6 & \color{orange} 3 & 1 \\
6 & 1 & \color{red} {10} & \color{orange} 6 \\ 
\end{bmatrix}
$$

$(10,6,6,3)$ vs $(10,10,6,1)$
