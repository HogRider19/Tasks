"""
n genetic algorithms, a crossover allows 2 chromosomes to exchange part of their genes.
For more details, you can visit these wikipedia links : Genetic algorithm and Crossover.
A chromosome is represented by a list of genes
"""

def crossover(ns, xs, ys):
    for n in list(set(ns)):
        xs, ys = xs[0:n]+ys[n:], ys[0:n]+xs[n:]
    return (xs,ys)