import numpy as np

def score_leximin(satisfaction, reorder=False):
    
    """
    Exemple : score_leximin((4, 2, 2, 1)) = 1224
    Limite : (0, 0, 1000, 0) > (1, 1, 1, 1) selon cette fonction mais pas le leximin...
    C'est parce que le leximin n'est pas scorisable ; voire grandeur_satisfaction
    """

    ordre_grandeur_satisfaction = 1
    
    if reorder:
        list(satisfaction).sort(reverse=True)

    score = 0
    for i in range(len(satisfaction)):
        score += satisfaction[i] * 10**(ordre_grandeur_satisfaction*i)
    return score


def score_utilitarisme(satisfaction):

    """
    Exemple : score_utilitarisme((4, 2, 2, 1)) = 9 (4+2+2+1)
    """

    return sum(satisfaction)


def score_prioritarisme(satisfaction, function=np.sqrt):
    # return np.sum(np.sqrt(satisfaction))
    return round(1000*sum(map(function, satisfaction)))