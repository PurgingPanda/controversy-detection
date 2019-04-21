# script to do a random walk on a graph, starting from a random node of a given side and counting the number of *times* we end up in either a node from the same side or from the other side

# random walk type3.

import networkx as nx;
import random,numpy,sys;
from decimal import Decimal
from operator import itemgetter;

from networkx import pagerank

filename = sys.argv[1];
file2 = sys.argv[2];
percent = float(sys.argv[3])/100;

G = nx.read_weighted_edgelist(filename,delimiter=',');

f1 = open("../communities_retweet_networks/community1_" + file2 + ".txt");
lines1 = f1.readlines();

f2 = open("../communities_retweet_networks/community2_" + file2 + ".txt");
lines2 = f2.readlines();



pageRankResult = pagerank(G)
print(pageRankResult)


PxxNumerator = Decimal(0)
Denumerator = Decimal(0)
halfDecimal = Decimal(0.5)

for v in lines1:
    v = v.strip()
    PxxNumerator += Decimal(pageRankResult[v])
    Denumerator += halfDecimal *Decimal(pageRankResult[v])

PyyNumerator = Decimal(0)
for v in lines2:
    v = v.strip()
    PyyNumerator += Decimal(pageRankResult[v])
    Denumerator += halfDecimal *Decimal(pageRankResult[v])

Pxx = (halfDecimal * PxxNumerator) / Denumerator
Pyy = (halfDecimal * PyyNumerator) / Denumerator

Pyx = 1 - Pxx
Pxy = 1 - Pyy
print("PxxNumerator", PxxNumerator)
print("PyyNumerator", PyyNumerator)
print("Denumerator", Denumerator)
print("Pxx", Pxx)
print("Pyy", Pyy)
print("Pyx", Pyx)
print("Pxy", Pxy)

RWC = Pxx * Pyy - Pxy * Pyx
print("RWC", RWC)
