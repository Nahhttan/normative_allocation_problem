# Formal definitions



Let $p\in\mathcal P$ be a profile of preferences.

## Normatively efficient allocations

Let $\mathcal C$ be a set of normative conceptions. We denote by $\mathcal A_{NE}^p(\mathcal C)$ the set of normatively efficient allocations, defined by [to be completed].

$$
    
$$


# Utilitarianism, egalitarianism, and prioritarianism

Let us denote $U$ utilitarianism, $E$ egalitarianism (based on the leximin criterion) and $P$ (any) prioritarianism.

It can be shown that $\mathcal A_{NE}^p(U,E)=\mathcal A_{NE}^p(U,E,P)$ for any degree of prioritarianism denoted by $P$. 

## Prioritarianism lies between utilitarianism and egalitarianism

It can be shown that

$$
\begin{cases}
    u\succeq_U v \\
    u\succeq_E w
\end{cases}
\implies u\succeq_P w
$$

and

$$
\begin{cases}
    u\succ_U v \\
    u\succ_E w
\end{cases}
\implies u\succ_P w
$$

for any degree of prioritarianism.

Formally, it means that if $u\succeq_{U,E}v$, then for any function $f$ that is increasing increasing and strictly concave, $\sum_i f(u_i) \geq \sum_i f(v_i)$.