# PROBLEM 48 from CHAPTER 7
# IMPORTING LIBRARY

import networkx as nx
from itertools import product

# IMPORTING DATASET
G = nx.read_edgelist('soc-sign-epinions.txt', nodetype=int, data=(('weight', float),), create_using=nx.Graph())

# POSITIVE AND NEGATIVE EDGES
positive_edges = sum(1 for _, _, sign in G.edges(data='weight') if sign > 0)
negative_edges = sum(1 for _, _, sign in G.edges(data='weight') if sign < 0)
total_edges = positive_edges + negative_edges
positive_fraction = positive_edges / total_edges
negative_fraction = negative_edges / total_edges

# TRIAD PROBABILITIES
triad_probabilities = {}
for triad_type in range(16):
    triad_probability = 1.0
    for edge_signs in product([-1, 1], repeat=3):
        sign_product = 1.0
        for sign in edge_signs:
            if sign == 1:
                sign_product *= positive_fraction
            else:
                sign_product *= negative_fraction
        triad_probability *= sign_product
    triad_probabilities[triad_type] = triad_probability

# RESULTS
print(f'Positive Fraction: {positive_fraction:.4f}')
print(f'Negative Fraction: {negative_fraction:.4f}')
print('Triad Probabilities:')
for triad_type, probability in triad_probabilities.items():
    print(f'Triad {triad_type}: Probability = {probability:.4f}')


print("Problem 48 Results by Armin Zakarian")
