# "Normative matching problem"

_Nathan LANGLOIS, personal thoughts, inspired by courses allocation mechanisms in French Grandes Écoles._

# Introduction: framework

## Individuals, courses and preferences

Let 4 students be Alice, Bob, Carl, and David. We will denote them $A,B,C,D$. We suppose they have to rank 4 courses $X,Y,Z,T$ that are proposed, with one constraint: each course can be offered to one and only one student.

Once the students have given their preferences (as an ordering, i.e. a binary relation that is reflexive, transitive and complete), an allocation mechanism occurs to allocate each course to one student, so that in the end, every student gets exactly one course and every course is allocated to exactly one student.

CAREFUL: the framework looks like a classic Arrovian framework, but it is not. The students compete to get the course they prefer, and only they will get their course. In the Arrovian framework, only one alternative is socially chosen.

To put it more intuitively,

- in the Arrovian framework, everybody is happier and the job is easy if everybody has the same preferences;
- in the framework here, everybody is happier and the job is easy if nobody has the same preferences (so that everybody can get the course they prefer).

## Preferences representation: the profile of preferences

Let us take an example: we suppose that the students’ preferences are as follows:

- A, B and C: $X\succ Y\succ Z\succ T$;
- D: $Z\succ X\succ T\succ Y$.

We can then summarize the preferences into a matrix, each row representing an student, and each column representing the rank of the choice. We then obtain the following matrix:

$$
\begin{array}{rcccc}
& \text{1st} & \text{2nd} & \text{3rd} & \text{4th} \\
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

In what follows, we will refer to the set of preferences of as the _profile of preferences_, to use Arrow's expression.

### Allocation mechanism, linear well-being assumption

We now suppose that the allocation mechanism aims at maximizing social welfare (the overall well-being of the students). To achieve this goal, the allocation mechanism makes the assumption that the well-being of a student is linearly negatively correlated to the rank of the course he receives. It means that for 4 courses, a 1st choice gives 4 units of well-being, a 2nd choice gives 3 units, a 3rd choice 2 units, and a 4th choice 1 unit.

(This is a strong assumption. Non-linear well-being should be considered in the future; see extensions.)

Now, we can represent the profile of preferences, i.e. the preferences of $A,B,C,D$, in a simplier way: the following matrix is such that each row now corresponds to a student, and each columns corresponds to n course.

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

The allocation mechanism must choose 4 numbers in the former matrix: 1 per row and per column, so that there is a bijection between the set of students and the set of courses.

For example, the following matrix corresponds to allocating $X$ to $A$ (producing 4 units of well-being), $Z$ to $B$ (2 units), $Y$ to $C$ (3) and $T$ to $D$ (2):

$$
\begin{bmatrix}
\blue 4 & 3 & 2 & 1 \\
4 & \blue 3 & 2 & 1 \\
4 & 3 & \blue 2 & 1 \\
3 & 1 & 4 & \blue 2 \\ 
\end{bmatrix}
$$

The well-being vector associated with the former allocation is $(4,3,2,2)$.

Another allocation could be:

$$
\begin{bmatrix}
4 & 3 & 2 & \red 1 \\
\red 4 & 3 & 2 & 1 \\
4 & \red 3 & 2 & 1 \\
3 & 1 & \red 4 & 2 \\ 
\end{bmatrix}
$$

This one would produce the vector $(4,4,3,1)$.

Note that we can also, when possible, represent 2 allocations on a same matrix to compare them better. See:

$$
\begin{bmatrix}
\blue 4 & 3 & 2 & \red 1 \\
\red 4 & \blue 3 & 2 & 1 \\
4 & \red 3 & \blue 2 & 1 \\
3 & 1 & \red 4 & \blue 2 \\ 
\end{bmatrix}
$$

    

### The heart of the problem

But in the former example, what is preferable? $(4,3,2,2)$ or $(4,4,3,1)$?

- The utilitarist view would state that $(4,4,3,1)$ is better, because the sum of its components amounts to $12$, and the sum of $(4,3,2,2)$ is only $11$.
- The egalitarian view, based on the leximin method, would say that $(4,3,2,2)$ is better, because its minimum component is $2$, and the minimum of $(4,4,3,1)$ is only $1$.

Moreover, it appears (and can easily be proven) that it cannot be found any allocation that would reconciliates both view by being better than both allocations according to both views. So we are stuck with a moral conflict.

There is thus no best answer to this question of which allocation is preferable: it is all about which theory of justice we believe in, which _normative conception_ we adopt.

We have just showed something important: to allocate 4 courses to 4 students with one course per student, a mechanism must necessarily choose some normative conception, since (at least) two normative conceptions come into conflict.

Is it always the case, no matter the number of courses and the number of students?


## Problematic & consequences

The raison d'être of this project is the following question: *is any wish allocation mechanism doomed to take a moral stand if it is required to function (i.e., to return an allocation) whatever the preferences of the indiduals [unrestricted domain]?*

Otherly put: *does there exist (at least) one profile of preferences that poses a moral conflict to the allocation mechanism, for any number of courses and students?*

If it is the case, the heavy corollary is that any allocation algorithm designed to function for any preferences profile carries a moral bias.


# Formally put

On considère le cas simple avec $n$ étudiants, $n$ cours à choisir et un cours alloué à chaque étudiant (et donc un seul étudiant par cours).

## Definitions

- **Préférences** : on nomme _préférences_ une liste ordonnée de cours qui traduit les préférences d'un étudiant.

- **Profil de préférences** : l'ensemble des préférences de chaque étudiant forme un _profil de préférences_ que l'on peut résumer dans une matrice où chaque ligne représente les préférences d'un étudiant.

- **Allocation** : on nomme _allocation_ tout $n$-uplet de cours, traduisant le fait que le $i$<sup>e</sup> cours du $n$-uplet est affecté au $i$<sup>e</sup> étudiant (pour un profil de préférences donné).

- **Satisfaction** : on nomme _satisfaction_ pour une allocation le vecteur dont la $i$<sup>e</sup> composante est le bien-être de l'étudiant $i$. 

   Note : puisque toute conception normative respectable respecte la condition d'anonymat (symétrie des individus), on pourra se permettre d'utiliser le terme _satisfaction_ pour désigner ce même vecteur rangé par ordre décroissant.

- **Préférabilité selon une conception normative** : une allocation $a$ est dite _préférable à $b$ selon la conception normative_ $u$ si la satisfaction de $a$ est préférée à celle de $b$ selon $u$ (pour un profil de préférences donné).

   On note $a\succ_u b$ si la préférence est stricte, $a\succeq_u b$ si elle est large, et $a\sim_u b$ s'il ya indifférence.

- **Dominance normative** : une allocation $a$ _domine normativement_ $b$ si $a\succeq_u b$ pour toute conception normative $u$ (pour un profil de préférences et un ensemble de conceptions normatives donnés, non précisés s'il n'y a pas d'ambiguïté).

- **Efficacité normative** : une allocation $a$ est dite _normativement efficace_ si elle n'est normativement dominée par aucune autre allocation (pour un profil de préférences et un ensemble de conceptions normatives donnés, non précisés s'il n'y a pas d'ambiguïté).


# Partie computationnelle


## Fonctionnement

Le notebook présent dans se repo permet de prouver computationnellement l'existence de profils de préférences qui créent un conflit normatif, pour $n\in\{4,5\}$, et son inexistence pour $n=3$.

Plus largement, il permet d'exhiber chaque conflit normatif possible entre deux conceptions normatives données, pour $n$ donné, en donnant un profil de préférences donnant lieu à ce conflit.

Note : la fonction n'affiche pas les doublons. Par exemple, si plusieurs profils de préférences _différents_ conduisent au _même_ conflit normatif (i.e., au _même_ ensemble d'allocations normativement efficace), alors un seul représentant sera affiché.

Par exemple, `print_dilemmes(4, score_utilitarisme, score_leximin)` affiche tous les dilemmes possibles entre utilitarisme et égalitarisme pour $n=4$.


## Un exemple de bout en bout

Cet exemple reprend celui de l'introduction, pas à pas.

~~~
Combinaison de préférences

[['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['C' 'A' 'D' 'B']]
~~~

Considérons la combinaison de préférences ci-dessus. Chaque ligne de la matrice représente un élève, plus précisément les préférences d'un élève : l'élève 1 préfère A, puis B, C, D.

Intuitivement, comment allouer optimalement les cours ? Puisque les élèves 1, 2, 3 préfèrent tous les trois A, on peut allouer A à l'un des trois seulement. Disons à 1. Et allouons C à 4, clairement (c'est son préféré et les autres ne l'aiment pas). Ensuite, peu de latitude : on alloue B à 2 et D à 4 (c'est pareil que de faire l'inverse). On obtient l'allocation (A, B, D, C), et la satisfaction associée $(4,3,1,4)$, ou $(4,4,3,1)$ par ordre décroissant.

Mais dans l'option précédente, l'un des élèves est profondément insatisfait, avec 1 point. Peut-être pourrait-on faire en sorte que personne ne soit si malheureux. On pourrait allouer D à 4 : il aurait une satisfaction de $2>1$, et on s'assurerait que les élèves 1, 2, 3 n'aient pas leur dernier choix. On leur assignerait ensuite A, B et C indifféremment (puisqu'ils ont les mêmes préférences), par exemple A à 1, B à 2, C à 3. On obtient l'allocation (A, B, C, D), et la satisfaction associée $(4,3,2,2)$.

Quelle option est la meilleure ? Si l'on considère les conceptions normatives utilitaristes et égalitaristes (en se basant pour cette dernière sur le critère du leximin), alors
- $(4,4,3,1)\succ(4,3,2,2)$ pour un utilitariste puisque $4+4+3+1=12>11=4+3+3+2+2$ ;
- $(4,3,2,2)\succ(4,4,3,1)$ pour un égalitariste, puisque le moins bien-loti est à $2$ dans le 1er cas, et seulement à $1$ dans le second cas.

C'est ce brainstorming, qui consiste à chercher les meilleures allocations - les allocations _normativement efficaces_ - que réalise ce code. Voici l'output pour la combinaison de préférences considérée, et qui correspond à notre dilemme.

Note : on a codé une fonction de score pour le leximin, qui fonctionne tant que les niveaux de satisfaction sont inférieurs à 9. Elle est facilement adaptable.

~~~
   Satisfaction  Score_1  Score_2    Allocation
0  (4, 4, 3, 1)       12     1344  (A, B, D, C)
1  (4, 3, 2, 2)       11     2234  (A, B, C, D)
~~~


## [À venir / incomplet] Annexe : comment l'algorithme détermine-t-il les allocations normativement efficaces ?

On construit cet ensemble par récurrence. On note $\mathcal A_{NE}^P$ l'ensemble "provisoire" des allocations normativement efficaces. Soient une combinaison de préférences et $u,v$ deux conceptions normatives.

Il y a autant d'étapes que d'allocations possibles (i.e., $n!$).

À l'étape 1, $\mathcal A_{NE}^P=\empty$. On considère l'allocation $a_1$. On ajoute $a_1$ à $\mathcal A_{NE}^P$, puisque $a_1$ est normativement efficace au sein de l'ensemble des allocations $\mathcal A_{NE}^P \cup \{a_1\}$.

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

Prenons un exemple pour intuiter la suite. Traduisons ces relations de préférences par des inégalités sur des scores. On va considérer qu'on peut quantifier la recommandabilité des alloactions selon les normes $u$ et $v$ via des fonctions de score $s_u$ et $s_v$. Par exemple, si $u$ désigne l'utilitarisme, $s_u(\hat a)=7$ si la satisfaction de $\hat a$ est $(3,3,1)$.

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

Pour l'instant, on passe en revue toutes les combinaisons de préférences possibles en prenant en compte la symétrie des individus : $(ABC, ABC, CBA)$ et $(CBA, ABC, ABC)$ sont identiques à cet égard, donc le code ne regardera que le premier des deux.

Mais on peut encore diminuer le nombre de combinaisons de préférences à étudier.

Ex : $(ABC, ACB, ACB) \sim (ABC, ABC, ACB)$ (il suffit de remplacer $B$ par $C$ et $C$ par $B$, ce qu'on peut faire par symétrie) $\sim (XYZ, XYZ, XZY)$ plus généralement.


## Fonction de satisfaction non linéaire

À ce stade, la satisfaction est linéaire :
- un 1er choix donne $n$ points de satisfaction,
- un 2e choix donne $n-1$,
- ...
- un dernier choix donne $1$.

On devrait pouvoir utiliser des fonctions de satisfaction non linéaires, par exemple
- convexes (un élève aime plus son 1er choix par rapport à son 2e, que son 2e par rapport à son 3e ; i.e., il veut autant que possible son choix 1, et à la rigueur peu lui importe 2 ou 3),
- concaves (un élève aime plus son 2e choix par rapport à son 3e, que son 1er par rapport à son 2e ; i.e., il veut autant que possible ne pas avoir son choix 3, et à la rigueur peu lui importe 1 ou 2).


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


## Augmenter le nombre de cours par élèves, d'élèves par cours

On est pour l'instant dans le cas simple où $n$ = nombre d'élèves = nombre de cours.

À voir ce qu'il est numériquement possible de faire (en termes de capacité informatique), mais il serait intéressant de checker l'existence de dilemmes dans des cas plus complexes.

Par exemple (relativement simple) : 8 cours, 4 élèves, 2 cours à choisir par élève


## Usage réel pour une combinaison de préférences donnée

L'usage premier de ce code était de prouver l'existence de combinaisons de préférences qui créent un dilemme.

Mais il serait intéressant de rendre ce code opérationnel pour, étant donné une combinaison de préférences (un input réel, par exemple les voeux de cours réels des élèves d'une école/université), donner toutes les allocations efficaces (en fonction de fonctions de score, i.e. de conceptions de la justice distributive, données).


# Partie théorique

Here, I try to answer the problematic given in the introduction: _does there exist (at least) one profile of preferences that poses a moral conflict to the allocation mechanism, for any number of courses and students?_

To do so, I will consider the conflict "utilitarianism vs egalitarianism" (egalitarianism is represented by the leximin criterium).

I use the way profiles of preferences are represented in the introduction to skip the explicit courses names and directly consider the matrix of preferences, which is enough to show results.

## $n$ students, $n$ courses

### $n=3$

There is no preferences profile that creates a dilemma. It exists two “dilemma” vectors : $(3,3,1)$ and $(2,2,2)$ but it can be shown that the vector $(3,3,2)$ can always be reached if $(3,3,1)$ and $(2,2,2)$ can. 

### $n=4$

The matrix preferences we gave as an exemple earlier works:

$$
\begin{bmatrix}
\blue 4 & 3 & 2 & \red 1 \\
\red 4 & \blue 3 & 2 & 1 \\
4 & \red 3 & \blue 2 & 1 \\
3 & 1 & \red 4 & \blue 2 \\ 
\end{bmatrix}
$$

I will not give a proof here but it can be easily intuited that with such a matrix, $(4,4,3,1)$ and $(4,3,2,2)$ are both normatively efficient.

### $n\geq5$

We can use the same matrix of preferences and just extend it.

See:

$$
\begin{bmatrix}
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 4 & 3 & 2 & 1 \\
5 & 3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$

The reasoning is the following:

- either we give the first course to one of students $A,B,C,D$, and then the matrix representing the preferences of the 4 remaining students over the 4 remaining courses is the same as for $n=4$, and so we can best produce the vectors $(5,4,4,3,1)$ and $(5,4,3,2,2)$;
    
    $$
    \begin{bmatrix}
    \blue 5 & 4 & 3 & 2 & \red 1 \\
    \red 5 & \blue 4 & 3 & 2 & 1 \\
    5 & \red 4 & \blue 3 & 2 & 1 \\
    5 & 4 & \red 3 & \blue 2 & 1 \\
    5 & 3 & 1 & \red 4 & \blue 2 \\ 
    \end{bmatrix}
    $$
    
- or we give the first course to student $E$, and then all the allocations of the 4 remaining course to students $A,B,C,D$ will give the same well-being vector since they have the same preferences; so we get the vector $(5,4,3,2,1)$ anyway.
    
    $$
    \begin{bmatrix}
    5 & \green 4 & 3 & 2 & 1 \\
    5 & 4 & \green 3 & 2 & 1 \\
    5 & 4 & 3 & \green 2 & 1 \\
    5 & 4 & 3 & 2 & \green 1 \\
    \green 5 & 3 & 1 & 4 & 2 \\ 
    \end{bmatrix}
    $$
    

But $(5,4,3,2,1)$ is clearly normatively inefficient, so we have to choose between $(5,4,4,3,1)$ and $(5,4,3,2,2)$

And we can move on to greater $n$ in the same way. The dilemma is $(n,n-1,\dots,5,4,3,2,2)$ vs $(n,n-1,\dots,5,4,4,3,1)$ appears in color.

$$
\begin{bmatrix}
\blue n & n-1 & n-2 & \dots & 5 & 4 & 3 & 2 & \red 1 \\
\red n & \blue {n-1} & n-2 & \dots & 5 & 4 & 3 & 2 & 1 \\
n & \red {n-1} & \blue {n-2} & \dots & 5 & 4 & 3 & 2 & 1 \\
\vdots & \vdots & \vdots & \vdots  & \vdots & \vdots & \vdots & \vdots & \vdots \\
n & n-1 & n-2 & \dots & \blue 5 & 4 & 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & \red 5 & \blue 4 & 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & \red 4 & \blue 3 & 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & 4 & \red 3 & \blue 2 & 1 \\
n & n-1 & n-2 & \dots & 5 & \bf 3 & \bf 1 & \red {\bf 4} & \blue {\bf 2} \\ 
\end{bmatrix}
$$

## $n\geq2$ students, $p\geq 4$ courses, $n/p$ slots per course

Remark: we need that $n/p\in\N^\star$, so $p|n$ ($p$ divides $n$).

### Example: 8 students, 4 courses, 2 students per course

We must choose 2 numbers per column (since there are 2 slots per course), but still 1 number per row (each student still only gets 1 course). 

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

This profile of preferences raises the dilemma $(4,4,3,3,2,2,2,2)$ vs $(4,4,4,4,3,3,1,1)$:

$$
\begin{bmatrix}
\blue 4 & 3 & 2 & \red 1 \\
\blue 4 & 3 & 2 & \red 1 \\
\red 4 & \blue 3 & 2 & 1 \\
\red 4 & \blue 3 & 2 & 1 \\
4 & \red 3 & \blue 2 & 1 \\
4 & \red 3 & \blue 2 & 1 \\
3 & 1 & \red 4 & \blue 2 \\ 
3 & 1 & \red 4 & \blue 2 \\ 
\end{bmatrix}
$$

- Proof
    
    $(4,4,4,4,3,3,1,1)$: if we want 4 times $4$, we have to give $4$ to the last two students, and give $4$ to 2 other students (no matter which: the 6 remaining have the same preferences). Then we can only give twice $3$ and twice $1$. It is quite clearly the best we can do from a utilitarian standpoint.
    
    With the same kind of reasoning, we can easily check that $(4,4,3,3,2,2,2,2)$ is the best we can do from an egalitarian standpoint.
    

We can also find other normatively efficient allocations, like $(4,4,4,3,3,2,2,1)$, and we may create dilemmas with them too.

$$
\begin{bmatrix}
\green 4 & 3 & 2 & 1 \\
\green 4 & 3 & 2 & 1 \\
4 & \green 3 & 2 & 1 \\
4 & \green 3 & 2 & 1 \\
4 & 3 & \green 2 & 1 \\
4 & 3 & 2 & \green 1 \\
3 & 1 & \green 4 & 2 \\ 
3 & 1 & 4 & \green 2 \\ 
\end{bmatrix}
$$

## $n$ students, $p$ courses, $p/n$ slots per student

### Example: 4 students, 2 courses, 2 slots per student

We must choose 2 numbers per row (since there are 2 slots per student), but 1 number per column (there is 1 slot per course).

 

$$
\begin{bmatrix}
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
6 & 5 & 2 & 1 & 8 & 7 & 4 & 3 \\ 
\end{bmatrix}
$$

This profile of preferences raise the dilemma $(8,7,6,5,4,4,3,3)$ vs $(8,8,7,7,6,5,2,1)$:

$$
\begin{bmatrix}
\blue 8 & \blue 7 & 6 & 5 & 4 & 3 & \red 2 & \red 1 \\
\red 8 & \red 7 & \blue 6 & \blue 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \red 6 & \red 5 & \blue 4 & \blue 3 & 2 & 1 \\
6 & 5 & 2 & 1 & \red 8 & \red 7 & \blue 4 & \blue 3 \\ 
\end{bmatrix}
$$

Once again, we can easily find other normatively efficient allocations, like $(8,8,7,6,5,3,3,2)$, and we may create dilemmas with them too.

$$
\begin{bmatrix}
\green 8 & \green 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \green 6 & \green 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & \green 3 & \green 2 & 1 \\
6 & 5 & 2 & 1 & \green 8 & 7 & 4 & \green 3 \\ 
\end{bmatrix}
$$

## $n$ students, $p$ courses, $k$ slots per student, $nk/p$ slots per course

### Example: 12 students, 8 courses, 2 slots per student, 3 slots per course

$$
\begin{bmatrix}
\blue 8 & \blue 7 & 6 & 5 & 4 & 3 & \red 2 & \red 1 \\
\blue 8 & \blue 7 & 6 & 5 & 4 & 3 & \red 2 & \red 1 \\
\blue 8 & \blue 7 & 6 & 5 & 4 & 3 & \red 2 & \red 1 \\
\red 8 & \red 7 & \blue 6 & \blue 5 & 4 & 3 & 2 & 1 \\
\red 8 & \red 7 & \blue 6 & \blue 5 & 4 & 3 & 2 & 1 \\
\red 8 & \red 7 & \blue 6 & \blue 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \red 6 & \red 5 & \blue 4 & \blue 3 & 2 & 1 \\
8 & 7 & \red 6 & \red 5 & \blue 4 & \blue 3 & 2 & 1 \\
8 & 7 & \red 6 & \red 5 & \blue 4 & \blue 3 & 2 & 1 \\
6 & 5 & 2 & 1 & \red 8 & \red 7 & \blue 4 & \blue 3 \\
6 & 5 & 2 & 1 & \red 8 & \red 7 & \blue 4 & \blue 3 \\
6 & 5 & 2 & 1 & \red 8 & \red 7 & \blue 4 & \blue 3 \\
\end{bmatrix}
$$

## Extensions

### Non-linear utility
   
If the matrix is

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
\blue a & b & c & \red d \\
\red a & \blue b & c & d \\
a & \red b & \blue c & d \\
b & d & \red a & \blue c \\ 
\end{bmatrix}
$$

$(a,b,c,c)$ is always better than $(a,a,b,d)$ for an egalitarian, but for the dilemma to emerge, we need the utilitarist view to disagree, i.e. we need $2c<a+d$. It is always true for a convex utility function (where $a-b>b-c>c-d$), since we then have:

$$
\begin{align*}
a+d &>b+c \\
&\geq c+c \\
&=2c
\end{align*}
$$

Example

$$
\begin{bmatrix}
\blue {10} & 6 & 3 & \red 1 \\
\red {10} & \blue 6 & 3 & 1 \\
10 & \red 6 & \blue 3 & 1 \\
6 & 1 & \red {10} & \blue 6 \\ 
\end{bmatrix}
$$

$(10,6,6,3)$ vs $(10,10,6,1)$
