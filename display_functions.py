import numpy as np
import pandas as pd

def df_allocations_lst(allocations_lst):
    
    
    """
    
    - Arguments
        - allocations_lst (liste d'allocations)
    
    - Return
        - un dataframe avec toutes les informations
    
    """
    
    df = pd.DataFrame({"Satisfaction": [],
                       "Score_1": [],
                       "Score_2": [],
                       "Allocation": []})

    for allocation in allocations_lst:
        df = df.append({"Satisfaction": allocation.satisfaction,
                       "Score_1": allocation.score_1,
                       "Score_2": allocation.score_2,
                       "Allocation": allocation.uplet},
                 ignore_index=True)
    df['Score_1'] = df['Score_1'].astype(int)
    df['Score_2'] = df['Score_2'].astype(int)

    return df

def df_allocations_lst_2(allocations_lst, score_function_1, score_function_2):
    
    
    """
    
    - Arguments
        - allocations_lst (liste d'allocations)
    
    - Return
        - un dataframe avec toutes les informations
    
    """
    
    df = pd.DataFrame({"Satisfaction": [],
                       "Score_1": [],
                       "Score_2": [],
                       "Allocation": []})

    for allocation in allocations_lst:
        df = df.append({"Satisfaction": allocation.satisfaction,
                       "Score_1": score_function_1(allocation.satisfaction),
                       "Score_2": score_function_2(allocation.satisfaction),
                       "Allocation": allocation.uplet},
                 ignore_index=True)
    df['Score_1'] = df['Score_1'].astype(int)
    df['Score_2'] = df['Score_2'].astype(int)

    return df


"""

Ci-dessous, les mêmes fonctions, pour le notebook alternatif.

"""
    
def print_allocations_lst(allocations_lst):
    
    """
    
    - print une liste d'allocations proprement, en affichant le profil de préférences associé au préalable
    - repose sur la fonction df_allocations_lst
    
    
    """
    
    print("Profil de préférences")
    print()
    print(np.array(allocations_lst[0].profil_de_prefs.uplet))
    print()
    print(df_allocations_lst(allocations_lst))
    print()
    print("==========")
    print()

def print_allocations_lst_2(allocations_lst, score_function_1, score_function_2):
    
    """
    
    - print une liste d'allocations proprement, en affichant le profil de préférences associée au préalable
    - repose sur la fonction df_allocations_lst
    
    
    """
    
    print("Profil de préférences")
    print()
    print(np.array(allocations_lst[0].profil_de_prefs.uplet))
    print()
    print(df_allocations_lst_2(allocations_lst, score_function_1, score_function_2))
    print()
    print("==========")
    print()
