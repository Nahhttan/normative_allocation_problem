# "Normative matching problem"

_Nathan LANGLOIS, personal thoughts, inspired by courses allocation mechanisms in French Grandes Écoles._

NOTE : une version française est disponible dans le repo :)


# Introduction: framework

## Individuals, courses and preferences

Let 4 students be Alice, Bob, Carl, and David. We will denote them $A,B,C,D$. We suppose they have to rank 4 courses $X,Y,Z,T$ that are proposed.

Once the students have given their preferences (as an ordering, i.e. a binary relation that is reflexive, transitive and complete), an allocation mechanism occurs to allocate each course to one student, so that in the end, every student gets exactly one course and every course is allocated to exactly one student.

CAREFUL: the framework looks like a classic Arrovian framework, but it is not. The students compete to get the course they prefer, and only they will get their course. In the Arrovian framework, only one alternative is socially chosen.

To put it more intuitively,

- in the Arrovian framework, everybody is happier and the job is easy if everybody has the same preferences (the unanimously preferred alternative is chosen);
- in the framework here, everybody is happier and the job is easy if nobody has the same preferences (so that each student can be assigned the course they prefer).

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

In what follows, we will refer to the set of preferences as the _profile of preferences_, to use Arrow's expression.

### Allocation mechanism, linear well-being assumption

We now suppose that the allocation mechanism aims at maximizing social welfare (the overall well-being of the students). To achieve this goal, the allocation mechanism makes the assumption that the well-being of a student is linearly negatively correlated to the rank of the course he receives. It means that for 4 courses, a 1st choice gives 4 units of well-being, a 2nd choice gives 3 units, a 3rd choice 2 units, and a 4th choice 1 unit.

(This is a strong assumption. Non-linear well-being should be considered in the future; see extensions.)

Now, we can represent the profile of preferences, i.e. the preferences of $A,B,C,D$, in a simplier way: the following matrix is such that each row now corresponds to a student, and each columns corresponds to a course.

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
\color{orange} 4 & 3 & 2 & 1 \\
4 & \color{orange} 3 & 2 & 1 \\
4 & 3 & \color{orange} 2 & 1 \\
3 & 1 & 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$

The well-being vector associated with the former allocation is $(4,3,2,2)$.

Another allocation could be:

$$
\begin{bmatrix}
4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & 3 & 2 & 1 \\
4 & \color{red} 3 & 2 & 1 \\
3 & 1 & \color{red} 4 & 2 \\ 
\end{bmatrix}
$$

This one would produce the vector $(4,4,3,1)$.

Note that we can also, when possible, represent 2 allocations on a same matrix to compare them better. See:

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$

    

### The heart of the problem

But in the former example, what is preferable? $(4,3,2,2)$ or $(4,4,3,1)$?

- The utilitarian view would state that $(4,4,3,1)$ is better, because the sum of its components amounts to $12$, and the sum of $(4,3,2,2)$ is only $11$.
- The egalitarian view, based on the leximin criterion, would say that $(4,3,2,2)$ is better, because its minimum component is $2$, and the minimum of $(4,4,3,1)$ is only $1$.

Moreover, it appears (and can easily be proven) that it cannot be found any allocation that would reconciliates both view by being better than both allocations according to both views. So we are stuck with a moral conflict.

There is no best answer to this question of which allocation is preferable: it is all about which theory of justice we believe in, which _normative conception_ we adopt.

We have just showed something important: to allocate 4 courses to 4 students with one course per student, an allocation mechanism must necessarily choose some normative conception, since (at least) two normative conceptions come into conflict.

Is it always the case, no matter the number of courses and the number of students?


## Problematic & consequences

The raison d'être of this project is the following question: *is any wish allocation mechanism doomed to take a moral stand if it is required to function (i.e., to return an allocation) whatever the preferences of the indiduals [unrestricted domain]?*

Otherly put: *does there exist (at least) one profile of preferences that poses a moral conflict to the allocation mechanism, for any number of courses and students?*

If it is the case, the heavy corollary is that any allocation algorithm designed to function for any preferences profile carries a moral bias.


# Formally put

We consider the simple case with $n$ students, $n$ courses to be chosen, and one course assigned to each student (and therefore only one student per course).


## Definitions

- **Preferences**: an ordered list of courses reflecting a student's preferences is called _preferences_.

- **Profile of preferences** : the set of preferences of all students forms a _preference profile_ that can be summarized in a matrix where each row represents the preferences of a student.

- **Allocation**: any tuple of courses is called an _allocation_, meaning that the i<sup>th</sup> course in the tuple is assigned to the i<sup>th</sup> student (for a given profile of preferences).

- **Satisfaction**: _satisfaction_ for an allocation is the "well-being vector", i.e. the vector whose $i$<sup>th</sup> component is student $i$'s well-being.

    Note: since any respectable normative design respects the condition of anonymity (symmetry of individuals), we may take the liberty of using the term satisfaction to designate this same vector arranged in descending order.

- **Preferability according to a normative conception**: an allocation $a$ is said to be _preferable to $b$ according to the normative conception_ $u$ if the satisfaction of $a$ is preferred to that of $b$ according to $u$ (for a given profile of preferences).

   We note $a\succ_u b$ if the preference is strict, $a\succeq_u b$ if it is broad, and $a\sim_u b$ if there is indifference.

- **Normative dominance**: an allocation $a$ _normatively dominates_ $b$ if $a\succeq_u b$ for any normative conception $u$ (for a given preference profile and set of normative conceptions, unspecified if unambiguous).

- **Normative efficiency**: an allocation $a$ is said to be _normatively efficient_ if it is not normatively dominated by any other allocation (for a given profile of preferences and set of normative conceptions, unspecified if unambiguous).

- **Extensions to satisfactions**: we can easily extend the definitions of _preferability according to a normative conception_, _normative dominance_ and _normative efficiency_ to satisfactions (vectors of well-being).

# Computationnal part


## How it works

The notebook in this repo can be used to computationally prove the existence of profiles of preferences that create a normative conflict, for $n$, and its non-existence for $n=3$.

More broadly, it allows us to display every possible normative conflict between two given normative conceptions, for a given $n$, by giving a preference profile giving rise to this conflict.

Note: the function does not display duplicates. For example, if several _different_ profiles of preferences lead to the _same_ normative conflict (i.e., to the _same_ set of normatively efficient allocations), then only one representative will be displayed.

For example, `print_dilemmas(4, score_utilitarisme, score_leximin)` displays all possible dilemmas between utilitarianism and egalitarianism for $n=4$.


## An example from start to finish

This example repeats the one in the introduction, step by step.

~~~
Profil de préférences

[['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['A' 'B' 'C' 'D']
 ['C' 'A' 'D' 'B']]
~~~

Consider the above preference profile. Each row of the matrix represents a student, or more precisely, a student's preferences: student 1 prefers A, then B, C, D.

Intuitively, how can we best allocate lessons? Since students 1, 2 and 3 all prefer A, we can allocate A to only one of the three, say to 1. Let's say to 1. And let's allocate C to 4, clearly (it's his favorite and the others don't like him). Then, there's little latitude: we allocate B to 2 and D to 4 (it's the same as doing it the other way round). You get the allocation (A, B, D, C), and the associated satisfaction $(4,3,1,4)$, or $(4,4,3,1)$ in descending order.

But in the previous option, one of the students is deeply dissatisfied, with 1 point. Perhaps we could make sure that no one is so unhappy. We could allocate D to 4: he would have a satisfaction of $2>1$, and we'd make sure that students 1, 2, 3 don't get their last choice. We would then assign them A, B and C indifferently (since they have the same preferences), for example A to 1, B to 2, C to 3. We obtain the allocation (A, B, C, D), and the associated satisfaction $(4,3,2,2)$.

Which option is better? If we consider the utilitarian and egalitarian normative conceptions (based on the leximin criterion for the latter), then
- $(4,4,3,1)\succ(4,3,2,2)$ for a utilitarian since $4+4+3+1=12>11=4+3+3+2+2$ ;
- $(4,3,2,2)\succ(4,4,3,1)$ for an egalitarian, since the least well-loved is $2$ in the first case, and only $1$ in the second.

It is this brainstorming, looking for the best allocations - the _normatively efficient_ allocations - that this code performs. Below is the output for the preference profile under consideration, which corresponds to our dilemma.

Note: I have coded a score function for the leximin, which works as long as satisfaction levels are below 9. It's easily adaptable.

~~~
   Satisfaction  Score_1  Score_2    Allocation
0  (4, 4, 3, 1)       12     1344  (A, B, D, C)
1  (4, 3, 2, 2)       11     2234  (A, B, C, D)
~~~


## [To come / incomplete] Appendix: How does the algorithm determine normatively efficient allocations?

We construct this set by recurrence. Let $\mathcal A_{NE}^P$ be the "provisional" set of normatively efficient allocations. Let be a profile of preferences and $u,v$ two normative conceptions.

There are as many steps as there are possible allocations (i.e., $n!$).

In step 1, $\mathcal A_{NE}^P=\emptyset$. Consider allocation $a_1$. We add $a_1$ to $\mathcal A_{NE}^P$, since $a_1$ is normatively efficient within the set of allocations $\mathcal A_{NE}^P \cup \{a_1\}$.

At step $n$, suppose we have $\mathcal A_{NE}^P=\{a_{(1)},\dots,a_{(n)}\}$ with

$$
\begin{cases}
   a_{(1)}\succeq_u\dots\succeq_u a_{(n)} \\
   a_{(1)}\preceq_v\dots\preceq_v a_{(n)}
\end{cases}
$$

Consider the allocation $a_{n+1}$. Then there exist $i,j$ such that


$$
\begin{cases}
   a_{(1)}\succeq_u\dots\succeq_u a_{(i)}\succeq_u a_{n+1}\succeq_u a_{(i+1)}\succeq_u\dots\succeq_u a_{(n)} \\
   a_{(1)}\preceq_u\dots\preceq_u a_{(j)}\preceq_u a_{n+1}\preceq_u a_{(j+1)}\preceq_u\dots\preceq_u a_{(n)} \\
\end{cases}
$$

Let's take an example to illustrate what follows. Let's translate these preference relations into inequalities on scores. We'll consider that we can quantify the recommendability of allocations according to the $u$ and $v$ norms via score functions $s_u$ and $s_v$. For example, if $u$ denotes utilitarianism, $s_u(\hat a)=7$ if $\hat a$'s satisfaction is $(3,3,1)$.

$$
\begin{cases}
   10 &>& 8 &>& 6 &>& 4 &>& 2 \\
   12 &<& 14 &<& 16 &<& 18 &<& 20 
\end{cases}
$$

- If $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 15)$, then $a_{n+1}$ is normatively efficient, and fits perfectly into the chain, between $a_{(2)}$ and $a_{(3)}$.
- If $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 13)$, then $a_{n+1}$ will not be normatively efficient, since it is normatively dominated by $a_{(2)}$ because $7<8$ on the one hand and $13<14$ on the other.
- If $(s_u(a_{n+1}), s_v(a_{n+1}))=(7, 19)$, then not only is $a_{n+1}$ normatively efficient, but it eliminates $a_{(3)}$ and $a_{(4)}$.

# Areas for improvement


## Taking into account the symmetry of alternatives

For the moment, the code is reviewing all possible profiles of preferences, taking into account the symmetry of the individuals: $(ABC, ABC, CBA)$ and $(CBA, ABC, ABC)$ are identical in this respect, so the code will only look at the first of the two.

But you can also reduce the number of profiles of preferences to be studied.

For example: $(ABC, ACB, ACB) \sim (ABC, ABC, ACB)$ (just replace $B$ by $C$ and $C$ by $B$, which can be done by symmetry) $\sim (XYZ, XYZ, XZY)$ more generally.


## Non-linear satisfaction function

At this stage, satisfaction is linear:
- a 1st choice gives $n$ points of satisfaction,
- a 2nd choice gives $n-1$,
- ...
- a last choice gives $1$.

We should be able to use non-linear satisfaction functions, for example
- convex (a student likes his 1st choice more than his 2nd, than his 2nd more than his 3rd; i.e., he wants his choice 1 as much as possible, and doesn't really care about 2 or 3),
- concave (a student likes his 2nd choice more than his 3rd, than his 1st choice more than his 2nd; i.e., he wants as much as possible not to have his 3rd choice, and doesn't really care about 1 or 2).


## Comparing more than 2 normative conceptions

For the moment, the code looks at dilemmas between 2 normative conceptions only.

It should be possible to compare more than that, starting with 3. Here are a few examples of what this would look like for 3 normative conceptions, denoted $u,v,w$.

### Relevant example 1


$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\\
b &\succ_v& a &\succ_v& c \\
c &\succ_w& a &\succ_w& b 
\end{cases}
$$

### Exemple pertinent 2

In the following example, one could believe that $c$ is not a normatively efficient allocation, because better can be reached according to any normative conceptions. Actually, $c$ is an efficient allocation, because no allocation normatively dominates it, i.e., is preferable to it according to any normative conception; one should keep in mind that the latter is the criterion for normative efficiency for an allocation.

$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\
a &\succ_v& c &\succ_v& b \\
b &\succ_w& c &\succ_w& a 
\end{cases}
$$


### Irrelevant example

Here, $c$ is normatively dominated by $b$, so it is not normatively efficient.

$$
\begin{cases}
a &\succ_u& b &\succ_u& c \\
b &\succ_v& c &\succ_v& a \\
b &\succ_w& a &\succ_w& c 
\end{cases}
$$


## Increase the number of courses per student, of students per course

So far, the code only adress the simple case where $n$ = number of students = number of courses.

It remains to be seen what is numerically possible (in terms of computing capacity), but it would be interesting to check the existence of dilemmas in more complex cases.

For example (relatively simple): 8 courses, 4 students, 2 courses to choose per student.


## Real-world use for a given preference profile

The primary use of this code was to prove the existence of profiles of preferences that raise to a dilemma.

But it would be interesting to make this code operational to, given a profile preferences (a real input, for example the real course wishes of students at a school/university), give all normatively efficient allocations (as a function of given score functions, i.e. conceptions of distributive justice).


# Theoretical part

Here, I try to answer the problematic given in the introduction: _does there exist (at least) one profile of preferences that poses a moral conflict to the allocation mechanism, for any number of courses and students?_

To do so, I will consider the conflict "utilitarianism vs egalitarianism" (egalitarianism is represented by the leximin criterion).

I use the way profiles of preferences are represented in the introduction to skip the explicit courses names and directly consider the matrix of preferences, which is enough to show results.

## $n$ students, $n$ courses

### $n=3$

There is no profile of preferences that raises a dilemma. It exists two “dilemma” vectors : $(3,3,1)$ and $(2,2,2)$ but it can be shown that the vector $(3,3,2)$, that normatively dominates those two vectors, can always be reached if $(3,3,1)$ and $(2,2,2)$ can. 

### $n=4$

The matrix preferences we gave as an exemple earlier works:

$$
\begin{bmatrix}
\color{orange} 4 & 3 & 2 & \color{red} 1 \\
\color{red} 4 & \color{orange} 3 & 2 & 1 \\
4 & \color{red} 3 & \color{orange} 2 & 1 \\
3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
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
\color{orange} 5 & 4 & 3 & 2 & \color{red} 1 \\
\color{red} 5 & \color{orange} 4 & 3 & 2 & 1 \\
5 & \color{red} 4 & \color{orange} 3 & 2 & 1 \\
5 & 4 & \color{red} 3 & \color{orange} 2 & 1 \\
5 & 3 & 1 & \color{red} 4 & \color{orange} 2 \\ 
\end{bmatrix}
$$
    
- or we give the first course to student $E$, and then all the allocations of the 4 remaining course to students $A,B,C,D$ will give the same well-being vector since they have the same preferences; so we get the vector $(5,4,3,2,1)$ anyway.
    
$$
\begin{bmatrix}
5 & \color{green} 4 & 3 & 2 & 1 \\
5 & 4 & \color{green} 3 & 2 & 1 \\
5 & 4 & 3 & \color{green} 2 & 1 \\
5 & 4 & 3 & 2 & \color{green} 1 \\
\color{green} 5 & 3 & 1 & 4 & 2 \\ 
\end{bmatrix}
$$
    

But $(5,4,3,2,1)$ is clearly normatively inefficient, so we have to choose between $(5,4,4,3,1)$ and $(5,4,3,2,2)$

And we can move on to a greater $n$ in the same way. The dilemma is $(n,n-1,\dots,5,4,3,2,2)$ vs $(n,n-1,\dots,5,4,4,3,1)$, and appears in color.

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

## $n\geq2$ students, $p\geq 4$ courses, $n/p$ slots per course

Remark: we need that $n/p\in\mathbb N^\star$, so $p|n$ ($p$ divides $n$).

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

- Proof
    
    $(4,4,4,4,3,3,1,1)$: if we want 4 times $4$, we have to give $4$ to the last two students, and give $4$ to 2 other students (no matter which: the 6 remaining have the same preferences). Then we can only give twice $3$ and twice $1$. It is quite clearly the best we can do from a utilitarian standpoint.
    
    With the same kind of reasoning, we can easily check that $(4,4,3,3,2,2,2,2)$ is the best we can do from an egalitarian standpoint.
    

We can also find other normatively efficient allocations, like $(4,4,4,3,3,2,2,1)$, and we may create dilemmas with them too.

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
\color{orange} 8 & \color{orange} 7 & 6 & 5 & 4 & 3 & \color{red} 2 & \color{red} 1 \\
\color{red} 8 & \color{red} 7 & \color{orange} 6 & \color{orange} 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \color{red} 6 & \color{red} 5 & \color{orange} 4 & \color{orange} 3 & 2 & 1 \\
6 & 5 & 2 & 1 & \color{red} 8 & \color{red} 7 & \color{orange} 4 & \color{orange} 3 \\ 
\end{bmatrix}
$$

Once again, we can easily find other normatively efficient allocations, like $(8,8,7,6,5,3,3,2)$, and we may create dilemmas with them too.

$$
\begin{bmatrix}
\color{green} 8 & \color{green} 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
8 & 7 & \color{green} 6 & \color{green} 5 & 4 & 3 & 2 & 1 \\
8 & 7 & 6 & 5 & 4 & \color{green} 3 & \color{green} 2 & 1 \\
6 & 5 & 2 & 1 & \color{green} 8 & 7 & 4 & \color{green} 3 \\ 
\end{bmatrix}
$$

## $n$ students, $p$ courses, $k$ slots per student, $nk/p$ slots per course

### Example: 12 students, 8 courses, 2 slots per student, 3 slots per course

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
\color{orange} a & b & c & \color{red} d \\
\color{red} a & \color{orange} b & c & d \\
a & \color{red} b & \color{orange} c & d \\
b & d & \color{red} a & \color{orange} c \\ 
\end{bmatrix}
$$

$(a,b,c,c)$ is always better than $(a,a,b,d)$ for an egalitarian, but for the dilemma to emerge, we need the utilitarian view to disagree, i.e. we need $2c < a+d$. It is always true for a convex utility function (where $a-b>b-c>c-d$), since we then have:

$$
\begin{align}
a+d &>b+c \\
&\geq c+c \\
&=2c
\end{align}
$$

Example

$$
\begin{bmatrix}
\color{orange} {10} & 6 & 3 & \color{red} 1 \\
\color{red} {10} & \color{orange} 6 & 3 & 1 \\
10 & \color{red} 6 & \color{orange} 3 & 1 \\
6 & 1 & \color{red} {10} & \color{orange} 6 \\ 
\end{bmatrix}
$$

$(10,6,6,3)$ vs $(10,10,6,1)$
