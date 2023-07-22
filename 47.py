# PROBLEM 47 from CHAPTER 7
# IMPORTING LIBRARY

import networkx as nx

# IMPORTING DATASET
G = nx.read_edgelist('soc-sign-epinions.txt', nodetype=int, data=(('weight', float),), create_using=nx.Graph())

# TC: TRIAD COUNTS
# TT: TOTAL TRIADS
# TF: TRIAD FRACTION

TC = nx.triangles(G)
TT = sum(TC.values())
TF = {triad_type: count / TT for triad_type, count in TC.items()}

for triad_type, count in TC.items():
    fraction = TF[triad_type]
    print(f'Triad {triad_type}: Count = {count}, Fraction = {fraction:.4f}')
print("Problem 47 Results by Armin Zakarian")
